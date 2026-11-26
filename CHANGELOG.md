# DERIVA — CHANGELOG
Ogni modifica al gioco o al progetto aggiunge una riga qui, con la versione
che l'utente vede in gioco. Versioni: `0.x` = progetto/prototipo, `1.0` = prima pubblicabile.

## 0.2q — 26 nov 2026 — in gioco si legge «v0.2q · isometrica · grafica Muse»
- **Zattera immersa nell'acqua** (la zattera 3D sembrava sospesa): rifatte le 32 viste in Blender con i barili a metà sotto il pelo dell'acqua (piano «holdout» a z=0 che nasconde la parte immersa; modello in `raft_blender.py`).
- **Effetti acqua nel gioco (solo zattera 3D):** onde che si allargano dallo scafo, acqua scura a contatto, schiuma a tratti irregolari sui lati verso di noi, scia di cerchi quando naviga.
- Tutto senza `ctx.filter` (che su alcuni telefoni disegna un rettangolo).
- Possibile passo successivo: acqua animata renderizzata in Blender attorno alla zattera.

## 0.2p — 26 nov 2026 — in gioco si legge «v0.2p · isometrica · grafica Muse»
- **Tolta l'ombra rettangolare** sotto la zattera 3D (era l'ombra pensata per la zattera di Muse, più grande del modello 3D) e il filo di schiuma rettangolare. Ora l'ombra è la sagoma della vista stessa, sfumata a mano e spostata in basso. La zattera di Muse conserva la sua ombra di prima.
- **Zattera più veloce:** `SAIL_SPEED` 210 → 290 (+38%).

## 0.2o — 26 nov 2026 — in gioco si legge «v0.2o · isometrica · grafica Muse»
- **Corretto:** la zattera 3D lasciava un'immagine doppia semitrasparente mentre girava (lo sfumo fra viste vicine copriva tutto l'intervallo). Ora le 32 viste cambiano di netto (cambio netto a metà fra due viste), quindi non c'è più fantasma.

## 0.2n — 26 nov 2026 — in gioco si legge «v0.2n · isometrica · grafica Muse»
- **La zattera 3D (Blender, 32 viste) diventa quella di serie.** Quella disegnata da Muse (16 viste) resta scegliibile da Menu → Prova → Zattera (o `?zattera=muse`).

## 0.2m — 26 nov 2026 — in gioco si legge «v0.2m · isometrica · grafica Muse»
- **Corretto:** rettangolo scuro attorno alla zattera sul telefono di Davide. Causa: l'ombra usava `ctx.filter = blur()`, che su alcuni dispositivi riempie tutta la tela. Ora l'ombra e la schiuma sono sfumate a mano con strati sovrapposti, senza filtri.

## 0.2l — 26 nov 2026 — in gioco si legge «v0.2l · isometrica · grafica Muse»
- **Zattera 3D di prova (Claude, Blender):** 32 viste, una ogni 11,25°, stessa tela 704×512 e stesso centro (352,336) di Muse. Si attiva da Menu → Prova → Zattera (o `?zattera=3d`); di serie resta quella di Muse.
- Modello costruito da zero in Python (`assets/iso/mezzi/zattera3d/raft_blender.py`): ponte di assi, barili, tenda, cassa, taniche, albero. Angoli e posizioni degli oggetti identici in ogni vista. Colori e texture sono una prima bozza, da migliorare.
- Allineamento verificato confrontando le sagome con le 16 viste di Muse (la rotazione segue lo stesso verso).
- Prossimo: colori/texture più vicini allo stile di Muse, dondolo da ferma, taniche e motore a scelta.

