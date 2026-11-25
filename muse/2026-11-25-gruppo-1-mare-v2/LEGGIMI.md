# Gruppo 1 — correzione chiazze d'olio (v2)

Correzione della consegna `2026-11-25-gruppo-1-mare`, su feedback di Davide (25 nov 2026):
«Le macchie di olio rispetto allo sfondo sono troppo di un colore distaccato, dovremmo farle più omogenee allo sfondo dell'acqua».

## Cosa sono i file
Solo i 4 fotogrammi della chiazza, corretti. Tutto il resto del Gruppo 1 resta quello della cartella originale.

| File | Uso nel gioco | Misura |
|---|---|---|
| `macchia_olio_1.png` … `macchia_olio_4.png` | Chiazza d'olio tonda che galleggia e si muove nella zona (stesso uso e stesso movimento della v1: ciclo ~2 fps + deriva) | 512×512 (in gioco 128 px) |
| `macchia_petrolio_1.png` … `macchia_petrolio_4.png` | **Variante B «petrolio»** (chiesta da Davide il 25 nov): i colori dell'olio (viola, verde, bronzo) restano ma spenti e intonati al mare — saturazione ×0,34, mescola col mare 38%, contrasto 0,78, alpha ×0,86. Stesso uso e movimento della variante acqua. Uso suggerito: zone di petrolio vero (piattaforme, relitti che perdono); la variante acqua per le zone leggere | 512×512 (in gioco 128 px) |
| `anteprima_chiazza_p6.png` | Confronto sul mare vero: a sinistra la variante acqua (p5), a destra e sotto la variante petrolio | 1024×768 |
| `anteprima_chiazza_p5.png` | Confronto sul mare vero: in alto a sinistra il quarto passaggio, a destra il quinto (un pelo più visibile); sotto i 4 fotogrammi del quinto passaggio. Nome nuovo a ogni passaggio: riusare lo stesso nome fa vedere in chat l'anteprima vecchia in cache | 1024×768 |
| `anteprima_macchia_olio_v2.png` | Anteprima dei passaggi precedenti (storico, non usare) | 1024×768 |

## Cosa è cambiato rispetto alla v1
Cinque passaggi (Davide: 1 «ancora troppo staccata», 2 «troppo poco», 3 «a metà», poi la richiesta precisa «che si sfuma con il colore dell'acqua» e sul 4 «un pelo che si vede di più»). I file qui dentro sono il **quinto passaggio**, metodo del quarto spinto un pelo:
- Il **colore della chiazza è quello dell'acqua**: preso il colore medio di `mare_medio` e modulato solo in luminosità dal disegno dei vortici della v1 (fattore 0,74 + 0,26 per il rapporto con la media), appena più scuro (×0,95).
- Della v1 resta solo il disegno: i vortici si vedono come variazioni di luce sulla stessa acqua, non come un altro colore. Cromia originale residua: 16%, come accenno di riflesso oleoso.
- Alpha ×0,92 e bordi sfumati: la chiazza si sfuma nello sfondo e si riconosce dalla superficie più liscia e dai vortici.
- Forma, dimensione e ordine dei fotogrammi invariati: per Claude è una sostituzione secca dei 4 file.

## Cosa NON deve cambiare
- La chiazza si deve comunque riconoscere: tonda, più scura dell'acqua, con i vortici del grezzo. Se diventa invisibile, abbiamo corretto troppo.

## Verifiche fatte
- Stessa trasformazione applicata ai 4 fotogrammi (saturazione media misurata: da ~0,13 a ~0,04 in tutti e 4).
- Anteprima composta sul mare vero del Gruppo 1 e vista ingrandita: confronto v1/v2 nella stessa immagine.

## Nota di caricamento
Come le altre consegne di Deriva: i PNG salgono come `nome.png.b64` + `elenco.txt`. Questa cartella SOSTITUISCE i `macchia_olio_*.png` della cartella Gruppo 1 (che restano come storico) e AGGIUNGE la variante `macchia_petrolio_*`.

## Verdetto
- Davide, 25 nov 2026: **entrambe le varianti approvate** («Entrambe bene — carica la v2»).

STATO: pronto
