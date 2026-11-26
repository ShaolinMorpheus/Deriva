# DERIVA — Progetto
Versione documento: **0.1-progetto** (25 nov 2026)
Stato: concept scelto dall'utente — Variante A «Deriva: Waterworld / Mad Max sul mare».
Codice: giocabile **v0.2h** (motore isometrico, menu, salvataggi, APK). Prossimo: mondo da esplorare con piattaforme da saccheggiare (vedi «Visione di gioco»).

## In una frase
Mare infinito senza terraferma. Vivi su una zattera-base, la benzina è il tuo tempo:
esci, saccheggi relitti e avamposti, torni a convertire il bottino in carburante e riparazioni.
Se sprechi benzina, resti alla deriva.

## Pilastri (non si toccano senza ok dell'utente)
1. **Niente terraferma.** Solo mare, atolli poveri, relitti, piattaforme, avamposti su pali.
2. **Scarsità vera.** Piante, acqua e benzina sono rare e valgono una scelta.
3. **La zattera è casa.** È veicolo, deposito e unico posto sicuro. La potenzi a pezzi.
4. **Mondo infinito, leggero.** Si genera da seed mentre navighi; si salva solo ciò che cambi tu.
5. **Tensione senza punizione cieca.** A benzina zero non muori: remi piano (vedi «Anti-blocco»).

## Decisioni dell'utente e correzioni (25 nov 2026)
Decise dall'utente:
- **Vista isometrica 2:1** (25 nov 2026, sera): sostituisce la vista dall'alto per strutture, oggetti e personaggi. Il mare resta fondo continuo. Il resto del documento (generazione, POI, giro benzina) vale ancora; le misure in px e la «vista dall'alto» sono da aggiornare quando c'è il motore iso. Regole di Muse in `muse/ISTRUZIONI.md`.
- **Telefono in orizzontale.** Joystick nel 55% sinistro dello schermo, azioni a destra.
- **Niente contorni scuri** attorno agli oggetti (solo giunture interne scure, es. tra le assi).
- **I relitti si raccolgono dalla zattera** col tasto azione, senza sbarcare. A piedi si scende solo su atollo, avamposto e piattaforma.
- **Prima la grafica:** anteprima di stile di Muse, poi Gruppi 1–3, poi si riprende da v0.1c.

