### Challenge
```
web/inspector-general
NotDeGhost

My friend made a new webpage, can you find a flag?
```

### Recon

### Solve
```
kali@kali.org$ curl https://redpwn.net/
<!DOCTYPE html>
<html lang="en-us">
  <head>
	<meta name="generator" content="Hugo 0.72.0" />
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="redpwnctf2020" content="flag{1nspector_g3n3ral_at_w0rk}">
    <title>Home | redpwn</title>
    <link rel="stylesheet" href="/css/style.css" />
    <link rel="stylesheet" href="/css/fonts.css" />
    <link rel="stylesheet" href="/css/theme-override.css">
    <header>

  
  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/atom-one-light.min.css">
  <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
  <script>hljs.initHighlightingOnLoad();</script>
  <nav>
    <ul>
      
      
      
      
      <li class="pull-left current">
        <a href="/">~/home</a>
      </li>
      
      
      <li class="pull-left ">
        <a href="/writeups/">~/writeups</a>
      </li>
      
      
      <li class="pull-left ">
        <a href="/ctfs/">~/ctfs</a>
      </li>
      
      
      <li class="pull-left ">
        <a href="/categories/">~/categories</a>
      </li>
      

      
      
      <li class="pull-right">
        <a href="/index.xml">~/atom_feed</a>
      </li>
      

    </ul>
  </nav>
</header>

  </head>

  <body>
    <br/>




<div class="main">
<p><img src="/logo.png" alt="logo"></p>
<p><a href="https://github.com/redpwn">GitHub</a></p>
<p><a href="/writeups/">Writeups</a></p>
<p><a href="https://ctftime.org/team/59759">CTFtime</a></p>
<p><a href="https://ctf.redpwn.net">RedpwnCTF</a></p>
</main>




    <footer>
      
<script>
(function() {
  function center_el(tagName) {
    var tags = document.getElementsByTagName(tagName), i, tag;
    for (i = 0; i < tags.length; i++) {
      tag = tags[i];
      var parent = tag.parentElement;
      
      if (parent.childNodes.length === 1) {
        
        if (parent.nodeName === 'A') {
          parent = parent.parentElement;
          if (parent.childNodes.length != 1) continue;
        }
        if (parent.nodeName === 'P') parent.style.textAlign = 'center';
      }
    }
  }
  var tagNames = ['img', 'embed', 'object'];
  for (var i = 0; i < tagNames.length; i++) {
    center_el(tagNames[i]);
  }
})();
</script>

      
    </footer>
  </body>
</html>

kali@kali.org$ curl https://redpwn.net/ | grep flag
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2337  100  2337    0     0   2337      0  0:00:01 --:--:--  0:00:01  6754
    <meta name="redpwnctf2020" content="flag{1nspector_g3n3ral_at_w0rk}">

kali@kali.org$

```
