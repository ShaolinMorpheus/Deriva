# Zattera in 16 viste — LOTTI A+B+C (Deriva)

Zattera che ruota fluida a 360° (una vista ogni 22,5°) per il nuovo sistema di montaggio. Questa consegna contiene **il lotto A (viste diagonali 00, 04, 08, 12), il lotto B (viste cardinali 02, 06, 10, 14) e il lotto C (viste dispari 01, 03, 05, 07, 09, 11, 13, 15)**: le 16 viste sono complete e la rotazione è montabile a 16 passi. **Sostituisce la zattera del Gruppo iso 3** (le viste singole `zattera_iso_ne/se/so/no.png` restano come storico). Il testo integrale della richiesta è in `RICHIESTA.md` in questa cartella.

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

## Lotto C — viste dispari 01, 03, 05, 07, 09, 11, 13, 15
**Metodo**: stesso del FIX lotto B — generazioni guidate (pannello del foglio guida + viste vicine approvate), selezione per misura dell'angolo di prua (tenda→albero, punti da visual grounding sul grezzo 1760×1280, correzione d'aspetto applicata), montaggio con ritaglio v3, scala uniforme da compromesso d'area (area assito → 98304 px², con tetto di fit per stare in tela), centro assito a (352, 306), centro impronta (352, 336) per costruzione. **Nominali prua** (angolo schermo dell'asse U, formula di `mount_view.py`: 01: 50,4° · 03: 129,6° · 05: 168,3° · 07: 191,7° · 09: 230,4° · 11: 309,6° · 13: 348,3° · 15: 11,7°); i nominali sono stati verificati contro i marcatori M del foglio guida (accordo entro ~1° sui pannelli 01/09, tolto il sollevamento di 30 px del livello assito). Residuo magenta e tinta forte **0 su tutte le 8 viste**. Master a piena risoluzione in `lavoro-gruppo4a/gen_zattera16/` (`zattera_iso_<vista>_master.png`, 1446×1057 – 1634×952); script `lavoro-gruppo4a/build_zattera16_lotto_c.py`, scheda `scheda_lotto_c.png` (8 viste sul mare vero con parallelogramma impronta e punti-base + striscia con la sequenza completa 00→15).

**Difficoltà del lotto**: il generatore tende a incollarsi alle 4 diagonali approvate (iso 3): le generazioni fresche atterrano quasi sempre sugli angoli 00/04/08/12 (01 a ~31° invece di 50,4°; 03 a ~149° invece di 129,6°; 09 a ~200° invece di 230,4°; 11/13 a ~325° invece di 309,6°/348,3°), e le correzioni per ripresa saltano spesso all'attrattore successivo (01 a 87° = vista 02; 09 a 268° = vista 10). Servono molti tentativi e solo le rotazioni piccole richieste per ripresa (8–11°) spostano l'angolo di poco per volta. **4 viste su 8 restano fuori dal criterio ±11°** dopo 5–7 tentativi ciascuna: sono consegnate come migliori disponibili, con lo scarto dichiarato (come previsto dalla richiesta).

| Vista | Prua misurata (tenda→albero) | Nominale U | Scarto | Tentativi | Sorgente scelta |
|---|---|---|---|---|---|
| `zattera_iso_01.png` | 46,1° (centro→albero 45,3°) | 50,4° | −4,2° ✓ | 5 | lottoc5 (ripresa da gen1, +10° richiesti) |
| `zattera_iso_03.png` | 145,3° (centro→albero 147,3°) | 129,6° | **+15,6°** | 6 | lottoc3 (ripresa da gen1, −20° richiesti) |
| `zattera_iso_05.png` | 157,9° (centro→albero 156,7°) | 168,3° | −10,4° ✓ | 3 | lottoc2 (generazione fresca, prompt rafforzato) |
| `zattera_iso_07.png` | 198,4° (centro→albero 205,2°) | 191,7° | +6,7° ✓ | 1 | gen1 |
| `zattera_iso_09.png` | 199,5° (centro→albero 205,5°) | 230,4° | **−30,8°** | 7 | gen1 |
| `zattera_iso_11.png` | 324,6° (centro→albero 329,5°) | 309,6° | **+15,0°** | 6 | gen1 |
| `zattera_iso_13.png` | 328,7° (centro→albero 331,8°) | 348,3° | **−19,6°** | 5 | lottoc2 (generazione fresca, prompt rafforzato) |
| `zattera_iso_15.png` | 9,1° (centro→albero 19,9°) | 11,7° | −2,6° ✓ | 3 | lottoc3 (ripresa da gen1, −13° richiesti) |

