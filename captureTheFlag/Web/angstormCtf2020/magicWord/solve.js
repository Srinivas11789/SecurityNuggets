/*
(env) Srinivass-MacBook-Pro:magicWord darkknight$ node solve.js 
actf{1nsp3c7_3l3m3nt_is_y0ur_b3st_fri3nd}
*/

const fetch = require("node-fetch");
fetch("https://magicword.2020.chall.actf.co/flag?msg=" + encodeURIComponent("please give flag")).then(res => res.text()).then(txt => console.log(txt.split``.map(v => String.fromCharCode(v.charCodeAt(0) ^ 0xf)).join``));
