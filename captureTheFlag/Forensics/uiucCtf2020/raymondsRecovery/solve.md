### Challenge

```
Uh-oh! Someone corrupted all my important files and now I can’t open any of them. I really need one of them in particular, a png of something very important. Please help me recover it!

Here, take this ext4 filesystem and see what you can find. If you can figure out which file it is and how to fix it, you’ll get something in return!
```

### Solve

```
$ foremost -a raymonds_fs
foremost: /usr/local/etc/foremost.conf: No such file or directory
Processing: raymonds_fs
|*|

$ cat audit.txt 
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Sun Jul 19 00:16:05 2020
Invocation: foremost -a raymonds_fs 
Output directory: /
Configuration file: /usr/local/etc/foremost.conf
------------------------------------------------------------------
File: raymonds_fs
Start: Sun Jul 19 00:16:05 2020
Length: Unknown
 
Num	 Name (bs=512)	       Size	 File Offset	 Comment 

0:	00009476.jpg 	      86 KB 	    4851712 	 
1:	00017248.jpg 	       1 MB 	    8830976 	  (Header dump)
2:	00017954.jpg 	      15 KB 	    9192448 	 
3:	00017986.jpg 	      51 KB 	    9208832 	 
4:	00018090.jpg 	       9 KB 	    9262080 	 
5:	00018110.jpg 	      40 KB 	    9272320 	 
6:	00019458.jpg 	     166 KB 	    9962496 	 
7:	00019812.jpg 	      34 KB 	   10143744 	 
8:	00019938.jpg 	      15 KB 	   10208256 	 
9:	00019990.jpg 	       5 KB 	   10234880 	  (Header dump)
10:	00002896.bmp 	       2 MB 	    1483113 	  (Header dump)
11:	00002951.bmp 	       2 MB 	    1510942 	  (Header dump)
12:	00003019.bmp 	       2 MB 	    1545902 	  (Header dump)
13:	00003213.bmp 	       2 MB 	    1645229 	  (Header dump)
14:	00003434.bmp 	       2 MB 	    1758482 	  (Header dump)
15:	00003452.bmp 	       2 MB 	    1767609 	  (Header dump)
16:	00003845.bmp 	       2 MB 	    1968745 	  (Header dump)
17:	00004178.bmp 	       2 MB 	    2139505 	  (Header dump)
18:	00004233.bmp 	       2 MB 	    2167334 	  (Header dump)
19:	00004301.bmp 	       2 MB 	    2202294 	  (Header dump)
20:	00004495.bmp 	       2 MB 	    2301621 	  (Header dump)
21:	00004716.bmp 	       2 MB 	    2414874 	  (Header dump)
22:	00004734.bmp 	       2 MB 	    2424001 	  (Header dump)
23:	00005127.bmp 	       2 MB 	    2625137 	  (Header dump)
24:	00005460.bmp 	       2 MB 	    2795889 	  (Header dump)
25:	00005515.bmp 	       2 MB 	    2823718 	  (Header dump)
26:	00005583.bmp 	       2 MB 	    2858678 	  (Header dump)
27:	00005777.bmp 	       2 MB 	    2958005 	  (Header dump)
28:	00005998.bmp 	       2 MB 	    3071258 	  (Header dump)
29:	00006016.bmp 	       2 MB 	    3080385 	  (Header dump)
30:	00006409.bmp 	       2 MB 	    3281521 	  (Header dump)
31:	00006742.bmp 	       2 MB 	    3452273 	  (Header dump)
32:	00006797.bmp 	       2 MB 	    3480102 	  (Header dump)
33:	00006865.bmp 	       2 MB 	    3515062 	  (Header dump)
34:	00007059.bmp 	       2 MB 	    3614389 	  (Header dump)
35:	00007280.bmp 	       2 MB 	    3727642 	  (Header dump)
36:	00007298.bmp 	       2 MB 	    3736769 	  (Header dump)
37:	00007691.bmp 	       2 MB 	    3937905 	  (Header dump)
38:	00008403.bmp 	       2 MB 	    4302669 	  (Header dump)
39:	00008611.bmp 	       2 MB 	    4409013 	  (Header dump)
40:	00008832.bmp 	       2 MB 	    4522266 	  (Header dump)
41:	00008850.bmp 	       2 MB 	    4531393 	  (Header dump)
42:	00009243.bmp 	       2 MB 	    4732529 	  (Header dump)
43:	00009479.bmp 	       2 MB 	    4853743 	  (Header dump)
44:	00009699.bmp 	       2 MB 	    4966070 	  (Header dump)
45:	00009893.bmp 	       2 MB 	    5065397 	  (Header dump)
46:	00010114.bmp 	       2 MB 	    5178650 	  (Header dump)
47:	00010132.bmp 	       2 MB 	    5187777 	  (Header dump)
48:	00010525.bmp 	       2 MB 	    5388913 	  (Header dump)
49:	00010858.bmp 	       2 MB 	    5559665 	  (Header dump)
50:	00010913.bmp 	       2 MB 	    5587494 	  (Header dump)
51:	00010981.bmp 	       2 MB 	    5622454 	  (Header dump)
52:	00011175.bmp 	       2 MB 	    5721781 	  (Header dump)
53:	00011396.bmp 	       2 MB 	    5835034 	  (Header dump)
54:	00011414.bmp 	       2 MB 	    5844161 	  (Header dump)
55:	00011807.bmp 	       2 MB 	    6045297 	  (Header dump)
56:	00012201.bmp 	       2 MB 	    6247093 	  (Header dump)
57:	00012422.bmp 	       2 MB 	    6360346 	  (Header dump)
58:	00012440.bmp 	       2 MB 	    6369473 	  (Header dump)
59:	00012833.bmp 	       2 MB 	    6570609 	  (Header dump)
60:	00013166.bmp 	       2 MB 	    6741361 	  (Header dump)
61:	00013221.bmp 	       2 MB 	    6769190 	  (Header dump)
62:	00013289.bmp 	       2 MB 	    6804150 	  (Header dump)
63:	00013483.bmp 	       2 MB 	    6903477 	  (Header dump)
64:	00013704.bmp 	       2 MB 	    7016730 	  (Header dump)
65:	00013722.bmp 	       2 MB 	    7025857 	  (Header dump)
66:	00014115.bmp 	       2 MB 	    7226993 	  (Header dump)
67:	00016475.bmp 	       1 MB 	    8435636 	  (Header dump)
68:	00016539.bmp 	       1 MB 	    8468428 	  (Header dump)
69:	00016571.bmp 	       1 MB 	    8484537 	  (Header dump)
70:	00016715.bmp 	       1 MB 	    8558376 	  (Header dump)
71:	00016949.bmp 	       1 MB 	    8678021 	  (Header dump)
72:	00017321.bmp 	       1 MB 	    8868533 	  (Header dump)
73:	00017507.bmp 	       1 MB 	    8964006 	  (Header dump)
74:	00017584.bmp 	       1 MB 	    9003112 	  (Header dump)
75:	00017709.bmp 	       1 MB 	    9067500 	  (Header dump)
76:	00017987.bmp 	    1006 KB 	    9209424 	  (Header dump)
77:	00018149.bmp 	     925 KB 	    9292523 	  (Header dump)
78:	00018812.bmp 	     593 KB 	    9632033 	  (Header dump)
79:	00018962.bmp 	     518 KB 	    9708989 	  (Header dump)
80:	00018983.bmp 	     508 KB 	    9719365 	  (Header dump)
81:	00019061.bmp 	     469 KB 	    9759309 	  (Header dump)
82:	00019353.bmp 	     323 KB 	    9908968 	  (Header dump)
83:	00019564.bmp 	     217 KB 	   10017258 	  (Header dump)
84:	00019601.bmp 	     199 KB 	   10035774 	  (Header dump)
85:	00019618.bmp 	     190 KB 	   10044497 	  (Header dump)
86:	00019865.bmp 	      67 KB 	   10170964 	  (Header dump)
87:	00002933.exe 	    1024 KB 	    1501926 	  (Header dump)
88:	00002976.exe 	    1024 KB 	    1524158 	  (Header dump)
89:	00003193.exe 	    1024 KB 	    1635238 	  (Header dump)
90:	00003313.exe 	    1024 KB 	    1696644 	  (Header dump)
91:	00003338.exe 	    1024 KB 	    1709478 	  (Header dump)
92:	00003374.exe 	    1024 KB 	    1727797 	  (Header dump)
93:	00003419.exe 	    1024 KB 	    1751014 	  (Header dump)
94:	00003734.exe 	    1024 KB 	    1912090 	  (Header dump)
95:	00003943.exe 	    1024 KB 	    2018986 	  (Header dump)
96:	00003949.exe 	    1024 KB 	    2022128 	  (Header dump)
97:	00004072.exe 	    1024 KB 	    2085373 	  (Header dump)
98:	00004215.exe 	    1024 KB 	    2158318 	  (Header dump)
99:	00004258.exe 	    1024 KB 	    2180550 	  (Header dump)
100:	00004475.exe 	    1024 KB 	    2291630 	  (Header dump)
101:	00004595.exe 	    1024 KB 	    2353036 	  (Header dump)
102:	00004620.exe 	    1024 KB 	    2365870 	  (Header dump)
103:	00004656.exe 	    1024 KB 	    2384189 	  (Header dump)
104:	00004701.exe 	    1024 KB 	    2407406 	  (Header dump)
105:	00005016.exe 	    1024 KB 	    2568482 	  (Header dump)
106:	00005225.exe 	    1024 KB 	    2675378 	  (Header dump)
107:	00005231.exe 	    1024 KB 	    2678520 	  (Header dump)
108:	00005355.exe 	    1024 KB 	    2741765 	  (Header dump)
109:	00005497.exe 	    1024 KB 	    2814702 	  (Header dump)
110:	00005540.exe 	    1024 KB 	    2836934 	  (Header dump)
111:	00005757.exe 	    1024 KB 	    2948014 	  (Header dump)
112:	00005877.exe 	    1024 KB 	    3009420 	  (Header dump)
113:	00005902.exe 	    1024 KB 	    3022254 	  (Header dump)
114:	00005938.exe 	    1024 KB 	    3040573 	  (Header dump)
115:	00005983.exe 	    1024 KB 	    3063790 	  (Header dump)
116:	00006298.exe 	    1024 KB 	    3224866 	  (Header dump)
117:	00006507.exe 	    1024 KB 	    3331762 	  (Header dump)
118:	00006513.exe 	    1024 KB 	    3334904 	  (Header dump)
119:	00006637.exe 	    1024 KB 	    3398149 	  (Header dump)
120:	00006779.exe 	    1024 KB 	    3471086 	  (Header dump)
121:	00006822.exe 	    1024 KB 	    3493318 	  (Header dump)
122:	00007039.exe 	    1024 KB 	    3604398 	  (Header dump)
123:	00007159.exe 	    1024 KB 	    3665804 	  (Header dump)
124:	00007184.exe 	    1024 KB 	    3678638 	  (Header dump)
125:	00007220.exe 	    1024 KB 	    3696957 	  (Header dump)
126:	00007265.exe 	    1024 KB 	    3720174 	  (Header dump)
127:	00007580.exe 	    1024 KB 	    3881250 	  (Header dump)
128:	00007789.exe 	    1024 KB 	    3988146 	  (Header dump)
129:	00007795.exe 	    1024 KB 	    3991288 	  (Header dump)
130:	00007919.exe 	    1024 KB 	    4054533 	  (Header dump)
131:	00008304.exe 	    1024 KB 	    4252140 	  (Header dump)
132:	00008591.exe 	    1024 KB 	    4399022 	  (Header dump)
133:	00008711.exe 	    1024 KB 	    4460428 	  (Header dump)
134:	00008736.exe 	    1024 KB 	    4473262 	  (Header dump)
135:	00008772.exe 	    1024 KB 	    4491581 	  (Header dump)
136:	00008817.exe 	    1024 KB 	    4514798 	  (Header dump)
137:	00009132.exe 	    1024 KB 	    4675874 	  (Header dump)
138:	00009341.exe 	    1024 KB 	    4782770 	  (Header dump)
139:	00009347.exe 	    1024 KB 	    4785912 	  (Header dump)
140:	00009471.exe 	    1024 KB 	    4849157 	  (Header dump)
141:	00009656.exe 	    1024 KB 	    4944326 	  (Header dump)
142:	00009873.exe 	    1024 KB 	    5055406 	  (Header dump)
143:	00009993.exe 	    1024 KB 	    5116812 	  (Header dump)
144:	00010018.exe 	    1024 KB 	    5129646 	  (Header dump)
145:	00010054.exe 	    1024 KB 	    5147965 	  (Header dump)
146:	00010099.exe 	    1024 KB 	    5171182 	  (Header dump)
147:	00010414.exe 	    1024 KB 	    5332258 	  (Header dump)
148:	00010623.exe 	    1024 KB 	    5439154 	  (Header dump)
149:	00010629.exe 	    1024 KB 	    5442296 	  (Header dump)
150:	00010753.exe 	    1024 KB 	    5505541 	  (Header dump)
151:	00010895.exe 	    1024 KB 	    5578478 	  (Header dump)
152:	00010938.exe 	    1024 KB 	    5600710 	  (Header dump)
153:	00011155.exe 	    1024 KB 	    5711790 	  (Header dump)
154:	00011275.exe 	    1024 KB 	    5773196 	  (Header dump)
155:	00011300.exe 	    1024 KB 	    5786030 	  (Header dump)
156:	00011336.exe 	    1024 KB 	    5804349 	  (Header dump)
157:	00011381.exe 	    1024 KB 	    5827566 	  (Header dump)
158:	00011696.exe 	    1024 KB 	    5988642 	  (Header dump)
159:	00011905.exe 	    1024 KB 	    6095538 	  (Header dump)
160:	00011911.exe 	    1024 KB 	    6098680 	  (Header dump)
161:	00012035.exe 	    1024 KB 	    6161925 	  (Header dump)
162:	00012181.exe 	    1024 KB 	    6237102 	  (Header dump)
163:	00012301.exe 	    1024 KB 	    6298508 	  (Header dump)
164:	00012326.exe 	    1024 KB 	    6311342 	  (Header dump)
165:	00012362.exe 	    1024 KB 	    6329661 	  (Header dump)
166:	00012407.exe 	    1024 KB 	    6352878 	  (Header dump)
167:	00012722.exe 	    1024 KB 	    6513954 	  (Header dump)
168:	00012931.exe 	    1024 KB 	    6620850 	  (Header dump)
169:	00012937.exe 	    1024 KB 	    6623992 	  (Header dump)
170:	00013061.exe 	    1024 KB 	    6687237 	  (Header dump)
171:	00013203.exe 	    1024 KB 	    6760174 	  (Header dump)
172:	00013246.exe 	    1024 KB 	    6782406 	  (Header dump)
173:	00013463.exe 	    1024 KB 	    6893486 	  (Header dump)
174:	00013583.exe 	    1024 KB 	    6954892 	  (Header dump)
175:	00013608.exe 	    1024 KB 	    6967726 	  (Header dump)
176:	00013644.exe 	    1024 KB 	    6986045 	  (Header dump)
177:	00013689.exe 	    1024 KB 	    7009262 	  (Header dump)
178:	00014004.exe 	    1024 KB 	    7170338 	  (Header dump)
179:	00014213.exe 	    1024 KB 	    7277234 	  (Header dump)
180:	00014219.exe 	    1024 KB 	    7280376 	  (Header dump)
181:	00014343.exe 	    1024 KB 	    7343621 	  (Header dump)
182:	00016669.exe 	    1024 KB 	    8534850 	  (Header dump)
183:	00016977.exe 	    1024 KB 	    8692706 	  (Header dump)
184:	00017051.exe 	    1024 KB 	    8730139 	  (Header dump)
185:	00017125.exe 	    1024 KB 	    8768477 	  (Header dump)
186:	00017384.exe 	    1024 KB 	    8900675 	  (Header dump)
187:	00017461.exe 	    1024 KB 	    8940112 	  (Header dump)
188:	00017694.exe 	    1024 KB 	    9059443 	  (Header dump)
189:	00017880.exe 	    1024 KB 	    9155009 	  (Header dump)
190:	00017952.exe 	    1023 KB 	    9191854 	  (Header dump)
191:	00018029.exe 	     985 KB 	    9231185 	  (Header dump)
192:	00018031.exe 	     984 KB 	    9232239 	  (Header dump)
193:	00018085.exe 	     957 KB 	    9259659 	  (Header dump)
194:	00018098.exe 	     950 KB 	    9266294 	  (Header dump)
195:	00018115.exe 	     942 KB 	    9275283 	  (Header dump)
196:	00018173.exe 	     913 KB 	    9304996 	  (Header dump)
197:	00018348.exe 	     825 KB 	    9394466 	  (Header dump)
198:	00018587.exe 	     706 KB 	    9516708 	  (Header dump)
199:	00018597.exe 	     701 KB 	    9522163 	  (Header dump)
200:	00018996.exe 	     501 KB 	    9726398 	  (Header dump)
201:	00019103.exe 	     448 KB 	    9781070 	  (Header dump)
202:	00019105.exe 	     447 KB 	    9782124 	  (Header dump)
203:	00019159.exe 	     420 KB 	    9809544 	  (Header dump)
204:	00019249.exe 	     375 KB 	    9855708 	  (Header dump)
205:	00019287.exe 	     356 KB 	    9875133 	  (Header dump)
206:	00019304.exe 	     347 KB 	    9883696 	  (Header dump)
207:	00019319.exe 	     340 KB 	    9891728 	  (Header dump)
208:	00019377.exe 	     311 KB 	    9921441 	  (Header dump)
209:	00019677.exe 	     161 KB 	   10075095 	  (Header dump)
210:	00004078.png 	     640 KB 	    2087936 	  (640 x 640)
211:	00005360.png 	     640 KB 	    2744320 	  (640 x 640)
212:	00006642.png 	     640 KB 	    3400704 	  (640 x 640)
213:	00010758.png 	     640 KB 	    5508096 	  (640 x 640)
214:	00013066.png 	     640 KB 	    6689792 	  (640 x 640)
Finish: Sun Jul 19 00:16:07 2020

215 FILES EXTRACTED
	
jpg:= 10
bmp:= 77
exe:= 123
png:= 5
------------------------------------------------------------------

Foremost finished at Sun Jul 19 00:16:07 2020
```

* Flag is in PNG files in output directory

<img src=flag.png>