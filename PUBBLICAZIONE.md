# Come si pubblica Deriva e si crea l'APK

Tutto parte da **un solo file di istruzioni** (`deriva.yml`) e da **un solo zip** che prepara Claude.
Claude non può scrivere sul repo: lo zip si carica a mano da telefono, il resto lo fa GitHub.

## Una volta sola
1. **Pagine:** repo → Settings → Pages → *Build and deployment* → Source: **GitHub Actions**.
2. **Istruzioni:** apri `https://github.com/ShaolinMorpheus/Deriva/upload/main/.github/workflows`
   (Chrome, «Sito desktop» attivo), scegli `deriva.yml`, **Commit changes**.
3. **Zip:** apri `https://github.com/ShaolinMorpheus/Deriva/upload/main`, scegli lo zip, **Commit changes**.
   (Lo zip va nella cartella principale, non dentro altre cartelle.)

Parte da solo (scheda **Actions**, «Deriva — pubblica il gioco e crea l'APK»): scompatta lo zip nel repo,
pubblica il gioco e, se nello zip c'è `.ricompila-apk`, crea l'APK (10-15 minuti).

## Scaricare l'APK
Repo → **Releases** → «apk-ultimo» → `Deriva.apk`. In alternativa: Actions → l'esecuzione → Artifacts → `deriva-apk` (uno zip con dentro l'APK).
Sul telefono: permetti l'installazione da questa fonte. L'app si chiama «Deriva» e non tocca Sette Mari.

## Aggiornamenti
- **Gioco:** nuovo zip caricato come al punto 3. Non serve rifare l'APK: l'app carica il gioco da Pages e mostra
  «Nuova versione: tocca per aggiornare» (salva e ricarica).
- **APK nuovo** (solo se cambia l'app: icona, orientamento, permessi): Claude mette `.ricompila-apk` nello zip,
  oppure Actions → Run workflow (con «Crea anche l'APK» acceso).

## Se qualcosa non va
- «Pages non attivo / deploy fallito»: manca il punto 1.
- Il passaggio «Salva» non riesce a scrivere: Settings → Actions → General → Workflow permissions → *Read and write*.
- Mandami lo screenshot dell'errore.
