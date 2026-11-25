# DERIVA — CHANGELOG
Ogni modifica al gioco o al progetto aggiunge una riga qui, con la versione
che l'utente vede in gioco. Versioni: `0.x` = progetto/prototipo, `1.0` = prima pubblicabile.

## Progetto — 26 nov 2026, notte — in gioco resta «v0.2c · prova isometrica» (pubblicata)
- **Decisione dell'utente: la zattera avrà 16 viste (una ogni 22,5°)** per girare fluida a 360°, disegnate da Muse. Richiesta e guide pronte in `muse/2026-11-26-zattera-16-viste/` (`RICHIESTA.md`, `guide/guide_zattera_16_foglio.png` e 16 guide singole): tela fissa 704×512, centro impronta a (352,336), disposizione degli oggetti a bordo in coordinate fisse, luce sempre da in alto a sinistra. Consegna a lotti (4 → 8 → 16 viste). Sostituisce la zattera v2.
- **Motore pronto** (non pubblicato, nessuna differenza visibile finché non arrivano i disegni): `CFG.RAFT_VIEWS` = 4 | 8 | 16 (anche `?viste=8|16` nell'indirizzo, per provare). Le viste stanno in `assets/iso/mezzi/zattera16/zattera_iso_00..15.png`; con 16 viste la sfumatura fra due viste vicine (22,5°) copre tutto l'intervallo; ombra e schiuma seguono la vista. Provato con un set finto: 4/8/16 viste senza errori, ~2 ms per fotogramma.
- Da fare quando arriva il lotto A: montarlo (8 viste = lotti A+B), verifica di coerenza degli oggetti fra viste vicine, poi il lotto C.

## 0.2c — 26 nov 2026 — PROVA ISOMETRICA: in gioco si legge «v0.2c · prova isometrica · grafica Muse»
- **Ombra della zattera corretta.** Nella v0.2b l'ombra ruotava con l'angolo continuo mentre il disegno ha solo 4 viste: l'ombra girava e la zattera no, e sembrava che volasse. Ora ombra e schiuma sono una per ciascuna delle 4 viste (stessa impronta del disegno) e cambiano insieme alla zattera con la stessa sfumatura. Ombra più stretta e a contatto con l'acqua, più un filo di schiuma sul bordo.
- Resta il limite delle 4 viste (vedi 0.2b): rotazione fluida solo con più viste.

## 0.2b — 26 nov 2026 — PROVA ISOMETRICA: in gioco si legge «v0.2b · prova isometrica · grafica Muse»
Correzioni dopo la prova sul telefono (letto: 120 fps fissi, picco 8,5 ms; scala reale dei disegni 1,88× con dpr 3,75).
- **Baracca: niente più vista interna.** Era comparsa/scomparsa avvicinandosi e non piaceva: ora si vede sempre da fuori (il file `baracca_interno_iso.png` resta nel progetto, non viene più caricato).
- **Pali del pontile: di nuovo col disegno di Muse** (`palo_iso.png`, assi grigie con muschio) al posto del marrone piatto provvisorio. Quello ai capi era messo male (la cima sporgeva fuori dal pontile): i due estremi ora rientrano di 0,32 tessere e la cima resta sotto il pontile. Il file di Muse ha una striscia trasparente (colonne 28–35, alpha 34) e il piede tagliato netto: dietro gli metto un sottofondo del colore medio così non si vede il mare attraverso; **palo v2 da far rifare a Muse**.
- **Zattera: rotazione continua.** L'angolo di prua ora è un numero continuo (`raft.phi`, 0°=SE, 90°=SO, 180°=NO, 270°=NE): la zattera gira con calma verso dove spingi il joystick (`RAFT_TURN`, 3,2 rad/s) e avanza lungo la prua, quindi il percorso è curvo e senza scatti. Il disegno però resta quello delle 4 viste: fra due viste si sfuma per un attimo (`RAFT_FADE`, 0 = salto netto). **Limite dichiarato:** con 4 viste lontane 90° la sfumatura fa vedere due zattere sovrapposte per ~0,1 s; per una rotazione davvero fluida servono più viste (16–32) della zattera. Scelta da fare con l'utente (Muse disegna 16 viste / modello 3D di Claude con i materiali di Muse / si tiene la sfumatura).
- Ingombro della zattera: rettangolo 3×2 ruotato (a scatola); se girando entra nel pontile viene spinta fuori.
- Pulsante «Scendi» ora con soglia in px/s (la velocità della zattera adesso è in px CSS/s).

## 0.2a — 25 nov 2026, sera — PROVA ISOMETRICA (pagina separata): in gioco si legge «v0.2a · prova isometrica · grafica Muse»
Il gioco v0.1b.8 dall'alto **non cambia** (resta pubblicato com'è). Questa è una pagina di prova nuova, per vedere la grafica isometrica di Muse che si muove.
- **Motore a rombi 2:1** (geometria di Muse): coordinate di terra (i,j), schermo x=(i−j)·128, y=(i+j)·64 px PNG. Scala in gioco 0,5 px CSS per px PNG (rombo 128×64 CSS); sul telefono (dpr ~2,6) i disegni sono ingranditi 1,3× (il debug mostra «scala disegni»).
- **Base statica preparata una volta** (1:1 px PNG, un canvas solo): ombra sul mare, pali, pavimenti d'acciaio (a/b/c a caso dalle coordinate) e di legno, buco, facce SE/SO, ringhiere sui lati nord, ombre a terra degli oggetti (luce da in alto a sinistra → ombra verso SE). Sotto ogni rombo un sottofondo del suo colore medio: i bordi antialias dei rombi lasciavano un filo di mare fra due caselle.
- **Oggetti** (derrick, testa pozzo, serbatoio, gru, baracca, 2 container, 3 tubi) piazzati per centro dell'impronta con la formula di Muse; ordine di disegno con confronto fra ingombri (non per centro) e ordine fisso dei fissi; il protagonista si inserisce dove serve. Baracca: vista interna quando ti avvicini.
- **Protagonista** a piedi: joystick a sinistra, 4 sprite diagonali scelte con isteresi, collisioni con bordi, buco e oggetti. Rimbalzo di 2,5 px in camminata **provvisorio** (`WALK_BOB`, 0 = spento) finché non c'è il ciclo di passo.
- **Zattera** attraccata a sud del pontile (a livello del mare, 64 px sotto il ponte), pulsante **Sali / Scendi**, navigazione con le 4 viste, ombra morbida, collisione con la piattaforma; davanti o dietro alla piattaforma secondo da che lato sta. Mare: 2 strati d'onda di Muse come nel gioco attuale. In barca il protagonista non si disegna (aspetta la zattera v2 di Muse).
- **Pali del pontile provvisori, disegnati dal codice.** Il `palo_iso.png` di Muse non coincide con quello della sua anteprima: ha una striscia bianca semitrasparente a un terzo della larghezza e il piede tagliato netto, senza ombra. Da far rifare (palo v2).
- **Prestazioni** (simulatore software, ~1,5× più lento del telefono, raster forzato): ~14 ms medi per fotogramma. Ingrandendo si usa il filtro bilineare (con quello «alto» erano ~28 ms per niente).
- **Da decidere (domande all'utente):** container troppo alti (parete 220 px = 2,2 volte il protagonista; reale ~1,5) → farli rifare più bassi? e risoluzione dei PNG: a 1,3× i pavimenti sono ingranditi, chiedere a Muse esportazioni a 384 px per pavimenti/facce/bordi e 1,5× per gli oggetti?

## Progetto — 25 nov 2026, sera — nessun cambio al gioco: in gioco resta «v0.1b.8 · grafica Muse»
- **Svolta isometrica (decisione dell'utente, ore 19:29).** Deriva passa dalla vista dall'alto alla vista **isometrica 2:1** (rombi, si vedono il sopra e due facce). La 4a/4b/4c dall'alto a tessere quadrate è scartata. Il mare dei Gruppi 1 e v4 resta come fondo continuo; zattera, relitti e protagonista andranno ridisegnati in isometrico.
- **Ricevuti e controllati** i Gruppi iso 1 (pavimenti e bordi) e iso 2 (12 oggetti + anteprima completa a due parti): file e misure corretti. Da far rifare a Muse: alone magenta su derrick, serbatoio, baracca e container ocra; facce sud-ovest con geometria sbagliata (fanno una scalinata); scala e ancoraggi degli oggetti non dichiarati. Dettagli in `muse/2026-11-25-gruppo-iso-2-oggetti/RISPOSTA.md`.
- **Correzioni v2 di Muse verificate** (21 file): alone magenta 0 su tutti i 12 oggetti, facce sud-ovest a spessore uniforme (65 px in ogni colonna), oggetti già in scala dell'anteprima (da ~24 MB a ~2 MB di PNG), misure tutte corrette. Via libera a zattera e protagonista isometrici (scala 1:1 con l'anteprima v2).
- **Gruppo iso 3 ricevuto** (zattera 4 diagonali + protagonista fermo 4 direzioni, 100 px): misure e alone ok; zattera v2 richiesta (cassa mancante in NE, disposizione di cassa/taniche incoerente in NE e SO, 31 px vuoti nel file SE, anteprima con zattera sopra il pontile).
- **Non montato nel gioco**: serve il motore a rombi (movimento, collisioni, ordine di disegno) e, per giocare, zattera e protagonista isometrici. Il gioco dall'alto v0.1b.8 resta intatto (`www/` e `www/storico/`).

## 0.1b.8 — 25 nov 2026 — in gioco si legge «v0.1b.8 · grafica Muse»
- **Risolti gli scatti** (sul telefono la v0.1b.7 faceva ~6 fps, picco 280 ms). Due cause, due rimedi, nessuna grafica ridotta:
  - **Il mare si compone una volta sola.** Prima ogni fotogramma rifaceva ~15 passaggi a schermo intero (tessere, blu, maschere). Ora il mare è composto in blocchi da 512×512 pixel del dispositivo, tenuti in memoria; ogni fotogramma ne copia solo quelli visibili. Un blocco nuovo per fotogramma viene preparato in anticipo nella direzione di marcia; quelli lontani si buttano. Se cambiano bottoni o schermo, i blocchi si rifanno da soli. Nel simulatore (caso del tuo screenshot): ~260 → ~40 ms.
  - **Le onde non sono più disegnate nel canvas.** Sono 4 strati (2 Muse + 2 Claude) fatti con elementi della pagina che il telefono sposta con la GPU, senza ridisegnarli: ogni fotogramma cambia solo la posizione. Ordine dal basso: mare → onde → chiazze, scia, zattera, joystick (secondo canvas trasparente). Nel simulatore il mix passa da ~62 a ~7 ms.
- **Mix onde Claude + Muse** (richiesta dell'utente). Nuova scelta di serie del bottone «Onde»: Muse + Claude → Muse → Claude → spente.
- **Di serie ora:** onde Muse + Claude, blu Muse, varianti b **no** (come deciso dall'utente). Chiave di salvataggio nuova `deriva_prova2`: le vecchie scelte della v0.1b.7 si azzerano.
- **Cambiamento visibile:** il secondo strato di Claude non è più ruotato (0,45 rad): con gli elementi della pagina un strato ruotato dovrebbe essere enorme. Resta più piccolo (×1,7) e scorre in direzione diversa, quindi le onde si incrociano lo stesso. Muse invariato.
- Le chiazze prendono il velo blu della zona anche con «Blu: Claude» (prima solo con «Blu: Muse»), perché ora il blu sta nel mare, sotto.
- Pannello debug: riga nuova `ms: mare … onde … tutto … blocchi`, per vedere dove va il tempo.
- **FPS veri da leggere sul telefono** (pannello debug). Nel simulatore software (1,5× più lento del telefono): fermo ~7 ms, in moto ~10 ms medi (picchi ~30–45 ms quando entra un blocco nuovo).
- Versione precedente (v0.1b.7) conservata in `www/storico/`.

## 0.1b.7 — 25 nov 2026 — in gioco si legge «v0.1b.7 · grafica Muse»
- **Montata la consegna v4 di Muse** (`gruppo-1-mare-v4`): overlay onde, tessere blu (medio e fondo), varianti b di basso/medio/fondo.
- **Bottoni «prova mare»** in alto a destra (si vedono finché il pannello debug è acceso; toccando la versione in basso due volte spariscono). Ognuno cambia al tocco e la scelta resta salvata sul telefono:
  - **Onde:** Muse → Claude (provvisorie) → spente. Muse = overlay di Muse in due strati nella stessa orientazione (ruotarli faceva un reticolo), scorrimento lento. Claude = il flusso provvisorio ricavato dalla tessera media.
  - **Blu:** Muse → Claude → spento. Muse = tessere `mare_medio_blu` / `mare_fondo_blu` sfumate con le stesse zone del velo (stesso rumore fisso nel mondo). Claude = velo di colore in codice.
  - **Varianti b:** sì / no. Alterna le tessere a e b (scelta dalle coordinate, stessa seed = stesso mare) per spezzare la ripetizione.
- Di serie: tutto «Muse», varianti b «sì». In `CFG`: `MARE_ONDE`, `MARE_BLU`, `MARE_VAR`, `ONDE_A1` (0,8), `ONDE_A2` (0,55).
- Visto nel simulatore: **blu Muse e blu Claude sono quasi uguali** (Muse ha mescolato nelle sue tessere lo stesso colore (56, 98, 142) al 35–40% che usavo io in codice). Le **varianti b** rompono bene la ripetizione a quadri del mare basso senza giunture visibili. L'**overlay** dà creste di luce naturali.
- Costo nel simulatore software (non rappresentativo): tutto spento ~50 ms, versione Claude ~80–95 ms, versione Muse ~110 ms per fotogramma: **FPS veri da leggere sul telefono** con i bottoni nelle due combinazioni.
- Versione precedente (v0.1b.6) conservata nella cronologia della repo.

## 0.1b.6 — 25 nov 2026 — in gioco si legge «v0.1b.6 · grafica Muse»
- **Profondità: tocchi di blu** (richiesta dell'utente, «sempre nello stile di adesso»). Un velo di blu desaturato (56, 98, 142) con opacità variabile, da rumore fisso nel mondo (stessa seed = stesse zone ovunque).
- Più frequente dove il mare è fondo: nel mondo di prova ~72% del mare fondo ha blu (più della metà forte), ~26% del medio (zone sparse), quasi nulla nel basso (si vede la sabbia). Sul totale ~30% del mare ha un tocco di blu.
- Disegnato **sopra** mare e chiazze (così anche le chiazze si intonano) e **sotto** scia e zattera.
- Regolabile in `CFG`: `BLUE_A` (0,40; 0 = spento), `BLUE_RGB`, `BLUE_SCALE` (16 tessere = grandezza delle zone), `BLUE_LO`/`BLUE_HI` (quante zone), `BLUE_DEPTH` (quanto segue la profondità).
- Provvisorio, in codice: la versione definitiva può essere una tessera «fondo blu» di Muse (richiesta nel `RISPOSTA.md` del Gruppo 1 v3).
- Costo nel simulatore software: ~+20% del tempo di disegno (non rappresentativo): FPS veri da leggere sul telefono.

## 0.1b.5 — 25 nov 2026 — in gioco si legge «v0.1b.5 · grafica Muse»
- **Chiazze più rapide** (richiesta dell'utente: così lenta sembrava il mare sotto a muoversi, non la chiazza). Cambio ogni **1,2 s** (era 1,8) con dissolvenza di **0,6 s** (era 1,0). Deriva invariata (±1,5 px). Regolabili in `CFG`: `SLICK_PERIOD`, `SLICK_FADE`, `SLICK_DRIFT`.
- **Mare in movimento (PROVVISORIO, richiesta dell'utente: «lo vedo fermo, voglio che si veda che è in movimento»).** Fino alla v0.1b.4 il mare era fermo: dalla v0.1b.2 ho tolto le onde provvisorie e restavano solo le tessere statiche di Muse.
  - Ora due strati di sola **luce** (ricavati dalla tessera media di Muse, in modalità `overlay`) scorrono piano in direzioni diverse sopra il mare, ancorati al mondo: sovrapposti si incrociano come onde. Il colore del mare non cambia, cambia la luce.
  - Regolabili in `CFG`: `FLOW_A1` (0,30), `FLOW_A2` (0,24), `FLOW_SPEED` (1,0). Con `FLOW_A1: 0` e `FLOW_A2: 0` il mare torna fermo come nella v0.1b.4.
  - Misurato nel simulatore: con il flusso il mare cambia in media ~6,5/255 ogni mezzo secondo (prima ~0). Costo: +~47% del tempo di disegno nel simulatore software (non rappresentativo): **da leggere sul telefono** (FPS nel pannello debug).
  - A occhio fermo il mare risulta più «macchiato» di prima: è la luce che si sovrappone. Se non piace si abbassano i due valori.
  - Versione definitiva: onde/riflessi disegnati da Muse (richiesta scritta nel `RISPOSTA.md` del Gruppo 1 v3).

## 0.1b.4 — 25 nov 2026 — in gioco si legge «v0.1b.4 · grafica Muse»
- **Chiazze quasi ferme** (v3 di Muse, richiesta dell'utente: «troppe animazioni, meno, più statiche ma che diano sempre l'effetto»).
- 2 fotogrammi per tipo (acqua / petrolio) invece di 4. Cambio ogni **1,8 s** con dissolvenza morbida di **1 s**; il resto del tempo la chiazza è ferma.
- **Deriva ridotta** da ±14 px a **±1,5 px**, lentissima. Tutto regolabile in `CFG`: `SLICK_PERIOD` (1,8), `SLICK_FADE` (1,0), `SLICK_DRIFT` (1,5; 0 = ferma del tutto).
- Misurato in simulatore: la variazione media tra due istanti a 0,1 s resta sotto 1,5/255 per canale (nessuno scatto al cambio di fotogramma). Il giudizio vero è a occhio sul telefono.
- Tolti dal gioco i fotogrammi 3 e 4 delle v2 (restano nella repo come storico).

## 0.1b.3 — 25 nov 2026 — in gioco si legge «v0.1b.3 · grafica Muse»
- **Chiazze v2 di Muse** (`gruppo-1-mare-v2`, approvate da Davide): colore intonato al mare, si riconoscono dai vortici e dalla superficie più liscia.
- **Due tipi di chiazza:** «acqua» (leggera) e **«petrolio»** (più scura, per le zone inquinate). Nel mondo di prova ~1/3 sono petrolio. Vicino alla partenza ce n'è una per tipo: acqua in alto a destra, petrolio in basso a sinistra.
- Il chunk ora ha una **lista** di chiazze (`slicks`) invece di una sola: servirà ai punti di interesse (v0.1c).
- Le 4 chiazze v1 restano come storico nella cartella `muse/2026-11-25-gruppo-1-mare/`; nel gioco ci sono solo le v2.
- Provato: nessun errore in console, mondo deterministico (stessa seed = stesse chiazze), test del mondo tutti OK.

## 0.1b.2 — 25 nov 2026 — in gioco si legge «v0.1b.2 · grafica Muse»
- **Grafica di Muse montata** (Gruppo 1 mare, Gruppo 2 zattera, macchie d'olio). Niente più colori provvisori.
- **Mare:** tre tessere (basso / medio / fondo). Il passaggio tra profondità è una sfumatura continua (maschere a bassa risoluzione, allineate al mondo): nessuna giunzione tra tessere né tra chunk.
- **Zattera:** sprite di Muse a 4× (192×128 px in gioco), prua a sinistra nel disegno → ruotata di π rispetto alla rotta. Ombra e scia sono disegnate dal gioco (niente ombre nel PNG, luce da sinistra in alto).
- **Macchie d'olio:** 4 fotogrammi a ~2/s con dissolvenza e deriva lenta. Chunk (0,0) ha sempre una macchia vicino alla partenza; negli altri ~12 %.
- Caricamento con schermata «Carico la grafica…»; il gioco parte solo a grafica pronta.
- Numero di build: sulle pubblicazioni di GitHub Pages il gioco controlla `v.txt` ogni 45 s e, se c'è una build nuova, mostra «Nuova versione: tocca per aggiornare» (nessuna ricarica a sorpresa).
- Provato in browser simulato 892×412: nessun errore, 9 chunk attivi, prua nel verso giusto, nessuna banda visibile sulle transizioni.
- **Difetti da grafica (per Muse):** c'è una sola variante per livello → ripetizione visibile a ogni tessera; i tre livelli hanno strutture diverse; mancano costa/riva, sabbia atollo e scia. Vedi `RISPOSTA.md`.
- Da leggere sul telefono: **FPS veri** (il simulatore non ha GPU; il rumore di fondo è software).
- Versione precedente (grafica provvisoria) conservata in `index_v0.1b.1_provvisoria.html`.

## 0.1b.1 — 25 nov 2026 — in gioco si legge «v0.1b.1 · grafica provvisoria»
- Gioco in **orizzontale** (richiesta dell'utente). In verticale compare «Ruota il telefono in orizzontale» e il gioco si ferma.
- Joystick solo nel 55% sinistro dello schermo; a destra resta lo spazio per le azioni (v0.1d).
- Camera con anticipo di 0,45 s di corsa, per vedere davanti nella vista larga (`LOOKAHEAD: 0` la toglie).
- Provato in browser simulato 892×412 e 412×892: tocco a destra ignorato, a sinistra muove, overlay in verticale, 9 chunk attivi, nessun errore.
- Per l'APK: bloccare l'orientamento in orizzontale (`sensorLandscape`) quando si imposta Capacitor.

## 0.1b — 25 nov 2026 — in gioco si legge «v0.1b · grafica provvisoria»
- **Mare infinito.** Chunk di 16×16 tessere (tessera 64 px, chunk 1024 px). Sono attivi solo i 3×3 attorno alla zattera: i nuovi si creano davanti, quelli lontani si scaricano.
- **Profondità del mare** (basso / medio / fondo) da rumore deterministico: hash a numeri interi, niente `Math.random`. Seed fissa di prova **12345**: stessa seed = stesso mare su ogni telefono (provato: identico dopo ricarica e senza dipendere dall'ordine di generazione).
- **Mare provvisorio:** colore morbido per chunk (senza giunture tra chunk) + onde in sovrimpressione che scorrono + scia della zattera. Le tessere di Muse si disegneranno per tessera dalla stessa mappa di profondità, con le transizioni sfumate in codice.
- **Debug** (tocca la versione in basso: info → info + griglia chunk → spento): tessera, chunk, chunk attivi, profondità, velocità, rotta, percorso, tempo, FPS, picco di un fotogramma, tempo di creazione dei chunk.
- Prove fatte (browser simulato, telefono verticale): 9 chunk attivi sempre, caricamento/scarico corretto su 120 s di corsa (~31 000 px, ~30 chunk attraversati), nessun errore in console, distribuzione dei livelli ≈ 27 % basso / 49 % medio / 24 % fondo. **Gli FPS veri vanno letti sul Galaxy S25 Plus** (il simulatore non ha la GPU).
- Non ancora: POI, sbarco, benzina, salvataggio.

## 0.1a — 25 nov 2026 — scheletro (non pubblicato a parte, assorbito in 0.1b)
- Canvas a schermo intero alla densità reale dello schermo, joystick fluttuante (tocca e trascina ovunque), tastiera per prove da PC.
- Zattera provvisoria disegnata nel codice, 3×2 tessere: ruota verso dove spingi, accelera, si ferma in ~0,5 s se rilasci.
- Tutti i numeri da regolare in un blocco `CFG` in cima al file: velocità 4 tessere/s, accelerazione, frenata, virata, raggio del joystick.
- Versione sempre visibile in basso.

## 0.1-progetto — 25 nov 2026
- PROGETTO.md: aggiunte le decisioni dell'utente (orizzontale, niente contorni scuri, relitti dalla zattera, grafica prima) e le correzioni tecniche (POI per regione 5×5, hash a interi, PNG a 4×, costa a 3 pezzi, scia, salvataggio versionato).

## 0.0-progetto — 25 nov 2026
- Concept scelto dall'utente: Variante A «Deriva — Waterworld / Mad Max sul mare».
- Scritto PROGETTO.md: pilastri, generazione a chunk da seed, 4 tipi di POI,
  3 risorse (benzina, rottami, acqua), piano prototipo v0.1 in 6 passi (v0.1a–v0.1f).
- Scritto PROMPT_CLAUDE.md: lista grafica in 6 gruppi (prima consegna: Gruppi 1–3).
- Nessun codice ancora. Prossima versione prevista: **v0.1a** (scheletro navigabile).
