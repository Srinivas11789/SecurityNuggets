// # The passcode seems to be a ??? char/digit combination --> bruteforce?
// # * Strict comparison is used, so we cant use equality or comparison bugs
// # Before bruteforce ==> Lets check extract vuln --> we have to pass an array to the GET query

<?php
$passcode = "Hi\n";
echo "Welcome\n";
extract($_GET);
echo file_get_contents("auth.php");
echo $input;
if ($input) {
   if ($input === file_get_contents($passcode, false, null, 0, 4)) {
     echo "flag!\n";
   } else {
     echo "Invalid!\n";
   }
}
?>
