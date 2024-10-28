L'obbiettivo e' effettuare il login come admin. 
La route di login e' vulnerabile a una SQL injection.
La soluzione e' una payload del tipo

```
' OR 1=1 username='admin' --
```

da inserire nel prompt della password
