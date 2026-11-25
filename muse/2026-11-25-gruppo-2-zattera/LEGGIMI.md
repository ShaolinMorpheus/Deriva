# Gruppo 2 — Zattera e protagonista (Deriva)

## Cosa sono i file
PNG trasparenti, vista dall'alto pura, luce neutra dall'alto, niente ombre proiettate, niente contorno scuro.
Misure PNG = 4× la misura in gioco.

| File | Uso nel gioco | Misura PNG | In gioco |
|---|---|---|---|
| `zattera_base.png` | La zattera-casa del giocatore: assi, bidoni ai lati lunghi, vela ammainata, tenda rattoppata, cassa e taniche sul ponte | 768×512 | 192×128 (3×2 tessere) |
| `zattera_motore.png` | Stessa zattera con motore fuoribordo a poppa (lato corto destro) e serbatoio rosso sul ponte | 768×512 | 192×128 |
| `protagonista_alto.png` | Protagonista a piedi, fermo, dall'alto: berretto rosso sbiadito, giubbotto di salvataggio arancio, zaino | 256×256 | 64×64 (1 tessera) |
| `protagonista_remata.png` | Stesso personaggio in posa remata (modalità deriva a benzina zero): remo lungo tenuto con le due mani, testa in alto come il fermo | 320×256 | 80×64 |
| `anteprima_gruppo2.png` | Anteprima sul mare vero del Gruppo 1: sopra zattera base con protagonista a bordo, sotto variante motore, fermo e remata | 1024×800 | — |

## Dove vanno nel gioco
- La prua è il lato corto SINISTRO; il gioco ruota gli sprite per la direzione di navigazione e disegna lui l'ombra.
- `zattera_motore` sostituisce `zattera_base` quando il giocatore monta il motore: non vanno mai disegnate insieme.
- `protagonista_remata` si disegna sopra la zattera (al posto del fermo) solo in modalità deriva.

## Cosa NON deve cambiare
- Stesso design tra base e motore (scafo, bidoni, tenda, albero) e tra fermo e remata (berretto rosso, giubbotto arancio, zaino).
- Niente scritte, niente ombre nei PNG, niente contorno scuro attorno agli oggetti.

## Verifiche fatte (controllo dichiarato)
- Scontorno da fondo magenta a programma; margini del contenuto: base ≥12 px, motore ≥16 px, fermo ≥10 px, remata ≥10 px.
- Anteprima composta sul mare vero (tessere Gruppo 1) e vista ingrandita.
- Limiti dichiarati: (1) la variante motore è scalata ~7% più piccola della base per far stare il motore nella tela — scafo non perfettamente sovrapponibile pixel a pixel; (2) nella variante motore la rigenerazione ha spostato leggermente cassa e taniche sul ponte (lo scafo è invariato). Se serve la sovrapponibilità esatta, si rifà in una cartella `-v2`.

## Cosa è nuovo
- Primi oggetti di gioco di Deriva: la casa del giocatore e il personaggio, nella palette approvata con la prova di stile.

## Cosa manca ancora (Gruppo 2)
- Stati di danno della zattera (intera / danneggiata / quasi affondata): servono quando il combattimento esiste, non nel prototipo v0.1.
- Camminata del protagonista (4 direzioni): il prototipo usa il fermo ruotato; i passi si fanno dopo il verdetto su v0.1.

## Verdetto
- Davide, 25 nov 2026: **Gruppo 2 approvato** («Sì, Gruppo 2 va bene — avanti col Gruppo 3»), limiti dichiarati accettati.

## Nota di caricamento (25 nov 2026)
I PNG di questa consegna sono saliti su GitHub come `nome.png.b64` (base64, una riga) con `elenco.txt` che dà l'ordine: l'invio diretto dei PNG non è passato. Per usarli: decodificare ogni `.b64` nel `nome.png` corrispondente. Contenuto identico ai PNG originali (verifica per hash fatta da Muse dopo l'invio).

STATO: pronto
