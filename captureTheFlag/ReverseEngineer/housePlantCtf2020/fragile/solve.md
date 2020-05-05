### Challenge
```
Can you help me move my stuff? This one's fragile!
```

### Solve

* Reverse the logic to get the flag

```
public static void reverse(){
    String flag = "h1_th3r3_1ts_m3";
    String realFlag = "ÐdØÓ§åÍaèÒÁ¡";
    String theflag = "";
    for(int i = 0; i < flag.length(); i++){
        theflag += (char)((int)(realFlag.charAt(i)) - (int)(flag.charAt(i)));
    }
    System.out.println("rtcp{"+ theflag + "}");
}
```

* Solve

```
kali@kali$ java fragile 
Enter flag: rtcp{h1_th3r3_1ts_m3}
What you inputed is: 
rtcp{h1_th3r3_1ts_m3}
Stripped flag is:
h1_th3r3_1ts_m3
Reversed answer is: 
rtcp{h3y_1ts_n0t_b4d}
Access denied!

kali@kali$ java fragile 
Enter flag: rtcp{h3y_1ts_n0t_b4d}
What you inputed is: 
rtcp{h3y_1ts_n0t_b4d}
Stripped flag is:
h3y_1ts_n0t_b4d
Reversed answer is: 
rtcp{h3y_1ts_n0t_b4d}
Access granted.
```

* Flag: rtcp{h3y_1ts_n0t_b4d}