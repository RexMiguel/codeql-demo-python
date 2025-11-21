# codeql-demo-python

Mini proyecto con código **intencionalmente vulnerable** para demostrar
GitHub Code Scanning (CodeQL).

Archivos:

- `insecure_subprocess.py`: posible command injection con `subprocess.run(..., shell=True)`.
- `insecure_eval.py`: uso inseguro de `eval` sobre entrada del usuario.
- `insecure_sql.py`: SQL injection con `sqlite3` y concatenación de strings.
