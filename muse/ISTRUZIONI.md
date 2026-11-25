# ISTRUZIONI — cartella di scambio con Muse

## REGOLE
- Scrivi solo dentro `muse/`. Il gioco lo integra Claude.
- Una consegna = una sottocartella `AAAA-MM-GG-argomento`. Non sovrascrivere consegne vecchie: le correzioni vanno in una nuova cartella con suffisso `-v2`, `-v3`.
- Ogni consegna ha un `LEGGIMI.md` con: cosa sono i file e dove vanno nel gioco; misure in px, nomi e ordine; cosa NON deve cambiare; cosa è nuovo. Ultima riga `STATO: pronto` (finché lavori: `STATO: in lavorazione`).
- Formato: PNG trasparente per oggetti, PNG opaco per tessere piene. Nomi minuscoli, senza spazi. Se non puoi caricare PNG: `nome.png.b64` (una riga) e `elenco.txt` con l'ordine.
- Gioco: «Deriva», mare infinito post-apocalittico, telefono in orizzontale (schermo 892×412 px, tessera 64 px).
- VISTA (decisione di Davide, 25 nov 2026 sera — sostituisce la vecchia regola «dall'alto pura»): **isometrica 2:1** per strutture, oggetti e personaggi: si vedono il sopra e le due facce sud (sud-est e sud-ovest). Disegni di riferimento approvati: cartella `2026-11-25-piattaforme-isometriche/` (4 varianti di piattaforma). Il mare resta un fondo continuo desaturato (le tessere di mare dei Gruppi 1 e v4 restano valide come fondo); la zattera e gli oggetti dei Gruppi 2–3, disegnati dall'alto, saranno ridisegnati in isometrico nei prossimi gruppi.
- GEOMETRIA ISO (vincolante): tessera a rombo 2:1 — nel PNG canvas 256×256 con rombo dai vertici (128,64) (256,128) (128,192) (0,128), cioè rombo 256×128 centrato; passo di griglia (128, 64) px nel PNG, in gioco tessera 128×64 px con passo (64, 32). Pezzi di faccia e di bordo stanno nello stesso canvas 256×256 della tessera a cui appartengono (facce sotto il rombo, spessore 64 px PNG; bordi/ringhiere sopra i lati nord). Ordine di disegno: per somma (i+j) crescente; facce e oggetti si ancorano al centro del rombo.
- Materiali: lamiera, ruggine, legno bagnato, corde, bidoni. Oggetti originali, niente cose riconoscibili da film o giochi.
- NIENTE contorno scuro attorno agli oggetti: li stacchi dal mare con luce e colore. Le giunture interne (tra assi, lamiere) possono essere marrone molto scuro.
- Oggetti: colori saturi (ruggine, lamiera colorata). Verifica sempre sul fondo vero (mare e sabbia del gioco), mai su fondo neutro.
- Mare: registro acquerello desaturato già approvato per Sette Mari; mai blu saturi lisci; schiuma mai bianco bruciato; mai ovali o cerchi nell'acqua (si leggono come bolle).
- Luce neutra dall'alto. NIENTE ombre proiettate nei PNG: gli sprite li ruota il gioco e le ombre le disegna lui.
- Risoluzione: i PNG sono a 4× la misura in gioco (tessera 64 px → tessera di mare 256 px), per restare nitidi sul telefono.
- Niente scritte nei disegni.
- Gli stati dello stesso oggetto mantengono lo stesso design.
- Claude non ritocca i tuoi disegni: se qualcosa stona, li rifai tu.

## COSA FA CLAUDE
- Legge la consegna, la prova nel gioco e risponde in `muse/<consegna>/RISPOSTA.md`. Dopo l'ok di Davide la rende definitiva.