## 0.2k — 26 nov 2026 — in gioco si legge «v0.2k · isometrica · grafica Muse»
- **Protagonista in 8 direzioni:** montate le 4 cardinali di Muse (Gruppo iso 5: N, E, S, O; fermo + 6 passi, 28 sprite, tela 70×108, piedi in (35,104), magenta 0). Direzione scelta ogni 45° sull'angolo sul terreno (si cambia solo oltre 30° dal centro: niente scatti); il fermo cardinale usa lo stesso punto-piedi della camminata. Il codice di salvataggio e gli slot già conoscono le 8 direzioni (i salvataggi vecchi restano validi).
- Verifica: 8 direzioni provate sul molo, personaggio coerente, piedi fermi sullo stesso punto.
- Il «Gruppo iso 5» di Muse è questo; gli oggetti di scena diventano **Gruppo iso 6**.
- Test: 18 prove automatiche ok, nessun errore.

## 0.2j — 26 nov 2026 — in gioco si legge «v0.2j · isometrica · grafica Muse»
- **Zattera: lotto C montato (viste dispari) → 16/16 viste**, una ogni 22,5°; il motore le usa da solo, con cambio netto di vista (nessuna sfumatura, quindi niente doppia immagine). Verifica: tela 704×512 e magenta 0 in 8/8, lotti A+B identici. Provata a 16 angoli sul mare: rotazione continua e coerente. Note: viste 01 e 03 con il ponte un po' più piccolo delle vicine.
- Test: 18 prove automatiche ok, nessun errore.

## 0.2i — 26 nov 2026, notte — in gioco si legge «v0.2i · isometrica · grafica Muse»
- **Zattera: lotto B montato (viste 02, 06, 10, 14)** → con A+B il motore usa da solo **8 viste** (una ogni 45°, sfumatura nella parte centrale di ogni passo). Verifica: tela 704×512 e magenta 0 in 4/4, lotto A identico a quello già montato. Provata a 16 angoli sul mare: 02 e 10 (le critiche) escono bene — ponte rettangolare piatto 362×272, albero verticale, tenda in piedi; 06 e 14 sono larghi e sottili (544×182) come vuole la geometria isometrica, con il bordo alto appena storto (dichiarato da Muse).
- Resta: con 8 viste la sfumatura fra diagonale e cardinale mostra ancora una leggera doppia immagine (forme diverse del ponte): attenuata con il lotto C (viste dispari → 16 viste). Taniche in 04/12 ancora al centro (limite dichiarato).
- Test: 18 prove automatiche ok, nessun errore.

## Progetto — 26 nov 2026, notte — in gioco resta «v0.2h · isometrica · grafica Muse»
- L'utente descrive la **visione del gioco**: esplorare il mare, piattaforme con rottami da raccogliere (servono a migliorare), taniche, **missioni** sulle piattaforme (vuote o con nemici), **fortezze di ferro arrugginito** e nemici in stile «smokers» con **motoscafi**, **inizio partita fisso con dialoghi** del personaggio, **menu con le missioni**, **sete e fame**. Scritto in `PROGETTO.md` («Visione di gioco») con un piano proposto in 5 passi (v0.3a–e); l'ordine non è ancora deciso. Nota: sete e fame da fare morbide (pilastro 5).

