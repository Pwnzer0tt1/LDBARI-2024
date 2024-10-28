```python
target = target.replace(" ", "")
command = f"traceroute {target} | tail +2"
```

Questa volta dalla variabile `target` vengono rimossi gli spazi. Non possiamo piu' eseguire una payload come  `127.0.0.1;cat flag.txt`, poiche' verrebbe eseguito il comando `catflag.txt` (senza spazi), che non esiste.

Possiamo usare la variabile d'ambiente `${IFS}` per inserire separatori di parametri. Non possiamo pero' scrivere commenti quindi dobbiamo scrivere due righe o eseguire due comandi diversi per bypassare il `tail +2`.

Una possibile paylaod e' `127.0.0.1;cat${IFS}flag.txt${IFS}flag.txt`.
