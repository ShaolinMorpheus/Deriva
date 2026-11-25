# Richiesta a Muse — zattera in 16 viste (rotazione fluida a 360°)

**Perché.** Con 4 sole viste la zattera, girando, "salta" da una vista all'altra. Serve una vista ogni 22,5° (16 viste) per farla ruotare fluida. Questa richiesta **sostituisce la zattera v2** già chiesta: le 4 diagonali sono le viste 00, 04, 08, 12.

**Cosa consegnare.** 16 PNG `zattera_iso_00.png … zattera_iso_15.png` (più i master a piena risoluzione, e se riesci anche al doppio: 1408×1024). Sono sempre **la stessa zattera che gira su sé stessa**, come su una piattaforma girevole.

**Tela e ancoraggio (uguali per tutte).** 704×512 px, sfondo trasparente, **centro dell'impronta** (centro del rettangolo 3×2 sul pelo dell'acqua) sempre al pixel **(352, 336)**. Non ritagliare le viste e non cambiare la tela: così il motore le monta senza ancoraggi diversi per vista.

**Vista k** = prua (il lato dell'albero) a k·22,5°, in senso orario sullo schermo:
00 basso-destra · 01 giù un po' a destra · 02 giù · 03 giù un po' a sinistra · 04 basso-sinistra · 05 sinistra un po' in basso · 06 sinistra · 07 sinistra un po' in alto · 08 alto-sinistra · 09 su un po' a sinistra · 10 su · 11 su un po' a destra · 12 alto-destra · 13 destra un po' in alto · 14 destra · 15 destra un po' in basso.

**Disposizione fissa a bordo** (in tessere; u = verso la prua, v = a destra guardando la prua; origine al centro; piano dell'assito ~30 px sopra l'acqua):
- albero con vela avvolta: (1,04 ; −0,10), alto ~180 px
- tenda: (−0,76 ; +0,18), ~1,1×0,9 tessere, alta ~140 px, ingresso verso prua
- cassa: (0 ; +0,41), ~0,45×0,45, alta ~75 px
- tanica rossa: (−0,78 ; −0,80) e tanica verde: (−0,50 ; −0,85), alte ~70 px (a sinistra guardando la prua)
Gli oggetti stanno **sempre agli stessi punti della zattera**: se ruotando le viste in sequenza (animazione) qualcosa salta, va rifatta.

**Geometria.** Proiezione isometrica 2:1 come tutto il resto; impronta rettangolare 3×2 tessere (passo di griglia 128×64 px) con barili sul bordo e assito dentro; stesse dimensioni in tutte le viste. Il file `guide/guide_zattera_16_foglio.png` (4×4) mostra per ogni vista il rettangolo-impronta, l'asse della prua e le basi degli oggetti: **disegna dentro quelle impronte** (le guide singole sono `guida_zattera_00..15.png`, 704×512, stesso centro).

**Luce e stile.** La luce arriva **sempre da in alto a sinistra dello schermo** e non gira con la zattera: girando, chiari e scuri sui barili e sull'assito cambiano di conseguenza. Nessun contorno scuro, nessun alone (magenta 0), stesso stile e materiali delle altre viste (barili blu e ruggine con corda, assi con muschio, tenda rattoppata).

**Ordine di consegna** (ogni lotto si monta da solo: 4 → 8 → 16 viste):
- lotto A: 00, 04, 08, 12
- lotto B: 02, 06, 10, 14
- lotto C: 01, 03, 05, 07, 09, 11, 13, 15
Se non riesci a tenere la coerenza a 16, dichiaralo e consegna le 8 (lotti A+B).

Cartella di consegna: `muse/<data>-zattera-16-viste/`, con LEGGIMI.md ed `elenco.txt` come al solito.
