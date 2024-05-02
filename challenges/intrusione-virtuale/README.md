# Intrusione Virtuale

## Descrizione
Salve futuro Hacker di élite! Se pensavi di poter entrare nel nostro esclusivo club segreto senza passare attraverso il fuoco delle nostre Regex difensive, 
ti sei sbagliato di grosso! Abbiamo preparato per te una sfida di registrazione all'avanguardia, e le nostre Regex sono più taglienti di un codice malevolo.

Riuscirai a superare le barriere cibernetiche e a infiltrarti nel nostro sistema con stile da vero hacker? 
Solo coloro che padroneggiano l'arte delle Regex potranno ottenere il titolo di "Intruso Supremo"!

Per ottenere il titolo di 'Intruso Supremo' visita la pagina: [http://www.beginner.havce.it:8080](http://www.beginner.havce.it:8080).

HINT: Utilizzare la rappresentazione esadecimale potrebbe esserti d'aiuto.

*Author: [@benjamin](https://github.com/b3nj4m1no)*


## Soluzione
You should make a JSON that satisfies the following conditions:

The `backend` server, i.e. a JSON parser of Express, recognizes it as a JSON containing a key `dammilaflag`.
The `proxy` server fails to parse it as a JSON value at `JSON.parse(req.body)`.
In conclusion, the following JSON satisfies them where `\ufeff` is a BOM:

```py
# Author: @benjamin

import requests

url = "http://www.beginner.havce.it:8080"

# 192145884 --> numero più grande --> hex(192145884) = 0xb73e9dc
# 192014812 --> numero
# 131072    --> differenza --> hex(131072) = 0x20000

payload = {
    "password": "0xb73e9dc-0x20000"
}

r = requests.post(url, data=payload)

print(r.text)
```

## Flag
havceCTF{m4l3det7o_3va1}
