<html>
<head>
  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/default.min.css">
  <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/highlight.min.js"></script>
  <script>hljs.initHighlightingOnLoad();</script>
</head>
<body>
  <pre>
    <code class="php">
      // Pseudocode
      $passcode = '???';
      $flag = '????'

      extract($_GET);
      if (($input is detected)) {
        if ($input === get_contents($passcode)) {
          return $flag
        } else {
          echo "Invalid ... Please try again!"
        }
      }
    </code>
  </pre>
</body>
</html>

