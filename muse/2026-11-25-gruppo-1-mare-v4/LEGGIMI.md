# Gruppo 1 — movimento e profondità (v4)

Consegna aggiuntiva sul mare, dalle richieste di Claude nella RISPOSTA alla v3 (riferite da Davide il 25 nov 2026). Registro: desaturato acquerello approvato, come tutto il Gruppo 1.

## Cosa sono i file
| File | Uso nel gioco | Misura |
|---|---|---|
| `onde_overlay.png` | Overlay di movimento: creste e riflessi chiari desaturati + zone appena più scure, da far scorrere piano in due strati sopra il mare | 1024×1024 trasparente (= 4×4 tessere) |
| `mare_medio_blu.png` | Variante profondità del medio, tendente al blu-acciaio | 256×256 opaca |
| `mare_fondo_blu.png` | Variante profondità del fondo, tendente al blu-acciaio | 256×256 opaca |
| `mare_basso_b.png` | Variante b del basso (spezza la ripetizione) | 256×256 opaca |
| `mare_medio_b.png` | Variante b del medio | 256×256 opaca |
| `mare_fondo_b.png` | Variante b del fondo | 256×256 opaca |
| `anteprima_onde_v4.png` | A sinistra il mare solo, a destra con l'overlay in due strati sfasati (come in gioco) | 1024×512 |
| `anteprima_profondita_v4.png` | Sopra medio a | blu, sotto fondo a | blu | 1024×512 |
| `anteprima_varianti_b_v4.png` | Le tre varianti b affiancate (basso, medio, fondo) | 1536×512 |

## Come sono fatti (dichiarato)
- **Overlay**: generato a programma con rumore periodico allungato in orizzontale (creste, non ovali) + dettaglio fine. Copertura misurata con alpha > 10: **33,5%** (chiesto 25–35%). Colore creste RGB (199, 217, 219) con alpha massimo ~138: chiaro desaturato, mai bianco bruciato. Zone scure RGB (86, 106, 112), alpha massimo ~62. Tileabile per costruzione (funzioni periodiche sulla tela; salto medio alpha ai bordi ~1,3 su 255).
- **Profondità**: stessa trama delle tessere attuali, cambiato solo il colore: mescola verso RGB (56, 98, 142) — il riferimento che il gioco usa già — al 35% per il medio e al 40% per il fondo. Colori medi risultanti: medio (129,150,153) → (103,132,149); fondo (81,99,100) → (71,99,117). Blu-acciaio spento, trama acquerello intatta, tileabilità invariata. Se serve una spinta in più, si può salire di percentuale senza rifare la trama.
- **Varianti b**: remix a programma della rispettiva tessera a (specchio orizzontale + spostamento toroidale 128/37 px, mescola 55/45). Stessa palette e stessa trama statistica, disegno diverso; tileabili per costruzione (operazioni toroidali su tessere già tileabili). Non sono disegni nuovi: servono solo a spezzare la ripetizione.

## Uso in gioco (per Claude)
- Overlay in due strati che scorrono piano in direzioni/velocità leggermente diverse; movimento lento e continuo, mai a scatti. L'overlay non ha ombre e non deve essere ruotato a scatti di 90°: se serve varietà, il secondo strato può essere specchiato.
- Le varianti blu si mescolano alle a nelle zone profonde (o sostituiscono medio/fondo dove il gioco oggi applica la tinta blu al 40%).
- Le b si alternano alle a con la stessa scelta deterministica dalle coordinate già usata per le profondità.

## Nota di caricamento
Come le altre consegne di Deriva: i PNG salgono come `nome.png.b64` + `elenco.txt`.

## Verdetto
- Davide, 25 nov 2026: **scrittura su GitHub riautorizzata, v4 da caricare** («Autorizzo: carica la v4»).

STATO: pronto
