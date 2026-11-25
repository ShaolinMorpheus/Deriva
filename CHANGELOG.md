# DERIVA — CHANGELOG
Ogni modifica al gioco o al progetto aggiunge una riga qui, con la versione
che l'utente vede in gioco. Versioni: `0.x` = progetto/prototipo, `1.0` = prima pubblicabile.

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
