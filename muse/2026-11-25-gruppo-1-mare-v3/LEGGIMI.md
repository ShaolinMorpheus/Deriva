# Gruppo 1 — chiazze quasi ferme (v3)

Correzione della consegna `2026-11-25-gruppo-1-mare-v2`, su feedback di Davide provando il gioco (25 nov 2026):
«La chiazza ha troppe animazioni, ne farei meno, più statiche però che diano sempre l'effetto».

## Cosa sono i file
| File | Uso nel gioco | Misura |
|---|---|---|
| `macchia_olio_1.png`, `macchia_olio_2.png` | Variante acqua: SOLO 2 fotogrammi | 512×512 (in gioco 128 px) |
| `macchia_petrolio_1.png`, `macchia_petrolio_2.png` | Variante petrolio: SOLO 2 fotogrammi | 512×512 (in gioco 128 px) |
| `anteprima_chiazza_v3.png` | Le due varianti sul mare vero (fotogramma 1) | 1024×512 |
| `anteprima_chiazza_v3.gif` | L'effetto animato alla velocità consigliata (cambio ogni 1,6 s) | 768×384 |

## Cosa è cambiato rispetto alla v2
- Da 4 fotogrammi a **2 soli** per variante.
- Il fotogramma 1 è l'approvato della v2. Il fotogramma 2 è lo stesso, deformato di pochissimo (onda da 3 px su 512): differenza media misurata ~5,5 su 255 per canale. Alternandoli, la chiazza «respira» appena — non si vede più il vortice che cambia forma.
- Colori invariati dalla v2 approvata.

## Come va animata in gioco (per Claude)
- Alternare i 2 fotogrammi **lenti**: un cambio ogni ~1,5–2 secondi; ancora meglio una dissolvenza incrociata di ~1 secondo tra i due, se il motore la fa senza costi.
- **Deriva: toglierla o ridurla al minimo** (l'oscillazione di pochi px della v1/v2 sommata ai fotogrammi dava l'effetto «troppo animato»). Se resta, che sia lentissima e di 1–2 px.
- Questa cartella sostituisce le chiazze della v2; il resto del Gruppo 1 non cambia.

## Nota di caricamento
Come le altre consegne di Deriva: i PNG salgono come `nome.png.b64` + `elenco.txt`. GIF e MP4 sono solo anteprime per la chat (nella sua app non si animano: l'effetto si verifica in gioco) e restano in locale.

## Verdetto
- Davide, 25 nov 2026: **da caricare** — non è riuscito a vedere l'animazione in chat (GIF e video gli restano fermi), la mostra a Claude e la verifica direttamente in gioco.

STATO: pronto
