# Gruppo iso 4 — camminata del protagonista in isometrico (Deriva)

Camminata del protagonista del Gruppo iso 3 (stesso personaggio: berretto rosso sbiadito, giubbotto di salvataggio arancione con cinghie e fibbie, camicia strappata grigio-verde, pantaloni cargo marroni, stivali scuri, barba corta): **6 fotogrammi per direzione × 4 direzioni diagonali (NE, SE, SO, NO) = 24 sprite**, alla stessa scala del fermo (passo griglia 128×64, **PNG 1:1 in gioco, non vanno ridimensionati**). Niente ombre proiettate, niente contorno scuro, niente scritte.

## Tela, ancoraggio e scala (uguali per tutti i 24 fotogrammi)
- **Tela unica 70×108 px** per tutti i fotogrammi di tutte le direzioni.
- **Ancoraggio ai piedi, centro-basso: (35, 104)** in ogni file — lo stesso punto-piedi del fermo del Gruppo iso 3 (lì dichiarato (W/2, 100) nella sua tela): il gioco piazza fermo e camminata con la stessa regola, P − ancoraggio, e il personaggio non salta passando da fermo a camminata e tra un fotogramma e l'altro.
- **Altezza sprite esattamente 100 px piedi-testa in OGNI fotogramma** (misurata sul bbox alfa di ciascuno dei 24 file: min 100, max 100). I piedi stanno sulla stessa riga di base (y = 104) in ogni fotogramma; l'asse verticale del corpo (centroide del busto) è allineato sulla x di ancoraggio, così il busto non oscilla lateralmente: si muovono solo gambe e braccia.

## Come si usa
- Ordine: `passo1 → passo2 → … → passo6 → passo1 …` (ciclo chiuso: il passo6 si raccorda col passo1). Ciclo vero: passi alternati delle gambe, braccia in controfase, lieve rimbalzo assorbito nella normalizzazione dell'altezza.
- Direzioni: SE e SO di fronte (volto visibile), NE e NO di spalle — come il fermo del Gruppo iso 3.
- Velocità suggerita: 120 ms per fotogramma (è il ritmo delle GIF di anteprima).

## I file (PNG trasparenti 70×108, ancoraggio (35, 104) per tutti)
| File | Direzione | Note |
|---|---|---|
| `protagonista_iso_se_passo1..6.png` | SE | Cammina verso sud-est |
| `protagonista_iso_so_passo1..6.png` | SO | Cammina verso sud-ovest |
| `protagonista_iso_ne_passo1..6.png` | NE | Cammina verso nord-est, di spalle |
| `protagonista_iso_no_passo1..6.png` | NO | Cammina verso nord-ovest, di spalle |
| `scheda_camminata_iso4.png` | — | Anteprima di verifica: 4 strisce sul mare vero, per ogni direzione il fermo del Gruppo iso 3 + i 6 passi ingranditi ×3 |
| `camminata_iso_se.gif`, `camminata_iso_so.gif`, `camminata_iso_ne.gif`, `camminata_iso_no.gif` | — | Anteprime animate del ciclo sul mare (×2, 120 ms/fotogramma, loop). Nota: nell'app di Davide le GIF possono restare ferme — la verifica vera è la scheda e i fotogrammi singoli |

## Controlli fatti
- Generazione: un foglio unico da 6 pose per direzione, partendo dal grezzo del fermo della stessa direzione (stesso design e stessi colori); separazione dei fotogrammi a programma per componente connessa.
- Ritaglio dal fondo magenta con l'algoritmo v3 (despill per tonalità + riempimento RGB delle zone trasparenti dal vicino opaco): **residuo magenta 0 e tinta magenta forte 0 su tutti i 24 fotogrammi** (stesse due metriche dei Gruppi iso 2 v2 e iso 3).
- Verifica numerica: altezza sprite 100 px esatti in 24/24 fotogrammi; base dei piedi a y = 104 in 24/24; nessun fotogramma esce dalla tela.
- Verifica a vista sulla scheda (mare vero, ingrandimento ×3): lo stesso personaggio in tutti i 24 fotogrammi — stesse proporzioni, stessi colori, berretto e giubbotto identici; bordi puliti, niente alone, niente ombre.
- Master a piena risoluzione: i fotogrammi ritagliati prima della scalatura a 100 px sono in `lavoro-gruppo4a/gen_iso4/` come `protagonista_iso_<dir>_passo<N>_master.png` (~450×800), accanto ai 4 fogli di generazione.

## Caratteristica dichiarata
- Nelle direzioni frontali (SE e SO) i fogli generati rendono la camminata quasi di profilo (si vede bene nella scheda, a confronto col fermo tre quarti del Gruppo iso 3); NE e NO invece combaciano col fermo di spalle tre quarti. Personaggio, proporzioni e colori sono gli stessi in tutti i fotogrammi: è una differenza di angolo di ripresa della camminata frontale, dichiarata qui perché la valuti Davide.

## Cosa NON deve cambiare
- Design del protagonista (berretto rosso, giubbotto arancione), scala (100 px), tela e ancoraggio: gli stati futuri (remata, attrezzi) devono mantenere design, scala e punto-piedi di fermo e camminata.

## Cosa manca / prossime consegne
- Variante zattera con motore fuoribordo in isometrico (nel Gruppo 2 esiste dall'alto).
- Eventuale camminata frontale SE/SO più «tre quarti», solo se Davide boccia l'angolo quasi-profilo dichiarato sopra.

STATO: pronto
