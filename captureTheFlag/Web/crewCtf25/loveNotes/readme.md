# Bug 1:
* IDOR on notes (as long as we know the noteUUID it shld be accessible)

# Bug 2:
* headless browser action (headless browser to cause JS exec and leak noteUUID)

# Bug 3: 
* no sanitization on notes (at upload/api or dashboard pages) --> title bound by 1000 but not content

# Bug 4:
* note HTML interpretation and endpoint /api/note/id with no xss protection

# Recon
* CSPs configured at dashboard atmost covers self srcs.
* Inject notes via /api/notes POST with HTML and JS
* `/api/notes/<note-id>` has no CSP, hence executable
* /dashboard and /static/dashboard.js have a CSP blocking network calls and script executions via src and no-inline
  - connect-src self so no way for cross-origin exfil
  - script-src <file>, no way to inject js
* Report from bot only visits `/dashboard` context, we need to get it past that

# Exploit
* Create 2 notes --> 
  - 1 with the payload that can execute script --> as simple as cross origin note exfil via noteIDs
  - 2 create a meta tag note that would redirect the page via HTML to note1 --> `<meta http-equiv="refresh" content="0;url=/api/notes/target-id">`
* Report the second note so we can cause a redirect

# Not Bug:
* dashboard with CSP sources to hcaptcha

## Exploit vs Intended
* meta redirect and xss allowed solving it
* intended:
  - was actually curious reading the flag as I had not directly used css here
  - another chal `hateNotes` were created with the fix to intended solution --> ref: https://albertofdr.github.io/post/crewctf-2025 using path relaxation and font-src:url() 