Verifica in `scheda_lotto_c.png` (8 viste sul mare vero con parallelogramma impronta e punti-base attesi in giallo + striscia con la sequenza completa 00→15 per giudicare il flusso di rotazione). Posizioni oggetti misurate sui finali (u,v) vs guida M (1,04; −0,10) · T (−0,76; +0,18) · C (0; +0,41) · R (−0,78; −0,80) · V (−0,50; −0,85):
- **01**: M (+1,19; −0,08) ✓, T (−0,88; +0,03), C (+0,12; +0,42) ✓, R (−0,83; −0,47), V (−0,64; −0,55) — taniche ~0,3 in v dalla guida.
- **03**: M (+1,16; +0,32), T (−0,87; −0,16), C (−0,07; +0,45) ✓, R (−0,27; −0,15), V (+0,25; −0,15) — taniche lontane dalla guida (~0,8 tessere, al centro ponte invece che a poppa).
- **05**: M (+1,19; −0,39), T (−0,69; +0,17) ✓, C (+0,36; +0,55), R (−0,34; −0,34), V (−0,62; −0,32) — taniche ~0,5 dalla guida.
- **07**: M (+1,10; +0,42), T (−0,73; +0,06), C (+0,13; +0,86), R (−0,21; −0,41), V (+0,01; −0,47) — cassa e taniche spostate ~0,4–0,5 verso il centro.
- **09**: M (+1,04; −0,46), T (−0,50; +0,51), C (+0,70; +0,51), R (−0,40; −0,13), V (−0,29; −0,33) — tenda e cassa ~0,5–0,7 verso prua/centro, taniche ~0,6 dalla guida.
- **11**: M (+1,03; +0,33), T (−0,91; −0,10), C (−0,99; +0,21), R (+0,03; +0,50), V (−0,10; +0,31) — cassa ~1,0 tessere verso poppa (vicina alla tenda), taniche ~1,3–1,5 dalla guida (al centro ponte).
- **13**: M (+0,99; −0,45), T (−0,70; +0,45), C (−0,56; +0,87), R (+0,33; +0,35), V (+0,10; +0,31) — cassa ~0,7 verso poppa, taniche ~1,1–1,2 dalla guida.
- **15**: M (+1,14; +0,27), T (−0,53; +0,41), C (+0,10; +0,50) ✓, R (−0,57; −0,83) ✓, V (−0,37; −0,89) ✓ — la più vicina alla guida in tutte le posizioni.

Limiti dichiarati del lotto C:
- **Prua fuori criterio in 03 (+15,6°), 09 (−30,8°), 11 (+15,0°), 13 (−19,6°)**: nella sequenza 00→15 la rotazione rallenta visibilmente in 08→09 (la 09 è quasi ferma sull'angolo della 08, poi salto alla 10) e in 12→13 (la 13 è quasi ferma sull'angolo della 12, poi salto alla 14); 02→03→04 e 10→11→12 scorrono più lenti del passo nominale. Le 4 viste in criterio (01, 05, 07, 15) scorrono regolari.
- **Taniche le meno precise** (come già nel lotto B, ma qui di più): in 03/11/13 stanno al centro ponte invece che al bordo di poppa (scarti fino a ~1,5 tessere in 11); in 09/05/07 ~0,5–0,6. Ordine rosso/verde sempre corretto (rossa sempre verso poppa rispetto alla verde, come da guida).
- **Cassa spostata verso poppa** in 11 (−0,99 in u, vicina alla tenda) e in 13 (−0,56 in u); in 09 spostata verso prua (+0,70 in u).
- **Scale di montaggio** limitate dall'altezza in tela (albero alto + assito): s 0,341–0,447, quindi le dispari risultano un poco più piccole delle pari in tela (assito ~73–93% dell'area impronta); bbox forte con centro x 344,5–356 e y max 504–507.
- **Scarti**: 09-lottoc4 (generazione con solo pannello guida, senza viste vicine) aveva un altro disegno — albero a croce con vela orizzontale, barili di legno, tenda diversa con tiranti — e le sue riprese c5/c6: scartate, non usate. 05-gen1 aveva un telone blu sotto la tenda e un tappeto marrone sul ponte: scartata, sostituita dalla c2 pulita. Il resume di 13-lottoc2 per un 5° tentativo ha dato `invalid_resume_id` (non ripetuto).

## Disposizione a bordo (dalla RICHIESTA)
Coordinate in tessere (u = verso prua, v = a destra guardando la prua): albero (1,04 ; −0,10) · tenda (−0,76 ; +0,18), ingresso verso prua · cassa (0 ; +0,41) · tanica rossa (−0,78 ; −0,80) · tanica verde (−0,50 ; −0,85). Nel lotto A le posizioni sono quelle dei disegni approvati iso 3; nel lotto B sono state chieste ai punti esatti della guida in generazione e le deviazioni residue sono quelle misurate sopra (il generatore non piazza gli oggetti con precisione sub-tessera: deviazioni tipiche 0,2–0,6 tessere, taniche le meno precise).

## Nota di caricamento
- `scheda_lotto_c.png` è caricata in 2 parti `scheda_lotto_c.png.b64.1` + `scheda_lotto_c.png.b64.2` (limite di dimensione del singolo invio): concatenare in ordine e decodificare per ricostruire il PNG originale.

## Cosa manca
- **Palo v2** (citato nella RICHIESTA): non fa parte di questi lotti.

STATO: pronto (16 viste)
