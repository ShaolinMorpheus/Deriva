# RISPOSTA di Claude — Gruppo 2 (zattera) e Gruppo 1 (mare) montati nel gioco

Gioco: **v0.1b.2 · «grafica Muse»** (paesaggio, 892×412 px, tessera 64 px).
Sul prompt `PROMPT_PER_CLAUDE_v0.1a.md`: chiedeva lo scheletro «da zero». Il gioco esisteva già (v0.1b.1, mare infinito a chunk con grafica provvisoria), quindi ho **montato la tua grafica su quel codice** invece di rifare tutto. Stesse regole: orizzontale, joystick a sinistra, versione sempre visibile in basso al centro.

## Cosa è montato e come
| File | Dove | Come lo uso |
|---|---|---|
| `mare_basso_a`, `mare_medio_a`, `mare_fondo_a` | `www/assets/mare/` | Una tessera 256 px disegnata a 64 px (4×). Il livello di profondità viene dal rumore del mondo. Tra un livello e l'altro **sfumo in modo continuo** (maschere sfumate allineate al mondo): niente bordo a scalini tra tessere. |
| `zattera_base` | `www/assets/zattera/` | 768×512 disegnata a 192×128. **Prua = lato corto SINISTRO** (come scritto da te): il gioco la ruota di rotta+180°. Ombra e scia le disegna il gioco, la luce arriva da sinistra in alto. |
| `macchia_olio_1…4` | `www/assets/olio/` | 512 px disegnati a 128 px. 4 fotogrammi a ~2/s con dissolvenza, deriva lenta di pochi px. Nel chunk di partenza ce n'è una vicino alla zattera; negli altri ~12%. |

I PNG sono decodificati dai tuoi `.png.b64` (controllo firma PNG, misure e canale alfa: tutti corretti).

## Cosa NON ho montato (ancora)
- `zattera_motore`: lo scafo è scalato ~7% più piccolo e cassa/taniche sono spostate (lo dichiari tu): non si può sostituire alla base senza che lo scafo «salti». Serve la versione `-v2` sovrapponibile (vedi sotto) prima del motore in gioco.
- `protagonista_alto`/`protagonista_remata`: arrivano con lo sbarco (v0.1d) e la modalità deriva (v0.1e).
- `mare_macchia_petrolio` e tutto il Gruppo 3 (relitti): arrivano con i punti di interesse (v0.1c).

## Difetti che vedo nel gioco (per te: li rifai tu, io non ritocco)
1. **Ripetizione visibile.** C'è una sola tessera per livello: in mare basso e fondo si leggono i «ciuffi» che tornano ogni 64 px, a griglia. Il medio regge meglio.
   → Chiedo **varianti `b` e `c`** di basso/medio/fondo (stessa struttura, particolari diversi), oppure **tessere grandi 1024×1024** (16×16 tessere) tileabili: ripetono ogni 256 px in gioco invece di 64.
2. **I tre livelli hanno strutture diverse** (il medio ha onde allungate, il basso ha ciuffi tondeggianti, il fondo ha un altro ritmo). Nella sfumatura si nota il cambio di «tessitura», non solo di colore.
   → Stessa trama di base nei tre livelli, cambiano solo luminosità, colore e quantità di sabbia/profondità.
3. **Mancano** `riva_sabbia_bordo` (costa a **3 pezzi**: lato dritto + angolo esterno + angolo interno, tileabili, con sabbia che sfuma nel mare), `sabbia_atollo_a/b` e una **scia** della zattera (per ora la disegno in codice: due righe bianche sottili).
4. **Zattera motore -v2:** stesso scafo, stessa scala e stessa posizione di cassa/taniche della base; cambia solo il motore a poppa (lato corto destro) e il serbatoio.
5. (Facoltativo) **Icona dell'app** 512×512, quadrata, senza trasparenza: zattera vista dall'alto sul mare + niente scritte. Per ora l'APK usa l'icona standard di Capacitor.

## Cosa NON cambiare
Palette e registro approvati (mare desaturato, ruggine/lamiera/legno bagnato), niente contorni scuri, niente ombre nei PNG, niente scritte.

STATO: risposta pronta — attendo `-v2` (varianti mare, costa, zattera motore)
