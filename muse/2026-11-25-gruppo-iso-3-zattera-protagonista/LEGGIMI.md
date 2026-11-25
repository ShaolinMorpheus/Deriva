# Gruppo iso 3 — zattera e protagonista in isometrico (Deriva)

Zattera-base (la casa del giocatore, stesso design del Gruppo 2) e protagonista fermo, ridisegnati in vista isometrica 2:1 alla scala dell'anteprima iso 2 v2 (passo griglia 128×64): **i PNG sono 1:1 in gioco, non vanno ridimensionati**. Niente ombre proiettate, niente contorno scuro, niente scritte.

Questa consegna segue le specifiche definitive di Davide (25 nov, ore 21:48) e **sostituisce la bozza** `2026-11-25-gruppo-iso-3-zattera-protagonista-bozza/` (specifiche diverse: viste cardinali, protagonista 230 px, zattera 3×3 senza albero/tenda) — la bozza resta in locale come storico, non va usata.

## Zattera — design e direzioni
Stesso design del Gruppo 2: ponte di assi di legno, file di bidoni blu e ruggine legati con corde lungo i due lati lunghi (galleggianti), albero con vela rattoppata ammainata all'estremità di prua, tenda rattoppata a poppa, cassa e due taniche (verde e rossa) sul ponte. **La prua è l'estremità con l'albero** (come nel Gruppo 2).

Consegnate le **4 direzioni diagonali**: NE, SE, SO, NO. Le 4 cardinali (N, E, S, O) sono state tentate e **scartate**: il generatore non le rende in isometrico coerente (la S è uscita quasi dall'alto, N/E/O sono uscite come duplicati delle diagonali). I grezzi restano in `lavoro-gruppo4a/gen_iso3/` come storico.

- Impronta: **3×2 tessere**, larghezza disegno 640 px ((3+2)·128).
- **Ancoraggio centro-basso: (320, H)** in ogni file = il punto a terra sotto il centro dello scafo; il centro dell'impronta 3×2 sta a (320, H−160) nel PNG. Per piazzare la zattera con centro impronta nel punto schermo P: angolo alto-sinistro del PNG = P − (320, H−160).
- Controllo impronta fatto: con l'esagono 3×2 centrato sull'ancoraggio, i lati sud dello scafo (quelli di attracco) seguono l'impronta; sul lato nord il disegno sporge di qualche decina di px oltre il rombo (disegno artistico, non proiezione meccanica) — ai fini di navigazione/attracco fa fede l'impronta dichiarata.
- Limite dichiarato: nella direzione NE il generatore ha omesso la cassa sul ponte (ci sono tenda e taniche); nelle altre tre direzioni la cassa c'è. Scafo, bidoni, albero e tenda sono gli stessi in tutte e quattro.

## Protagonista — fermo, 4 direzioni
Stesso personaggio della prova 3/4 e del Gruppo 2: berretto rosso sbiadito, giubbotto di salvataggio arancione con cinghie e fibbie, camicia strappata grigio-verde, pantaloni cargo marroni, stivali scuri, barba corta. Fermo, braccia lungo i fianchi.

- Altezza: **esattamente 100 px piedi-testa in tutte e 4 le direzioni** (stesse proporzioni e stessi colori, verificati con scheda di confronto sul mare: SE e SO di fronte tre quarti, NE e NO di spalle tre quarti).
- **Ancoraggio ai piedi, centro-basso: (W/2, 100)** in ogni file. Per piazzarlo con i piedi nel punto schermo P: angolo alto-sinistro del PNG = P − ancoraggio.
- La **camminata (6 fotogrammi per direzione) NON è in questa consegna**: viene dopo, come da programma.

## I file (PNG trasparenti, già in scala 1:1)
| File | Dimensioni px | Impronta | Ancoraggio (x, y) | Note |
|---|---|---|---|---|
| `zattera_iso_ne.png` | 640×468 | 3×2 | (320, 468) | Prua (albero) a nord-est, lunghezza lungo l'asse j. Senza cassa sul ponte (vedi limite) |
| `zattera_iso_se.png` | 640×436 | 3×2 | (320, 436) | Prua a sud-est, lunghezza lungo l'asse i |
| `zattera_iso_so.png` | 640×401 | 3×2 | (320, 401) | Prua a sud-ovest, lunghezza lungo l'asse j |
| `zattera_iso_no.png` | 640×461 | 3×2 | (320, 461) | Prua a nord-ovest, lunghezza lungo l'asse i |
| `protagonista_iso_ne.png` | 37×100 | — (personaggio) | (18, 100) | Fermo, di spalle tre quarti verso nord-est |
| `protagonista_iso_se.png` | 40×100 | — | (20, 100) | Fermo, di fronte tre quarti verso sud-est |
| `protagonista_iso_so.png` | 38×100 | — | (19, 100) | Fermo, di fronte tre quarti verso sud-ovest |
| `protagonista_iso_no.png` | 36×100 | — | (18, 100) | Fermo, di spalle tre quarti verso nord-ovest |
| `anteprima_iso3.png` | 2500×1750 | — | — | Scena 1:1 sul mare vero: piattaforma iso 1 (6×4 + pontile a sud con pali in acqua), container e serbatoio iso 2 v2 in scala sul ponte, zattera SE attraccata a sud del pontile, protagonista SE in piedi sul ponte |

## Controlli fatti
- Ritaglio dal fondo magenta con l'algoritmo v3 (despill per tonalità + riempimento RGB delle zone trasparenti dal vicino opaco): **residuo magenta 0 e tinta magenta forte 0 su tutti gli 8 sprite** (stesse due metriche della v2 iso 2).
- Ogni sprite verificato sul mare vero: bordi puliti, niente alone, niente ombre.
- Scala: zattera larga 640 px esatti, protagonista alto 100 px esatti in tutte le direzioni; anteprima assemblata solo con pezzi 1:1 (iso 1, iso 2 v2, questa consegna) e controllata a vista: le proporzioni reciproche tornano (protagonista sul ponte, zattera contro il pontile).
- Master a piena risoluzione: i ritagli interi prima della scalatura sono in `lavoro-gruppo4a/gen_iso3/` come `<nome>_master.png`, accanto ai grezzi di generazione.

## Cosa NON deve cambiare
- Design della zattera (scafo, bidoni, albero+vela ammainata a prua, tenda a poppa) e del protagonista (berretto rosso, giubbotto arancione): gli stati futuri (motore, camminata) devono mantenere questi design e questa scala.

## Cosa manca / prossime consegne
- Camminata del protagonista: 6 fotogrammi × 4 direzioni, stessa scala e stesso ancoraggio ai piedi.
- Variante zattera con motore fuoribordo in isometrico (nel Gruppo 2 esiste dall'alto).
- Direzioni cardinali della zattera (N, E, S, O): da riprovare solo se il motore di gioco le richiede davvero.

STATO: pronto
