### Challenge
```
Rotten
100
Ick, this salad doesn't taste too good!
```

### Recon
* Connect and check
```
nc jh2i.com 50034
send back this line exactly. no flag here, just filler.
send back this line exactly. no flag here, just filler.
kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 6 gx lzw xdsy ak 'g'
kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 6 gx lzw xdsy ak 'g'
FAILURE
```

* Salad in chal description is hint --> caesar maybe
```
kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 6 gx lzw xdsy ak 'g'

send back this line exactly. character 6 of the flag is 'o'
```

### Solve

* Script
```
import sys

try:
    from pwn import *
except ImportError:
    print("In order to complete this challenge, please install pwntools")
    print("https://pwntools.readthedocs.io/en/stable/install.html")
    sys.exit(1)

flag = ["" for i in range(50)]

def processResponse(data):
    data = data.decode("utf-8").strip()
    print("Got..." + data)
    message = caesarDecode(data)
    print("Sending... " + message)
    if "character" in message:
        # send back this line exactly. character 25 of the flag is 'e'
        m = message.split(" ")
        index = int(m[-6])
        flag[index] = m[-1].strip("'")
    #print(flag)
    return message

def caesarDecode(message):
    cipherText = list(message)
    for i in range(0, 26):
        plainText = ""
        for j in range(len(cipherText)):
            if not cipherText[j].isalpha():
                plainText += cipherText[j]
            else:
                caesar_plain = ord(cipherText[j])+i
                if caesar_plain > 122:
                    caesar_plain = caesar_plain - 122
                    while (caesar_plain - 122) > 122:
                        caesar_plain = caesar_plain - 122
                    caesar_plain = 96 + caesar_plain
                plainText += chr(caesar_plain)
        #print(plainText)
        if "flag" in plainText:
            return plainText
    return ""

def talk(address, port, key):
    connection = remote(address, port)
    response = connection.recvuntil(".\n")
    response = response.decode("utf-8")
    print("Got... " + response)
    connection.sendline(response.strip())
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
            print("".join(flag))
            connection.interactive()
        connection.sendline(processResponse(response))

def main():
    try:
        address = "jh2i.com"
        port = "50034"
        output_key_to_read_until = "\n"
    except:
        print("Usage: ./client.py [IP] [Port] [Key]")
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()
```

