# KI i SDLC — mulighetskatalog

**256 konkrete ideer for hvordan prosjekter kan bruke KI gjennom hele systemutviklingens læringssløyfe.** Katalogen kobler oppgaver og forventet nytte til nødvendig grunnlag, kontroll og effektmåling.

**[Les katalogen](docs/index.md)** · **[Finn ideer ut fra behov](docs/veiledning/behov.md)** · **[Alle 256 ideene](docs/register.md)**

Problem → Hypotese → Kontekst → Agentutførelse → Verifisering → Produksjon → Observasjon → Læring

## Innhold

| Steg | Ideer | Formål |
| --- | --- | --- |
| [Problem](docs/steg/problem.md) | P01–P32 | Finne et dokumentert problem som er verdt å løse. |
| [Hypotese](docs/steg/hypotese.md) | H01–H32 | Formulere forventet effekt og planlegge et troverdig forsøk. |
| [Kontekst](docs/steg/kontekst.md) | K01–K32 | Gi mennesker og agenter riktig og tilstrekkelig grunnlag. |
| [Agentutførelse](docs/steg/agentutforelse.md) | A01–A32 | Gjennomføre avgrenset arbeid og lage vurderbare leveranser. |
| [Verifisering](docs/steg/verifisering.md) | V01–V32 | Kontrollere korrekthet, kvalitet og risiko med etterprøvbare bevis. |
| [Produksjon](docs/steg/produksjon.md) | R01–R32 | Ta riktig leveranse i bruk med kontroll og beredskap. |
| [Observasjon](docs/steg/observasjon.md) | O01–O32 | Undersøke faktisk nytte, kostnader og uønskede følger. |
| [Læring](docs/steg/laering.md) | L01–L32 | Endre praksis ut fra det prosjektet faktisk har lært. |

Katalogen inneholder også [åtte arbeidsløp](docs/arbeidslop.md), [tilpasning til 16 prosjektprofiler](docs/prosjektprofiler.md), [måleveiledning](docs/veiledning/effektmaaling.md), [maler](docs/maler.md), [begreper](docs/begreper.md) og [kilder](docs/kilder.md).

Innholdet er på norsk bokmål og viderefører den komplette mulighetskatalogen fra 18. november 2026. Hver idé har en egen Markdown-fil og en stabil ID. Markdown-filene i `docs/` er den redigerbare kilden; nettstedet bygges fra de samme filene.

## Rediger innhold

- Endre en idé i `docs/ideer/<ID>.md`. Bevar ID-en når du forbedrer teksten.
- Bevar beskrivelse, grunnlag, forutsetninger, eksempel, kontroll, effektmåling, arbeidsform og prosjektprofiler.
- Oppdater tilhørende stegoversikt og [idéregisteret](docs/register.md) når en tittel eller plassering endres.
- Bruk relative `.md`-lenker, for eksempel `[P01](../ideer/P01.md)`, slik at lenkene fungerer både i GitHub og på nettstedet.
- Bruk eksplisitte, stabile HTML-ankere når du trenger fragmentlenker som skal fungere likt begge steder. Norske overskrifter kan få ulike automatiske ankere.
- Beskriv forventet effekt som en hypotese. Dokumenter lokale målinger og forutsetninger når en idé faktisk er prøvd.

Ved utvidelse med nye ideer må antall og ID-serier oppdateres i katalogoversiktene og i kontrollskriptet. Se også [forvaltning av katalogen](docs/forvaltning.md).

## Forhåndsvis og kontroller lokalt

Bruk Python 3.12 og et virtuelt miljø:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
python scripts/check_catalog.py
python -m mkdocs build --strict
python -m mkdocs serve
```

På Windows aktiveres miljøet med `.venv\Scripts\Activate.ps1` i PowerShell. Åpne adressen som `mkdocs serve` skriver ut, normalt `http://127.0.0.1:8000/ai-sdlc/`.

Kontrollskriptet undersøker katalogens ID-er, obligatoriske idéseksjoner, stegoversikter, register og interne lenker. MkDocs bygger med streng validering. Generert innhold i `site/` og det lokale miljøet skal ikke sjekkes inn.

## Publiser på GitHub Pages

[Dokumentasjonsworkflowen](.github/workflows/docs.yml) kontrollerer og bygger nettstedet på pull requests. Den publiserer bare ved push til `main` eller manuell kjøring fra `main`.

Før første publisering må en administrator gjøre dette én gang:

1. Åpne **Settings → Pages** i dette repoet.
2. Velg **GitHub Actions** under **Build and deployment → Source**.
3. Innlem dokumentasjonsendringen i `main`, eller kjør **Actions → Dokumentasjon → Run workflow** fra `main`.

Etter vellykket publisering er nettstedets adresse **[https://grove.github.io/ai-sdlc/](https://grove.github.io/ai-sdlc/)**. Deployment-jobben viser også den faktiske adressen. Hvis miljøet `github-pages` har godkjenningsregler, gjelder de også for denne workflowen.

Publiseringen bruker GitHubs innebygde token og trenger ingen egne deploy-hemmeligheter. Byggejobben har bare lesetilgang; bare deployment-jobben får rettigheter til Pages og OIDC. Python-avhengigheter er versjonslåst, og Actions er låst til commit-SHA-er. Oppgrader dem i en egen PR med katalogkontroll og nytt strict-bygg.

Oppsettet følger [GitHubs veiledning for egne Pages-workflower](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) og [MkDocs' publiseringsmodell](https://www.mkdocs.org/user-guide/deploying-your-docs/).

## Lisens

[Apache License 2.0](LICENSE).