Correzioni tecniche proposte da Claude il 25 nov (non contestate dall'utente):
- POI decisi **per regione 5×5 chunk**, non per chunk: solo così il minimo di 1 è garantito. Ogni POI sta dentro un solo chunk.
- Generazione con **hash a numeri interi** (niente `Math.random`, niente seno): stessa seed = stesso mondo su ogni telefono.
- Numeri di partenza nel blocco `CFG` del codice: velocità 4 tessere/s. Stima: con la densità dei POI scritta sotto esce 1 POI ogni ~1,5–3 min; da misurare in gioco. Consumo di benzina e raggio di vista si fissano in v0.1e.
- **PNG a ~4× la misura in gioco** (tessera 64 px → mare 256 px; zattera 3×2 tessere → 768×512; protagonista 1 tessera → 256×256). **Niente ombre nei PNG**: gli sprite ruotano, le ombre le disegna il gioco.
- Costa degli atolli come sovrapposizioni: lato + angolo esterno + angolo interno (ruotabili). Più la scia della zattera.
- Le varianti a/b di ogni tessera di mare devono potersi affiancare senza giunture; basso/medio/fondo hanno la stessa struttura e cambiano solo colore: le sfumature tra livelli le fa il gioco.
- Salvataggio con numero di versione (gli aggiornamenti arrivano da GitHub Pages e non devono rompere i salvataggi).
- Nei prompt a Muse niente nomi di film: si descrivono solo i materiali.

## Visione di gioco — richieste dell'utente (26 nov 2026, notte)
Dette dall'utente (con il vecchio elenco «fuori dal prototipo» ora entrano tutte, una alla volta):
- **Esplorare il mare** e trovare **piattaforme** con sopra rottami e altro da raccogliere; i rottami **servono a migliorare altro** (zattera/base). Raccogliere anche **taniche di petrolio/benzina**.
- Sulle piattaforme **missioni**: alcune **vuote** (solo da saccheggiare), altre **con nemici**, nello spirito di Waterworld.
- **Fortezze nemiche in ferro arrugginito** e **nemici in stile «smokers»** del film: predoni, **motoscafi** compresi. (Nei prompt a Muse niente nomi di film: si descrivono materiali e forme.)
- **Inizio partita sempre uguale**: introduzione con **dialoghi detti dal personaggio**, poi parte il mondo.
- **Menu** (il ☰ che c'è già) con le **missioni**.
- **Sete e fame.**

### Piano proposto da Claude (NON ancora approvato: l'ordine lo decide l'utente)
Ogni passo si chiude con versione visibile, riga in CHANGELOG e prova sul telefono; la grafica nuova passa da Muse con anteprima e ok prima.
1. **v0.3a Mare da esplorare** — mondo infinito a chunk dalla seed (regola POI per regione 5×5 già scritta sopra), piattaforme e relitti come POI, **rottami e taniche** raccolti col tasto azione, inventario, benzina con HUD e deriva a secco. Il salvataggio (già pronto, versionato) si estende.
2. **v0.3b Piattaforme e missioni** — sbarco sulle piattaforme (tipi: vuota / con scorte / con nemici), primi **nemici a piedi** semplici, missione = obiettivo + ricompensa; scheda **Missioni** nel menu ☰. Rottami → **miglioramenti** della zattera.
3. **v0.3c Inizio partita** — scena fissa all'avvio con **dialoghi** (riquadri di testo, il protagonista parla), saltabile dopo la prima volta; poi parte il mondo. Il sistema di dialogo serve anche per le missioni.
4. **v0.3d Sete e fame** — acqua e cibo (acqua da pozzi/raccolta pioggia, cibo da pesca e scorte: gli oggetti di scena già chiesti a Muse, reti da pesca e raccolta acqua, servono a questo).
5. **v0.3e Predoni** — **motoscafi nemici** in mare (inseguono, speronano), **fortezze di ferro arrugginito** come POI grande con missione.

Attenzione al pilastro 5 («tensione senza punizione cieca»): sete e fame vanno fatte **morbide** (a zero ti indebolisci, rallenti, vedi male, ma puoi recuperare; niente morte improvvisa). Da confermare con l'utente.

Grafica da chiedere a Muse (per gruppi, con le regole iso già in `muse/ISTRUZIONI.md`): piattaforme varie e relitti, rottami e taniche come oggetti raccoglibili, nemici a piedi (4 direzioni, camminata), motoscafi e fortezza, icone di interfaccia (acqua, cibo, rottami, benzina), riquadro dei dialoghi e ritratto. Il Gruppo iso 5 (oggetti di scena) in corso ne copre già una parte.

## Base tecnica (stessa di Sette Mari)
- HTML/JS su canvas, APK Android con Capacitor, pubblicazione GitHub Pages.
- Telefono di prova: Samsung Galaxy S25 Plus.
- Vista dall'alto, a tessere (tile). Niente 3D.
- Versione sempre visibile in gioco (angolo in basso) e CHANGELOG aggiornato a ogni modifica.
- Grafica: PNG di Muse, livelli separati (fondo / oggetti / personaggi / interfaccia).
  Qualità grafica mai ridotta; anteprima e ok dell'utente prima di grandi cambiamenti visivi.

## Come si genera il mondo
- **Tessera:** 64 px in gioco. **Chunk:** 16×16 tessere (1024×1024 px).
- Attivi solo i chunk 3×3 attorno al giocatore; gli altri si scaricano.
- **Rumore deterministico** da seed + coordinate (hash → value noise / simplex):
  stessa seed = stesso mondo, su ogni telefono, senza salvare il mondo.
- Livelli generati, in ordine:
  1. Profondità del mare (3 livelli: basso, medio, fondo) → colore dell'acqua.
  2. Correnti / zone sporche (macchie di petrolio, alghe) → solo visivo nel prototipo.
  3. **Punti di interesse (POI)**, con lancio separato dal rumore (vedi sotto).
- **Salvataggio delta:** si salvano solo seed, stato del giocatore e modifiche
  (es. `chunkX,chunkY:tileX,tileY = raccolto`). Il resto si rigenera identico.

## I POI — 4 tipi nel prototipo
Il rumore da solo ripete; i POI danno il tema. Regola di densità del prototipo:
in ogni area di 5×5 chunk cade **almeno 1 POI** e al massimo 3; il resto è mare vuoto voluto
(il vuoto fa paura e fa valore al POI). Lancio deterministico per regione 5×5 chunk, mai a mano.

| # | Tipo | Cosa trovi | Rischio |
|---|------|-----------|---------|
| 1 | **Relitto galleggiante** | Rottami, 0–1 tanica di benzina | Nessuno. È il pane quotidiano. |
| 2 | **Atollo povero** | Sabbia, 1–2 palme secche/mezza palma viva, pozzo di acqua piovana | Nessuno. Raro: è una festa quando appare. |
| 3 | **Avamposto nemico** | Pontili su pali, baracche di lamiera, deposito di benzina | Nemici semplici che ti vengono incontro quando sbarchi. Bottino migliore del gioco. |
| 4 | **Piattaforma / pompa rotta** | Petrolio grezzo da raffinare in benzina, molti rottami | Rara (1 su ~4 aree). Nel prototipo: solo raccolta lenta, nessun nemico. |

## Risorse — solo 3 nel prototipo
- **Benzina** — muove la zattera. Si trova in taniche o si raffina: 1 petrolio grezzo → 1 benzina, alla zattera, 5 secondi.
- **Rottami** — riparano la zattera e (dopo il prototipo) la potenziano.
- **Acqua** — nel prototipo è solo bottino da pozzi/atolli e punteggio di sopravvivenza; niente sete ancora.
Niente cibo, niente crafting libero nel prototipo: prima si prova il giro benzina↔bottino.

## Giro di gioco (il loop da provare)
1. Parti dalla zattera con benzina contata.
2. Navighi: la benzina cala con la distanza. HUD sempre visibile.
3. Avvisti un POI, attracca, scendi a piedi (joystick), raccogli col pulsante azione.
4. Se è un avamposto, decidi: bottino grosso con nemici, o via col poco dei relitti.
5. Torni alla zattera, raffini/ripari, riparti più lontano.

## Anti-blocco (importante)
A benzina zero la zattera va in **deriva**: puoi remare a velocità ~20% fino al POI
più vicino. Lento e umiliante, mai un vicolo cieco. Niente game over nel prototipo.

## Comandi touch (prototipo)
- Telefono in orizzontale; joystick fluttuante nel 55% sinistro, azioni a destra.
- In mare: joystick sinistro = direzione/velocità della zattera.
- A piedi: stesso joystick = movimento; pulsante destro grande = raccogli / interagisci.
- Attracco automatico quando tocchi il bordo del POI a bassa velocità.

## PIANO PROTOTIPO v0.1 — ordine di costruzione
Obiettivo: rispondere a 3 domande, non «fare il gioco».
1. Navigare 10 minuti è piacevole o ci sono vuoti troppo lunghi?
2. La benzina crea tensione o solo frustrazione?
3. Regge i 60 fps sul Galaxy S25 Plus con chunk 3×3?

Passi (ognuno si chiude con versione visibile in gioco e riga in CHANGELOG):
1. **v0.1a Scheletro** — canvas, joystick, zattera che si muove, versione in schermo.
2. **v0.1b Mare infinito** — chunk 3×3, rumore di profondità, coordinate e seed in debug.
   Seed di prova fissa: `12345` (stesso mondo per tutti i test).
3. **v0.1c POI** — i 4 tipi piazzati dalla regola di densità, disegnati con grafica provvisoria.
4. **v0.1d Attracco e sbarco** — scendi a piedi su atollo e avamposto, raccogli risorse.
5. **v0.1e Giro benzina** — consumo, taniche, raffina petrolio, deriva a secco, HUD.
6. **v0.1f Salvataggio delta** — chiudi e riapri: mondo identico, raccolti restano raccolti.
   Nemico semplice dell'avamposto solo qui, se i passi prima reggono.

**Fuori dal prototipo:** costruzione libera, meteo, notte, missioni/storia, fazioni,
commercio, potenziamenti della zattera, sete/fame, suoni. Entrano uno alla volta dopo il verdetto su v0.1.

## Criteri di riuscita v0.1
- [ ] 10 minuti di navigazione senza mai vedere la fine del mondo né scatti.
- [ ] Almeno 1 POI ogni ~2 minuti di rotta dritta.
- [ ] Una tanica trovata ≈ una gita a un POI vicino e ritorno (bilanciamento da misurare, non da indovinare).
- [ ] Riaprendo l'app: stessa seed, stesse modifiche, benzina e posizione salvate.
