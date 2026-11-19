# Velg og mål et avgrenset forsøk

<a id="avsnitt-avklar-hvorfor-akkurat-denne-ideen-bor-proves"></a>

## Avklar hvorfor akkurat denne ideen bør prøves

Beskriv først problemet med et eksempel fra eget prosjekt. Velg deretter en idé som påvirker dette problemet, og avklar hva som blir enklere, raskere eller riktigere. Dersom en enkel regel, et skript eller tydeligere ansvar løser problemet bedre, er det et relevant alternativ å sammenligne med.

| **Vurdering** | **Spørsmål prosjektet må svare på** |
| --- | --- |
| Verdi | Hvem får et bedre utfall, og hvor stort er problemet i dag? |
| Volum og variasjon | Gjentar oppgaven seg ofte nok, og er tilfellene sammenlignbare? |
| Kontekst | Finnes autoritative krav, data og eksempler som teamet har lov til å bruke? |
| Verifisering | Hvordan kan en annen person eller et kontrollert verktøy avgjøre om resultatet er riktig? |
| Risiko | Hva er konsekvensen av et feilaktig svar eller en uventet handling, og kan skaden begrenses? |
| Innsats | Hva koster oppsett, integrasjon, opplæring, kontroll og vedlikehold? |
| Måling | Har vi baseline, datakvalitet og et troverdig sammenligningsgrunnlag? |
| Eierskap | Hvem godkjenner resultatet, følger målingen og endrer praksis etter forsøket? |

Vurder kriteriene med konkrete begrunnelser. Unngå en samlet skår som skjuler at et kritisk krav ikke er oppfylt. Et forsøk bør ha én tydelig primæreffekt, noen få kvalitets- eller risikogrenser og en dato for beslutning.

<a id="avsnitt-mal-bade-den-lokale-oppgaven-og-leveransens-utfall"></a>

## Mål både den lokale oppgaven og leveransens utfall

Måleforslaget i hver idé er et utgangspunkt. Definer teller, nevner, enhet, tidsvindu, start og slutt, datakilde og eier før forsøket. Skill aktiv arbeidstid fra kalender- og ventetid. Tell også forkastede forsøk, kontrollarbeid, avbrudd og feilretting.

For ideer som hjelper analyse eller beslutninger, som [P01](../ideer/P01.md), [P31](../ideer/P31.md) og [H01](../ideer/H01.md), er kortere analysetid et lokalt mål. Følg også om beslutningen senere ga relevant arbeid, færre omkamper eller bedre brukerutfall. Et raskt, feilaktig beslutningsgrunnlag er ingen forbedring.

SPACE beskriver utviklerproduktivitet som flerdimensjonal. Derfor bør teamet se på oppgaveutfall sammen med kvalitet, samarbeid, flyt og arbeidsopplevelse. Bruk team- og oppgavenivå med tydelig formål; antall prompt, kodeforslag eller linjer kode er diagnostikk og gir ikke alene bevis på verdi. [2](../kilder.md#kilde-2)

| **Dimensjon** | **Eksempler på effektmål** | **Et balanserende mål** |
| --- | --- | --- |
| Tid | Aktiv innsats og tid fra klar oppgave til akseptert bruk. | Omarbeiding og feil etter aksept. |
| Kapasitet | Aksepterte sammenlignbare leveranser per periode. | Oppgavemiks, kvalitet og alder på uferdig arbeid. |
| Kostnad | Total kostnad per akseptert oppgave eller nyttig transaksjon. | Vedlikehold, kontroll og etterfølgende driftskostnad. |
| Kvalitet | Korrekt oppgaveløsning og feil med kjent alvorlighet. | Feil som kontrollen overser og unødvendige avslag. |
| Brukerverdi | Fullført brukeroppgave, korrekt beslutning eller redusert saksarbeid. | Tilgjengelighet, støttebehov og negative følger. |
| Mennesker | Opplevd friksjon, forståelse og nødvendig kontrollarbeid. | Trygghet, læring og representativitet i svarene. |

<a id="avsnitt-bruk-leveransemal-der-de-passer"></a>

## Bruk leveransemål der de passer

For en tjeneste eller applikasjon med produksjonsutrulling beskriver DORA fem mål: endringsledetid, utrullingsfrekvens, tid til gjenoppretting etter mislykket utrulling, endringsfeilrate og andel utrullinger som er uplanlagt arbeid etter produksjonshendelser. Bruk dem i tjenestens kontekst og sammen med produktutfall. For dokumenter og formelle beslutninger bruker teamet tilsvarende lokale aksept- og kvalitetsmål, uten å omtale dem som DORA. [1](../kilder.md#kilde-1)

<a id="avsnitt-gjor-sammenligningen-troverdig"></a>

## Gjør sammenligningen troverdig

Registrer hypotese og analyseplan før resultatene kommer. Når praktisk, bruk tilfeldig tildeling av sammenlignbare oppgaver eller en kontrollert trinnvis innføring. Sammenligning før og etter kan gi nyttig læring, men bemanning, oppgavemiks, sesong, opplæring og andre tiltak kan forklare endringen. Vis observasjonsantall, variasjon, datamangler og usikkerhet. Definer senere oppfølging når feil eller verdi viser seg langsomt.

KI kan klargjøre analyse og kode, men utfall og intervaller må beregnes fra faktiske data i etterprøvbare verktøy. En språklig plausibel forklaring er ikke et effektbevis. Bruk analysekompetanse når forsøket krever statistisk metode, og fortsett måling når datagrunnlaget ikke er tilstrekkelig.

<a id="avsnitt-regn-pa-netto-ressursbruk"></a>

## Regn på netto ressursbruk

Netto frigjort arbeidstid er spart innsats minus ny innsats til kontekst, agentoppfølging, kontroll, feilretting og drift. Total kostnad omfatter også lisenser, modellbruk, infrastruktur, integrasjon, opplæring og vedlikehold. Oppgi periode og fordelingsantakelser. Samme innsats skal bare telles én gang.

Illustrasjon: Hvis sammenlignbare oppgaver bruker 40 færre timer, men forsøket krever 9 timer ekstra kontroll, 5 timer kontekstvedlikehold og 4 timer feilretting, er netto frigjort kapasitet 22 timer. Modell- og lisenskostnader kommer i tillegg i kroner. Tallene illustrerer regnemåten og er ingen forventet gevinst. Kontantbesparelse krever faktisk redusert utgift; frigjorte timer kan også gi verdi gjennom annet prioritert arbeid.

<a id="avsnitt-ta-en-eksplisitt-beslutning"></a>

## Ta en eksplisitt beslutning

| **Det dere observerer** | **Anbefalt neste handling** |
| --- | --- |
| Positiv effekt med tilstrekkelig grunnlag og oppfylte grenser | Utvid til neste avgrensede oppgavegruppe og følg varigheten. |
| Lovende effekt men usikkert grunnlag | Fortsett måling eller forbedre forsøksdesignet før skalering. |
| Liten eller negativ nettoeffekt | Juster avgrensningen, prøv et enklere alternativ eller avslutt. |
| Brudd på kritisk kvalitet, tilgang eller sikkerhet | Stans berørt bruk, håndter avvik og revurder utforming. |
| Manglende data eller uklart utfall | Forbedre målegrunnlaget og la gevinsten stå som uavklart. |

[Til katalogens start](../index.md) · [Alle ideene](../register.md)
