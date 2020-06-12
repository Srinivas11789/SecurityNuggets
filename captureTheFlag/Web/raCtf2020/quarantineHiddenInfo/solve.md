kali@kali:~$ 
kali@kali:~$ curl http://88.198.219.20:29593
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Really Awesome Quarantine Entertainment</title>
    
<link rel="stylesheet" href="/static/home.css" type="text/css">

    <link rel="stylesheet" href="/static/style.css" type="text/css">
</head>
<body>
    <div class="menu">
        <p class="menu-item menu-home"><a class="menu-link" href="/">RAQE</a></p>
    </div>
    
<div class="attention-grabber">
    <center>
        <div class="heading">
            <h1 class="title">Really Awesome Quarantine Entertainment</h1>
            <h3 class="subtitle">Stuck in quarantine? Us too! We've put together a handy library full of awesome hacking-related content for you to browse at one low monthly fee!</h3>
        </div>
        <br/>
        <div class="buttons">
            <button onclick="document.location.href='/sign-in';" class="button sign-in">Sign in</button>
            <button onclick="document.location.href='/sign-up';" class="button sign-up">Sign up</button>
        </div>
    </center>
</div>

    <div class="footer-container">
        <div class="footer">
            
                <p class="menu-item footer-item"><a class="menu-link" href="/sign-in">Login</a></p>
                <p class="menu-item footer-item"><a class="menu-link" href="/sign-up">Register</a></p>
            
            <p class="menu-item footer-item footer-right"><a class="menu-link" href="/admin">Admin</a></p>
        </div>
    </div>
</body>
</html>kali@kali:~$ curl http://88.198.219.20:29593/robots.txt
User-Agent: *
Disallow: /admin-stashkali@kali:~$ curl http://88.198.219.20:29593/admin-stash
ractf{1m_n0t_4_r0b0T}kali@kali:~$ 
