 ### Challenge

 ```
crypto/pseudo-key
Boolean

Keys are not always as they seem...

Note: Make sure to wrap the plaintext with flag{} before you submit!
 ```

 ### Recon
* Script, flag for sure is not in the format with the flag{} as the flag string for plaintext is from 5:-1
* Created reverse key function based on,
  * The encrypt arguments were both same as the key is same
  * assuming to reverse this logic --> `(x + y) % 26` we can do 2 things
    * //2 to get exactly half
    * Kind of implement the modular inverse
* Got plaintext flags applying each of these techniques. 
* Was able to figure out the flag using both plains

 ### Solve

```
> python pseudo-key.py 
('Pseudo-key:', 'qqmikkkaiyu')
('ReversedKey1:', 'rrqpwwwnpts')
('ReversedKey2:', 'eedcjjjacgf')
('Plain from key1:', 'i_tuess_csruqb_keys_aee_cseudo_srchee')
('Plain from key2:', 'v_ghrff_pfehdo_xrlf_nrr_pfrhqb_fepurr')
```

* Combining these 2, we get the flag --> `i_guess_pseudo_keys_are_pseudo_secure`