* Output
```
$ python3 solve.py 
[+] Opening connection to jh2i.com on port 50034: Done
Got... send back this line exactly. no flag here, just filler.

Got...nziy wvxf ocdn gdiz zsvxogt. xcvmvxozm 3 ja ocz agvb dn 'b'
Sending... send back this line exactly. character 3 of the flag is 'g'
Got...dpyo mlnv estd wtyp pilnewj. yz qwlr spcp, ufde qtwwpc.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. vatktvmxk 12 hy max yetz bl '_'
Sending... send back this line exactly. character 12 of the flag is '_'
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...gsbr poqy hvwg zwbs sloqhzm. bc tzou vsfs, xigh twzzsf.
Sending... send back this line exactly. no flag here, just filler.
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...fraq onpx guvf yvar rknpgyl. punenpgre 4 bs gur synt vf '{'
Sending... send back this line exactly. character 4 of the flag is '{'
Got...yktj hgiq znoy rotk kdgizre. tu lrgm nkxk, payz lorrkx.
Sending... send back this line exactly. no flag here, just filler.
Got...oajz xwyg pdeo heja atwyphu. ydwnwypan 26 kb pda bhwc eo 'o'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...ugpf dcem vjku nkpg gzcevna. pq hnci jgtg, lwuv hknngt.
Sending... send back this line exactly. no flag here, just filler.
Got...eqzp nmow ftue xuzq qjmofxk. za rxms tqdq, vgef ruxxqd.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. gh yetz axkx, cnlm ybeexk.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 26 yp dro pvkq sc 'c'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 14 tk ymj kqfl nx 's'
Sending... send back this line exactly. character 14 of the flag is 'n'
Got...coxn lkmu drsc vsxo ohkmdvi. xy pvkq robo, tecd psvvob.
Sending... send back this line exactly. no flag here, just filler.
Got...myhx vuwe nbcm fchy yruwnfs. wbuluwnyl 25 iz nby zfua cm 'y'
Sending... send back this line exactly. character 25 of the flag is 'e'
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...nziy wvxf ocdn gdiz zsvxogt. ij agvb czmz, epno adggzm.
Sending... send back this line exactly. no flag here, just filler.
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 29 ne sgd ekzf hr 'r'
Sending... send back this line exactly. character 29 of the flag is 's'
Got...pbka yxzh qefp ifkb buxzqiv. zexoxzqbo 19 lc qeb cixd fp 'l'
Sending... send back this line exactly. character 19 of the flag is 'o'
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...vhqg edfn wklv olqh hadfwob. qr iodj khuh, mxvw iloohu.
Sending... send back this line exactly. no flag here, just filler.
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...iudt rqsa jxyi bydu unqsjbo. de vbqw xuhu, zkij vybbuh.
Sending... send back this line exactly. no flag here, just filler.
Got...zluk ihjr aopz spul lehjasf. johyhjaly 6 vm aol mshn pz 'v'
Sending... send back this line exactly. character 6 of the flag is 'o'
Got...fraq onpx guvf yvar rknpgyl. punenpgre 30 bs gur synt vf '}'
Sending... send back this line exactly. character 30 of the flag is '}'
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 29 yp dro pvkq sc 'c'
Sending... send back this line exactly. character 29 of the flag is 's'
Got...zluk ihjr aopz spul lehjasf. uv mshn olyl, qbza mpssly.
Sending... send back this line exactly. no flag here, just filler.
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 10 gx lzw xdsy ak 'g'
Sending... send back this line exactly. character 10 of the flag is 'o'
Got...wirh fego xlmw pmri ibegxpc. glevegxiv 13 sj xli jpek mw 'o'
Sending... send back this line exactly. character 13 of the flag is 'k'
Got...kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 30 gx lzw xdsy ak '}'
Sending... send back this line exactly. character 30 of the flag is '}'
Got...oajz xwyg pdeo heja atwyphu. ydwnwypan 20 kb pda bhwc eo 'q'
Sending... send back this line exactly. character 20 of the flag is 'u'
Got...yktj hgiq znoy rotk kdgizre. ingxgizkx 12 ul znk lrgm oy '_'
Sending... send back this line exactly. character 12 of the flag is '_'
Got...yktj hgiq znoy rotk kdgizre. tu lrgm nkxk, payz lorrkx.
Sending... send back this line exactly. no flag here, just filler.
Got...qclb zyai rfgq jglc cvyarjw. afypyarcp 14 md rfc djye gq 'l'
Sending... send back this line exactly. character 14 of the flag is 'n'
Got...xjsi gfhp ymnx qnsj jcfhyqd. st kqfl mjwj, ozxy knqqjw.
Sending... send back this line exactly. no flag here, just filler.
Got...bnwm kjlt cqrb urwn ngjlcuh. lqjajlcna 30 xo cqn oujp rb '}'
Sending... send back this line exactly. character 30 of the flag is '}'
Got...wirh fego xlmw pmri ibegxpc. glevegxiv 11 sj xli jpek mw 'y'
Sending... send back this line exactly. character 11 of the flag is 'u'
Got...pbka yxzh qefp ifkb buxzqiv. kl cixd ebob, grpq cfiibo.
Sending... send back this line exactly. no flag here, just filler.
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 21 ne sgd ekzf hr 'q'
Sending... send back this line exactly. character 21 of the flag is 'r'
Got...zluk ihjr aopz spul lehjasf. uv mshn olyl, qbza mpssly.
Sending... send back this line exactly. no flag here, just filler.
Got...vhqg edfn wklv olqh hadfwob. qr iodj khuh, mxvw iloohu.
Sending... send back this line exactly. no flag here, just filler.
Got...bnwm kjlt cqrb urwn ngjlcuh. wx oujp qnan, sdbc oruuna.
Sending... send back this line exactly. no flag here, just filler.
Got...nziy wvxf ocdn gdiz zsvxogt. xcvmvxozm 3 ja ocz agvb dn 'b'
Sending... send back this line exactly. character 3 of the flag is 'g'
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 5 tk ymj kqfl nx 's'
Sending... send back this line exactly. character 5 of the flag is 'n'
Got...pbka yxzh qefp ifkb buxzqiv. kl cixd ebob, grpq cfiibo.
Sending... send back this line exactly. no flag here, just filler.
Got...amvl jiks bpqa tqvm mfikbtg. kpizikbmz 26 wn bpm ntio qa 'a'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...qclb zyai rfgq jglc cvyarjw. afypyarcp 16 md rfc djye gq 'u'
Sending... send back this line exactly. character 16 of the flag is 'w'
Got...bnwm kjlt cqrb urwn ngjlcuh. wx oujp qnan, sdbc oruuna.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 22 yp dro pvkq sc '_'
Sending... send back this line exactly. character 22 of the flag is '_'
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 4 pg uif gmbh jt '{'
Sending... send back this line exactly. character 4 of the flag is '{'
Got...myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
Sending... send back this line exactly. no flag here, just filler.
Got...iudt rqsa jxyi bydu unqsjbo. sxqhqsjuh 8 ev jxu vbqw yi '_'
Sending... send back this line exactly. character 8 of the flag is '_'
Got...jveu srtb kyzj czev vortkcp. tyrirtkvi 22 fw kyv wcrx zj '_'
Sending... send back this line exactly. character 22 of the flag is '_'
Got...zluk ihjr aopz spul lehjasf. johyhjaly 29 vm aol mshn pz 'z'
Sending... send back this line exactly. character 29 of the flag is 's'
Got...bnwm kjlt cqrb urwn ngjlcuh. lqjajlcna 11 xo cqn oujp rb 'd'
Sending... send back this line exactly. character 11 of the flag is 'u'
Got...fraq onpx guvf yvar rknpgyl. punenpgre 25 bs gur synt vf 'r'
Sending... send back this line exactly. character 25 of the flag is 'e'
Got...qclb zyai rfgq jglc cvyarjw. afypyarcp 19 md rfc djye gq 'm'
Sending... send back this line exactly. character 19 of the flag is 'o'
Got...ugpf dcem vjku nkpg gzcevna. pq hnci jgtg, lwuv hknngt.
Sending... send back this line exactly. no flag here, just filler.
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...fraq onpx guvf yvar rknpgyl. punenpgre 4 bs gur synt vf '{'
Sending... send back this line exactly. character 4 of the flag is '{'
Got...dpyo mlnv estd wtyp pilnewj. yz qwlr spcp, ufde qtwwpc.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 14 yp dro pvkq sc 'x'
Sending... send back this line exactly. character 14 of the flag is 'n'
Got...myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
Sending... send back this line exactly. no flag here, just filler.
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 18 ne sgd ekzf hr 'x'
Sending... send back this line exactly. character 18 of the flag is 'y'
Got...dpyo mlnv estd wtyp pilnewj. nslclnepc 17 zq esp qwlr td '_'
Sending... send back this line exactly. character 17 of the flag is '_'
Got...zluk ihjr aopz spul lehjasf. johyhjaly 10 vm aol mshn pz 'v'
Sending... send back this line exactly. character 10 of the flag is 'o'
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 25 pg uif gmbh jt 'f'
Sending... send back this line exactly. character 25 of the flag is 'e'
Got...lxgw utvd mabl ebgx xqtvmer. gh yetz axkx, cnlm ybeexk.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 1 yp dro pvkq sc 'v'
Sending... send back this line exactly. character 1 of the flag is 'l'
Got...qclb zyai rfgq jglc cvyarjw. afypyarcp 26 md rfc djye gq 'q'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 27 tk ymj kqfl nx 'f'
Sending... send back this line exactly. character 27 of the flag is 'a'
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. xy pvkq robo, tecd psvvob.
Sending... send back this line exactly. no flag here, just filler.
Got...gsbr poqy hvwg zwbs sloqhzm. qvofoqhsf 9 ct hvs tzou wg 'm'
Sending... send back this line exactly. character 9 of the flag is 'y'
Got...iudt rqsa jxyi bydu unqsjbo. sxqhqsjuh 13 ev jxu vbqw yi 'a'
Sending... send back this line exactly. character 13 of the flag is 'k'
Got...gsbr poqy hvwg zwbs sloqhzm. qvofoqhsf 13 ct hvs tzou wg 'y'
Sending... send back this line exactly. character 13 of the flag is 'k'
Got...pbka yxzh qefp ifkb buxzqiv. zexoxzqbo 8 lc qeb cixd fp '_'
Sending... send back this line exactly. character 8 of the flag is '_'
Got...fraq onpx guvf yvar rknpgyl. ab synt urer, whfg svyyre.
Sending... send back this line exactly. no flag here, just filler.
Got...wirh fego xlmw pmri ibegxpc. glevegxiv 7 sj xli jpek mw 'a'
Sending... send back this line exactly. character 7 of the flag is 'w'
Got...yktj hgiq znoy rotk kdgizre. ingxgizkx 11 ul znk lrgm oy 'a'
Sending... send back this line exactly. character 11 of the flag is 'u'
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...dpyo mlnv estd wtyp pilnewj. nslclnepc 4 zq esp qwlr td '{'
Sending... send back this line exactly. character 4 of the flag is '{'
Got...pbka yxzh qefp ifkb buxzqiv. kl cixd ebob, grpq cfiibo.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. xy pvkq robo, tecd psvvob.
Sending... send back this line exactly. no flag here, just filler.
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 3 tk ymj kqfl nx 'l'
Sending... send back this line exactly. character 3 of the flag is 'g'
Got...kwfv tsuc lzak dafw wpsuldq. fg xdsy zwjw, bmkl xaddwj.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...amvl jiks bpqa tqvm mfikbtg. kpizikbmz 10 wn bpm ntio qa 'w'
Sending... send back this line exactly. character 10 of the flag is 'o'
Got...yktj hgiq znoy rotk kdgizre. ingxgizkx 24 ul znk lrgm oy 'g'
Sending... send back this line exactly. character 24 of the flag is 'a'
Got...wirh fego xlmw pmri ibegxpc. glevegxiv 21 sj xli jpek mw 'v'
Sending... send back this line exactly. character 21 of the flag is 'r'
Got...zluk ihjr aopz spul lehjasf. uv mshn olyl, qbza mpssly.
Sending... send back this line exactly. no flag here, just filler.
Got...gsbr poqy hvwg zwbs sloqhzm. qvofoqhsf 20 ct hvs tzou wg 'i'
Sending... send back this line exactly. character 20 of the flag is 'u'
Got...bnwm kjlt cqrb urwn ngjlcuh. wx oujp qnan, sdbc oruuna.
Sending... send back this line exactly. no flag here, just filler.
Got...wirh fego xlmw pmri ibegxpc. glevegxiv 0 sj xli jpek mw 'j'
Sending... send back this line exactly. character 0 of the flag is 'f'
Got...htcs qprz iwxh axct tmprian. rwpgpritg 22 du iwt uapv xh '_'
Sending... send back this line exactly. character 22 of the flag is '_'
Got...ugpf dcem vjku nkpg gzcevna. ejctcevgt 6 qh vjg hnci ku 'q'
Sending... send back this line exactly. character 6 of the flag is 'o'
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 12 pg uif gmbh jt '_'
Sending... send back this line exactly. character 12 of the flag is '_'
Got...eqzp nmow ftue xuzq qjmofxk. otmdmofqd 17 ar ftq rxms ue '_'
Sending... send back this line exactly. character 17 of the flag is '_'
Got...oajz xwyg pdeo heja atwyphu. ydwnwypan 11 kb pda bhwc eo 'q'
Sending... send back this line exactly. character 11 of the flag is 'u'
Got...iudt rqsa jxyi bydu unqsjbo. de vbqw xuhu, zkij vybbuh.
Sending... send back this line exactly. no flag here, just filler.
Got...xjsi gfhp ymnx qnsj jcfhyqd. st kqfl mjwj, ozxy knqqjw.
Sending... send back this line exactly. no flag here, just filler.
Got...rdmc azbj sghr khmd dwzbskx. mn ekzf gdqd, itrs ehkkdq.
Sending... send back this line exactly. no flag here, just filler.
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...eqzp nmow ftue xuzq qjmofxk. otmdmofqd 8 ar ftq rxms ue '_'
Sending... send back this line exactly. character 8 of the flag is '_'
Got...dpyo mlnv estd wtyp pilnewj. nslclnepc 25 zq esp qwlr td 'p'
Sending... send back this line exactly. character 25 of the flag is 'e'
Got...pbka yxzh qefp ifkb buxzqiv. kl cixd ebob, grpq cfiibo.
Sending... send back this line exactly. no flag here, just filler.
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 2 pg uif gmbh jt 'b'
Sending... send back this line exactly. character 2 of the flag is 'a'
Got...yktj hgiq znoy rotk kdgizre. ingxgizkx 7 ul znk lrgm oy 'c'
Sending... send back this line exactly. character 7 of the flag is 'w'
Got...qclb zyai rfgq jglc cvyarjw. lm djye fcpc, hsqr dgjjcp.
Sending... send back this line exactly. no flag here, just filler.
Got...myhx vuwe nbcm fchy yruwnfs. wbuluwnyl 17 iz nby zfua cm '_'
Sending... send back this line exactly. character 17 of the flag is '_'
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 22 pg uif gmbh jt '_'
Sending... send back this line exactly. character 22 of the flag is '_'
Got...myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
Sending... send back this line exactly. no flag here, just filler.
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...pbka yxzh qefp ifkb buxzqiv. zexoxzqbo 22 lc qeb cixd fp '_'
Sending... send back this line exactly. character 22 of the flag is '_'
Got...nziy wvxf ocdn gdiz zsvxogt. ij agvb czmz, epno adggzm.
Sending... send back this line exactly. no flag here, just filler.
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...bnwm kjlt cqrb urwn ngjlcuh. lqjajlcna 16 xo cqn oujp rb 'f'
Sending... send back this line exactly. character 16 of the flag is 'w'
Got...qclb zyai rfgq jglc cvyarjw. lm djye fcpc, hsqr dgjjcp.
Sending... send back this line exactly. no flag here, just filler.
Got...myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
Sending... send back this line exactly. no flag here, just filler.
Got...eqzp nmow ftue xuzq qjmofxk. za rxms tqdq, vgef ruxxqd.
Sending... send back this line exactly. no flag here, just filler.
Got...gsbr poqy hvwg zwbs sloqhzm. bc tzou vsfs, xigh twzzsf.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. gh yetz axkx, cnlm ybeexk.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. xy pvkq robo, tecd psvvob.
Sending... send back this line exactly. no flag here, just filler.
Got...nziy wvxf ocdn gdiz zsvxogt. xcvmvxozm 9 ja ocz agvb dn 't'
Sending... send back this line exactly. character 9 of the flag is 'y'
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 6 pg uif gmbh jt 'p'
Sending... send back this line exactly. character 6 of the flag is 'o'
Got...eqzp nmow ftue xuzq qjmofxk. otmdmofqd 16 ar ftq rxms ue 'i'
Sending... send back this line exactly. character 16 of the flag is 'w'
Got...amvl jiks bpqa tqvm mfikbtg. kpizikbmz 6 wn bpm ntio qa 'w'
Sending... send back this line exactly. character 6 of the flag is 'o'
Got...xjsi gfhp ymnx qnsj jcfhyqd. st kqfl mjwj, ozxy knqqjw.
Sending... send back this line exactly. no flag here, just filler.
Got...pbka yxzh qefp ifkb buxzqiv. kl cixd ebob, grpq cfiibo.
Sending... send back this line exactly. no flag here, just filler.
Got...wirh fego xlmw pmri ibegxpc. rs jpek livi, nywx jmppiv.
Sending... send back this line exactly. no flag here, just filler.
Got...oajz xwyg pdeo heja atwyphu. ydwnwypan 29 kb pda bhwc eo 'o'
Sending... send back this line exactly. character 29 of the flag is 's'
Got...myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
Sending... send back this line exactly. no flag here, just filler.
Got...fraq onpx guvf yvar rknpgyl. ab synt urer, whfg svyyre.
Sending... send back this line exactly. no flag here, just filler.
Got...nziy wvxf ocdn gdiz zsvxogt. ij agvb czmz, epno adggzm.
Sending... send back this line exactly. no flag here, just filler.
Got...wirh fego xlmw pmri ibegxpc. rs jpek livi, nywx jmppiv.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. rwpgpritg 0 du iwt uapv xh 'u'
Sending... send back this line exactly. character 0 of the flag is 'f'
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 29 yp dro pvkq sc 'c'
Sending... send back this line exactly. character 29 of the flag is 's'
Got...yktj hgiq znoy rotk kdgizre. tu lrgm nkxk, payz lorrkx.
Sending... send back this line exactly. no flag here, just filler.
Got...amvl jiks bpqa tqvm mfikbtg. kpizikbmz 17 wn bpm ntio qa '_'
Sending... send back this line exactly. character 17 of the flag is '_'
Got...eqzp nmow ftue xuzq qjmofxk. za rxms tqdq, vgef ruxxqd.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 10 yp dro pvkq sc 'y'
Sending... send back this line exactly. character 10 of the flag is 'o'
Got...vhqg edfn wklv olqh hadfwob. qr iodj khuh, mxvw iloohu.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. vatktvmxk 24 hy max yetz bl 't'
Sending... send back this line exactly. character 24 of the flag is 'a'
Got...gsbr poqy hvwg zwbs sloqhzm. qvofoqhsf 13 ct hvs tzou wg 'y'
Sending... send back this line exactly. character 13 of the flag is 'k'
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. vatktvmxk 18 hy max yetz bl 'r'
Sending... send back this line exactly. character 18 of the flag is 'y'
Got...amvl jiks bpqa tqvm mfikbtg. vw ntio pmzm, rcab nqttmz.
Sending... send back this line exactly. no flag here, just filler.
Got...iudt rqsa jxyi bydu unqsjbo. sxqhqsjuh 11 ev jxu vbqw yi 'k'
Sending... send back this line exactly. character 11 of the flag is 'u'
Got...pbka yxzh qefp ifkb buxzqiv. zexoxzqbo 21 lc qeb cixd fp 'o'
Sending... send back this line exactly. character 21 of the flag is 'r'
Got...rdmc azbj sghr khmd dwzbskx. mn ekzf gdqd, itrs ehkkdq.
Sending... send back this line exactly. no flag here, just filler.
Got...rdmc azbj sghr khmd dwzbskx. mn ekzf gdqd, itrs ehkkdq.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...wirh fego xlmw pmri ibegxpc. rs jpek livi, nywx jmppiv.
Sending... send back this line exactly. no flag here, just filler.
Got...fraq onpx guvf yvar rknpgyl. punenpgre 21 bs gur synt vf 'e'
Sending... send back this line exactly. character 21 of the flag is 'r'
Got...fraq onpx guvf yvar rknpgyl. ab synt urer, whfg svyyre.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. xy pvkq robo, tecd psvvob.
Sending... send back this line exactly. no flag here, just filler.
Got...amvl jiks bpqa tqvm mfikbtg. kpizikbmz 26 wn bpm ntio qa 'a'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...bnwm kjlt cqrb urwn ngjlcuh. wx oujp qnan, sdbc oruuna.
Sending... send back this line exactly. no flag here, just filler.
Got...bnwm kjlt cqrb urwn ngjlcuh. wx oujp qnan, sdbc oruuna.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...xjsi gfhp ymnx qnsj jcfhyqd. st kqfl mjwj, ozxy knqqjw.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. vatktvmxk 2 hy max yetz bl 't'
Sending... send back this line exactly. character 2 of the flag is 'a'
Got...jveu srtb kyzj czev vortkcp. ef wcrx yviv, aljk wzccvi.
Sending... send back this line exactly. no flag here, just filler.
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 30 ne sgd ekzf hr '}'
Sending... send back this line exactly. character 30 of the flag is '}'
Got...ugpf dcem vjku nkpg gzcevna. ejctcevgt 24 qh vjg hnci ku 'c'
Sending... send back this line exactly. character 24 of the flag is 'a'
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 10 ne sgd ekzf hr 'n'
Sending... send back this line exactly. character 10 of the flag is 'o'
Got...gsbr poqy hvwg zwbs sloqhzm. qvofoqhsf 11 ct hvs tzou wg 'i'
Sending... send back this line exactly. character 11 of the flag is 'u'
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 28 tk ymj kqfl nx 'w'
Sending... send back this line exactly. character 28 of the flag is 'r'
Got...kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 29 gx lzw xdsy ak 'k'
Sending... send back this line exactly. character 29 of the flag is 's'
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. vatktvmxk 16 hy max yetz bl 'p'
Sending... send back this line exactly. character 16 of the flag is 'w'
Got...jveu srtb kyzj czev vortkcp. ef wcrx yviv, aljk wzccvi.
Sending... send back this line exactly. no flag here, just filler.
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 0 ne sgd ekzf hr 'e'
Sending... send back this line exactly. character 0 of the flag is 'f'
Got...htcs qprz iwxh axct tmprian. rwpgpritg 12 du iwt uapv xh '_'
Sending... send back this line exactly. character 12 of the flag is '_'
Got...nziy wvxf ocdn gdiz zsvxogt. xcvmvxozm 30 ja ocz agvb dn '}'
Sending... send back this line exactly. character 30 of the flag is '}'
Got...dpyo mlnv estd wtyp pilnewj. nslclnepc 21 zq esp qwlr td 'c'
Sending... send back this line exactly. character 21 of the flag is 'r'
Got...iudt rqsa jxyi bydu unqsjbo. de vbqw xuhu, zkij vybbuh.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 26 yp dro pvkq sc 'c'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...eqzp nmow ftue xuzq qjmofxk. otmdmofqd 17 ar ftq rxms ue '_'
Sending... send back this line exactly. character 17 of the flag is '_'
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 12 pg uif gmbh jt '_'
Sending... send back this line exactly. character 12 of the flag is '_'
Got...gsbr poqy hvwg zwbs sloqhzm. qvofoqhsf 27 ct hvs tzou wg 'o'
Sending... send back this line exactly. character 27 of the flag is 'a'
Got...eqzp nmow ftue xuzq qjmofxk. za rxms tqdq, vgef ruxxqd.
Sending... send back this line exactly. no flag here, just filler.
Got...dpyo mlnv estd wtyp pilnewj. nslclnepc 6 zq esp qwlr td 'z'
Sending... send back this line exactly. character 6 of the flag is 'o'
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 2 pg uif gmbh jt 'b'
Sending... send back this line exactly. character 2 of the flag is 'a'
Got...coxn lkmu drsc vsxo ohkmdvi. xy pvkq robo, tecd psvvob.
Sending... send back this line exactly. no flag here, just filler.
Got...myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. xy pvkq robo, tecd psvvob.
Sending... send back this line exactly. no flag here, just filler.
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 23 tk ymj kqfl nx 'h'
Sending... send back this line exactly. character 23 of the flag is 'c'
Got...jveu srtb kyzj czev vortkcp. tyrirtkvi 20 fw kyv wcrx zj 'l'
Sending... send back this line exactly. character 20 of the flag is 'u'
Got...bnwm kjlt cqrb urwn ngjlcuh. lqjajlcna 28 xo cqn oujp rb 'a'
Sending... send back this line exactly. character 28 of the flag is 'r'
Got...qclb zyai rfgq jglc cvyarjw. afypyarcp 14 md rfc djye gq 'l'
Sending... send back this line exactly. character 14 of the flag is 'n'
Got...eqzp nmow ftue xuzq qjmofxk. za rxms tqdq, vgef ruxxqd.
Sending... send back this line exactly. no flag here, just filler.
Got...jveu srtb kyzj czev vortkcp. tyrirtkvi 11 fw kyv wcrx zj 'l'
Sending... send back this line exactly. character 11 of the flag is 'u'
Got...pbka yxzh qefp ifkb buxzqiv. zexoxzqbo 26 lc qeb cixd fp 'p'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...bnwm kjlt cqrb urwn ngjlcuh. lqjajlcna 2 xo cqn oujp rb 'j'
Sending... send back this line exactly. character 2 of the flag is 'a'
Got...pbka yxzh qefp ifkb buxzqiv. kl cixd ebob, grpq cfiibo.
Sending... send back this line exactly. no flag here, just filler.
Got...nziy wvxf ocdn gdiz zsvxogt. ij agvb czmz, epno adggzm.
Sending... send back this line exactly. no flag here, just filler.
Got...qclb zyai rfgq jglc cvyarjw. lm djye fcpc, hsqr dgjjcp.
Sending... send back this line exactly. no flag here, just filler.
Got...myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
Sending... send back this line exactly. no flag here, just filler.
Got...iudt rqsa jxyi bydu unqsjbo. sxqhqsjuh 16 ev jxu vbqw yi 'm'
Sending... send back this line exactly. character 16 of the flag is 'w'
Got...zluk ihjr aopz spul lehjasf. johyhjaly 29 vm aol mshn pz 'z'
Sending... send back this line exactly. character 29 of the flag is 's'
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...wirh fego xlmw pmri ibegxpc. rs jpek livi, nywx jmppiv.
Sending... send back this line exactly. no flag here, just filler.
Got...xjsi gfhp ymnx qnsj jcfhyqd. st kqfl mjwj, ozxy knqqjw.
Sending... send back this line exactly. no flag here, just filler.
Got...amvl jiks bpqa tqvm mfikbtg. kpizikbmz 25 wn bpm ntio qa 'm'
Sending... send back this line exactly. character 25 of the flag is 'e'
Got...iudt rqsa jxyi bydu unqsjbo. sxqhqsjuh 4 ev jxu vbqw yi '{'
Sending... send back this line exactly. character 4 of the flag is '{'
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 9 ne sgd ekzf hr 'x'
Sending... send back this line exactly. character 9 of the flag is 'y'
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 26 ne sgd ekzf hr 'r'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...pbka yxzh qefp ifkb buxzqiv. kl cixd ebob, grpq cfiibo.
Sending... send back this line exactly. no flag here, just filler.
Got...eqzp nmow ftue xuzq qjmofxk. za rxms tqdq, vgef ruxxqd.
Sending... send back this line exactly. no flag here, just filler.
Got...ugpf dcem vjku nkpg gzcevna. ejctcevgt 15 qh vjg hnci ku 'q'
Sending... send back this line exactly. character 15 of the flag is 'o'
Got...rdmc azbj sghr khmd dwzbskx. mn ekzf gdqd, itrs ehkkdq.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. gh yetz axkx, cnlm ybeexk.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. vatktvmxk 16 hy max yetz bl 'p'
Sending... send back this line exactly. character 16 of the flag is 'w'
Got...gsbr poqy hvwg zwbs sloqhzm. bc tzou vsfs, xigh twzzsf.
Sending... send back this line exactly. no flag here, just filler.
Got...xjsi gfhp ymnx qnsj jcfhyqd. st kqfl mjwj, ozxy knqqjw.
Sending... send back this line exactly. no flag here, just filler.
Got...gsbr poqy hvwg zwbs sloqhzm. qvofoqhsf 23 ct hvs tzou wg 'q'
Sending... send back this line exactly. character 23 of the flag is 'c'
Got...fraq onpx guvf yvar rknpgyl. punenpgre 18 bs gur synt vf 'l'
Sending... send back this line exactly. character 18 of the flag is 'y'
Got...lxgw utvd mabl ebgx xqtvmer. gh yetz axkx, cnlm ybeexk.
Sending... send back this line exactly. no flag here, just filler.
Got...pbka yxzh qefp ifkb buxzqiv. zexoxzqbo 2 lc qeb cixd fp 'x'
Sending... send back this line exactly. character 2 of the flag is 'a'
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 1 tk ymj kqfl nx 'q'
Sending... send back this line exactly. character 1 of the flag is 'l'
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...nziy wvxf ocdn gdiz zsvxogt. ij agvb czmz, epno adggzm.
Sending... send back this line exactly. no flag here, just filler.
Got...kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 7 gx lzw xdsy ak 'o'
Sending... send back this line exactly. character 7 of the flag is 'w'
Got...vhqg edfn wklv olqh hadfwob. qr iodj khuh, mxvw iloohu.
Sending... send back this line exactly. no flag here, just filler.
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...yktj hgiq znoy rotk kdgizre. ingxgizkx 15 ul znk lrgm oy 'u'
Sending... send back this line exactly. character 15 of the flag is 'o'
Got...gsbr poqy hvwg zwbs sloqhzm. bc tzou vsfs, xigh twzzsf.
Sending... send back this line exactly. no flag here, just filler.
Got...yktj hgiq znoy rotk kdgizre. tu lrgm nkxk, payz lorrkx.
Sending... send back this line exactly. no flag here, just filler.
Got...amvl jiks bpqa tqvm mfikbtg. kpizikbmz 27 wn bpm ntio qa 'i'
Sending... send back this line exactly. character 27 of the flag is 'a'
Got...eqzp nmow ftue xuzq qjmofxk. za rxms tqdq, vgef ruxxqd.
Sending... send back this line exactly. no flag here, just filler.
Got...pbka yxzh qefp ifkb buxzqiv. zexoxzqbo 23 lc qeb cixd fp 'z'
Sending... send back this line exactly. character 23 of the flag is 'c'
Got...yktj hgiq znoy rotk kdgizre. tu lrgm nkxk, payz lorrkx.
Sending... send back this line exactly. no flag here, just filler.
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 2 yp dro pvkq sc 'k'
Sending... send back this line exactly. character 2 of the flag is 'a'
Got...jveu srtb kyzj czev vortkcp. ef wcrx yviv, aljk wzccvi.
Sending... send back this line exactly. no flag here, just filler.
Got...qclb zyai rfgq jglc cvyarjw. afypyarcp 26 md rfc djye gq 'q'
Sending... send back this line exactly. character 26 of the flag is 's'
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 12 tk ymj kqfl nx '_'
Sending... send back this line exactly. character 12 of the flag is '_'
Got...dpyo mlnv estd wtyp pilnewj. yz qwlr spcp, ufde qtwwpc.
Sending... send back this line exactly. no flag here, just filler.
Got...eqzp nmow ftue xuzq qjmofxk. otmdmofqd 9 ar ftq rxms ue 'k'
Sending... send back this line exactly. character 9 of the flag is 'y'
Got...gsbr poqy hvwg zwbs sloqhzm. qvofoqhsf 8 ct hvs tzou wg '_'
Sending... send back this line exactly. character 8 of the flag is '_'
Got...vhqg edfn wklv olqh hadfwob. qr iodj khuh, mxvw iloohu.
Sending... send back this line exactly. no flag here, just filler.
Got...amvl jiks bpqa tqvm mfikbtg. vw ntio pmzm, rcab nqttmz.
Sending... send back this line exactly. no flag here, just filler.
Got...lxgw utvd mabl ebgx xqtvmer. gh yetz axkx, cnlm ybeexk.
Sending... send back this line exactly. no flag here, just filler.
Got...amvl jiks bpqa tqvm mfikbtg. kpizikbmz 17 wn bpm ntio qa '_'
Sending... send back this line exactly. character 17 of the flag is '_'
Got...qclb zyai rfgq jglc cvyarjw. afypyarcp 24 md rfc djye gq 'y'
Sending... send back this line exactly. character 24 of the flag is 'a'
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 2 tk ymj kqfl nx 'f'
Sending... send back this line exactly. character 2 of the flag is 'a'
Got...coxn lkmu drsc vsxo ohkmdvi. mrkbkmdob 25 yp dro pvkq sc 'o'
Sending... send back this line exactly. character 25 of the flag is 'e'
Got...xjsi gfhp ymnx qnsj jcfhyqd. hmfwfhyjw 18 tk ymj kqfl nx 'd'
Sending... send back this line exactly. character 18 of the flag is 'y'
Got...tfoe cbdl uijt mjof fybdumz. dibsbdufs 20 pg uif gmbh jt 'v'
Sending... send back this line exactly. character 20 of the flag is 'u'
Got...pbka yxzh qefp ifkb buxzqiv. kl cixd ebob, grpq cfiibo.
Sending... send back this line exactly. no flag here, just filler.
Got...oajz xwyg pdeo heja atwyphu. jk bhwc dana, fqop behhan.
Sending... send back this line exactly. no flag here, just filler.
Got...ugpf dcem vjku nkpg gzcevna. ejctcevgt 5 qh vjg hnci ku 'p'
Sending... send back this line exactly. character 5 of the flag is 'n'
Got...rdmc azbj sghr khmd dwzbskx. bgzqzbsdq 24 ne sgd ekzf hr 'z'
Sending... send back this line exactly. character 24 of the flag is 'a'
Got...fraq onpx guvf yvar rknpgyl. punenpgre 5 bs gur synt vf 'a'
Sending... send back this line exactly. character 5 of the flag is 'n'
Got...gsbr poqy hvwg zwbs sloqhzm. bc tzou vsfs, xigh twzzsf.
Sending... send back this line exactly. no flag here, just filler.
Got...wirh fego xlmw pmri ibegxpc. rs jpek livi, nywx jmppiv.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...wirh fego xlmw pmri ibegxpc. glevegxiv 9 sj xli jpek mw 'c'
Sending... send back this line exactly. character 9 of the flag is 'y'
Got...eqzp nmow ftue xuzq qjmofxk. otmdmofqd 3 ar ftq rxms ue 's'
Sending... send back this line exactly. character 3 of the flag is 'g'
Got...tfoe cbdl uijt mjof fybdumz. op gmbh ifsf, kvtu gjmmfs.
Sending... send back this line exactly. no flag here, just filler.
Got...htcs qprz iwxh axct tmprian. cd uapv wtgt, yjhi uxaatg.
Sending... send back this line exactly. no flag here, just filler.
Got...nziy wvxf ocdn gdiz zsvxogt. xcvmvxozm 25 ja ocz agvb dn 'z'
Sending... send back this line exactly. character 25 of the flag is 'e'
Got...iudt rqsa jxyi bydu unqsjbo. de vbqw xuhu, zkij vybbuh.
Sending... send back this line exactly. no flag here, just filler.
flag{now_you_know_your_caesars}

[*] Switching to interactive mode
myhx vuwe nbcm fchy yruwnfs. hi zfua byly, domn zcffyl.
$  
```

### Flag
* flag{now_you_know_your_caesars}