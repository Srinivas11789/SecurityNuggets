package main
// Can you guess my favorite salad name? ONEQ{m3nq67n8l4559247641o321qm60q1mp7751m4075oqp72nl351q0072131p6oom1}

import (
         "fmt"
       )

func solve(a string) string {
    // DCTF is the start so caesar shift logic: ONEQ <==> DCTF ( Formula: 11)
    n := len(a);
    //s := strings.Split(a, "");
    //fmt.Println(s);
    s := []rune(a)
    for i:=0; i < n; i++ {
        asc := int(s[i]);
        if asc >= 65 && asc <=90 {
            asc -= 11;
            if asc < 65 {
                asc = 90-(64-asc);
            }
        } else if asc >= 97 && asc <= 122 {
            asc -= 11;
            if asc < 97 {
                asc = 122-(96-asc);
            }
        }
        s[i] = rune(asc);
    } 
    //return strings.Join(s,"");
    return string(s);
}

func main() {
    s := "ONEQ{m3nq67n8l4559247641o321qm60q1mp7751m4075oqp72nl351q0072131p6oom1}";
    fmt.Println(solve(s));
}

