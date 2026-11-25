# RISPOSTA di Claude — Gruppo iso 1 e Gruppo iso 2 (25 nov 2026, sera)

Letti e provati entrambi i gruppi. In gioco non è ancora montato nulla: il gioco resta **v0.1b.8** (dall'alto) finché non c'è il motore isometrico.

## Cosa ho verificato (e va bene)
- Scaricati dal repo e decodificati: 15 pezzi del Gruppo iso 1, 12 oggetti + 2 anteprime del Gruppo iso 2.
- **Misure: tutte uguali ai LEGGIMI** (256×256, palo 96×256, e le dimensioni di tutti i 12 oggetti).
- **Anteprima completa ricucita** dalle due parti `.b64.1` + `.b64.2`: PNG valido, **3100×2150**, RGB. Impronta SHA-256 della mia copia: `d8ed8223e697cd0e22f32fc6e6da5cc7ba78da13d783e0ef68c0ee43ff74aaab` (se la tua è uguale, è identica bit per bit).
- Pezzi iso 1 assemblati da me (6×6 rombi, a/b/c a caso, buco, facce, ringhiere, angolo nord): **il pavimento si affianca senza giunture**, la ringhiera è continua sui due lati nord, l'angolo nord combacia, il buco lascia vedere il mare. Resta solo una ripetizione a croce delle macchie di ruggine a distanza regolare (non grave).
- Lo stile è quello approvato e, a occhio, nell'anteprima completa le proporzioni tra protagonista, container e derrick reggono (misura fatta a mano sul protagonista piccolo: da confermare con le correzioni di scala qui sotto).

## Da rifare (Claude non ritocca i disegni)

### 1. Filo magenta/viola sul bordo di 4 oggetti — Gruppo iso 2
Pixel semitrasparenti col colore del fondo-chiave (circa R150 G25 B140), a ~1 px dal bordo. Visibile a 1:1 sulla gamba destra del derrick e lungo il bordo del serbatoio sul mare.
| File | Pixel con alone |
|---|---|
| `derrick_iso.png` | 38.571 |
| `baracca_iso.png` | 9.595 |
| `serbatoio_iso.png` | 8.714 |
| `container_ocra_iso.png` | 7.405 |
Zero nei container verde e ruggine, nei tubi, nella gru, nella testa pozzo, nella baracca interno. Il LEGGIMI dice «0 pixel su tutti i file della seconda parte»: il controllo va fatto anche sulla prima parte. Rifare lo scontorno (despill) di questi 4 file. Come controllo, conta i pixel visibili con (R−G)>90 e (B−G)>90: devono essere 0.

### 2. `faccia_so.png` e `faccia_legno_so.png`: geometria sbagliata
La faccia SE è giusta: parallelogramma, spessore 64 px uniforme, bordo basso parallelo a quello alto. La faccia **SO no**: lo spessore va da 128 px (a sinistra) a 64 px (a destra) e il bordo basso è piatto a y=255. Messe in fila lungo il lato sud-ovest fanno una **scalinata** (provato su 6 tessere). Rifarla come specchio della SE: bordo alto (0,128)→(128,192), bordo basso (0,192)→(128,256), spessore 64. Se la scalinata sul pontile su pali è voluta, scrivilo nel LEGGIMI; per la faccia d'acciaio non può esserlo.

### 3. Ingombri dichiarati ≠ scala usata nell'anteprima (serve una scala chiara per ogni oggetto)
Il LEGGIMI dà impronte (3×3, 4×2, 4×4…) e dimensioni dei file, ma i file sono molto più grandi della scala con cui li hai messi nell'anteprima, e la scala non è scritta. Confrontando le immagini ho ricavato la scala dell'anteprima (px anteprima ÷ px del file; 1 passo di griglia = 128×64 px):

| Oggetto | File | Impronta dichiarata | Scala in anteprima | Larghezza in anteprima | Larghezza / 128 («W+D») | W+D dichiarato |
|---|---|---|---|---|---|---|
| serbatoio | 1892×1082 | 3×3 | 0,174 | 329 px | 2,6 | 6 |
| container ocra / ruggine / verde | ~1608×1178 | 4×2 | 0,298 | 480 px | 3,75 | 6 |
| baracca (e interno) | 1313×1087 | 3×3 | 0,252 | 331 px | 2,6 | 6 |
| testa pozzo | 1034×1061 | 2×2 | 0,252 | 261 px | 2,0 | 4 |
| derrick | 704×2092 | 4×4 | 0,240 | 169 px | 1,3 | 8 |
| gru | 1811×785 | 6×2 | 0,388 | 703 px | 5,5 | 8 |
| tubo dritto / curva / T | ~1400–1670 | 1×1 | 0,086 / 0,072 / 0,080 | ~121 px | 0,95 | 2 |

(Stima fatta a programma per confronto d'immagine: affidabile per serbatoio, container ocra, testa pozzo e tubi; meno per derrick, gru e baracca, che l'anteprima copre in parte. Container verde e ruggine non rilevati da soli: li ho assunti alla scala dell'ocra, che hai detto uguale.)

In pratica, alla scala dell'anteprima, gli ingombri veri sono circa: derrick e testa pozzo ≈ 1×1, serbatoio e baracca ≈ 1,3×1,3, container ≈ 2×2 (non 4×2), tubi < 1 tessera. Il motore ha bisogno di ingombri veri per le collisioni e per posizionare gli oggetti, e delle proporzioni giuste rispetto al protagonista.

**Richiesta:** riconsegna i 12 oggetti **già ridimensionati alla scala dell'anteprima approvata** (o alla scala che preferisci, ma allora scrivila), con nel LEGGIMI per ogni oggetto: impronta reale (larghezza×profondità in tessere) e il punto del PNG dove sta l'angolo frontale dell'impronta (ancora). Così il gioco li usa a scala 1 senza ricalcoli.
- Peso: oggi i 12 oggetti pesano ~24 MB di PNG (~75 MB decodificati in memoria). Alla scala dell'anteprima scendono a meno di un decimo. Sul telefono è importante.
- Qualità: per non perdere nitidezza sul Galaxy S25 Plus (tessera iso 128×64 css = ~333×166 px reali), conviene consegnare gli oggetti a **1,5× la scala dell'anteprima** (non 1×) e il pavimento/le facce/i bordi con canvas **384×384** (rombo 384×192) invece di 256×256. Ne parlo con Davide prima di fissarlo.

## Cosa serve subito dopo, per giocare in isometrico
1. **Zattera in isometrico** (nell'anteprima è ancora quella dall'alto).
2. **Protagonista in isometrico**, almeno fermo + camminata nelle 4 direzioni (NE, NO, SE, SO).
3. Le correzioni qui sopra (alone, faccia SO, scala/ancoraggi).

Claude, intanto: ragiona il motore a rombi (mare piatto come fondo continuo, piattaforme sulla griglia iso, ordine di disegno per i+j, collisioni sulla griglia della piattaforma). Niente lavori sul gioco finché Davide non dà l'ok al prototipo.

STATO: Claude ha letto e verificato; correzioni richieste (alone magenta, faccia SO, scala/ancoraggi).
