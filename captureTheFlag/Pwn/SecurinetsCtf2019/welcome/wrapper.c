/* author : Anis_Boss */
#include <stdio.h>



int search(char str[], char word[])
{
    int l, i, j;
    /*length of word */
   for (l = 0; word[l] != '\0'; l++); 
    for (i = 0, j = 0; str[i] != '\0' && word[j] != '\0'; i++)
    {
        if (str[i] == word[j])
        {
            j++;
        }
        else
        {
            j = 0;
        }
    }
    if (j == l)
    {
        /* substring found */
        return (i - j);
    }
    else
    {   
        return  - 1;
    }
}

int delete_word(char str[], char word[], int index)
{
    int i, l;
    /* length of word */
    for (l = 0; word[l] != '\0'; l++);

    for (i = index; str[i] != '\0'; i++)
    {
        str[i] = str[i + l + 1];
    }
}

void main(int argc, char* argv[])
{
char * blacklist[]={"cat","head","less","more","cp","man","scp","xxd","dd","od","python","perl","ruby","tac","rev","xz","tar","zip","gzip","mv","flag","txt","python","perl","vi","vim","nano","pico","awk","grep","egrep","echo","find","exec","eval","regexp","tail","head","less","cut","tr","pg","du","`","$","(",")","#","bzip2","cmp","split","paste","diff","fgrep","gawk","iconv","ln","most","open","print","read","{","}","sort","uniq","tee","wget","nc","hexdump","HOSTTYPE","$","arch","env","tmp","dev","shm","lock","run","var","snap","nano","read","readlink","zcat","tailf","zcmp","zdiff","zegrep","zdiff"};


 char str[80], word[50];
    int index;
    printf("Welcome to Securinets Quals CTF \o/ \n");
    printf("Enter string:\n");
    read(0,str,79);
    //printf("Input is %s",str);
    //printf("%d %d", sizeof(blacklist), sizeof(blacklist[0]));
for (int i=0;i<sizeof(blacklist)/sizeof(blacklist[0]);i++)
{
    index = search(str, blacklist[i]);
    //printf("%d", index);
    //printf("%s", str);
    if (index !=  - 1)
    {
        delete_word(str, blacklist[i], index);
	//printf("%s", str);
    }
    //printf("%s", str);

}
printf("Execuring... %s", str);
setreuid(geteuid(),geteuid());
close(0);
system(str);
}


