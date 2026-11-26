# Zattera parametrica — set completo (32 viste + dondolo)

## Metodo (decisione utente 26 nov 2026)
Per la rotazione a 360° si usa il metodo parametrico: «quello che si vede
meglio a 360 gradi senza oggetti che si spostano ruotando». La zattera è
**un unico modello 3D a coordinate fisse** (quelle della guida), ruotato
per formula in proiezione isometrica 2:1 vera. Gli oggetti di bordo non
vengono mai ridisegnati: sono gli stessi solidi proiettati, quindi non
possono saltare tra una vista e l'altra, per costruzione.
Renderer: `lavoro-gruppo4a/build_zattera_param2.py` (Python/PIL, disegno
diretto su trasparente, niente fondo magenta e niente alone; rendering a
3× e riduzione per i bordi morbidi, nessun contorno scuro marcato).

## Contenuto
- **32 viste**: `zattera_iso_00.png` … `_15.png` (passo 22,5°) +
  `zattera_iso_00b.png` … `_15b.png` (intermedie a +11,25°). Stesse
  convenzioni di nome del set generato, stessa tela 704×512, centro
  impronta (352, 336) per costruzione in ogni vista.
- **Dondolo**: per ognuna delle 16 viste principali, 4 fotogrammi
  `zattera_iso_<NN>_f1.png` … `_f4.png` (64 file).
- `rotazione_parametrica_completa_32.gif` — giro completo, 32 viste sul
  mare vero (tessera Gruppo 1 v4), 120 ms/fotogramma, loop.
- `dondolo_vista00.gif` — ciclo di dondolo della vista 00 (base + f1…f4),
  ritaglio ingrandito 1,5×, 170 ms/fotogramma, loop.
- `scheda_confronto_set.png` — parametrica 00 vs generata 00 approvata,
  stessa scala, sul mare vero.

## Modello e parametri
- Coordinate guida (u = verso prua, v = destra guardando la prua):
  albero con vela avvolta (1,04 ; −0,10), alto ~185 px; tenda
  (−0,76 ; +0,18), impronta 1,1×0,9, alta ~140 px, ingresso verso prua;
  cassa (0 ; +0,41), ~75 px; tanica rossa (−0,78 ; −0,80), tanica verde
  (−0,50 ; −0,85), ~70 px. Scafo 3×2, assito ~30 px sull'acqua, barili
  sdraiati blu/ruggine lungo i bordi, infilati sotto il bordo dell'assito.
- Luce **fissa** da in alto a sinistra dello schermo: non ruota con la
  zattera; ruotando, chiari e scuri si spostano sulle facce come devono.
- Dondolo = fasi j = 1..4 di un ciclo sinusoidale completo a 5 fasi
  (j = 0 è la vista base): il ciclo base → f1 → f2 → f3 → f4 → base è
  chiuso e senza scatti per costruzione. Ampiezze: rollio ±2,2° attorno
  all'asse di prua, beccheggio ±1,4° (sfasato di 1,1 rad), sollevamento
  ±3 px (sfasato di 0,6 rad).

## Miglioramenti di stile applicati (dalla NOTA_PILOTA)
Texture e usura sono **geometria del modello**, ancorate alle coordinate
locali con seme fisso: ruotano insieme all'oggetto, identiche in ogni
fotogramma (anche nel dondolo).
- Assito: assi segmentate con variazione di tono per segmento, venature
  ondulate e nodi in posizioni fisse, chiazze di muschio, linea di
  galleggiamento sui fianchi.
- Barili: profilo bombato, doghe longitudinali, 3 anelli metallici,
  toppe di ruggine e di colore alternato con seme fisso per barile.
- Tenda: falde in pannelli con variazioni di tono, cuciture e pieghe,
  due toppe con bordo cucito (una blu-grigio, una grezza), tiranti agli
  angoli.
- Vela: bande di cucitura orizzontali, due toppe di superficie, legature
  di corda; cime dell'albero a tre punte come nel disegno approvato.
- Cassa: montanti angolari, doghe su coperchio e fianchi. Taniche: X in
  rilievo sulle facce e tappo.

## Verifiche
- **Rigidità**: proiezione analitica della base dell'albero ai 32 angoli
  — distanza dal centro costante (1,044797 tessere, min = max) e angolo
  sullo schermo monotono per tutto il giro (passi 5,6°–22,3°, tutti
  positivi): rotazione rigida esatta, non approssimata.
- Tutti i 96 PNG sono 704×512. Sagoma mai tagliata: margine minimo
  10 px nelle 32 viste; nei fotogrammi di dondolo il margine scende a
  3 px solo nella fase estrema f3 delle viste 11 e 12 (nessun taglio).
- **Continuità dondolo** (vista 00, differenza media assoluta tra fasi
  consecutive, chiusura compresa): 6,19 · 5,25 · 6,83 · 3,11 · 5,40 —
  passi confrontabili, nessuno scatto.

## Note dichiarate
- L'ingresso della tenda verso prua, come da coordinate guida, nella
  vista 00 risulta **coperto dalla cassa**: è la conseguenza geometrica
  delle posizioni fisse, identica nel pilota.
- La sagoma totale è ~660 px di larghezza contro i 640 del set generato
  (i barili stanno fuori dal rombo dell'assito, come nel pilota); il
  centro impronta (352, 336) e la tela sono identici.
- Limiti di stile residui, dichiarati: la resa resta a **facce ombreggiate
  con dettaglio procedurale**, non acquerello dipinto — niente venature a
  pennello, ruggine pittorica o tela stropicciata dei disegni generati.
  La vela è un solido rastremato con cuciture e toppe, senza pieghe né
  effetto sacchetto; la tenda è un prisma pulito con cuciture e toppe.
  Geometria, proporzioni, posizioni e palette coincidono col disegno
  approvato (vedi scheda confronto); la mano pittorica no — è il prezzo
  della rotazione rigida, ed è il compromesso scelto dall'utente.

## Formato di consegna (GitHub)
- I file binari (PNG e GIF) sono caricati come `nome.est.b64` (base64 su
  una riga), elencati in `elenco.txt`: decodificare per riottenere i file
  originali.
- `rotazione_parametrica_completa_32.gif` è caricata in 3 parti
  `rotazione_parametrica_completa_32.gif.b64.1` + `.b64.2` + `.b64.3`
  (limite di dimensione del singolo invio): concatenare in ordine e
  decodificare per ricostruire la GIF originale.

STATO: pronto (set parametrico completo)
