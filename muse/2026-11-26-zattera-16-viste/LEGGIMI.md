# Zattera in 16 viste — LOTTI A+B (Deriva)

Zattera che ruota fluida a 360° (una vista ogni 22,5°) per il nuovo sistema di montaggio. Questa consegna contiene **il lotto A (viste diagonali 00, 04, 08, 12) e il lotto B (viste cardinali 02, 06, 10, 14)**: con le 8 viste pari la rotazione è già montabile. **Sostituisce la zattera del Gruppo iso 3** (le viste singole `zattera_iso_ne/se/so/no.png` restano come storico). Il testo integrale della richiesta è in `RICHIESTA.md` in questa cartella.

## Tela e centro impronta (tutte le viste)
- Tela **704×512** per tutte le viste, sfondo trasparente, nessun ritaglio.
- **Centro dell'impronta (centro del rettangolo 3×2 sul pelo dell'acqua) al pixel (352, 336) in ogni vista**, per costruzione.
- Ritaglio/despill metodo v3 su tutti i file: **residuo magenta 0 e tinta magenta forte 0** (misurati sui file finali). Luce fissa da in alto a sinistra dello schermo in tutte le viste (non ruota con la zattera); niente contorno scuro, niente ombre proiettate.
- Master a piena risoluzione in `lavoro-gruppo4a/gen_zattera16/` (`zattera_iso_<vista>_master.png`).

## Lotto A — viste diagonali 00, 04, 08, 12
Le 4 diagonali coincidono con le direzioni già approvate del Gruppo iso 3: i disegni sono gli stessi master approvati (stessa zattera, set coerente: ponte di assi, barili blu/ruggine legati sul bordo, albero con vela avvolta a prua, tenda rattoppata a poppa con ingresso verso prua, cassa, taniche rossa e verde), ripuliti e rimontati sulla tela fissa:
- rimossi speck alfa residui ai bordi (nella SE due pixel spuri allungavano la tela di ~80 righe a piena risoluzione);
- despill per tonalità applicato anche al master NE-con-cassa (era un edit ritagliato a parte: 339 px con tinta magenta forte → 0);
- contenuto riscalato a larghezza esatta 640 px (impronta 3×2, passo 128×64) e montato **senza ritaglio** sulla tela 704×512.
- Misura sui file finali: centro x del bbox forte = 351,5 in tutte le viste; vertice sud dell'impronta sulla riga 495 (bordo inferiore a y=496) in tutte le viste.

| Vista | Prua | Contenuto px | Offset di montaggio | Master sorgente |
|---|---|---|---|---|
| `zattera_iso_00.png` | SE (basso-destra) | 640×405 | (32, 91) | iso 3 SE |
| `zattera_iso_04.png` | SO (basso-sinistra) | 640×401 | (32, 95) | iso 3 SO |
| `zattera_iso_08.png` | NO (alto-sinistra) | 640×461 | (32, 35) | iso 3 NO |
| `zattera_iso_12.png` | NE (alto-destra) | 640×472 | (32, 24) | iso 3 NE con cassa (v2) |

