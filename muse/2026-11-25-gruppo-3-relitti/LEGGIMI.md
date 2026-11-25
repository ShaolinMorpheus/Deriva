# Gruppo 3 — Relitti e risorse (Deriva)

## Cosa sono i file
PNG trasparenti, vista dall'alto pura, luce neutra dall'alto, niente ombre proiettate, niente contorno scuro.
Misure PNG = 4× la misura in gioco.

| File | Uso nel gioco | Misura PNG | In gioco |
|---|---|---|---|
| `relitto_barca.png` | Relitto galleggiante: scafo di legno spezzato pieno di assi rotte, prua a sinistra | 768×512 | 192×128 |
| `relitto_auto.png` | Carcassa d'auto arrugginita su pontile galleggiante, muso a sinistra | 512×384 | 128×96 |
| `cumulo_rottami.png` | Cumulo di lamiere, tubi e rottami: la risorsa «rottami» da raccogliere | 512×512 | 128×128 |
| `tanica_benzina.png` | Tanica rossa arrugginita: raccolto = benzina | 256×256 | 64×64 |
| `barile_petrolio.png` | Barile scuro dall'alto con macchia di grezzo sul coperchio: raccolto = petrolio da raffinare | 256×256 | 64×64 |
| `cassa_rifornimenti.png` | Cassa di legno con maniglie di corda: raccolto misto | 256×256 | 64×64 |
| `anteprima_gruppo3.png` | Anteprima sul mare vero (Gruppo 1): relitti in acqua, risorse sul basso | 1024×768 | — |

## Dove vanno nel gioco
- I relitti sono POI minori: stanno in mare aperto, il gioco li ruota a piacere (sono rottami, non hanno una prua di navigazione da rispettare, ma la forma è orizzontale).
- Tanica, barile e cassa sono i raccolti: compaiono su relitti, atolli e avamposti; quando il giocatore li prende, il gioco salva la modifica nel delta (vedi PROGETTO) e il pezzo sparisce.
- L'effetto «semisommerso» del relitto barca lo fa il gioco (trasparenza e tinta), il PNG è lo scafo intero.

## Cosa NON deve cambiare
- Palette approvata: ruggine e lamiera saturi sul mare desaturato; niente scritte, niente ombre nei PNG, niente contorno scuro.

## Verifiche fatte (controllo dichiarato)
- Scontorno da fondo magenta a programma (i pezzi nascono da due fogli da 3 oggetti, tagliati per terzi).
- Barca e auto erano state generate in verticale: ruotate di 90° in orizzontale a programma, design invariato.
- Margini del contenuto ≥14 px in tutti i pezzi; anteprima composta sul mare vero e vista ingrandita.

## Cosa è nuovo
- I primi POI saccheggiabili e le tre risorse del giro di gioco (benzina, petrolio, rottami/cassa).

## Cosa manca ancora (Gruppo 3)
- Variante relitto grande (nave) e relitto con contenitore: solo se il prototipo chiede più varietà di POI minori.
- Stati «già saccheggiato» dei relitti (scafo vuoto): si fanno col verdetto su v0.1.

## Nota di caricamento
Come le altre consegne di Deriva: i PNG salgono su GitHub come `nome.png.b64` (una riga) con `elenco.txt`, da decodificare nei `nome.png` corrispondenti.

## Verdetto
- Davide, 25 nov 2026: **Gruppo 3 approvato** («Sì, Gruppo 3 va bene — caricalo»).

STATO: pronto
