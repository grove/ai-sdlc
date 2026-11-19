# Slik bruker prosjektet katalogen

Katalogen er laget for oppslag og utvelgelse. De 256 ideene er fordelt på 32 temaområder, med 32 ideer i hvert steg. Et prosjekt trenger vanligvis bare et lite utvalg om gangen. Mer KI-bruk er i seg selv ingen gevinst; tiltaket må forbedre en viktig oppgave eller et dokumentert problem i prosjektets samlede leveranseflyt.

<a id="avsnitt-tre-praktiske-leseveier"></a>

## Tre praktiske leseveier

| **Når prosjektet trenger** | **Begynn her** |
| --- | --- |
| Oversikt over mulighetene | Les de åtte fasenes formål og temaområder. Bruk [idéregisteret](../register.md) for å finne enkelttema. |
| Tiltak mot en kjent flaskehals | Bruk [behovstabellen](behov.md). Les de foreslåtte ideene og velg ett forsøk med [Velg og mål et avgrenset forsøk](effektmaaling.md). |
| En sammenhengende arbeidsmåte | Bruk [arbeidsløpene](../arbeidslop.md) og [tilpasningene til ulike prosjektprofiler](../prosjektprofiler.md). Konkretiser forsøket med [malene](../maler.md). |

<a id="avsnitt-slik-leses-en-id"></a>

## Slik leses en idé

Identifikatoren er en stabil henvisning som kan brukes i sakssystem og eksperimentregister. P betyr Problem, H Hypotese, K Kontekst, A Agentutførelse, V Verifisering, R Produksjon, O Observasjon og L Læring. R brukes for produksjonssteget for å skille det fra Problem.

| **Felt** | **Hva feltet hjelper teamet å avklare** |
| --- | --- |
| Muligheten | Oppgaven KI støtter og hvordan bidraget kan forbedre arbeidet. |
| Grunnlag | Data, kilder, krav og eksempler som trengs for oppgaven. |
| Forutsetninger | Tilgang, kompetanse og eksisterende arbeidsmekanismer som må være på plass. |
| Eksempel og leveranse | Et konkret anvendelsestilfelle og et vurderbart resultat. |
| Kontroll | Den viktigste spesifikke kvalitets- eller risikokontrollen og menneskelig beslutningsansvar. |
| Mål effekt | Et målbart utfall og balanserende mål som kan avsløre uønskede følger. |
| Arbeidsform og særlig relevant for | Veiledende form på KI-bidraget og eksempler på prosjektprofiler. Andre profiler kan også bruke ideen. |
| Bruk ideen i prosjektet | Hvordan ideen inngår i læringssløyfen, med lenker til måling, maler og neste idé. |

<a id="avsnitt-arbeidsform-sier-hva-ki-gjor"></a>

## Arbeidsform sier hva KI gjør

Rådgivning betyr at KI analyserer eller forklarer. Utforming betyr at KI lager et forslag, dokument, plan, kode eller annet artefakt som skal vurderes. Avgrenset utførelse betyr at KI bruker tillatte verktøy for å utføre en oppgave innen et eksplisitt mandat. Arbeidsformen er et forslag, ikke en fullmakt eller modenhetsvurdering.

<a id="avsnitt-katalogen-skiller-mellom-mulighet-og-dokumentert-effekt"></a>

## Katalogen skiller mellom mulighet og dokumentert effekt

Oppføringene er forslag til lokale utprøvinger. Effekten avhenger blant annet av oppgavetype, modell, verktøy, kontekst, kontroll og teamets arbeidsflyt. En løsning kan kreve samspill mellom språkmodell, søk, analyseverktøy, kompilator, testverktøy og mennesker. Beregninger, kontroller og kjøreresultater må komme fra etterprøvbare verktøy og kilder.

Katalogen er åpen for nye varianter. Bruk [Hold katalogen relevant](../forvaltning.md) til å utvide den med erfaringer, og merk hvilke ideer som er uprøvd, prøves, har dokumentert nytte eller er frarådet i en bestemt kontekst.

<a id="avsnitt-liknende-temaer-har-ulike-oppgaver-i-sloyfen"></a>

## Liknende temaer har ulike oppgaver i sløyfen

Problem bruker eksisterende erfaringer til å finne neste utfordring. Observasjon vurderer en bestemt levert endring. Hypotese designer et forsøk; de øvrige stegene gjennomfører og evaluerer det. Eksempelvis gjelder [H21](../ideer/H21.md) til [H24](../ideer/H24.md) forsøk med autonomi, oppdeling, kontekst og kontroll, mens [Kontekst](../steg/kontekst.md), [Agentutførelse](../steg/agentutforelse.md) og [Verifisering](../steg/verifisering.md) beskriver det praktiske arbeidet.

[V29](../ideer/V29.md) samler test- og verifikasjonsbevis. [R01](../ideer/R01.md) vurderer operativ beredskap, [R07](../ideer/R07.md) kontrollerer nødvendig autorisasjon og [R08](../ideer/R08.md) kontrollerer at riktig artefakt blir levert. [O32](../ideer/O32.md) samler analysegrunnlaget; [L01](../ideer/L01.md) fastsetter læringskonklusjonen og videre handling.

<a id="avsnitt-felles-forutsetninger-for-alle-ideene"></a>

## Felles forutsetninger for alle ideene

- Bruk godkjente modeller og tjenester med lovlig databehandling, nødvendige rettigheter og minst mulig sensitivt innhold.

- Avtal oppgave, kilder, verktøy, filområder, kostnadsramme, stoppsignaler og hvem som tar over ved uklarhet.

- Behandle kode, dokumenter, nettsider og logger som mulige feilkilder. Instruksjoner i slike kilder kan ikke gi agenten nye fullmakter.

- La tekniske mekanismer håndheve tilgang og grenser. En språkmodell kan ikke alene være sikkerhetssperre for sine egne handlinger.

- Verifiser påstander og artefakter uavhengig av agentens selvtillit. En kontrollagent kan dele samme feilantakelser og er et supplement til faktiske bevis.

- La produksjon, publisering, kommunikasjon til andre, irreversible endringer og tilgangsøkning følge eksplisitt mandat og prosjektets godkjenningsregler.

Disse lokale kontrollprinsippene bygger på risikobasert utvikling og kjente utfordringer ved generativ KI. NIST beskriver sikker utvikling som praksis som kan innarbeides i ulike SDLC-modeller. NISTs GenAI-profil og OWASP beskriver forhold som må håndteres i KI-systemer, blant annet feilaktige utdata, sensitiv informasjon og for vid handlekraft. [3](../kilder.md#kilde-3) · [4](../kilder.md#kilde-4) · [5](../kilder.md#kilde-5)

[Til katalogens start](../index.md) · [Alle ideene](../register.md)
