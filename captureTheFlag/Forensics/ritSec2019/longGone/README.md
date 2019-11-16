# Solve

* Received a chromeBin file ( never worked with chrome laid out artifacts for forensics before )

* After file and binwalk analysis --> Spent a few minutes with foremost to extract file and dig through different html, pngs, jpeg files --> Took a lot of time without any benefit
  - grep for flag format was not helpful too

* After digging through for a while on the next challenge which was similar ---> vacation. 

* `Relearned` and Started again.

* Used file again 
```
srimbp-623:longGone sri$ file chromebin 
chromebin: POSIX tar archive (GNU)
```

* It was a tar file ( mistake: too soon to jump to tools ) --> Extract to obtain a more detailed chrome artifacts with metadata

* full fledge grep for flag format `ritsec` --> no success but a hint --> works well with challenge description which claimed about HISTORY

```
srimbp-623:User Data sri$ grep -ir "ritsec" *
Binary file Default/Favicons matches
Binary file Default/Cache/data_1 matches
Binary file Default/History Provider Cache matches
Binary file Default/History matches
Binary file SwReporter/77.224.200/software_reporter_tool.exe matches
Binary file SwReporter/77.224.200/em004_64.dll matches
```

* Dig through History 
  - File command on history file and found out it is sqlite3 db

  - Sql connect --> Look for all tables --> look at all urls table --> search for ritsec url --> http to the same url to get the flag

  ```
srimbp-623:Default sri$ file History
History: SQLite 3.x database, last written using SQLite version 3029000

srimbp-623:Default sri$ sqlite3 History
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> .tables
downloads                meta                     urls                   
downloads_slices         segment_usage            visit_source           
downloads_url_chains     segments                 visits                 
keyword_search_terms     typed_url_sync_metadata
sqlite> select * from urls
   ...> ;
36|http://google.com/|Google|2|2|13218330672211254|0
37|http://www.google.com/|Google|2|0|13218330672211254|0
38|https://www.google.com/|Google|4|0|13218330672777218|0
39|https://www.google.com/search?source=hp&ei=jRfPXb-wCKXp_Qa0vITIBQ&q=useless+rampant+perish&oq=useless+rampant+perish&gs_l=psy-ab.3...430.3526..3958...0.0..0.352.2802.7j13j1j1......0....1..gws-wiz.......0j0i131j0i22i30j0i22i10i30j33i160j33i299.0WcyE90xxng&ved=0ahUKEwj_qvXIk-3lAhWldN8KHTQeAVkQ4dUDCAg&uact=5|useless rampant perish - Google Search|3|0|13218330273590047|0
40|https://www.google.com/search?ei=khfPXcT8Kc3n_QbJjJ7oDQ&q=cuddly+immure+dreary&oq=cuddly+immure+dreary&gs_l=psy-ab.3...1653.5440..13288...0.0..1.284.2238.12j7j1......0....1..gws-wiz.......0i273j0j0i131j0i10j0i22i30j33i160j33i299.95jTSxdPm9w&ved=0ahUKEwjEjcjLk-3lAhXNc98KHUmGB90Q4dUDCAs&uact=5|cuddly immure dreary - Google Search|3|0|13218330288274819|0
41|https://www.google.com/search?ei=oRfPXZGgHajl_Qbk5Y_QDA&q=state+animated+second&oq=state+animated+second&gs_l=psy-ab.3..33i160.1567.3622..3833...0.1..1.195.2164.9j11......0....1..gws-wiz.......0i71j0i273i70i249j0i273j0i67j0i131j0j0i22i30j0i22i10i30.NzSvci6k3aM&ved=0ahUKEwjR9M7Sk-3lAhWoct8KHeTyA8oQ4dUDCAs&uact=5|state animated second - Google Search|3|0|13218330293642406|0
42|https://www.google.com/search?ei=phfPXb-8NOSJggeW_aWgCA&q=romantic+crow+road&oq=romantic+crow+road&gs_l=psy-ab.3...1586.3887..4200...0.1..0.186.2130.4j14......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i22i30j33i160.y9_Lxqms_wQ&ved=0ahUKEwi_p5fVk-3lAhXkhOAKHZZ-CYQQ4dUDCAs&uact=5|romantic crow road - Google Search|3|0|13218330299534543|0
43|https://www.google.com/search?ei=rBfPXcCYFs7k_Aa2kYSICg&q=cooperative+fix+public&oq=cooperative+fix+public&gs_l=psy-ab.3..33i160.1756.4225..4363...0.1..1.321.3619.2j14j5j1......0....1..gws-wiz.......0i71j0i67j0i273j0j0i131j0i10i67j0i22i30j33i299.g_ba6gRwfMI&ved=0ahUKEwjAnufXk-3lAhVOMt8KHbYIAaEQ4dUDCAs&uact=5|cooperative fix public - Google Search|3|0|13218330305055487|0
44|https://www.google.com/search?ei=shfPXfL0FNDl_Qb2uYbgDA&q=wretched+breakfast+renounce&oq=wretched+breakfast+renounce&gs_l=psy-ab.3..33i160.1514.7058..7350...1.1..0.403.3211.15j11j1j0j1......0....1..gws-wiz.......0i71j0i273j0i131i273j0j0i131j0i67j0i131i67j0i10j0i70i249j0i22i30j33i22i29i30j33i299.IdFBDjYZEjM&ved=0ahUKEwjyldTak-3lAhXQct8KHfacAcwQ4dUDCAs&uact=5|wretched breakfast renounce - Google Search|3|0|13218330313918999|0
45|https://www.google.com/search?ei=uxfPXbPCCKal_Qbw1rrIAQ&q=tempt+dress+install&oq=tempt+dress+install&gs_l=psy-ab.3..33i160.2412.4303..4507...0.1..2.309.3314.2j10j6j1......0....1..gws-wiz.......0i71j0i273j0i67j0j0i131j0i10j0i22i30j0i22i10i30j33i299.xSkyadwqeoQ&ved=0ahUKEwjzi-3ek-3lAhWmUt8KHXCrDhkQ4dUDCAs&uact=5|tempt dress install - Google Search|3|0|13218330319853337|0
46|https://www.google.com/search?ei=wRfPXaLfC4KQ_QajhaqYBw&q=colofor+angle+degree&oq=colofor+angle+degree&gs_l=psy-ab.3..33i160.3870.6997..7241...0.1..0.206.2539.6j12j2......0....1..gws-wiz.......0i71j0i273j0j0i131j0i67j0i10i67j0i10j0i30j0i10i30j0i5i30j0i22i30j33i22i29i30j33i299.vN0UtsHRidg&ved=0ahUKEwjiw97hk-3lAhUCSN8KHaOCCnMQ4dUDCAs&uact=5|colofor angle degree - Google Search|3|0|13218330329309948|0
47|https://www.google.com/search?ei=yRfPXdqCNNDj_Aa2tJjYCg&q=cultured+shut+rabid&oq=cultured+shut+rabid&gs_l=psy-ab.3..33i160.1121.4512..4701...1.1..0.153.2002.10j9......0....1..gws-wiz.......0i71j0i273j0i67j0j0i131j0i67i70i249j0i10j33i299.8VYVxwjg0Po&ved=0ahUKEwiai-_lk-3lAhXQMd8KHTYaBqsQ4dUDCAs&uact=5|cultured shut rabid - Google Search|3|0|13218330334662143|0
48|https://www.google.com/search?ei=0BfPXcbtGZGm_Qb6tJfgCQ&q=unsuitable+proceed+weak&oq=unsuitable+proceed+weak&gs_l=psy-ab.3..33i160.1975.5451..5963...0.1..1.302.3084.13j5j4j1......0....1..gws-wiz.......0i71j0i273i70i249j0i273j0j0i67j0i131j0i70i249j0i10j0i22i30j0i22i10i30j0i13j0i13i30j0i13i5i30j33i299.yIvAKWL87xE&ved=0ahUKEwjGlYDpk-3lAhURU98KHXraBZwQ4dUDCAs&uact=5|unsuitable proceed weak - Google Search|3|0|13218330342007470|0
49|https://www.google.com/search?ei=1xfPXbz8GKKQggednodo&q=account+bell+basked&oq=account+bell+basked&gs_l=psy-ab.3..33i160.1652.4137..4300...0.1..0.164.1732.16j3......0....1..gws-wiz.......0i71j0i273i70i249j0i273j0i67j0i131j0j0i10j0i22i10i30j0i22i30.tLuwOIglutM&ved=0ahUKEwj8w6rsk-3lAhUiiOAKHR3PAQ0Q4dUDCAs&uact=5|account bell basked - Google Search|3|0|13218330348483146|0
50|https://www.google.com/search?ei=3BfPXZfqJuSJggeW_aWgCA&q=seek+cool+train&oq=seek+cool+train&gs_l=psy-ab.3..33i160l2.530.1892..1997...0.1..0.207.1613.9j5j1......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i131i67j0i10j0i22i30j33i299.eklNCj7lxV8&ved=0ahUKEwiXyOnuk-3lAhXkhOAKHZZ-CYQQ4dUDCAs&uact=5|seek cool train - Google Search|3|0|13218330352130492|0
51|https://www.google.com/search?ei=4RfPXf6EFYOd_Qb6qYFQ&q=adjoining+create+hold&oq=adjoining+create+hold&gs_l=psy-ab.3..33i160l3.934.6030..6244...1.1..0.202.2210.13j8j1......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i67i70i249j0i70i249j0i22i30j33i299.6Zo19Vi3GP8&ved=0ahUKEwi--Yjxk-3lAhWDTt8KHfpUAAoQ4dUDCAs&uact=5|adjoining create hold - Google Search|3|0|13218330358891067|0
52|https://www.google.com/search?ei=6BfPXbCXLcHs_QaWza2gCw&q=do+zinc+train&oq=do+zinc+train&gs_l=psy-ab.3..33i160.23465.25172..25292...0.1..0.87.941.13......0....1..gws-wiz.......0i71j0i273j0i131j0i67j0j0i22i30j0i333j33i22i29i30.Xa0hqnzKEXE&ved=0ahUKEwiwq8z0k-3lAhVBdt8KHZZmC7QQ4dUDCAs&uact=5|do zinc train - Google Search|3|0|13218330385104847|0
53|https://www.google.com/search?ei=AxjPXcenBZKJggeZ0rPQAg&q=thrive&oq=thrive&gs_l=psy-ab.3..0i67j0j0i67j0l4j0i67j0l2.1857.2459..2713...0.1..0.85.453.6......0....1..gws-wiz.......0i71j0i273j0i131.DGBqiYdzwNs&ved=0ahUKEwiHtZSBlO3lAhWShOAKHRnpDCoQ4dUDCAs&uact=5|thrive - Google Search|3|0|13218330389267435|0
54|https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwi3wfWClO3lAhVMdt8KHU2FBDgQPAgH|Google|2|0|13218330390750065|0
55|https://www.google.com/search?hl=en&source=hp&ei=CRjPXa-ID8mKggeA7rmoDg&q=organization+cook+behold&oq=organization+cook+behold&gs_l=psy-ab.3...2363.6059..6245...0.0..1.218.1888.22j1j1......0....1..gws-wiz.......0j0i131j0i10j0i22i30j0i22i10i30j33i299j33i160j33i22i29i30.UJe1zA96tZw&ved=0ahUKEwjvsIyElO3lAhVJheAKHQB3DuUQ4dUDCAg&uact=5|organization cook behold - Google Search|3|0|13218330398241481|0
56|https://www.google.com/search?hl=en&ei=EBjPXfzcB-KE_QbMg6rADg&q=abash+operate+ambitious&oq=abash+operate+ambitious&gs_l=psy-ab.3...56644.60185..60459...0.1..1.184.2049.20j3......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i10j0i22i10i30j0i22i30j33i160j33i299.0HO-qFxKwpI&ved=0ahUKEwj8pLCHlO3lAhViQt8KHcyBCugQ4dUDCAs&uact=5|abash operate ambitious - Google Search|3|0|13218330459758188|0
57|https://www.google.com/search?hl=en&ei=TRjPXcOFKJG-ggfpv7-ADw&q=answer&oq=answer&gs_l=psy-ab.3..0l7j0i131j0l2.11317.12948..13152...1.1..0.169.701.4j3......0....1..gws-wiz.......0i71j0i67j0i273j0i10i67.yZmdVoXYNAI&ved=0ahUKEwiD4NuklO3lAhURn-AKHenfD_AQ4dUDCAs&uact=5|answer - Google Search|3|0|13218330474575667|0
58|https://www.google.com/search?hl=en&ei=WxjPXYHwNOuqgge2q4NQ&q=behol+babies+cook&oq=behol+babies+cook&gs_l=psy-ab.3..33i160l2.7166.8890..9034...0.1..0.132.1540.15j2......0....1..gws-wiz.......0i71j0i273j0j0i131j0i67j0i273i70i249j0i70i249j0i10i70i249j0i10j0i13j0i13i30j0i8i13i30j33i299.WUGAJWoiNsg&ved=0ahUKEwjBib-rlO3lAhVrleAKHbbVAAoQ4dUDCAs&uact=5|behol babies cook - Google Search|3|0|13218330484952152|0
59|https://www.google.com/search?hl=en&ei=ZhjPXeyACefm_Qbk6INg&q=scabble+petitie+grant&oq=scabble+petitie+grant&gs_l=psy-ab.3..33i160.1612.4152..4304...0.1..0.180.1843.20j1......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i10j0i13i10j0i13j0i22i10i30j0i22i30j0i13i30j0i8i13i30j0i8i13i10i30j33i299.Xw9ftkjpLiQ&ved=0ahUKEwjsy7KwlO3lAhVnc98KHWT0AAwQ4dUDCAs&uact=5|scabble petitie grant - Google Search|3|0|13218330489862214|0
60|https://www.google.com/search?hl=en&ei=axjPXYXHOMTM_Aa_4ZPYCg&q=overtake+farmer+b+rave&oq=overtake+farmer+b+rave&gs_l=psy-ab.3..33i160l2.1025.3860..4012...0.0..0.121.1869.19j3......0....1..gws-wiz.......0i273i70i249j0i273j0j0i131j0i10j0i22i30j0i22i10i30j33i299.U1O-rl4S1vQ&ved=0ahUKEwjFqJOzlO3lAhVEJt8KHb_wBKsQ4dUDCAs&uact=5|overtake farmer b rave - Google Search|3|0|13218330495104410|0
61|https://www.google.com/search?hl=en&ei=cBjPXeHNL46s_Qakj4HwBw&q=military+luxuriant+lean&oq=military+luxuriant+lean&gs_l=psy-ab.3..33i160.1747.5900..6065...0.1..1.277.2191.18j3j2......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i22i30j0i22i10i30j0i13j0i13i30j0i13i5i30j0i8i13i30j33i299.L-w7o20FSUc&ved=0ahUKEwjhxbu1lO3lAhUOVt8KHaRHAH4Q4dUDCAs&uact=5|military luxuriant lean - Google Search|3|0|13218330502110518|0
62|https://www.google.com/search?hl=en&ei=dxjPXYHFN42k_Qbfw66gDA&q=damp+beseech+overtake&oq=damp+beseech+overtake&gs_l=psy-ab.3..33i160.2626.5159..5272...0.0..0.116.1683.17j4......0....1..gws-wiz.......0i67j0i273j0i131j0j0i10j0i13j0i13i30j0i22i10i30j33i299.kIBZifIoNQw&ved=0ahUKEwjB3O64lO3lAhUNUt8KHd-hC8QQ4dUDCAs&uact=5|damp beseech overtake - Google Search|3|0|13218330508678543|0
63|https://www.google.com/search?hl=en&ei=fhjPXaj1D826ggfQ-5HYCg&q=perish+cuddly+immure&oq=perish+cuddly+immure&gs_l=psy-ab.3..33i160l2.2122.4063..4205...0.0..0.111.1769.17j3......0....1..gws-wiz.......0i273i70i249j0i273j0j0i67j0i10j0i3j0i22i10i30j0i22i30j33i299.wzR1CF252rM&ved=0ahUKEwiorPK7lO3lAhVNneAKHdB9BKsQ4dUDCAs&uact=5|perish cuddly immure - Google Search|3|0|13218330514060573|0
64|https://www.google.com/search?hl=en&ei=gxjPXZrlMqSs_QbylbyAAw&q=cool+train+adjoining&oq=cool+train+adjoining&gs_l=psy-ab.3..33i160.1041.4409..4572...0.1..1.318.1798.17j2j0j1......0....1..gws-wiz.......0i71j0i273j0i67j0j0i131j0i22i30j33i22i29i30.tPpl03LzGG8&ved=0ahUKEwjassa-lO3lAhUkVt8KHfIKDzAQ4dUDCAs&uact=5|cool train adjoining - Google Search|3|0|13218330519466017|0
65|https://www.google.com/search?q=cool+train+adjoining&hl=en&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiojqLBlO3lAhUBmuAKHUHtDOIQ_AUIEigB&biw=673&bih=492|cool train adjoining - Google Search|3|0|13218330522597307|0
66|https://www.google.com/search?hl=en&biw=673&bih=492&tbm=isch&sa=1&ei=ixjPXde7LuaI_QaTzrbwAQ&q=thrive+foregoing+farmer&oq=thrive+foregoing+farmer&gs_l=img.3...2516.6034..6138...0.0..0.105.1475.22j1......0....1..gws-wiz-img.......0i67j0j0i24.GxDwPRr0rFM&ved=0ahUKEwiXrarClO3lAhVmRN8KHROnDR4Q4dUDCAc&uact=5|thrive foregoing farmer - Google Search|3|0|13218330530325216|0
67|https://www.google.com/search?q=thrive+foregoing+farmer&hl=en&source=lnms&sa=X&ved=0ahUKEwilgoPGlO3lAhXDmOAKHSvbAfIQ_AUIDSgA&biw=673&bih=492&dpr=1|thrive foregoing farmer - Google Search|3|0|13218330532153844|0
68|https://www.google.com/search?hl=en&biw=673&bih=492&ei=lRjPXeCBK--kggfzgo3QBQ&q=ambitious+operate+answer&oq=ambitious+operate+answer&gs_l=psy-ab.3..33i160l2.1015.5047..5195...0.1..1.239.2024.22j1j1......0....1..gws-wiz.......0i71j0i273i70i249j0i273j0i131j0j0i131i67j0i67j0i70i249j0i22i30j0i22i10i30j33i299.9C5hLi05SxU&ved=0ahUKEwigoInHlO3lAhVvkuAKHXNBA1oQ4dUDCAs&uact=5|ambitious operate answer - Google Search|3|0|13218330538749939|0
69|https://www.google.com/search?hl=en&biw=673&bih=492&ei=nBjPXYWZDe6I_Qbr15LACw&q=cumbersome+laugh+increase&oq=cumbersome+laugh+increase&gs_l=psy-ab.3..33i160.101031.103643..103856...0.1..0.178.2183.19j6......0....1..gws-wiz.......0i71j0i273i70i249j0i273j0j0i131j0i67j0i70i249j0i333j0i22i30j33i299.HDAvCzA1yiI&ved=0ahUKEwiF15bKlO3lAhVuRN8KHeurBLgQ4dUDCAs&uact=5|cumbersome laugh increase - Google Search|3|0|13218330644088459|0
70|https://www.google.com/search?source=hp&ei=IhnPXb2XKs3L_QaM6osg&q=muscle+bucket+nine&oq=muscle+bucket+nine&gs_l=psy-ab.3...6520.8439..8564...0.0..0.515.1885.17j1j5-1......0....1..gws-wiz.....6..0i362i308i154i357j0i131j0j0i22i30j0i22i10i30j33i299j33i160.RtmHhSYI3kw&ved=0ahUKEwi9sKaKle3lAhXNZd8KHQz1AgQQ4dUDCAg&uact=5|muscle bucket nine - Google Search|3|0|13218330682780882|0
71|https://www.google.com/search?ei=LBnPXc-DG8fs_QaSnIWYBw&q=help+insult+heady&oq=help+insult+heady&gs_l=psy-ab.3...1544.3267..3458...0.1..0.106.1315.16j1......0....1..gws-wiz.......0i71j0i273j0j0i131j0i67j0i70i255j0i10j0i22i30j33i299j33i160.Yu6V5DMnRBE&ved=0ahUKEwjPyfmOle3lAhVHdt8KHRJOAXMQ4dUDCAs&uact=5|help insult heady - Google Search|3|0|13218330687347995|0
72|https://www.google.com/search?ei=MRnPXejZCILr_Qa365fYCQ&q=work+bang+arm&oq=work+bang+arm&gs_l=psy-ab.3..33i160l2.961.2298..2431...0.1..0.228.1052.11j0j1......0....1..gws-wiz.......0i71j0i131i273j0i273j0j0i131j0i67j0i10j0i22i30j0i22i10i30.QFDE2fwS6Lk&ved=0ahUKEwiotpiRle3lAhWCdd8KHbf1BZsQ4dUDCAs&uact=5|work bang arm - Google Search|3|0|13218330691004644|0
73|https://www.google.com/search?ei=NBnPXbO2JJCo_QaHy4vYCw&q=clouds+meaty+hate&oq=clouds+meaty+hate&gs_l=psy-ab.3...1200.4063..4169...1.1..0.157.1597.15j3......0....1..gws-wiz.......0i71j0i273j0j0i131j0i67j0i10i67j0i70i249j33i299j33i160.XxTPooQISYc&ved=0ahUKEwizoOuSle3lAhUQVN8KHYflArsQ4dUDCAs&uact=5|clouds meaty hate - Google Search|3|0|13218330696152447|0
74|https://www.google.com/search?ei=ORnPXaLIPKud_Qb_0prIDQ&q=writing+messy+go&oq=writing+messy+go&gs_l=psy-ab.3..33i160l2.1277.3106..3257...0.1..0.144.1208.15j1......0....1..gws-wiz.......0i71j0i131i273j0i273j0j0i131j0i67j0i22i30j0i22i10i30.1_jpJYLEI8I&ved=0ahUKEwjiyLSVle3lAhWrTt8KHX-pBtkQ4dUDCAs&uact=5|writing messy go - Google Search|3|0|13218330700439154|0
75|https://www.google.com/search?ei=PhnPXda2CsOZ_Qb8gLeYDg&q=nice+meme+dude&oq=nice+meme+dude&gs_l=psy-ab.3..0i22i30l6.2404.6314..6449...5.1..0.122.1313.15j2......0....1..gws-wiz.......0i71j0i273j0i131j0j0i273i70i249j0i67j0i131i67j0i10i67j0i22i10i30j33i160j0i8i13i30.fiprVCD9ItQ&ved=0ahUKEwjWzbOXle3lAhXDTN8KHXzADeMQ4dUDCAs&uact=5|nice meme dude - Google Search|3|0|13218330708468326|0
76|https://www.google.com/search?hl=en&biw=673&bih=492&ei=BRnPXf76EKHI_Qb03bqQCg&q=us-central-1.ritsec.club%2Fl%2Frelaxfizzblur&oq=us-central-1.ritsec.club%2Fl%2Frelaxfizzblur&gs_l=psy-ab.3...12572.24888..69087...2.1..1.298.3372.37j4j1......0....1..gws-wiz.......0i71j0i273i70i249j0i273j0j0i67j0i131j38j0i30j0i5i30j0i8i30j0i8i10i30.xUoJ6M10dd8&ved=0ahUKEwi-kaP8lO3lAhUhZN8KHfSuDqIQ4dUDCAs&uact=5|us-central-1.ritsec.club/l/relaxfizzblur - Google Search|3|0|13218330713643332|0
77|https://www.google.com/search?ei=RRnPXZuQJq6OggfFuKKoBw&q=shape+alikeoys&oq=shape+alikeoys&gs_l=psy-ab.3..33i160.9100.10806..10942...0.1..0.133.1180.11j3......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i22i30j0i22i10i30j0i13i10i30j0i13i30j0i8i13i30.ca2Zh_iR1DE&ved=0ahUKEwjbxvqale3lAhUuh-AKHUWcCHUQ4dUDCAs&uact=5|shape alikeoys - Google Search|3|0|13218330720252823|0
78|https://www.google.com/search?ei=UhnPXeGFEKLt_Qacj6bABA&q=desk+treat+pear&oq=desk+treat+pear&gs_l=psy-ab.3..33i160l2.1798.4995..5293...1.0..0.116.1216.13j3......0....1..gws-wiz.......0i273i70i249j0i273j0i131j0j0i67j0i10j0i22i30j33i299.n9VG57-Noco&ved=0ahUKEwjh9v2gle3lAhWidt8KHZyHCUgQ4dUDCAs&uact=5|desk treat pear - Google Search|3|0|13218330726938803|0
79|https://www.google.com/search?ei=WBnPXbrnHaSKggeosKG4Dw&q=declare&oq=declare&gs_l=psy-ab.3..0l5j0i131j0l4.1201.1850..2027...0.1..0.86.516.7......0....1..gws-wiz.......0i71j0i273j0i67.G6LG2xznJ1k&ved=0ahUKEwi68_mjle3lAhUkheAKHShYCPcQ4dUDCAs&uact=5|declare - Google Search|3|0|13218330730489395|0
80|https://www.google.com/search?ei=WxnPXfLfM-O8ggf2y7vABA&q=actor+beautiful+dizzy&oq=actor+beautiful+dizzy&gs_l=psy-ab.3...647.4383..4523...0.1..0.150.1718.18j3......0....1..gws-wiz.......0i71j0i67j0i131j0j0i273j0i10j0i22i10i30j0i22i30j0i333j33i160.Zk0cy74uC28&ved=0ahUKEwiy-calle3lAhVjnuAKHfblDkgQ4dUDCAs&uact=5|actor beautiful dizzy - Google Search|3|0|13218330736308870|0
81|https://www.google.com/search?ei=YRnPXYfIIIya_QbHl43ADg&q=flee+crowd+muscle&oq=flee+crowd+muscle&gs_l=psy-ab.3..33i160l2.4271.8303..8424...4.2..1.322.2273.15j2j2j1......0....1..gws-wiz.......0i71j0i131j0i67j0i273j0j0i131i273j0i10j0i22i10i30j0i22i30j0i13i10j0i13j0i13i10i30j0i13i30j0i8i13i30.EfAKjp3guhQ&ved=0ahUKEwjH_KGole3lAhUMTd8KHcdLA-gQ4dUDCAs&uact=5|flee crowd muscle - Google Search|3|0|13218330745875567|0
82|https://www.google.com/search?ei=axnPXe-KG6jn_Qb78bugCA&q=books+smash+coherent&oq=books+smash+coherent&gs_l=psy-ab.3..33i160.932.3256..3352...0.1..0.347.2063.16j2j1j1......0....1..gws-wiz.......0i71j0i273j0j0i131j0i67j0i10i67j0i273i70i249j0i10j0i22i30j0i22i10i30.s4331o-pfyQ&ved=0ahUKEwiv7P6sle3lAhWoc98KHfv4DoQQ4dUDCAs&uact=5|books smash coherent - Google Search|3|0|13218330750490787|0
83|https://www.google.com/search?ei=cBnPXZenBe-0ggfbs7XwDg&q=weary+note+fresh&oq=weary+note+fresh&gs_l=psy-ab.3..33i160.1523.3460..3709...0.1..0.105.1215.15j1......0....1..gws-wiz.......0i71j0i273j0i131j0j0i131i67j0i67j0i10j0i70i249j0i333j0i22i30j33i299.ANkmrJeXV90&ved=0ahUKEwiXn5qvle3lAhVvmuAKHdtZDe4Q4dUDCAs&uact=5|weary note fresh - Google Search|3|0|13218330755087576|0
84|https://www.google.com/search?ei=dRnPXd-cAaWQggfp9oHgCA&q=coast+vacuous&oq=coast+vacuous&gs_l=psy-ab.3...1803.3882..4177...0.1..0.166.1088.11j2......0....1..gws-wiz.......0i71j0i273j0j0i131j0i67j0i22i30j33i160.-SHwztSzjRk&ved=0ahUKEwifq8exle3lAhUliOAKHWl7AIwQ4dUDCAs&uact=5|coast vacuous - Google Search|3|0|13218330760024517|0
85|https://www.google.com/search?ei=ehnPXezAC-Tm_QaquongBw&q=kite+express+drill&oq=kite+express+drill&gs_l=psy-ab.3..33i160l2.1238.3789..3982...0.0..1.250.1563.17j0j1......0....1..gws-wiz.......0i273j0j0i131j0i67j0i273i70i249j0i22i30j0i22i10i30j33i22i29i30j33i299.Qkas89HNCC0&ved=0ahUKEwjs5YK0le3lAhVkc98KHSpdAnwQ4dUDCAs&uact=5|kite express drill - Google Search|3|0|13218330765203470|0
86|https://www.google.com/search?ei=fhnPXbycPKS0ggeTxJKwDA&q=lost+is+the+best+tv+show+ever&oq=lost+is+the+best+sho&gs_l=psy-ab.3.2.0j0i22i30l4j0i22i10i30j0i22i30l4.1036.3671..9171...1.0..1.211.1808.17j3j1......0....1..gws-wiz.....6..0i273j0i67j0i131j0i362i308i154i357j0i10.JlA6HPaKv-Q|lost is the best tv show ever - Google Search|3|0|13218330775831656|0
87|https://www.google.com/search?ei=iRnPXcrPFc-zggeM0Kr4BQ&q=drop+net+drop+paper&oq=drop+net+drop+paper&gs_l=psy-ab.3..33i160l2.2246.4422..4588...0.1..0.130.1545.17j2......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i10j0i22i30j0i22i10i30j33i22i29i30.Uc-u6IOV_1Q&ved=0ahUKEwiKuKC7le3lAhXPmeAKHQyoCl8Q4dUDCAs&uact=5|drop net drop paper - Google Search|3|0|13218330781747907|0
88|https://www.google.com/search?ei=jxnPXbv2D-Smggen5JWgBg&q=school+direction+weary&oq=school+direction+weary&gs_l=psy-ab.3...1344.5601..5791...0.1..0.202.1827.19j2j1......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i10i67j0i10j0i22i30j0i22i10i30j33i299j33i160.cFeWBk1NQDA&ved=0ahUKEwj7-Yi-le3lAhVkk-AKHSdyBWQQ4dUDCAs&uact=5|school direction weary - Google Search|3|0|13218330788630327|0
89|https://www.google.com/search?ei=lhnPXbGIHOSpggfo6aCADg&q=I+hate+CTFS&oq=I+hate+CTFS&gs_l=psy-ab.3...1164.2847..3387...0.1..1.184.931.10j1......0....1..gws-wiz.......0i71j0i273j0i131j0j0i67j0i131i273j0i10j33i160.v5ROHZ3lvsI&ved=0ahUKEwixq8DBle3lAhXklOAKHeg0COAQ4dUDCAs&uact=5|I hate CTFS - Google Search|3|0|13218330792798451|0
90|https://www.google.com/search?ei=mhnPXfH2OaLn_QbK4pLwBQ&q=how+to+solve+every+ctf+challenge+ever&oq=how+to+solve+every+ctf+challenge+ever&gs_l=psy-ab.3..33i160l4.1144.5901..6023...1.1..0.198.3230.32j6......0....1..gws-wiz.......0i71j0i273j0j0i131j0i22i30j33i22i29i30j33i10j33i299.5BRSuUIFDlo&ved=0ahUKEwjxq9LDle3lAhWic98KHUqxBF4Q4dUDCAs&uact=5|how to solve every ctf challenge ever - Google Search|3|0|13218330799712627|0
91|https://www.google.com/search?ei=oRnPXe_zLfLm_Qbrw5K4BA&q=jobs+in+security&oq=jobs+in+security&gs_l=psy-ab.3..0l10.1312.3034..3192...0.1..0.181.1255.14j2......0....1..gws-wiz.......0i71j0i273j0i131j0i67.1mVjb9WQYk0&ved=0ahUKEwivyPHGle3lAhVyc98KHeuhBEcQ4dUDCAs&uact=5|jobs in security - Google Search|3|0|13218330804505582|0
92|https://www.google.com/search?ei=pRnPXYTvM_C0ggfDlJz4Bw&q=jobs+at+fast+food+near+me&oq=jobs+at+fast+food+near+me&gs_l=psy-ab.3..0i22i30l3.1703.4886..4999...2.2..0.148.1879.16j5......0....1..gws-wiz.......0i71j0i273j0i131i273j0j0i10j0i13j0i13i5i30.dS57tlrJInk&ved=0ahUKEwjE1evIle3lAhVwmuAKHUMKB38Q4dUDCAs&uact=5|jobs at fast food near me - Google Search|3|0|13218330811519398|0
93|https://www.google.com/search?ei=rBnPXY74CI2yggf4wb-gDw&q=frogs+ugly+throw&oq=frogs+ugly+throw&gs_l=psy-ab.3..0i71l8.9242.10833..10974...0.1..1.0.0.......10....1..gws-wiz.eRM6so1eG10&ved=0ahUKEwiO_uvLle3lAhUNmeAKHfjgD_QQ4dUDCAs&uact=5|frogs ugly throw - Google Search|3|0|13218330823219043|0
94|https://www.google.com/search?ei=uBnPXcv4N425ggeXwpvoCQ&q=realize+paper+net+drop&oq=realize+paper+net+drop&gs_l=psy-ab.3..0i71l8.2543.9541..9777...0.1..5.0.0.......18....1..gws-wiz.g1TMvQZADfs&ved=0ahUKEwjLtPfRle3lAhWNnOAKHRfhBp0Q4dUDCAs&uact=5|realize paper net drop - Google Search|3|0|13218330833954332|0
95|https://www.google.com/search?ei=wxnPXdi_KoTp_QaS-rbQDw&q=writing+alike+frogs&oq=writing+alike+frogs&gs_l=psy-ab.3..0i71l8.2359.7964..8125...0.1..7.0.0.......34....1..gws-wiz.CXYqAIALbBw&ved=0ahUKEwiYrYnXle3lAhWEdN8KHRK9DfoQ4dUDCAs&uact=5|writing alike frogs - Google Search|3|0|13218330843292323|0
96|https://www.google.com/search?ei=zBnPXZrNOaPp_Qbp9I7gDg&q=alex+jones+truth+explained&oq=alex+jones+truth+explained&gs_l=psy-ab.3..0i71l8.796.3306..3788...0.1..4.0.0.......16....1..gws-wiz.KvfGHzmi9cM&ved=0ahUKEwia473ble3lAhWjdN8KHWm6A-wQ4dUDCAs&uact=5|alex jones truth explained - Google Search|3|0|13218330847957645|0
97|https://www.google.com/search?ei=0RnPXfbEOPKOggf4x5zYBQ&q=edward+snowden+joe+rogan+podcast&oq=edward+snowden+joe+rogan+podcast&gs_l=psy-ab.3...1242.18796..18977...0.0..15.0.0.......64....1..gws-wiz.....0.WTC92kD6nWE&ved=0ahUKEwi28e3dle3lAhVyh-AKHfgjB1sQ4dUDCAs&uact=5|edward snowden joe rogan podcast - Google Search|3|0|13218330868091144|0
98|https://www.google.com/search?ei=5RnPXZjjNIa-ggfxhRI&q=edward+snowden+national+hero%3F&oq=edward+snowden+national+hero%3F&gs_l=psy-ab.3...6849.8359..8589...0.0..1.0.0.......7....1..gws-wiz.baJyj2lMEyM&ved=0ahUKEwjY6a7nle3lAhUGn-AKHfGCBAAQ4dUDCAs&uact=5|edward snowden national hero? - Google Search|3|0|13218330877469444|0
99|https://www.google.com/search?ei=7xnPXZ6ZGYPI_QbChY6wCw&q=how+to+join+NSA&oq=how+to+join+NSA&gs_l=psy-ab.3...1635.3033..3317...0.0..0.0.0.......3....1..gws-wiz.hltKlzFvr1k&ved=0ahUKEwjezPXrle3lAhUDZN8KHcKCA7YQ4dUDCAs&uact=5|how to join NSA - Google Search|3|0|13218330882523627|0
100|https://www.google.com/search?ei=8xnPXZ3NLYPp_QbTha_gDg&q=how+to+join+CIA&oq=how+to+join+CIA&gs_l=psy-ab.3..0i71l8.909.1080..1428...0.2..0.0.0.......3....1..gws-wiz.L4nhAnbNKPM&ved=0ahUKEwjdkv7tle3lAhWDdN8KHdPCC-wQ4dUDCAs&uact=5|how to join CIA - Google Search|3|0|13218330885579960|0
101|https://www.google.com/search?ei=9hnPXbCTMu-Z_Qav7YvICQ&q=security+clearance+requirements&oq=security+clearance+requirements&gs_l=psy-ab.3..0i71l8.2343.5854..5935...0.1..1.0.0.......16....1..gws-wiz.eCyay5Kx-so&ved=0ahUKEwiw5rnvle3lAhXvTN8KHa_2ApkQ4dUDCAs&uact=5|security clearance requirements - Google Search|3|0|13218330892530189|0
102|https://www.google.com/search?ei=_hnPXYD_EZKf_QaN3oToCA&q=how+to+lie+to+NSA+and+CIA&oq=how+to+lie+to+NSA+and+CIA&gs_l=psy-ab.3..0i71l8.914.5927..6210...0.1..2.0.0.......21....1..gws-wiz.YgS-kHVOlVg&ved=0ahUKEwiA9oHzle3lAhWST98KHQ0vAY0Q4dUDCAs&uact=5|how to lie to NSA and CIA - Google Search|3|0|13218330899644039|0
103|https://www.google.com/search?ei=BRrPXc_OJ8Gvggfs8JfQBg&q=throw+harbor+support&oq=throw+harbor+support&gs_l=psy-ab.3..0i71l8.2780.4839..4972...0.1..1.0.0.......13....1..gws-wiz.dEHm_ya8xTs&ved=0ahUKEwiP5cL2le3lAhXBl-AKHWz4BWoQ4dUDCAs&uact=5|throw harbor support - Google Search|3|0|13218330905694049|0
104|https://www.google.com/search?ei=CxrPXfW4IemGggeewYOgCw&q=paper+wring+direction&oq=paper+wring+direction&gs_l=psy-ab.3..0i71l3.1139.3985..4178...0.1..3.0.0.......16....1..gws-wiz.qfjItTbsCIE&ved=0ahUKEwi16qr5le3lAhVpg-AKHZ7gALQQ4dUDCAs&uact=5|paper wring direction - Google Search|3|0|13218330911204137|0
105|https://www.google.com/search?ei=EBrPXYytMYKzggfPyZKwDg&q=actor+infest&oq=actor+infest&gs_l=psy-ab.3..0i71l8.865.2261..2389...0.1..2.0.0.......9....1..gws-wiz.K0Gk3Q-VOjA&ved=0ahUKEwiM9ev7le3lAhWCmeAKHc-kBOYQ4dUDCAs&uact=5|actor infest - Google Search|3|0|13218330914789781|0
106|https://www.google.com/search?ei=FBrPXf3PGsGOggf_2afoCQ&q=best+nicolas+cage+movies+&oq=best+nicolas+cage+movies+&gs_l=psy-ab.3..0i71l8.3039.9470..10248...0.1..4.0.0.......25....1..gws-wiz.EIwvJP6H3bQ&ved=0ahUKEwj9qcn9le3lAhVBh-AKHf_sCZ0Q4dUDCAs&uact=5|best nicolas cage movies - Google Search|3|0|13218330926962267|0
107|https://www.google.com/search?ei=HxrPXd2jMYru_QaJ8rqYBA&q=nicolas+cage+fanfic&oq=nicolas+cage+fanfic&gs_l=psy-ab.3...7612.10695..10907...0.0..2.0.0.......18....1..gws-wiz.zPk1NlJKqzY&ved=0ahUKEwidr_-Clu3lAhUKd98KHQm5DkMQ4dUDCAs&uact=5|nicolas cage fanfic - Google Search|3|0|13218330939023233|0
108|https://www.google.com/search?ei=LBrPXfnrKYmq_Qaknr6oDw&q=ugly+uneven+coast&oq=ugly+uneven+coast&gs_l=psy-ab.3...3197.6777..6888...0.0..1.0.0.......18....1..gws-wiz.3dyvZlRrg0o&ved=0ahUKEwj5sZGJlu3lAhUJVd8KHSSPD_UQ4dUDCAs&uact=5|ugly uneven coast - Google Search|3|0|13218330947366915|0
109|https://www.google.com/search?ei=NBrPXenfL--pggfkjaSQCQ&q=express+finicky+fortunate&oq=express+finicky+fortunate&gs_l=psy-ab.3..0i71l4.462.3757..3982...0.1..2.0.0.......14....1..gws-wiz.U3XmHB9kMyM&ved=0ahUKEwjpyf-Mlu3lAhXvlOAKHeQGCZIQ4dUDCAs&uact=5|express finicky fortunate - Google Search|3|0|13218330952585351|0
110|https://www.google.com/search?ei=OhrPXbijC-Tm_QaquongBw&q=soggy+direction+flee&oq=soggy+direction+flee&gs_l=psy-ab.3..0i71l8.2012.8763..8929...0.1..1.0.0.......16....1..gws-wiz.e_KC5Cygokc&ved=0ahUKEwi4qMmPlu3lAhVkc98KHSpdAnwQ4dUDCAs&uact=5|soggy direction flee - Google Search|3|0|13218330962489192|0
111|https://www.google.com/search?ei=RBrPXezjGJGe_QbG4qXwDg&q=kindly+nonstop+dig&oq=kindly+nonstop+dig&gs_l=psy-ab.3..0i71l8.3594.5404..5527...0.1..2.0.0.......10....1..gws-wiz.cahMfQMw0g0&ved=0ahUKEwjslbmUlu3lAhURT98KHUZxCe4Q4dUDCAs&uact=5|kindly nonstop dig - Google Search|3|0|13218330969294874|0
112|https://www.google.com/search?q=actor+beautiful+dizzy&rlz=1C1CHBF_enUS875US875&oq=a&aqs=chrome.2.69i59l3j69i57j0j5l3.2456j0j7&sourceid=chrome&ie=UTF-8|actor beautiful dizzy - Google Search|3|0|13218332414239001|0
113|https://en.wikipedia.org/wiki/DJ_Qualls|DJ Qualls - Wikipedia|0|0|0|0
116|https://www.reddit.com/r/dankmemes|Dankmemes|0|0|0|0
119|https://www.reddit.com/r/CongratsLikeImFive/?utm_campaign=redirect&utm_medium=desktop&utm_source=reddit&utm_name=random_subreddit|Wow! You did such a great job!|0|0|0|0
120|https://www.reddit.com/r/criticalrole/?utm_campaign=redirect&utm_medium=desktop&utm_source=reddit&utm_name=random_subreddit|Critical Role|0|0|0|0
121|https://www.reddit.com/r/Telegram/?utm_campaign=redirect&utm_medium=desktop&utm_source=reddit&utm_name=random_subreddit|Telegram|0|0|0|0
122|https://www.reddit.com/r/trailerparkboys/?utm_campaign=redirect&utm_medium=desktop&utm_source=reddit&utm_name=random_subreddit|Trailer Park Boys|0|0|0|0
123|https://www.reddit.com/r/NHLHUT/?utm_campaign=redirect&utm_medium=desktop&utm_source=reddit&utm_name=random_subreddit|Hockey Ultimate Team|0|0|0|0
125|https://www.reddit.com/r/LivestreamFail/?utm_campaign=redirect&utm_medium=desktop&utm_source=reddit&utm_name=random_subreddit|r/LivestreamFail: Livestream wins, fails, and everything in between|0|0|0|0
127|https://www.reddit.com/r/Vinesauce/?utm_campaign=redirect&utm_medium=desktop&utm_source=reddit&utm_name=random_subreddit|Vinesauce|0|0|0|0
129|https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3639369/|Dopamine reverses reward insensitivity in apathy following globus pallidus lesions|0|0|0|0
131|https://www.streetdirectory.com/travel_guide/3694/health/how_to_slay_the_toxic_dragon_in_your_life.html|How To Slay The Toxic Dragon In Your Life|0|0|0|0
133|https://www.amazon.com/Shoe-Protector-Spray-Hydrophobic-Eco-Friendly/dp/B075K6DNPC|Amazon.com: Shoe Protector Spray - Water Repellent/Waterproof Suede Shoes, Leather, Canvas, Nubuck & Fabric Boots. Latest Hydrophobic Nano-Tech Formula. Eco-Friendly. Stops Snow & Slush. Alcohol & Silicone Free: Home & Kitchen|0|0|0|0
136|https://www.amazon.com/Stainless-Steel-Pick-Set-Multi-Tool/dp/B07ZJFNB95/ref=sr_1_5?keywords=lock+picks&qid=1573855938&s=home-garden&sr=1-5|Stainless Steel Pick Set Multi-Tool - - Amazon.com|0|0|0|0
138|https://www.theflowerexpert.com/content/growingflowers/flowers-and-seasons|Flowers by Season - Winter Flowers, Summer, Spring Flowers, Autumn Flowers|0|0|0|0
141|http://www.davidsongifted.org/search-database/entry/a10496|Managing His Image: The challenge facing a gifted male|0|0|0|0
143|https://jamiegeller.com/browse/5-life-hacks-to-quench-your-thirst/|5 Life Hacks To Quench Your Thirst, Plus A Hydrating Recipe - Jamie Geller|0|0|0|0
145|https://support.office.com/en-us/article/align-text-left-or-right-center-text-or-justify-text-on-a-page-70da744d-0f4d-472e-916d-1c42d94dc33f|Align text left or right, center text, or justify text on a page - Word|0|0|0|0
148|https://books.google.com/books?id=XZkAAAAAMAAJ&pg=PA346&lpg=PA346&dq=shoe+world+roll&source=bl&ots=wRBXhRJVgl&sig=ACfU3U3IEHEFO9U03AkQWMHlklxNN-2sow&hl=en&sa=X&ved=2ahUKEwjmnr_5nu3lAhVGnOAKHczvCfcQ6AEwAHoECAYQAQ#v=onepage&q=shoe%20world%20roll&f=false|The World's Paper Trade Review - Google Books|0|0|0|0
151|https://books.google.com/books?id=oWUNCgAAQBAJ&pg=PA67&lpg=PA67&dq=guide+explore+adult&source=bl&ots=BczuQ0Ymin&sig=ACfU3U3rKQYwKm15w92qhi0hh39LcgSqrw&hl=en&sa=X&ved=2ahUKEwiI37eGn-3lAhXMdd8KHTgtDckQ6AEwDnoECAkQAQ#v=onepage&q=guide%20explore%20adult&f=false|An Intelligent Person’s Guide to Education - Tony Little - Google Books|0|0|0|0
153|https://www.youtube.com/watch?v=u3CKgkyc7Qo|Hackers (1995) - Hack the planet - YouTube|0|0|0|0
155|http://help.imis.com/classic/#Desktop/AR_Cash/Enter_and_edit_orders_window_-_Simple_order_entry.htm%3FTocPath%3DAR%252FCash%7CSimple%2520Orders%7C_____2|Enter and edit orders window - Simple order entry|0|0|0|0
sqlite> 
[1]+  Stopped                 sqlite3 History



srimbp-623:Default sri$ http http://us-central-1.ritsec.club/l/relaxfizzblur
HTTP/1.1 200 OK
Cache-Control: no-cache, no-store, must-revalidate
Connection: keep-alive
Content-Length: 31
Content-Type: text/plain; charset=utf-8
Date: Sat, 16 Nov 2019 06:06:51 GMT
ETag: "1573853123.9133823-31-3801943379"
Expires: 0
Last-Modified: Fri, 15 Nov 2019 21:25:23 GMT
Pragma: no-cache
Server: nginx/1.17.5

RITSEC{SP00KY_BR0WS3R_H1ST0RY}


  ```