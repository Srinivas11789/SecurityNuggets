### Challenge

```
ShifterMisc160167
What a strange challenge...

It'll be no problem for you, of course!

nc misc.2020.chall.actf.co 20300
```

### Recon

```
(env) Srinivass-MacBook-Pro:magicWord darkknight$ nc misc.2020.chall.actf.co 20300

Solve 50 of these epic problems in a row to prove you are a master crypto man like Aplet123!
You'll be given a number n and also a plaintext p.
Caesar shift `p` with the nth Fibonacci number.
n < 50, p is completely uppercase and alphabetic, len(p) < 50
You have 60 seconds!
--------------------
Shift HJUOWLTZMKGBLWMTSSUZVPLNYTAOTVXWKEDFKYPLISWQKIP by n=49
: Sorry, you got it wrong. The answer was UWHBJYGMZXTOYJZGFFHMICYALGNBGIKJXRQSXLCYVFJDXVC. Better luck next time!
(env) Srinivass-MacBook-Pro:magicWord darkknight$ 
```

### Solve

```
(env) Srinivass-MacBook-Pro:shifter darkknight$ python3 solve.py 
[+] Opening connection to misc.2020.chall.actf.co on port 20300: Done
b"Solve 50 of these epic problems in a row to prove you are a master crypto man like Aplet123!\nYou'll be given a number n and also a plaintext p.\nCaesar shift `p` with the nth Fibonacci number.\nn < 50, p is completely uppercase and alphabetic, len(p) < 50\nYou have 60 seconds!\n--------------------\n"
b'Shift XGKRVOSTYXCPCBBQSNITYUUVNOMVE by n=41\n'
b'XGKRVOSTYXCPCBBQSNITYUUVNOMVE' 165580141
WFJQUNRSXWBOBAAPRMHSXTTUMNLUD
b': Shift CPLXVSAHZYUCKVWQVBANXTOENFKKCLWCKUVJYLLEEVHWCW by n=42\n'
b'CPLXVSAHZYUCKVWQVBANXTOENFKKCLWCKUVJYLLEEVHWCW' 267914296
CPLXVSAHZYUCKVWQVBANXTOENFKKCLWCKUVJYLLEEVHWCW
b': Shift TRFDRDKJZLSLTNVCQIUKWQCAWPXRZOMTKNESSRKFOOFTJG by n=35\n'
b'TRFDRDKJZLSLTNVCQIUKWQCAWPXRZOMTKNESSRKFOOFTJG' 9227465
GESQEQXWMYFYGAIPDVHXJDPNJCKEMBZGXARFFEXSBBSGWT
b': Shift  by n=20\n'
b'' 6765

b': Shift WRESQAGFINLCCXUVEIUXNEXHVMHTGP by n=49\n'
b'WRESQAGFINLCCXUVEIUXNEXHVMHTGP' 7778742049
JERFDNTSVAYPPKHIRVHKARKUIZUGTC
b': Shift EFVEFVJC by n=33\n'
b'EFVEFVJC' 3524578
WXNWXNBU
b': Shift ATUEWCQVVSJLLWSLKZ by n=37\n'
b'ATUEWCQVVSJLLWSLKZ' 24157817
VOPZRXLQQNEGGRNGFU
b': Shift ZNPE by n=6\n'
b'ZNPE' 8
HVXM
b': Shift TKFDCGRBXBZHUJIJPDHISTOVYTIEJLQZVLLCCGABPPVOQQ by n=36\n'
b'TKFDCGRBXBZHUJIJPDHISTOVYTIEJLQZVLLCCGABPPVOQQ' 14930352
BSNLKOZJFJHPCRQRXLPQABWDGBQMRTYHDTTKKOIJXXDWYY
b': Shift TVZYMCGWNCIVNEMFESCBEISGDTTNFUDISTMYIZWVL by n=19\n'
b'TVZYMCGWNCIVNEMFESCBEISGDTTNFUDISTMYIZWVL' 4181
OQUTHXBRIXDQIZHAZNXWZDNBYOOIAPYDNOHTDURQG
b': Shift KRA by n=16\n'
b'KRA' 987
JQZ
b': Shift OXRH by n=34\n'
b'OXRH' 5702887
JSMC
b': Shift HMADLQRGYLBPXNXULCRNRLHWXLOAPVPRTWVJGGHVW by n=46\n'
b'HMADLQRGYLBPXNXULCRNRLHWXLOAPVPRTWVJGGHVW' 1836311903
EJXAINODVIYMUKURIZOKOIETUILXMSMOQTSGDDEST
b': Shift UBSQEPQUTSUFOYBOILJIDYVCJVYGOHZPIEY by n=0\n'
b'UBSQEPQUTSUFOYBOILJIDYVCJVYGOHZPIEY' 0
UBSQEPQUTSUFOYBOILJIDYVCJVYGOHZPIEY
b': Shift LBTHKZSVRXSDFSYCQLZJLUAWRFJNYRULOSJ by n=43\n'
b'LBTHKZSVRXSDFSYCQLZJLUAWRFJNYRULOSJ' 433494437
KASGJYRUQWRCERXBPKYIKTZVQEIMXQTKNRI
b': Shift LWJCGOYLEUIKGLABDRKPPNQIZISDOGICBHGLFKBDPZXUVP by n=30\n'
b'LWJCGOYLEUIKGLABDRKPPNQIZISDOGICBHGLFKBDPZXUVP' 832040
ZKXQUCMZSIWYUZOPRFYDDBEWNWGRCUWQPVUZTYPRDNLIJD
b': Shift P by n=32\n'
b'P' 2178309
S
b': Shift SDNIIHJSQZ by n=30\n'
b'SDNIIHJSQZ' 832040
GRBWWVXGEN
b': Shift WSAJRCAIWABSNBOOJPWMWSIMZIT by n=35\n'
b'WSAJRCAIWABSNBOOJPWMWSIMZIT' 9227465
JFNWEPNVJNOFAOBBWCJZJFVZMVG
b': Shift ERKTOLGLPGBEXPYKXOOOSZQPWCOPKT by n=29\n'
b'ERKTOLGLPGBEXPYKXOOOSZQPWCOPKT' 514229
FSLUPMHMQHCFYQZLYPPPTARQXDPQLU
b': Shift KJSQOQ by n=41\n'
b'KJSQOQ' 165580141
JIRPNP
b': Shift IKMECWSSTKWFDEGEHLSNQQNIBT by n=37\n'
b'IKMECWSSTKWFDEGEHLSNQQNIBT' 24157817
DFHZXRNNOFRAYZBZCGNILLIDWO
b': Shift RSFGFRXAANMRARZMFHIOYSMOJF by n=45\n'
b'RSFGFRXAANMRARZMFHIOYSMOJF' 1134903170
PQDEDPVYYLKPYPXKDFGMWQKMHD
b': Shift WVMKVONP by n=24\n'
b'WVMKVONP' 46368
GFWUFYXZ
b': Shift BPJFURIOXVFHSLDGKC by n=37\n'
b'BPJFURIOXVFHSLDGKC' 24157817
WKEAPMDJSQACNGYBFX
b': Shift ULHHNQFAJAXTWROLTFFRVNGYHRBOLZXDQIMELLQPJM by n=49\n'
b'ULHHNQFAJAXTWROLTFFRVNGYHRBOLZXDQIMELLQPJM' 7778742049
HYUUADSNWNKGJEBYGSSEIATLUEOBYMKQDVZRYYDCWZ
b': Shift OIIWLDVQWEJJE by n=9\n'
b'OIIWLDVQWEJJE' 34
WQQETLDYEMRRM
b': Shift HVPPCRDQEIFNEONDKSJLIXUTNHZYWWCVERIFENMXYSNMYUOJW by n=35\n'
b'HVPPCRDQEIFNEONDKSJLIXUTNHZYWWCVERIFENMXYSNMYUOJW' 9227465
UICCPEQDRVSARBAQXFWYVKHGAUMLJJPIREVSRAZKLFAZLHBWJ
b': Shift XYFTMCBCLFBEQUAQU by n=22\n'
b'XYFTMCBCLFBEQUAQU' 17711
CDKYRHGHQKGJVZFVZ
b': Shift Q by n=33\n'
b'Q' 3524578
I
b': Shift IQIGMHZXFONJMBJSUJRZH by n=6\n'
b'IQIGMHZXFONJMBJSUJRZH' 8
QYQOUPHFNWVRUJRACRZHP
b': Shift IDSCZACKGHMGBUA by n=4\n'
b'IDSCZACKGHMGBUA' 3
LGVFCDFNJKPJEXD
b': Shift HEGHSPSMUKWQGNWZFQWDCBOWAOROTOMOJRZ by n=15\n'
b'HEGHSPSMUKWQGNWZFQWDCBOWAOROTOMOJRZ' 610
TQSTEBEYGWICSZILRCIPONAIMADAFAYAVDL
b': Shift EQQEKUCWCADCRIMWGQRHMCIGK by n=46\n'
b'EQQEKUCWCADCRIMWGQRHMCIGK' 1836311903
BNNBHRZTZXAZOFJTDNOEJZFDH
b': Shift WYLTBQOAPDMPQFEIGLMMJQAIKLFBR by n=9\n'
b'WYLTBQOAPDMPQFEIGLMMJQAIKLFBR' 34
EGTBJYWIXLUXYNMQOTUURYIQSTNJZ
b': Shift TMZEGEUOFDHUGNYSIMEINYYEEIKACK by n=38\n'
b'TMZEGEUOFDHUGNYSIMEINYYEEIKACK' 39088169
WPCHJHXRIGKXJQBVLPHLQBBHHLNDFN
b': Shift CAARIIZW by n=38\n'
b'CAARIIZW' 39088169
FDDULLCZ
b': Shift YSLVIJMPXTZHVWQXIDUCSDKKLUEIMOF by n=36\n'
b'YSLVIJMPXTZHVWQXIDUCSDKKLUEIMOF' 14930352
GATDQRUXFBHPDEYFQLCKALSSTCMQUWN
b': Shift JAUJVHDBSGTGGYFORNRBNZSCMYXEKUCMDRZWTRYZ by n=37\n'
b'JAUJVHDBSGTGGYFORNRBNZSCMYXEKUCMDRZWTRYZ' 24157817
EVPEQCYWNBOBBTAJMIMWIUNXHTSZFPXHYMUROMTU
b': Shift TSRPRDGWRVYEPVVCITDXHQVVJOTKYPAWE by n=14\n'
b'TSRPRDGWRVYEPVVCITDXHQVVJOTKYPAWE' 377
GFECEQTJEILRCIIPVGQKUDIIWBGXLCNJR
b': Shift FVZRWRCUFQ by n=19\n'
b'FVZRWRCUFQ' 4181
AQUMRMXPAL
b': Shift MXLBQKVVZPDLWFKHGARQGEJZVSYSKWXFIOLVS by n=16\n'
b'MXLBQKVVZPDLWFKHGARQGEJZVSYSKWXFIOLVS' 987
LWKAPJUUYOCKVEJGFZQPFDIYURXRJVWEHNKUR
b': Shift OLTQETMG by n=2\n'
b'OLTQETMG' 1
PMURFUNH
b': Shift RRTFGVFDBQOHWCEFZONKAJGWSNDUO by n=42\n'
b'RRTFGVFDBQOHWCEFZONKAJGWSNDUO' 267914296
RRTFGVFDBQOHWCEFZONKAJGWSNDUO
b': Shift SPKEBTXZUAMHWROUTWWEKSA by n=5\n'
b'SPKEBTXZUAMHWROUTWWEKSA' 5
XUPJGYCEZFRMBWTZYBBJPXF
b': Shift IINOKBGOMXURGWXJMLTYQKQA by n=21\n'
b'IINOKBGOMXURGWXJMLTYQKQA' 10946
IINOKBGOMXURGWXJMLTYQKQA
b': Shift OVREIDREUUQEVMKCMJYALFQXAHODIXCHDZQIIG by n=15\n'
b'OVREIDREUUQEVMKCMJYALFQXAHODIXCHDZQIIG' 610
AHDQUPDQGGCQHYWOYVKMXRCJMTAPUJOTPLCUUS
b': Shift TJCGDLSUVKSGBKWABSKVNUT by n=33\n'
b'TJCGDLSUVKSGBKWABSKVNUT' 3524578
LBUYVDKMNCKYTCOSTKCNFML
b': Shift TORCYQZTMQYOXYOEPSEPMAYIYLCAHFHD by n=20\n'
b'TORCYQZTMQYOXYOEPSEPMAYIYLCAHFHD' 6765
YTWHDVEYRVDTCDTJUXJURFDNDQHFMKMI
b': Shift NSZP by n=30\n'
b'NSZP' 832040
BGND
b': actf{h0p3_y0u_us3d_th3_f0rmu14-1985098}\n'
Traceback (most recent call last):
  File "solve.py", line 83, in <module>
    main()
  File "solve.py", line 80, in main
    talk(address, port, output_key_to_read_until)
  File "solve.py", line 70, in talk
    connection.sendline(processResponse(response))
  File "solve.py", line 50, in processResponse
    plain_text = data[1]
IndexError: list index out of range
(env) Srinivass-MacBook-Pro:shifter darkknight$ 
```