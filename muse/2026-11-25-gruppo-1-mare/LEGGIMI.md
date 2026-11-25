# Gruppo 1 — Tessere di mare (Deriva)

## Cosa sono i file
Tessere di mare 256×256 px (PNG opache), in gioco 64 px ciascuna (4×).
Vista dall'alto pura. Registro acquerello desaturato approvato nella prova di stile.

| File | Uso nel gioco | Misura |
|---|---|---|
| `mare_basso_a.png` | Acqua bassa, sabbia sotto | 256×256 |
| `mare_medio_a.png` | Acqua media | 256×256 |
| `mare_fondo_a.png` | Acqua profonda | 256×256 |
| `mare_macchia_petrolio.png` | Acqua con alone di petrolio: è solo il fondo della zona, sopra ci va la chiazza (vedi sotto). In piccoli gruppi, non come mare intero | 256×256 |
| `macchia_olio_1.png` … `macchia_olio_4.png` | **La chiazza d'olio vera**: tonda, iridescente, si deve notare. PNG trasparenti, 4 fotogrammi dello stesso disegno che cambia forma piano | 512×512 (in gioco 128 px = 2×2 tessere) |
| `anteprima_macchia_olio.png` | Anteprima: sopra la chiazza sul mare vero, sotto i 4 fotogrammi in fila sul mare | 1024×768 |
| `anteprima_gruppo1.png` | Anteprima: ogni tessera ripetuta 2×2, griglia 2×2 (alto-sx basso, alto-dx medio, basso-sx fondo, basso-dx macchia) | 1024×1024 |
| `controllo_3x3_*.png` | Controllo giunture: ogni tessera ripetuta 3×3 | 768×768 |

## Dove vanno nel gioco
- Le 3 tessere di profondità sono il fondo del mondo: il gioco le affianca a perdita d'occhio e le mescola in base alla profondità del rumore.
- `mare_macchia_petrolio.png` segna zone inquinate (POI petrolio): poche tessere vicine, mai distese intere.
- **La chiazza si muove** (richiesta di Davide, 25 nov): il gioco disegna `macchia_olio_1..4` sopra la zona, le cicla lente (~2 fotogrammi al secondo) e fa derivare la chiazza di pochi px avanti e indietro dentro la sua zona, come galleggiasse. La chiazza è un oggetto sopra l'acqua, non una tessera: la regola «niente cerchi nell'acqua» vale per le tessere del mare, non per lei.

## Cosa NON deve cambiare
- Registro desaturato e gessoso del mare; niente blu saturi lisci, niente schiuma bianco bruciato, niente ovali/cerchi nell'acqua.
- Niente scritte, niente ombre proiettate.

## Verifiche fatte (controllo dichiarato)
- Ogni tessera è stata resa tileabile a programma (dissolvenza incrociata di 96 px sulle giunture) e controllata ripetuta 3×3 a occhio ingrandito.
- Giunture: basso, medio e fondo senza linee visibili; macchia con giunture appena percettibili se affiancata in distese larghe — per questo va usata in piccoli gruppi.
- Saturazione media misurata: basso 0,06 / medio 0,16 / fondo 0,19 / macchia 0,09 — registro desaturato rispettato (tetto 0,57 del mare di Sette Mari).
- Due pezzi rifatti in questa stessa consegna: `mare_basso_a` (v1 troppo a dune diagonali) e `mare_macchia_petrolio` (v1 con macchia centrale che si ripeteva come carta da parati). Le versioni qui dentro sono le v2.

- Fotogrammi chiazza: scontornati da 3 disegni su fondo magenta (il 4° è una deformazione ondulata del 1°); verifica numerica: tela 512×512, centro opaco (alpha 255), copertura ~66–72% della tela in tutti e 4.

## Cosa è nuovo
- Prime tessere di gioco di Deriva: il mare su cui poi stanno zattera, relitti e atolli.
- Chiazza d'olio come oggetto animato (25 nov, su richiesta di Davide): prima versione era solo un alone nella tessera e non si notava; ora è tonda, iridescente e si muove nella zona.

## Cosa manca ancora (Gruppo 1 incompleto)
- Varianti `b` di basso/medio/fondo (per non far ripetere sempre la stessa tessera).
- `riva_sabbia_bordo.png` e `sabbia_atollo_a/b.png` (servono quando si fa il Gruppo 4 atolli).

## Verdetto
- Davide, 25 nov 2026: **Gruppo 1 approvato** («Sì, Gruppo 1 va bene — avanti col Gruppo 2»), dopo la correzione della chiazza d'olio come oggetto tondo animato.

## Nota di caricamento (25 nov 2026)
I PNG di questa consegna sono saliti su GitHub come `nome.png.b64` (base64, una riga) con `elenco.txt` che dà l'ordine: l'invio diretto dei PNG non è passato. Per usarli: decodificare ogni `.b64` nel `nome.png` corrispondente. Contenuto identico ai PNG originali (verifica per hash fatta da Muse dopo l'invio).

STATO: pronto
