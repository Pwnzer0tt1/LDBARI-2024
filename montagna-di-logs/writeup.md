La soluzione e' richiede estrarre le parti della flag, sortarle e unirle 

Soluzione:
```
grep -Po "PART\K\d+{.*}" logs.txt | sort -n | grep -Po "{\K.*(?=})" |  tr '\n' ' ' | sed "s/ //g"
```

Usiamo la prima grep per estrarre le parti, sort numerico, poi estraiamo con la seconda grep il contenuto tra le graffe.
