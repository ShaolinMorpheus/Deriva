# Zattera in 16 viste — LOTTO A (Deriva)

Zattera che ruota fluida a 360° (una vista ogni 22,5°) per il nuovo sistema di montaggio. Questa consegna contiene **solo il lotto A: le 4 viste diagonali 00, 04, 08, 12** e **sostituisce la zattera del Gruppo iso 3** (le viste singole `zattera_iso_ne/se/so/no.png` restano come storico). Il testo integrale della richiesta è in `RICHIESTA.md` in questa cartella.

## Come sono fatte le 4 viste
Le 4 diagonali coincidono con le direzioni già approvate del Gruppo iso 3: i disegni sono gli stessi master approvati (stessa zattera, set coerente generato in un unico giro: ponte di assi, barili blu/ruggine legati sul bordo, albero con vela avvolta a prua, tenda rattoppata a poppa con ingresso verso prua, cassa, taniche rossa e verde), ripuliti e rimontati sulla tela fissa nuova:
- rimossi speck alfa residui ai bordi (nella SE due pixel spuri allungavano la tela di ~80 righe a piena risoluzione);
- despill per tonalità applicato anche al master NE-con-cassa (era un edit ritagliato a parte: 339 px con tinta magenta forte → 0);
- contenuto riscalato a larghezza esatta 640 px (impronta 3×2, passo 128×64) e montato **senza ritaglio** sulla tela 704×512.

## Tela e centro impronta (verificati)
- Tela **704×512** per tutte le viste, sfondo trasparente.
- **Centro dell'impronta (centro del rettangolo 3×2 sul pelo dell'acqua) al pixel (352, 336) in ogni vista**, per costruzione (convenzione iso 3: nel contenuto 640×H il centro impronta sta a (320, H−160); montaggio a offset (32, 496−H)).
- Misura sui file finali: centro x del bbox forte = 351,5 in tutte le viste; vertice sud dell'impronta sulla riga 495 (bordo inferiore a y=496) in tutte le viste.

| Vista | Prua | Contenuto px | Offset di montaggio | Master sorgente |
|---|---|---|---|---|
| `zattera_iso_00.png` | SE (basso-destra) | 640×405 | (32, 91) | iso 3 SE |
| `zattera_iso_04.png` | SO (basso-sinistra) | 640×401 | (32, 95) | iso 3 SO |
| `zattera_iso_08.png` | NO (alto-sinistra) | 640×461 | (32, 35) | iso 3 NO |
| `zattera_iso_12.png` | NE (alto-destra) | 640×472 | (32, 24) | iso 3 NE con cassa (v2) |

## Disposizione a bordo (dalla RICHIESTA) e verifica
Coordinate in tessere (u = verso prua, v = a destra guardando la prua): albero (1,04 ; −0,10) · tenda (−0,76 ; +0,18), ingresso verso prua · cassa (0 ; +0,41) · tanica rossa (−0,78 ; −0,80) · tanica verde (−0,50 ; −0,85).

Verifica in `scheda_lotto_a.png` (4 viste sul mare vero, con parallelogramma dell'impronta centrata a (352,336) e punti-base attesi degli oggetti in giallo):
- **Albero, tenda e cassa seguono la rotazione rigida in tutte e 4 le viste**: albero sempre all'estremità di prua, tenda sempre a poppa con ingresso verso prua, cassa sempre presso il centro; scostamenti dei punti-base dai marcatori entro la tolleranza artistica del disegno (~0,2–0,5 tessere; il disegno non è una proiezione meccanica, come già dichiarato per l'iso 3).
- **Limite dichiarato — taniche**: nelle viste 00 e 08 le due taniche stanno ai punti della guida (lato lontano, metà di poppa; ordine rossa/verde corretto in entrambe). Nelle viste **04 e 12** invece le taniche sono più centrali (04: accanto alla cassa; 12: a metà ponte verso prua): è la disposizione dei disegni approvati iso 3, non quella esatta della guida. Se serve la posizione esatta anche in 04/12, quelle due viste vanno ridisegnate.
- Luce fissa da in alto a sinistra dello schermo in tutte le viste (non ruota con la zattera); niente contorno scuro, niente ombre proiettate.

## Controlli fatti
- Ritaglio/despill metodo v3: **residuo magenta 0 e tinta magenta forte 0 su tutte e 4 le viste** (misurati sui file finali).
- Scheda sul mare vero (mare Gruppo 1 v4 + overlay onde) controllata a vista: scafo dentro l'impronta sui lati sud; sul lato nord il disegno sporge di qualche decina di px oltre il parallelogramma (disegno artistico, fa fede l'impronta dichiarata).
- Master a piena risoluzione: i master ripuliti sono in `lavoro-gruppo4a/gen_zattera16/` (`zattera_iso_00/04/08/12_master.png`, da 1711×1082 a 1819×1140 e 1753×1293).

## Cosa manca
- **Lotto B**: viste 02, 06, 10, 14.
- **Lotto C**: viste dispari 01, 03, 05, 07, 09, 11, 13, 15.
- **Palo v2** (citato nella RICHIESTA): non fa parte di questo lotto.

STATO: pronto (lotto A)