## 0.2h — 27 nov 2026, notte — PRIMA VERSIONE COME APP: in gioco si legge «v0.2h · isometrica · grafica Muse»
Richiesta di Davide: «Facciamo anche l'apk che così lo scarico, metti come su Sette Mari qualche salvataggio, l'impostazione per la grafica di prova».
- **Il motore isometrico diventa il gioco** (`www/index.html`). Il gioco di prima (v0.1b.8, dall'alto) e le versioni vecchie stanno in `www/storico/` (con `<base href="../">`, così ritrovano le loro immagini) e si aprono da Menu → Novità → Versioni precedenti: nulla è stato tolto.
- **Menu ☰** in alto a destra (anche tasto Esc; il tasto «indietro» di Android lo chiude invece di uscire dal gioco). Il gioco è in pausa mentre è aperto. 4 schede: Partita, Grafica, Prova, Novità.
- **Salvataggi:** automatico (ogni 6 s se qualcosa cambia, quando si esce dall'app e quando si apre il menu) + 3 slot manuali + **codice corto** (`DRV1-…`, 35 caratteri, con controllo, da copiare/incollare, anche su un altro telefono). Si salva: a piedi o in zattera, posizione, direzione, zattera e tempo di gioco. Se la posizione salvata finisce dentro un oggetto (disposizione cambiata) il protagonista va sulla casella libera più vicina. Se il telefono non lascia scrivere i dati, o i dati sono rovinati, il gioco parte lo stesso. «Nuova partita» (doppio tocco) non cancella gli slot. Il formato porta una versione (`v:1`) per aggiungere cose dopo (carburante, oggetti) senza rompere i salvataggi vecchi.
- **Grafica** (normale): Auto / Bassa / Media / Alta. Alta = tutta la nitidezza del telefono; Media = tetto ×2,5; Bassa = ×1,5 e senza luce scorrevole sul mare. Auto parte da Alta e scende di un livello solo se il lavoro per fotogramma resta sopra 16 ms per 150 fotogrammi (con avviso in gioco), non risale da sola. Predefinito Auto: sul Galaxy S25+ resta Alta.
- **Grafica di prova** (scheda Prova), separata dalla normale: disposizione piattaforma Nuova / Precedente (riavvia), viste della zattera (4 ora; 8 e 16 appena Muse le consegna; riavvia), sfumatura fra le viste, onde di Muse, luce scorrevole, macchie d'olio, sagoma dietro agli oggetti, info tecniche; «Tutto com'era» le rimette a posto. Ogni prova futura è una riga in più nella tabella `TEST_OPTS` del codice.
- **Novità** in gioco (con registro completo, letto da `CHANGELOG.md` della pubblicazione) e versioni precedenti. Info tecniche (fps) nascoste di partenza: si accendono toccando la versione in basso. Avviso «Nuova versione: tocca per aggiornare» (confronto con `v.txt`): toccandolo si salva e si ricarica, nessuna ricarica a sorpresa.
- **Pubblicazione e APK, con un solo file:** `.github/workflows/deriva.yml` (sostituisce `pages.yml` e `build-apk.yml`). Si carica nel repo **un solo zip**: il file scompatta lo zip, pubblica il gioco su GitHub Pages e, se nello zip c'è `.ricompila-apk`, compila l'APK (firma fissa, orizzontale, schermo intero) e lo mette in Releases («apk-ultimo») oltre che in Actions → Artifacts. Così da telefono basta caricare 1 file invece di una novantina. Istruzioni: `PUBBLICAZIONE.md`. L'app (`it.deriva.game`) carica il gioco da GitHub Pages: gli aggiornamenti del gioco arrivano da soli, l'APK si rifà solo se cambia l'app stessa. Icona: per ora quella predefinita di Capacitor (da disegnare con Muse).
- **Controlli:** 18 prove automatiche (menu, pausa, slot, codice andata e ritorno con numeri negativi, codici sbagliati rifiutati, grafica bassa/alta, riavvio con prova attiva, posizione dentro un oggetto, tasto indietro, dati rovinati), tutte ok; nessun errore; le versioni precedenti si aprono senza immagini mancanti; il passaggio «scompatta lo zip» provato in locale su un repo finto. **Non provato:** la compilazione vera dell'APK e la pubblicazione su GitHub (qui non ci sono Android SDK né accesso in scrittura al repo).

## 0.2g — 27 nov 2026, notte — anteprima, ora inclusa in v0.2h (la disposizione nuova è quella predefinita; la precedente resta in Grafica di prova)
Richiesta di Davide: «sistemare tutta la predisposizione degli oggetti sopra: messi a caso, devono avere senso, alla Water world / Mad Max».
- **Nuova disposizione con una logica** (solo con gli oggetti che ci sono): torre di perforazione dietro al foro nel ponte; testa del pozzo accanto; **tubi dal pozzo al serbatoio** (2 dritti + 1 a T in fila lungo SO); **serbatoio vicino al molo** (punto di rifornimento) con la **baracca** accanto (il benzinaio); **2 container come magazzino** (ocra + verde) e **gru sul bordo NO** con il braccio sul mare (recupero dal mare), tutti sul lato dietro. Il container ruggine e la zona est/sud-ovest restano liberi per gli oggetti di scena.
- **Regola di visibilità:** gli oggetti alti stanno dietro (verso nord), quelli bassi davanti, così non coprono la vista dei tubi e di chi cammina (provato: spostare un container a est copriva pozzo e tubi). Zattera attraccata di fronte al serbatoio (i = 6,5), partenza a piedi sul molo.
- **Sagoma chiara del protagonista** quando cammina dietro un oggetto solido (il disegno vero si confondeva con la ruggine dei container).
- Controllo di raggiungibilità: nessuna tasca irraggiungibile sul ponte (4705 punti liberi, tutti raggiungibili dal molo); nessun errore; 15,3 ms medi nel simulatore.
- **Richiesta a Muse per il Gruppo iso 5 (oggetti di scena):** `muse/2026-11-27-gruppo-iso-5-props/RICHIESTA.md` (barili, casse, tettoie di tela, pompa di rifornimento, lampioni, antenna, stenditoio, reti da pesca, raccolta acqua, rottami, bitte e scaletta, barricate, stufa, bandiera), consegna a lotti, bassi per primi.

## 0.2f — 27 nov 2026, notte — PROVA ISOMETRICA: in gioco si legge «v0.2f · prova isometrica · grafica Muse»
- **Zattera: lotto A delle 16 viste montato** (viste 00, 04, 08, 12 = le 4 diagonali, tela 704×512, centro impronta (352,336)) e **zattera NE v2** (con la cassa che mancava). Verificato: misure, magenta 0, bordo sud dell'impronta sulla riga 495 in tutte e 4, bordi puliti. Prova a vista in 4 direzioni sul mare: albero a prua, tenda a poppa, cassa al centro in tutte le viste.
- **Motore:** `CFG.RAFT_AVAIL` elenca le viste consegnate (ora 0,4,8,12) e il motore usa da solo 4, 8 o 16 viste quando il giro è completo (lotto B → 8 viste, lotto C → 16); `?viste=4|8` nell'indirizzo per confrontare. Senza altri lotti la rotazione è come prima: 4 viste con sfumatura (la sovrapposizione fra due viste a 90° resta finché non arrivano B e C).
- **Limite dichiarato da Muse (accettato per ora):** nelle viste 04 e 12 le due taniche (rossa e verde) stanno più al centro che sulle posizioni della guida; per la rotazione a 16 viste servono nelle stesse posizioni in tutte, altrimenti nella sfumatura «saltano». Chiesto a Muse di ridisegnare 04 e 12 insieme al lotto B.
- Controlli: nessun errore; zattera, Sali/Scendi e joystick tattile come prima; 14,7 ms medi nel simulatore software (come prima).

## 0.2e — 27 nov 2026, notte — PROVA ISOMETRICA: in gioco si legge «v0.2e · prova isometrica · grafica Muse»
Dopo la prova di v0.2d sul telefono: «la camminata non mi piace, non muove bene le braccia», «il gioco è tutto zoomato», «il mare è diverso da come avevamo fatto (macchie d'olio, blu…)».
- **Zoom.** Nelle prove 0.2a–d la scala era 0,5 px CSS per px PNG (rombo 128×64): il doppio del gioco v0.1b.8 (tessera 64 px CSS = 0,25), quindi 1,88× d'ingrandimento sul telefono e poco mare in vista. Ora di partenza **0,30** (1,13× sul telefono, quasi nativa), e due bottoni **+ / −** a destra (anche tasti + −) con 7 passi da 0,20 a 0,60 (0,25 = stessa scala del gioco di prima; 0,50 = le prove precedenti). La scelta resta salvata sul telefono. Le velocità restano in unità di mondo: a zoom diverso il personaggio impiega lo stesso tempo ad attraversare una tessera.
- **Mare com'era nel gioco v0.1b.8**, non più solo la tessera «media» ripetuta: profondità basso/medio/fondo da rumore fisso (seed 12345), tessere blu di Muse (medio-blu e fondo-blu), 2 strati d'onda di Muse + 2 di luce di Claude, chiazze d'olio e di petrolio con 2 fotogrammi e dissolvenza. Il codice è quello di allora (mare a blocchi in cache); una tessera di mare = 256 px PNG. Il centro della piattaforma cade dove partiva la zattera del gioco di prima (mare fondo). Le chiazze, tonde dall'alto, qui sono schiacciate 2:1 (ellissi sul piano isometrico): **da far rifare a Muse in isometrico** insieme a scia e relitti.
- **Camminata (Gruppo iso 4): non piace a Davide, «non muove bene le braccia».** I 6 passi restano montati come provvisori; rifacimento chiesto a Muse con un ciclo vero (contatto → passaggio → contatto opposto → passaggio) e braccia ben leggibili in controfase. Vedi `muse/2026-11-26-gruppo-iso-4-camminata-protagonista/RISPOSTA.md`.
- Controlli: nessun errore; zoom 0,20–0,60 e bottoni provati; 15 ms medi per fotogramma nel simulatore software (prima 14); cambio zoom ricompone i blocchi del mare in un colpo solo (nel simulatore ~0,4 s, sul telefono molto meno).

## 0.2d — 27 nov 2026, notte — PROVA ISOMETRICA: in gioco si legge «v0.2d · prova isometrica · grafica Muse»
- **Camminata vera del protagonista** (Gruppo iso 4 di Muse: 6 fotogrammi × 4 direzioni, tela 70×108, piedi in (35,104), alto 100 px come il fermo). Al posto del rimbalzo provvisorio (`WALK_BOB` tolto). Il passo avanza con la **distanza percorsa sullo schermo** (`CFG.WALK_CYCLE` = 118 px PNG per ciclo completo): i piedi seguono il terreno e a joystick più piano il passo rallenta. Da fermo torna il disegno fermo di Iso 3 (stesso punto-piedi, niente salto).
- **Velocità a piedi 130 → 110 px CSS/s** (`CFG.WALK_SPEED`): con 130 e il ciclo vero i piedi pattinavano. Se la vuole più veloce si alza `WALK_CYCLE` insieme.
- **Controllo della consegna** (31/31 file): tela 70×108 in 24/24, altezza 100 px esatti in 24/24, piedi a y=104 in 24/24, residuo magenta 0, chiusura del ciclo 6→1 coerente con gli altri passaggi. Dettagli in `muse/2026-11-26-gruppo-iso-4-camminata-protagonista/RISPOSTA.md`.
- **Difetto dichiarato (da far rifare):** in tutti i 6 fotogrammi di ogni direzione le gambe restano aperte alla stessa ampiezza (SE 49–55 px, SO 51–53, NE 48–51, NO 41–49 a livello dei piedi) e la gamba davanti è sempre la stessa: non c'è il passo «a gambe unite» (posa di passaggio) né lo scambio della gamba. Cambiano soprattutto le braccia, quindi in movimento il personaggio scivola con le braccia che dondolano. Si rifà con un ciclo vero (contatto → passaggio → contatto opposto → passaggio).
- Nota di Muse accettata: SE e SO sono quasi di profilo (il fermo è tre quarti); da valutare a occhio sul telefono.
- Controlli: nessun errore in console; zattera, Sali/Scendi, joystick tattile come prima; 14,2 ms medi per fotogramma nel simulatore software (come prima).

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
