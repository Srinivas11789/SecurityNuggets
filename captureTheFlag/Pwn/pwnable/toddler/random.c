#include <stdio.h>

int main(){
        unsigned int random;
        random = rand();        // random value!
        printf ("%u",random);
        unsigned int key=0;
        scanf("%d", &key);
        printf("%2d", 1804289383 ^ 3735928559);
        printf("%d", 0xdeadbeef);
        if( (key ^ random) == 0xdeadbeef ){
                printf("Good!\n");
                system("/bin/cat flag");
                return 0;
        }

        printf("Wrong, maybe you should try 2^32 cases.\n");
        return 0;
}

