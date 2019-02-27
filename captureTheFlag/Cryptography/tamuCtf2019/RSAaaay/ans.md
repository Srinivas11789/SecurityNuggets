Less confidence on Crypto Challenge but knew the RSA concept so took it over...

Steps tried:
1) As it was an easy challenge assumed just (n,d) were given to decrypt ( big math operation challenge and RSA operates on numbers for enc/dec )
  - string --> hex --> int
2) Assumed p, q to be given to compute rsa 
   - after few failed attempt, remembered something --> one of the number in the given pair () was not prime. So it was meaningless to assume p, q. So the number that is not prime should be n
3) Assume the given pair is (n, d)
   - Ended up at Alok's blog to crack rsa
   - Key crack and generation was success, but decryption failed. Even tried space separated data. did not work
   - Used the same params and performed decryption on the crypttool and the converted the integers obtained to char


Reference:
* Alok's Blog Helped a lot for this challenge: https://www.quaxio.com/exploring_three_weaknesses_in_rsa/
* https://www.cryptool.org/en/cto-highlights/rsa-step-by-step
* https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html
* https://asecuritysite.com/Encryption/rsa?val=11%2C3%2C3%2C4

Other dig/helpers:
* https://www.dcode.fr/rsa-cipher
* http://www.math.com/students/calculators/source/prime-number.htm
* https://crypto.stackexchange.com/questions/10590/what-makes-rsa-secure-by-using-prime-numbers
* https://www.mtholyoke.edu/courses/quenell/s2003/ma139/js/powermod.html
* https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#key-loading
* http://billatnapier.com/2011_tut_encryption.pdf
* https://gist.github.com/AArnott/c105f9a1c8ebf546a027
* https://www.calculator.net/big-number-calculator.html?cx=906851&cy=2531257&cp=20&co=pow
* 
