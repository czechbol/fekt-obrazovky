# fekt-obrazovky

Jednoduchý web-based slider na obrázky a videa.

## Soubory které slidovat

Do složky `static/resources` je potřebné uložit obrázky a videa která budou zobrazována. 
Je možné využít přímo složky `static/resources` a nebo v ní vytvořit podsložky které budou dostupné pod jinou URL cestou `/precise/slozka`.
Tato cesta bude zobrazovat pouze soubory v této složce. Pro `static/resources/dulezita_slozka` to bude pod cestou `/precise/dulezita_slozka`, 
ve vývojovém módu konkrétně například `http://127.0.0.1:5000/precise/dulezita_slozka`.

Tyto `precise` cesty mají navíc tu vlastnost, že pokud daná podsložka neexistuje, jsou použity soubory ze složky `static/resources`.
Díky tomu je možné na každé obrazovce nastavit již konkrétní URL cestu a za normálních okolností je nechat používat soubory ve `static/resources`.
Pokud nastane situace kdy bude třeba nastavit na některou z obrazovek jiný obsah, 
stačí pouze vytvořit složku která odpovídá cestě nastavené na obrazovce a uložit do ní vše potřebné.

## Nastavení vývojového režimu

```console
foo@bar:~$ python3 -m venv .venv
foo@bar:~$ python3 -m pip install -r requirements.txt
foo@bar:~$ python3 -m pip install -r requirements-dev.txt
```
## Spuštění ve vývojovém režimu

```console
foo@bar:~$ python3 __init__.py
```
V konzoli se vypíše URL kterou lze napsat do prohlížeče a testovat aplikaci.

## Produkční režim
Předpokládám že kdokoliv bude chtít tuto aplikaci nasadit na produkční prostředí, 
má o tom dostatečné znalosti, případně se doučí, protože je to značně individuální.
