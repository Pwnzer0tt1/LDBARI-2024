Decompilando il binario capiamo il funzionamento della funzione `check_key`

```c 
int64_t check_key(char* arg1, int64_t arg2)
{
    if (arg2 != 0x12)
        return 0;
    
    if (*arg1 != 0x48)
        return 0;
    
    if ((*arg1 + arg1[1]) != 0x6c)
        return 0;
    
    if ((arg1[1] ^ arg1[2]) <= 0x59)
        return 0;
    
    if ((arg1[2] * arg1[3]) != 0x17e8)
        return 0;
    
    if ((arg1[4] - arg1[5]) != 1)
        return 0;
    
    if ((arg1[6] % 0x32) != 5)
        return 0;
    
    if (strcmp((char *)(arg1 + 8),"love-linux"); == 0)
        return 1;
    
    return 0;
}
```

`arg2` e' calcolato in `main` come `strlen(input)`. 
- Per passare i check, la stringa dece essere lunga 0x12 (18) caratteri.
- il primo carattere deve essere = 0x48 (H)
- il primo + il secondo devono essere ugali a 0x6c; `0x48 + x = 0x6c` quindi `x = 0x6c - 0x48 = 0x24 ` ovvero il secondo carattere deve essere `$`.
- il secondo carattere xorato con il terzo deve essere <= 0x59. una soluzione e' il carattere `x`
- il terzo moltpilicato per il quarto deve essere uguale a 0x17e8, ovvero il quarto deve essere `3` se il terzo e' `x`
- il quinto carattere deve essere piu' grande di 1 rispetto al sesto. ci sono piu' soluzioni come `BA`, `CB`, ecc... 
- il settimo carattere deve essere modulo 50 uguale a 5. ci sono piu' soluzioni, come `7` o `i`
- l'ottavo carattere non e' verificato. 
- il resto della stringa(dal nono carattere in poi) deve essere uguale a "love-linux"
