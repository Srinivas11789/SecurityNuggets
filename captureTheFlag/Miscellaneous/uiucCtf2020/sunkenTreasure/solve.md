### Challenge

* Sunken Treasure: 200
```
We think Blathers might be looking for treasure in the Pacific Ocean not too far from an island. The only data we were able to find about his travel were these logs we pulled from his Uber app. Maybe you can make some sense of them?

Note: the flag format is slightly different in this challenge
```

### Recon & Solve
* Hints: Logs from Uber App
* Google for uber logs, coordinates and end up at https://eng.uber.com/h3/
* The example in github shows the similarity in the entries in logs ( Prefix and Suffix ffff )
* From the links --> https://github.com/uber/H3
* Install h3 and run `h3ToGeoBoundary` to get the hexagon boundry for each of the entry
* Use solve.py to do that iteratively
* Once we receive the coordinates of the hexagon vertices we plot them
* My friend helped to make it easier to plot via excel and it was fast!
* I also did it with matplotlib and expanded a bit to get a proper plot with flag at ans.jpg
* x y were altered to rotate the flag to proper legible format

<img src=ans.jpg>

### Flag
* uiuctf[H3_iZ_very_HEX]