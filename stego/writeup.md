Eseguendo `file` sul file raw notiamo la presenza di un filesystem
`pennetta.raw: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, root entries 512, sectors 8192 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 6, sectors/track 32, serial number 0x92d010cb, unlabeled, FAT (12 bit)`

Montandolo troviamo un file `hint` contenente il testo
```
Sembra che i file siano stati tutti eiliminati...
```

Possiamo estrarre i file cancellati con diversi tool, come `binwalk`, `photorec` o anche CyberChef.

La flag si trova nel commento exif dell'unica foto presente.

