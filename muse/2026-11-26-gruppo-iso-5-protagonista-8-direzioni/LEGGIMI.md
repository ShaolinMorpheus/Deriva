# Gruppo iso 5 — protagonista in 8 direzioni: le 4 cardinali N, E, S, O (Deriva)

Le **4 direzioni cardinali** del protagonista (stesso personaggio dei Gruppi iso 3 e 4: berretto rosso sbiadito, giubbotto di salvataggio arancione con cinghie e fibbie, camicia strappata grigio-verde, pantaloni cargo marroni, stivali scuri): per ciascuna direzione **1 fermo + 6 fotogrammi di camminata = 28 sprite**. Alla stessa scala dei gruppi precedenti (passo griglia 128×64, **PNG 1:1 in gioco, non vanno ridimensionati**). Niente ombre proiettate, niente contorno scuro, niente scritte.

**Il set completo a 8 direzioni si ottiene unendo tre consegne**: Gruppo iso 3 (fermo delle 4 diagonali NE/SE/SO/NO) + Gruppo iso 4 (camminata delle 4 diagonali) + questo Gruppo iso 5 (fermo e camminata delle 4 cardinali N/E/S/O). Convenzione direzioni: S = fronte verso il basso-schermo (volto visibile), N = di spalle verso l'alto-schermo, E = di profilo verso destra, O = di profilo verso sinistra.

## Tela, ancoraggio e scala (uguali per tutti i 28 sprite)
- **Tela unica 70×108 px** per tutti gli sprite di questa consegna, fermo compreso — la stessa tela della camminata del Gruppo iso 4.
- **Ancoraggio ai piedi, centro-basso: (35, 104)** in ogni file — lo stesso punto-piedi del fermo del Gruppo iso 3 e della camminata del Gruppo iso 4: il gioco piazza fermo e camminata di tutte e 8 le direzioni con la stessa regola, P − ancoraggio, e il personaggio non salta passando da fermo a camminata, tra un fotogramma e l'altro e girando direzione.
- **Altezza sprite esattamente 100 px piedi-testa in OGNI sprite** (misurata sul bbox alfa di ciascuno dei 28 file: min 100, max 100). I piedi stanno sulla stessa riga di base (y = 104) in ogni sprite; l'asse verticale del corpo (centroide del busto) è allineato sulla x di ancoraggio, così il busto non oscilla lateralmente: si muovono solo gambe e braccia.
- Nota: il fermo delle diagonali del Gruppo iso 3 sta in tele proprie (W×100, ancoraggio (W/2, 100)); qui il fermo delle cardinali è già sulla tela uniforme 70×108 con ancoraggio (35, 104). Il punto-piedi a terra è lo stesso: cambia solo la tela intorno.

## Come si usa
- Camminata: ordine `passo1 → passo2 → … → passo6 → passo1 …` (ciclo chiuso: il passo6 si raccorda col passo1). Ciclo vero: passi alternati delle gambe, braccia in controfase, lieve rimbalzo assorbito nella normalizzazione dell'altezza.
- Direzioni: S di fronte vera (volto visibile in tutti i fotogrammi — a differenza della camminata frontale SE/SO del Gruppo iso 4, uscita quasi di profilo e lì dichiarata), N di spalle vera (mai il volto), E e O di profilo per natura.
- Velocità suggerita: 120 ms per fotogramma (è il ritmo delle GIF di anteprima), come nel Gruppo iso 4.

## I file (PNG trasparenti 70×108, ancoraggio (35, 104) per tutti)
| File | Direzione | Note |
|---|---|---|
| `protagonista_iso_s.png` + `protagonista_iso_s_passo1..6.png` | S | Fermo + camminata verso sud (basso-schermo), di fronte |
| `protagonista_iso_n.png` + `protagonista_iso_n_passo1..6.png` | N | Fermo + camminata verso nord (alto-schermo), di spalle |
| `protagonista_iso_e.png` + `protagonista_iso_e_passo1..6.png` | E | Fermo + camminata verso est (destra), di profilo |
| `protagonista_iso_o.png` + `protagonista_iso_o_passo1..6.png` | O | Fermo + camminata verso ovest (sinistra), di profilo |
| `scheda_protagonista_iso5.png` | — | Anteprima di verifica: 4 strisce sul mare vero, per ogni direzione il fermo + i 6 passi ingranditi ×3 |
| `camminata_iso_s.gif`, `camminata_iso_n.gif`, `camminata_iso_e.gif`, `camminata_iso_o.gif` | — | Anteprime animate del ciclo sul mare (×2, 120 ms/fotogramma, loop). Nota: nell'app di Davide le GIF possono restare ferme — la verifica vera è la scheda e i fotogrammi singoli |

## Controlli fatti
- Generazione: un foglio unico da 6 pose per direzione, partendo dal grezzo del fermo della stessa direzione; il fermo è ritagliato dallo stesso grezzo. I grezzi cardinali sono quelli già generati ai tempi del Gruppo iso 3 (fronte, spalle, profilo destro, profilo sinistro — allora usati solo come tentativi per la zattera, mai consegnati per il protagonista): design e colori sono quindi gli stessi del personaggio approvato.
- Ritaglio dal fondo magenta con l'algoritmo v3 (despill per tonalità + riempimento RGB delle zone trasparenti dal vicino opaco): **residuo magenta 0 e tinta magenta forte 0 su tutti i 28 sprite** (stesse due metriche dei Gruppi iso 2 v2, iso 3 e iso 4), riverificati in modo indipendente sui file finali.
- Verifica numerica: altezza sprite 100 px esatti in 28/28 sprite; base dei piedi a y = 104 in 28/28; nessun fotogramma esce dalla tela 70×108.
- Verifica a vista sulla scheda (mare vero, ingrandimento ×3): lo stesso personaggio in tutti i 28 sprite — stesse proporzioni, stessi colori, berretto e giubbotto identici; S frontale vera col volto in ogni fotogramma, N di spalle vera, E/O di profilo con falcata leggibile; bordi puliti, niente alone, niente ombre.
- Master a piena risoluzione: i fotogrammi ritagliati prima della scalatura a 100 px sono in `lavoro-gruppo4a/gen_iso5/` come `protagonista_iso_<dir>_passo<N>_master.png` (camminata) e `protagonista_iso_<dir>_master.png` (fermo), accanto ai 4 fogli di generazione e ai grezzi del fermo (`ref_fermo_<dir>.webp`, copie dei grezzi di gen_iso3).

## Cosa NON deve cambiare
- Design del protagonista (berretto rosso, giubbotto arancione), scala (100 px), tela e ancoraggio: gli stati futuri (remata, attrezzi) devono mantenere design, scala e punto-piedi di fermo e camminata in tutte e 8 le direzioni.

## Cosa manca / prossime consegne
- Variante zattera con motore fuoribordo in isometrico (nel Gruppo 2 esiste dall'alto).
- Eventuale camminata frontale SE/SO più «tre quarti», solo se Davide boccia l'angolo quasi-profilo dichiarato nel Gruppo iso 4.

STATO: pronto