Verifica in `scheda_lotto_a.png` (viste sul mare vero, parallelogramma dell'impronta e punti-base attesi in giallo):
- **Albero, tenda e cassa seguono la rotazione rigida in tutte e 4 le viste**; scostamenti entro la tolleranza artistica del disegno (~0,2–0,5 tessere; il disegno non è una proiezione meccanica, come già dichiarato per l'iso 3).
- **Limite dichiarato — taniche**: nelle viste 00 e 08 le due taniche stanno ai punti della guida; nelle viste **04 e 12** sono più centrali (04: accanto alla cassa; 12: a metà ponte verso prua): è la disposizione dei disegni approvati iso 3, non quella esatta della guida.

## Lotto B — viste cardinali 02, 06, 10, 14
**RIFACIMENTO (26 nov): questa sezione sostituisce la prima versione del lotto B** (montaggio a «scala da compromesso d'area», 9 generazioni: ponti a rombo con prua a ~53° nella 02 e ~229° nella 10 invece che cardinali, taniche con ordine rosso/verde invertito nella 06). Le 4 viste qui consegnate sono rifatte con **ponti rettangolari piatti esatti** (362×272 per 02/10, 544×182 per 06/14) e **albero verticale in tutte le viste**; i file della prima versione sono stati sostituiti (i grezzi restano in `lavoro-gruppo4a/gen_zattera16/` con suffisso `lottob`/`fix`).

**FIX 02/10 (26 nov, successivo al rifacimento): le viste 02 e 10 sono state sostituite un'altra volta** con versioni a generazione guidata (pannelli del foglio guida + viste vicine approvate, selezione per misura dell'angolo di prua): i file attuali di 02/10 sono quelli del fix (prua misurata 90,6° e 259,8°; montaggio con il metodo del lotto B originale — ritaglio v3, scala uniforme da compromesso d'area/fit, centro assito a (352, 306), centro impronta (352, 336) per costruzione; master in `gen_zattera16/zattera_iso_02_master.png` 1361×1113 e `zattera_iso_10_master.png` 854×1237; residuo magenta e tinta forte 0). Le righe 06/14, il montaggio `mount_view.py` e i trapianti d'albero descritti sotto restano del rifacimento (i compositi 02/10 del rifacimento sono superati dal fix). Verifica aggiornata in `scheda_lotto_b_v2.png`.

Disegnate da zero (stesso design, materiali e colori del lotto A), perché le cardinali non esistono nel set iso 3. Generazioni totali per il rifacimento: 7 (02 ×2, 06 ×1, 10 ×1, 14 ×3). Scartate: 02-gen1 (ponte piatto giusto ma albero steso in diagonale sul ponte), 14-gen1 (ponte a parallelogramma diagonale), 14-gen2 (ponte e albero giusti ma tenda piatta come un telo steso, non in piedi).

Montaggio (`mount_view.py`): ritaglio v3, rettangolo impronta trovato per conteggio di pixel opachi per riga (soglia 40% in alto, 20% in basso; la campata min-max non è robusta: albero e corde della tenda la fanno scattare troppo in alto e il ponte si schiaccia), riscalamento anisotropo al rettangolo guida esatto e centro impronta a (352, 336). **Albero verticale in tutte le viste**: dove il generatore lo ha disegnato steso o inclinato (02, 10), è stato cancellato a programma e sostituito con lo sprite verticale ritagliato dalla 02-gen2 (`albero_verticale_master.png`, 56×180 px, script `composite_mast.py` / `composite_02.py`).

| Vista | Prua | Metodo | Centro impronta misurato | Scarto da (352, 336) |
|---|---|---|---|---|
| `zattera_iso_02.png` | S (giù) | FIX: generazione guidata (pannello 02 + viste 00/04), 6 tentativi, montaggio scala uniforme, centro assito (352, 306) | (352, 336) per costruzione | (0, 0) |
| `zattera_iso_06.png` | O (sinistra) | generazione diretta gen1, albero verticale disegnato | (348, 338) | (−4, +2) |
| `zattera_iso_10.png` | N (su) | FIX: generazione guidata (pannello 10 + viste 08/12), 5 tentativi, montaggio scala uniforme, centro assito (352, 306) | (352, 336) per costruzione | (0, 0) |
| `zattera_iso_14.png` | E (destra) | generazione diretta gen3, albero verticale disegnato | (357, 341) | (+5, +5) |

Verifica in `scheda_lotto_b.png` (4 viste sul mare vero con rettangolo impronta e punti-base attesi in giallo + striscia con la sequenza completa 00→14 per giudicare il flusso di rotazione); per le viste 02/10 del fix la verifica aggiornata è in `scheda_lotto_b_v2.png` (stesso formato). Deviazioni degli oggetti dai punti guida (misurate a vista sui controlli, tolleranza artistica ~0,2–0,5 tessere come nel lotto A):
- **02 (fix)**: prua tenda→albero **90,6°** (nominale 90°), asse centro impronta→albero 90,0°; albero (+1,24 ; 0,00), tenda (−0,68 ; −0,01) quasi esatta, taniche R (−1,04 ; −0,62) e V (−0,46 ; −0,72) entro ~0,27 dalla guida con ordine rosso/verde corretto; cassa (−0,59 ; +0,68).
- **06**: albero verticale alla base M ✓; tenda ~0,4 tessere a sinistra del punto T, cassa ~0,3–0,5 a sinistra del punto C; taniche vicine ai punti R/V (basi a ~20 px dai marcatori).
- **10 (fix)**: prua tenda→albero **259,8°** (nominale 270°, scarto −10,2°, dentro il criterio ±11°), asse centro impronta→albero 268,5° (scarto −1,5°); albero (+1,31 ; −0,02), tenda (−1,17 ; +0,21), cassa (+0,38 ; +0,24), taniche R (−0,80 ; −0,44) e V (−0,53 ; −0,53) quasi esatte in u e a ~0,35 dalla guida in v, ordine verde sopra rossa corretto.
- **14**: albero verticale alla base M ✓; tenda in piedi al punto T ✓; cassa al punto C ✓; taniche ~0,19 tessere a destra e ~0,28 sotto i punti R/V.

Limiti dichiarati del rifacimento:
- **02 (fix)**: cassa ~0,6 tessere verso poppa rispetto alla guida; scala di montaggio limitata dall'altezza in tela (assito ~92% dell'area impronta). Disegno unico generato (albero disegnato verticale, non trapiantato): niente cuciture.
- **10 (fix)**: vista più stretta delle altre (montaggio limitato dall'altezza dell'albero in tela: assito ~73% dell'area impronta); tenda e cassa ~0,4 tessere oltre i punti guida in u; angolo di prua al margine del criterio nella misura tenda→albero (−10,2° su ±11°; −1,5° nella misura centro→albero).
- **06**: tenda e cassa spostate a sinistra di ~0,3–0,5 tessere rispetto alla guida.
- **14**: taniche ~0,28 tessere sotto i punti guida.
- I ponti sono rettangoli piatti, ma resta una leggera inclinazione prospettica del disegno generato (il bordo superiore del ponte è un poco storto in 06 e 14).

## Disposizione a bordo (dalla RICHIESTA)
Coordinate in tessere (u = verso prua, v = a destra guardando la prua): albero (1,04 ; −0,10) · tenda (−0,76 ; +0,18), ingresso verso prua · cassa (0 ; +0,41) · tanica rossa (−0,78 ; −0,80) · tanica verde (−0,50 ; −0,85). Nel lotto A le posizioni sono quelle dei disegni approvati iso 3; nel lotto B sono state chieste ai punti esatti della guida in generazione e le deviazioni residue sono quelle misurate sopra (il generatore non piazza gli oggetti con precisione sub-tessera: deviazioni tipiche 0,2–0,6 tessere, taniche le meno precise).

## Cosa manca
- **Lotto C**: viste dispari 01, 03, 05, 07, 09, 11, 13, 15.
- **Palo v2** (citato nella RICHIESTA): non fa parte di questi lotti.

STATO: pronto (lotti A+B)
