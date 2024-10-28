Analizzando il codice notiamo come la variabile target viene inserita direttamente nel comando eseguito dalla shell.

```python
command = f"traceroute {target} | tail +2"
```

inviando come target `127.0.0.1; ls` notiamo come il comando ls viene eseguito e viene stampata la presenza del file `flag.txt`. 
Provando a effettuare un cat di flag.txt `127.0.0.1; cat flag.txt` non riusciamo a vedere la flag, poiche' e' su una sola riga, e il "tail +2" rimuove la prima riga dall'output. E' possibile bypassarlo in numerosi modi, il piu' semplice e' commentare il resto del comando con `#`

Payload finale: `127.0.0.1; cat flag.txt #`
