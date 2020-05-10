### Challenge

```
I intercepted an image in the communication of 2 sharkies from a shark gang. Those sharks knew I was listening and they hid a message in this image.

Do you think you can do something about it?
```

### Solve

* PNG and LSB Steganography --> Using ZSTEG
```
kali@kali.org$ file pretty_cat.png 
pretty_cat.png: PNG image data, 800 x 674, 8-bit/color RGB, non-interlaced


kali@kali.org$ zsteg -a pretty_cat.png 
imagedata           .. file: interLaced eXtensible Trace (LXT) file (Version 17742)
b1,rgb,lsb,xy       .. text: "Well done, you managed to use the classic LSB method. Now you know that there's nothing in the sea this fish would fear. Other fish run from bigger things. That's their instinct. But this fish doesn't run from anything. He doesn't fear. Here is your flag: "
b2,r,lsb,xy         .. text: "DTTUTUU@0"
b2,g,lsb,xy         .. text: "@K@A@QEG E"
b2,rgb,msb,xy       .. text: "<_}\\eU}}}"
b4,r,lsb,xy         .. text: "6bw&wfr\"gvw&g3s\"'&vfffvfg#vggr6#r"
b4,g,lsb,xy         .. text: "fs3wl,7ffcb"
b5,g,lsb,xy         .. text: "q0bkZv00\t"
b6,r,lsb,xy         .. text: "1CMQEPQDYI"
b6,b,msb,xy         .. text: "^RtiY$E_"
b8,r,lsb,xy         .. text: "8+/+055?4448>>?AHHMWWT]kr|"
b8,g,lsb,xy         .. text: "E8?9;@@FAA@EFFFLUUYee`hvr}"
b8,b,lsb,xy         .. text: "NMRLDKKTKKJNTUTV__blmip"
b8,rgb,lsb,xy       .. text: "8EN+8M/?R+9L0;D5@K5@K?FT4AK4AK4@J8EN>FT>FU?FTALVHU_HU_MYbWelWemT`i]hpkv"
b8,bgr,lsb,xy       .. text: "NE8M8+R?/L9+D;0K@5K@5TF?KA4KA4J@4NE8TF>UF>TF?VLA_UH_UHbYMleWmeWi`Tph]"
b2,g,msb,xy,prime   .. text: "]UUUUUUAj"
b4,r,lsb,xy,prime   .. text: "bvc&f&b7"
b4,g,lsb,xy,prime   .. text: "l{,u\\w,w"
b4,g,msb,xy,prime   .. text: "fgffvVewWWuuf%R"
b5,bgr,lsb,xy,prime .. file: PGP Secret Sub-key -
b6,r,lsb,xy,prime   .. text: "H=ITE1T}"
b8,r,lsb,xy,prime   .. text: "/+5?8>HWk"
b8,r,msb,xy,prime   .. text: "IaaaIaaI"
b8,g,lsb,xy,prime   .. text: "?9@FEFUev"
b8,g,msb,xy,prime   .. text: "eeueeeeeeueUUeuuuUuUUuUumm]##["
b8,b,lsb,xy,prime   .. text: "RLKTNU_l"
b8,rgb,lsb,xy,prime .. text: "/?R+9L5@K?FT8EN>FUHU_Welkv"
b8,bgr,lsb,xy,prime .. text: "R?/L9+K@5TF?NE8UF>_UHleW"
b8,bgr,msb,xy,prime .. file: OS9/68K module:
b2,r,lsb,yx         .. text: ")@\rPUVQ@?"
b2,g,lsb,yx         .. file: old 16-bit-int little-endian archive
b2,b,lsb,yx         .. text: "QQjjPUT?"
b2,bgr,lsb,yx       .. text: "TQBTRI(RJ$QBIe"
b3,rgb,msb,yx       .. text: "UFW\n])PH"
b4,r,lsb,yx         .. text: "UUR\"\"\"\"\"\"%.RUW"
b4,g,lsb,yx         .. text: "ffc3333336?cfjT"
b4,b,msb,yx         .. file: PGP Secret Sub-key -
b4,rgb,msb,yx       .. text: ",vb'vb'v"
b4,bgr,msb,yx       .. text: "y&gr&gr&"
b5,rgb,msb,yx       .. text: "~Nxt5?/S"
b7,rgb,lsb,yx       .. text: "Q+ny7,\n:"
b8,r,lsb,yx         .. text: "82992...2772.27?9<95559<<<9<<@@D<@D@<<99555555522....229%4.55259599<@@@@@DDDDIMIDIIIIDDDDD@DDDD@DDDIIDDD@<@<<99<M5555552222222222222252.5255579|A9<<9<99@<<<<<<@<@<@@D@@D@A"
b8,r,msb,yx         .. text: "LLttttLL"
b8,g,lsb,yx         .. text: "EBEEC???CJJC?CJGJMJFFFJMMMJMMQQVMQVQMMJJFFFFFFFCC????CCEDA?FFCFJFJJMQQQQQVVVV[_[V[[[[VVVVVQVVVVQVVV[[VVVQMQMMJJM_FFFFFFCCCCCCCCCCCCCCFC?FCFFFJE"
b8,g,msb,yx         .. text: "RRbbbbbbb"
b8,b,lsb,yx         .. text: "NYOOXSSSXYYXSXYT`e`]]]`eee`eejjnejnjee``]]]]]]]XXSSSSXXOLJS]]X]`]``ejjjjjnnnnsysnssssnnnnnjnnnnjnnnssnnnjejee``ey]]]]]]XXXXXXXXXXXXXX]XS]X]]]YO"
b8,b,msb,yx         .. text: "VVVVVvvvv"
b8,rgb,lsb,yx       .. text: "8EN2BY9EO9EO2CX.?S.?S.?S2CX7JY7JY2CX.?S2CX7JY?GT9J`<Me9J`5F]5F]5F]9J`<Me<Me<Me9J`<Me<Me@Qj@QjDVn<Me@QjDVn@Qj<Me<Me9J`9J`5F]5F]5F]5F]5F]5F]5F]2CX2CX.?S.?S.?S.?S2CX2CX9EO%DL4AJ.?S5F]5F]2CX5F]9J`5F]9J`9J`<Me@Qj@Qj@Qj@Qj@QjDVnDVnDVnDVnI[sM_yI[sDVnI[sI[sI[sI[sD"
b8,rgb,msb,yx       .. text: "V\"jv\"jv\"jv\"jv"
b8,bgr,lsb,yx       .. text: "NE8YB2OE9OE9XC2S?.S?.S?.XC2YJ7YJ7XC2S?.XC2YJ7TG?`J9eM<`J9]F5]F5]F5`J9eM<eM<eM<`J9eM<eM<jQ@jQ@nVDeM<jQ@nVDjQ@eM<eM<`J9`J9]F5]F5]F5]F5]F5]F5]F5XC2XC2S?.S?.S?.S?.XC2XC2OE9LD%JA4S?.]F5]F5XC2]F5`J9]F5`J9`J9eM<jQ@jQ@jQ@jQ@jQ@nVDnVDnVDnVDs[Iy_Ms[InVDs[Is[Is[Is[In"
b8,bgr,msb,yx       .. text: "vj\"vj\"vj\"vj\""
b2,g,lsb,yx,prime   .. text: "Uni^\\Tid"
b2,bgr,msb,yx,prime .. text: "kYXgY(g*\tg&"
b3,b,lsb,yx,prime   .. text: "PV2XZ-I-"
b3,rgb,msb,yx,prime .. text: "'\tRJKI.%J"
b4,rgb,lsb,yx,prime .. file: PGP Secret Key -
b5,r,lsb,yx,prime   .. text: "$!TB5-lc"
b6,g,msb,yx,prime   .. text: "Q8LQ,NQ*"
b7,rgb,msb,yx,prime .. text: "4P\\Ej;Ovj"
b8,r,lsb,yx,prime   .. text: "99..22<5<@D<552252<@DIIDDDD<952225<9<@@@@<IISY"
b8,g,lsb,yx,prime   .. text: "EE??CCMFMQVMFFCCFCMQV[[VVVVMJFCCCFMJMQQQQM[[do"
b8,b,lsb,yx,prime   .. text: "OOSSXXe]ejne]]XX]Xejnssnnnne`]XXX]e`ejjjjess~"
b8,b,msb,yx,prime   .. text: "\tf\"\"\"**zFz"
b8,rgb,lsb,yx,prime .. text: "9EO9EO.?S.?S2CX2CX<Me5F]<Me@QjDVn<Me5F]5F]2CX2CX5F]2CX<Me@QjDVnI[sI[sDVnDVnDVnDVn<Me9J`5F]2CX2CX2CX5F]<Me9J`<Me@Qj@Qj@Qj@Qj<MeI[sI[sSd~Yo"
b8,rgb,msb,yx,prime .. text: "\"jv\"jv\"jv\"jv<"
b8,bgr,lsb,yx,prime .. text: "OE9OE9S?.S?.XC2XC2eM<]F5eM<jQ@nVDeM<]F5]F5XC2XC2]F5XC2eM<jQ@nVDs[Is[InVDnVDnVDnVDeM<`J9]F5XC2XC2XC2]F5eM<`J9eM<jQ@jQ@jQ@jQ@eM<s[Is[I~dS"
b8,bgr,msb,yx,prime .. text: "vj\"vj\"vj\"vj\""
b2,r,lsb,XY         .. text: "UUQAU=TYYZY"
b2,b,lsb,XY         .. text: "UYUeVUUUe"
b2,b,msb,XY         .. text: "iVu*QUUUUiSE"
b4,r,lsb,XY         .. text: "{//+$w\"w\""
b4,r,msb,XY         .. text: "KdDhfhNXhX"
b4,g,lsb,XY         .. text: "W;wuwww}ww"
b4,g,msb,XY         .. text: "g82w7x<9"
b4,b,lsb,XY         .. text: "k//+$f\"f\""
b4,b,msb,XY         .. text: "..  PVUV&$\"T"
b4,bgr,lsb,XY       .. text: ">|k\tI;\t|d"
b8,r,lsb,XY         .. text: "ywyyywuwtrtttruoofokktrkkkfkrkfokoofkrkorkkokkokkooorrorokrwkrororkrtwwrrwwrryttyyuu|tyyy"
b8,g,lsb,XY         .. text: "|y|yvyvyvqnqqqnnnlilllingg_gccliccc_cic_gcgg_cicgiccgccgccgggiigigcincigigicilnniinniiqllqqnntlqqqvqltqqtqqnnqtqqqqqqqqntlqn~tnnvqtlqqnqqtltqlqvlnytqqii{vqtnttqttntvtvqvvtty"
b8,b,msb,XY         .. text: ")\t)\t)\tQaQQQaQa!A!!!AQ"
b8,rgb,lsb,XY       .. text: "kc{kc{tl"
b8,rgb,msb,XY       .. text: "A.6!.6!.6!N"
b8,bgr,lsb,XY       .. text: "go{ck{ck"
b8,bgr,msb,XY       .. text: "N!6.!6.!6.A"
b2,r,lsb,XY,prime   .. text: "~uYYJoLO"
b2,g,lsb,XY,prime   .. text: "VuA-o&q*"
b4,b,lsb,XY,prime   .. text: "Dbbibb\")"
b4,b,msb,XY,prime   .. text: "7>r2#V<?"
b4,rgb,lsb,XY,prime .. text: "&Bd=lb=lb=i"
b4,bgr,lsb,XY,prime .. text: "F$bm2lm2lm9"
b5,g,lsb,XY,prime   .. file: PDP-11 executable not stripped - version 58
b8,r,lsb,XY,prime   .. text: "yytookrfkroorkokw|yyyyyuyy|w||y||"
b8,r,msb,XY,prime   .. file: PGP Secret Key -
b8,g,lsb,XY,prime   .. text: "yyqqlggci_ciggicgcntqqqqqnqqtnttqttyy|||vvqqlnlilggc_gZincZ;$"
b8,b,lsb,XY,prime   .. text: ",,2>DOL[W[fnnswww|x"
b8,b,msb,XY,prime   .. text: ["Q" repeated 8 times]
b8,rgb,lsb,XY,prime .. text: "f_wkc{ri"
b8,rgb,msb,XY,prime .. file: PGP Secret Key -
b8,bgr,lsb,XY,prime .. text: "irw_f{ck"
b2,r,lsb,YX         .. file: PGP Secret Key -
b2,g,msb,YX         .. text: "UWPVUUYY"
b3,g,msb,YX         .. file: Tower/XP rel 3 object not stripped - version 21553
b3,rgb,msb,YX       .. text: "7]Kp-8p`"
b4,g,msb,YX         .. text: "Ggywwwyw"
b4,b,msb,YX         .. text: "w3334C3D"
b6,b,lsb,YX         .. text: "\rAu\n)CPQD\r4"
b8,r,lsb,YX         .. text: "wwyywy|yy|yw|}}||"
b8,g,lsb,YX         .. text: "yqvqntlqvtv"
b8,g,msb,YX         .. text: "n...nn..nnnnnn"
b8,b,msb,YX         .. text: "m]]]]]]]"
b2,r,lsb,YX,prime   .. text: "%U\\FEAj8ZU"
b2,g,lsb,YX,prime   .. file: SVR2 executable (USS/370) - version 1784328151
b4,rgb,msb,YX,prime .. text: "lc\tec\t5421"
b5,b,lsb,YX,prime   .. file: zlib compressed data
b6,rgb,msb,YX,prime .. file: MIPSEB-LE MIPS-II ECOFF executable - version 181.186
b8,r,lsb,YX,prime   .. text: "~yiXXXk@&959@559<<995722.4*?KI"
b8,g,lsb,YX,prime   .. text: "yvnnytyvtvyyty"
b8,g,msb,YX,prime   .. text: ">>Iq9%9%"
b8,b,lsb,YX,prime   .. text: "{j\\`]`j]]`ee``]YXXSJLT[f"
b8,bgr,msb,YX,prime .. text: ".>5I95I9]"
b1,bgr,msb,Xy       .. text: "7fcafd99e5a6_BSL_Hgu0rht_3m_DnUof_u0Y{FTCkhs :galf ruoy si ereH .raef t'nseod eH .gnihtyna morf nur t'nseod hsif siht tuB .tcnitsni rieht s'tahT .sgniht reggib morf nur hsif rehtO .raef dluow hsif siht aes eht ni gnihton s'ereht taht wonk uoy woN .dohtem B"
b2,r,lsb,Xy         .. text: "VTjTE@TD"
b2,b,msb,Xy         .. file: PGP Secret Sub-key -
b2,rgb,lsb,Xy       .. text: "Wq MTTLT"
b2,bgr,msb,Xy       .. text: "ms?M{UMq*"
b3,bgr,msb,Xy       .. text: "?_e45\tS`"
b4,b,lsb,Xy         .. text: "fgJEt]BC"
b4,rgb,lsb,Xy       .. text: "Y!bX0cY>="
b4,bgr,lsb,Xy       .. text: ")Ra8S`9]>"
b5,r,lsb,Xy         .. file: MPEG ADTS, layer II, v1,  96 kbps, 2x Monaural
b5,r,msb,Xy         .. text: ";F)3JTc\r"
b6,g,msb,Xy         .. text: "$Gp2Op<A"
b7,r,msb,Xy         .. text: "`P(L\"RD%R\tT"
b8,r,lsb,Xy         .. text: "|nkf`Z[WLDEH=A9A<8=<=8=<A@LLMM]]\\f}"
b8,g,lsb,Xy         .. text: "|wyugs_jihb_WV[LQKPLKMMLKMLTTZ[ZZihhs|"
b8,b,lsb,Xy         .. text: "w}vvryoorek`jeaeee`edbckkkkqpqzx~"
b8,b,msb,Xy         .. text: "]]u5]-]-"
b8,rgb,lsb,Xy       .. text: "f_w`j}Ziv[hvWbrL_yDWoEVoH[r=LeAQk9K`A"
b8,bgr,lsb,Xy       .. text: "skw_f}j`viZvh[rbWy_LoWDoVEr[HeL=kQA`K9j"
b2,g,lsb,Xy,prime   .. file: PGP Secret Key -
b2,rgb,msb,Xy,prime .. file: BIOS (ia32) ROM Ext. (165*512)
b2,bgr,msb,Xy,prime .. file: PGP Secret Key -
b4,g,lsb,Xy,prime   .. text: "><McRwPZ"
b4,g,msb,Xy,prime   .. text: "VvvWUfuVWwgf"
b5,bgr,msb,Xy,prime .. text: "`d[/^LxA"
b6,rgb,msb,Xy,prime .. text: ":_sX&r5'w"
b8,r,lsb,Xy,prime   .. text: "nfDA<L]f"
b8,g,lsb,Xy,prime   .. text: "|g_WQM[hs"
b8,g,msb,Xy,prime   .. text: "mUmueuuUUUemUumUuUuuueeee"
b8,rgb,lsb,Xy,prime .. text: "f_wDWoAQk<MeL[k]hpfsz"
b8,bgr,lsb,Xy,prime .. text: "gnw_foWDkQAeM<k[Lph]zsf"
b1,b,lsb,yX         .. file: MPEG ADTS, layer III, v1, 192 kbps, 48 kHz, 2x Monaural
b2,r,lsb,yX         .. text: "UQUYUTQE"
b2,g,lsb,yX         .. file: MPEG ADTS, layer II, v1, 44.1 kHz, Stereo
b2,g,msb,yX         .. text: "eYjeeUuU"
b2,b,lsb,yX         .. file: MPEG ADTS, layer II, v1,  80 kbps, 48 kHz, JntStereo
b2,bgr,msb,yX       .. file: MPEG ADTS, layer I, v2, 112 kbps, Monaural
b4,r,msb,yX         .. text: "\"UUUurwwDD"
b4,g,msb,yX         .. text: "le\\UeUeUUffeVeU"
b4,b,lsb,yX         .. text: "'~'~'wr\"w"
b4,b,msb,yX         .. text: ">D34C333w"
b4,rgb,msb,yX       .. text: "Xb'vb'vb"
b4,bgr,msb,yX       .. text: "gr&gr&gR"
b5,g,lsb,yX         .. text: ")J3Zc)C1"
b5,rgb,msb,yX       .. text: "`Yr%Xhdv"
b6,r,lsb,yX         .. text: "\\eU\\AUP8"
b6,r,msb,yX         .. file: MPEG ADTS, layer I, v2,  96 kbps, 24 kHz, Monaural
b7,bgr,lsb,yX       .. text: "\tNpJsv3\\"
b8,r,lsb,yX         .. text: "||ykffRIIKA???944*******.4.....22222595299995999577775555955995999<@<<@@@DDDDD@<@<<<999995<<55992555555555959@<9<<<@D@@<<D<9<<55<9955559955&-&,<@@@@@@@DIIIMMMSkfSSXSXXXXXXdiiiiYiiirrryyy~~y~"
b8,r,msb,yX         .. text: ",,TTTTTTTt,tttttLLLLL"
b8,g,lsb,yX         .. text: "yttqc___VVGMGGGEAA9999999?A?????CCCCCFJFCJJJJFJJJFJJJJFFFFJFFJJFJJJMQMMQQQVVVVVQMQMMMJJJJJFMMFFJJCFFFFFFFFFJFJQMJMMMQVQQMMVMJMMFFMJJFFFFJJFFNVCIMQQQQQQQV[[[___dc_ddidiiiiiituuuuouuu"
b8,g,msb,yX         .. text: "RRRRbRRRbRRRRbbbbRbbRRbRRR"
b8,b,lsb,yX         .. text: "{wwnff[WTTTOJJLLLLLLLSJSSSSSXXXXX]`]X````]```]YYYY]]]]`]]``]```ejeejjjnnnnnjejeee`````]ee]]``X]]]]]]]]]`]`je`eeejnjjeene`ee]]e``]]]]``]]\\djtejjjjjjjnsssyyy~{w~~"
b8,b,msb,yX         .. text: "RR2222222"
b8,rgb,lsb,yX       .. text: "kc{f_wf_wR_nIVfIVfKG[AMW?GT?GT?GT9EO4AJ4AJ*9L*9L*9L*9L*9L*9L*9L.?S4AJ.?S.?S.?S.?S.?S2CX2CX2CX2CX2CX5F]9J`5"
b8,bgr,lsb,yX       .. text: "qy{ckw_fw_fn_RfVIfVI[GKWMATG?TG?TG?OE9JA4JA4L9*L9*L9*L9*L9*L9*L9*S?.JA4S?.S?.S?.S?.S?.XC2XC2XC2XC2XC2]F5`J9]"
b2,r,msb,yX,prime   .. file: PGP Secret Key -
b4,rgb,lsb,yX,prime .. text: "(=M(9\nlb"
b4,bgr,lsb,yX,prime .. text: "8-M8*\tlc"
b6,g,lsb,yX,prime   .. text: "#LfK\\bF q"
b7,rgb,msb,yX,prime .. text: "S0q\n*RLE"
b8,r,lsb,yX,prime   .. text: "|R?9*..25975595<@9<555<D<555@@@ISYrr~"
b8,g,lsb,yX,prime   .. text: "t_GE9??CFJJFFJFMQJMFFFMVMFFFQQQ[do"
b8,g,msb,yX,prime   .. text: "%I>n>nnnn"
b8,b,lsb,yX,prime   .. text: "nTOLSSX]`Y]]`]ej`e]]]ene]]]jjjs~"
b8,rgb,lsb,yX,prime .. text: "R_n?GT9EO*9L.?S.?S2CX5F]9J`7JY5F]5F]9J`5F]<Me@Qj9J`<Me5F]5F]5F]<MeDVn<Me5F]5F]5F]@Qj@Qj@QjI[sSd~Yo"
b8,bgr,lsb,yX,prime .. text: "t|n_RTG?OE9L9*S?.S?.XC2]F5`J9YJ7]F5]F5`J9]F5eM<jQ@`J9eM<]F5]F5]F5eM<nVDeM<]F5]F5]F5jQ@jQ@jQ@s[I~dS"
b1,rgb,msb,xY       .. text: "u;Tud[vS"
b2,r,lsb,xY         .. text: "|UAEUUkUWy"
b2,g,lsb,xY         .. text: "Pj)\tUTiE"
b2,b,lsb,xY         .. text: "YUeUVYYjj"
b2,b,msb,xY         .. text: "nVUUYZUi"
b2,bgr,lsb,xY       .. text: "MjVUeVYT"
b3,rgb,msb,xY       .. text: "Uf\"I2S&w"
b3,bgr,lsb,xY       .. file: PGP Secret Sub-key -
b4,g,lsb,xY         .. text: "JJ*B*$$6"
b4,g,msb,xY         .. text: "M\"RRURRTBT$$lK"
b4,b,lsb,xY         .. text: "&fjfbf\"\"i&\""
b4,b,msb,xY         .. text: "hWWeVeuuUur"
b5,bgr,lsb,xY       .. text: "n$9Oe#rF"
b6,b,lsb,xY         .. file: byte-swapped cpio archive
b7,bgr,msb,xY       .. text: "TrIJ.I)d\n"
b8,g,msb,xY         .. text: ">AAQQIII!"
b8,b,msb,xY         .. text: "EY9yYiy%"
b3,b,lsb,xY,prime   .. text: "Q%\"IIm\t;"
b3,bgr,lsb,xY,prime .. file: PGP Secret Sub-key -
b4,b,msb,xY,prime   .. text: "bR%fUBeD"
b5,r,lsb,xY,prime   .. file: TeX generic font data
b5,b,msb,xY,prime   .. text: "OJ(ekI&)S)F7"
b5,rgb,msb,xY,prime .. text: "0]yXJWN("
b6,g,msb,xY,prime   .. text: "86]7vM9ve"
b6,b,lsb,xY,prime   .. file: byte-swapped cpio archive
b6,rgb,msb,xY,prime .. text: "C4@i(ou7"
b8,r,lsb,xY,prime   .. text: "|aZaWVRHA???4:*\"\""
b8,g,lsb,xY,prime   .. text: "khkec_UMGGGA;9))"
b8,g,msb,xY,prime   .. text: "A!!.!!!An"
b8,b,lsb,xY,prime   .. text: "|w|msn^WTTTJLL22''"
b8,b,msb,xY,prime   .. text: "***R22LL"
b8,rgb,lsb,xY,prime .. text: "ak|Zhwak|WemVcsR_nHU^AMW?GT?GT?GT4AJ:;L*9L\")2\")2"
b8,rgb,msb,xY,prime .. text: "9eM9eM9eM"
b8,bgr,lsb,xY,prime .. text: "||kawhZ|kameWscVn_R^UHWMATG?TG?TG?JA4L;:L9*2)\"2)\"'"
b8,bgr,msb,xY,prime .. text: "Me9Me9Me9"
b2,r,lsb,Yx         .. file: PGP Secret Key -
b2,r,msb,Yx         .. text: "UUYUUUUU"
b2,g,lsb,Yx         .. text: "DEXZUQEtU"
b2,g,msb,Yx         .. text: "_W=UUUfU"
b2,bgr,lsb,Yx       .. text: "]u=mO?]u"
b3,r,lsb,Yx         .. text: "VYZL KX$"
b3,b,lsb,Yx         .. text: "I%mUU2RI'"
b3,bgr,lsb,Yx       .. file: PGP Secret Sub-key -
b4,r,msb,Yx         .. text: "VfuVGu[V"
b4,g,lsb,Yx         .. text: "@NDPJ@\r@"
b4,g,msb,Yx         .. text: "wG|UUGtww'%U\"W\\R"
b4,b,msb,Yx         .. text: ">=3wGGttsFwG>"
b8,r,lsb,Yx         .. text: "zzvz~~~rqvzvvz~vz~rz~mzvzvqqqqqqvvqmqqimiqvmqriqrmmrqzviqrqqqqqimqmmmqrvvrqmmmrqmiiiimrrmmmmmmdidiiddmijidijamdaaidaaddidadjeea\\Zdadmddiadidaa\\da\\\\aa_\\Z\\\\\\\\Z\\aa\\\\aa\\ZZZa_aaffafRRVVVZZ"
b8,r,msb,Yx         .. text: "^^n^~~~N"
b8,g,lsb,Yx         .. text: "~~~~~~tztzztt~zsztzsp~tppztppttztptsyypmhtpt~ttuptztppmtpmmkpqmhmmmmhmppmmkkmhhhkqkk__Z___ccchh"
b8,g,msb,Yx         .. text: "~^^^^~AA~~~~~~.^.^^..~^"
b8,b,lsb,Yx         .. text: "y}w}}}}w}"
b8,b,msb,Yx         .. text: "i\t\t\t\t\t\tii\t"
b1,rgb,lsb,Yx,prime .. text: ":+-:A9SJ"
b2,bgr,msb,Yx,prime .. text: "_2Z5fu]gY"
b3,rgb,msb,Yx,prime .. text: "TJR)%'H0y"
b4,b,msb,Yx,prime   .. file: MPEG ADTS, layer III, v2,  80 kbps, 16 kHz, JntStereo
b4,rgb,lsb,Yx,prime .. text: "vgfv\"R%+"
b4,rgb,msb,Yx,prime .. text: "Xb'vb'vb"
b4,bgr,msb,Yx,prime .. text: "gr&gr&gR"
b5,b,lsb,Yx,prime   .. file: MPEG ADTS, AAC, v2, stereo + center
b8,r,lsb,Yx,prime   .. text: "v~z~z~qvqiqiqqqrqmmirdidadeaaa\\\\\\\\ZafaPPDDAALHHAA9940Y`is"
b8,r,msb,Yx,prime   .. text: "~^nnnNNN"
b8,g,lsb,Yx,prime   .. text: "tztptypppmmmmhk_Z]]PPMMYUUMMEEA:ox"
b8,b,lsb,Yx,prime   .. text: "}}}}w|wqee\\\\WWb^^WWOOJD"
b8,b,msb,Yx,prime   .. text: "9\ti\tQ\tQ\t\t\t"
b8,rgb,lsb,Yx,prime .. text: "\\m}\\m}\\m}\\m}Zhwak|f_waZqP]eP]eDP\\DP\\AMWAMWLYbHU^HU^AMWAMW9EO9EO4AJ0:DYo"
b8,bgr,lsb,Yx,prime .. text: "pa}m\\}m\\}m\\}m\\whZ|kaw_fqZae]Pe]P\\PD\\PDWMAWMAbYL^UH^UHWMAWMAOE9OE9JA4D:0"
kali@kali.org$ 
```

* Got half the flag, used stegsolve to get the rest

* Flag: `shkCTF{Y0u_foUnD_m3_thr0ugH_LSB_6a5e99dfacf793e27a}`