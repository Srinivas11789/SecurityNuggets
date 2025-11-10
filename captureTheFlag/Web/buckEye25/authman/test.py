import hashlib

"""
curl -X GET \
  -H "Referer: https://enlfg657jrgdt6s.m.pipedream.net" \
  https://authman.challs.pwnoh.io/api/check
{"status":401}
"""

# --- Server Challenge (Response #1) & Client Request (Request #2) Data ---

# Server Challenge
"""
Www-Authenticate: Digest realm="Authentication Required",nonce="df9bed82a7869058de3a81b48ff4ac70",opaque="ac42eeb89aca5c6f29d14e4fbb66e0d4",algorithm="MD5",qop="auth"
"""
KNOWN_REALM = "Authentication Required"
KNOWN_NONCE = "df9bed82a7869058de3a81b48ff4ac70"

# Client Request:
"""
Authorization: Digest username="test", realm="Authentication Required", nonce="df9bed82a7869058de3a81b48ff4ac70", uri="/auth", algorithm=MD5, response="50da83fac9d2510108bfffa72c65a1e1", opaque="ac42eeb89aca5c6f29d14e4fbb66e0d4", qop=auth, nc=00000002, cnonce="11a06c24e73d976e"
"""

KNOWN_USERNAME = "test"
KNOWN_PASSWORD = "test" # The secret being tested
KNOWN_URI = "/auth"
KNOWN_METHOD = "GET" # Assumed HTTP method for initial request
KNOWN_QOP = "auth"
KNOWN_NC = "00000002"
KNOWN_CNONCE = "11a06c24e73d976e"
TARGET_RESPONSE = "50da83fac9d2510108bfffa72c65a1e1"

# ----------------------------------------------------------------------

def calculate_md5(input_string: str) -> str:
    """Calculates the MD5 hash and returns the lowercase hex string."""
    return hashlib.md5(input_string.encode('utf-8')).hexdigest()

def calculate_ha1(username: str, realm: str, password: str) -> str:
    """Calculates HA1: MD5(username : realm : password)"""
    input_string = f"{username}:{realm}:{password}"
    print(f"\n[HA1 Input] {input_string}")
    return calculate_md5(input_string)

def calculate_ha2(method: str, uri: str) -> str:
    """Calculates HA2: MD5(method : uri)"""
    input_string = f"{method}:{uri}"
    print(f"[HA2 Input] {input_string}")
    return calculate_md5(input_string)

def calculate_final_response(ha1: str, nonce: str, nc: str, cnonce: str, qop: str, ha2: str) -> str:
    """Calculates the final response: MD5(HA1 : nonce : nc : cnonce : qop : HA2)"""
    input_string = f"{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}"
    print(f"[FINAL Input] {input_string}")
    return calculate_md5(input_string)

# --- VISUALIZE COMPUTATION ---
print("--- DIGEST AUTHENTICATION HASH VISUALIZATION ---")

# 1. Calculate HA1 (The User Secret)
HA1_result = calculate_ha1(KNOWN_USERNAME, KNOWN_REALM, KNOWN_PASSWORD)
print(f"[HA1 Result] {HA1_result}")

# 2. Calculate HA2 (The Request Context)
HA2_result = calculate_ha2(KNOWN_METHOD, KNOWN_URI)
print(f"[HA2 Result] {HA2_result}")

# 3. Calculate Final Response
FINAL_RESPONSE = calculate_final_response(
    HA1_result,
    KNOWN_NONCE,
    KNOWN_NC,
    KNOWN_CNONCE,
    KNOWN_QOP,
    HA2_result
)

print(f"\n[Final Hash Calculated] {FINAL_RESPONSE}")
print(f"[Target Hash from Client] {TARGET_RESPONSE}")

# 4. Verification
if FINAL_RESPONSE == TARGET_RESPONSE:
    print("\n✅ VERIFICATION SUCCESS: The calculated hash matches the client's response!")
else:
    print("\n❌ VERIFICATION FAILURE: The calculated hash does NOT match the client's response.")
