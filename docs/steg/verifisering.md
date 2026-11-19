# Verifisering

Frembringe tilstrekkelig og etterprøvbart bevis for at en leveranse oppfyller krav, tåler relevante feil og kan godkjennes for tilsiktet bruk. KI hjelper med å finne hull, utføre avgrensede tester og forklare resultater; godkjenning bygger på faktiske bevis og ansvarlige fagpersoner.

**Spørsmålet i dette steget:** Har vi tilstrekkelig bevis for riktig og trygg leveranse?

**Typisk overlevering:** Sporbare tester og faglige vurderinger med dokumentert restusikkerhet.

## Plass i læringssløyfen

En idé om å generere eller velge tester er et forslag til kontroll. Godkjenningen må bygge på faktiske testresultater, et egnet testorakel og ansvarlig vurdering. Kvalitet i KI-verifikasjon må selv evalueres, blant annet med kjente feil og relevante moteksempler.

Forrige steg er [Agentutførelse](agentutforelse.md). Neste steg er [Produksjon](produksjon.md). Sløyfen gjentas når erfaringene gir grunnlag for en ny forbedring.

## Finn en idé

De fire temaområdene gir ulike innganger til steget. Velg ideer som treffer prosjektets problem, og tilpass arbeidsform og målinger til risiko og tilgjengelig grunnlag. Hver idé har et eget eksempel, kontrollpunkt og forslag til effektmål.

- [Krav og funksjonell korrekthet](#v-kategori-1)
- [Sikkerhet og robusthet](#v-kategori-2)
- [Spesialiserte leveranser](#v-kategori-3)
- [Verifikasjonsprosess og bevis](#v-kategori-4)

<a id="v-kategori-1"></a>

## Krav og funksjonell korrekthet

Koble krav til faktiske bevis og et klart bilde av korrekt oppførsel. Undersøk grenseverdier, tilstand, kompatibilitet, migrering og regresjoner med relevante testorakler.

- [V01 Spor krav til faktiske testbevis](../ideer/V01.md)
- [V02 Avklar hva som er et korrekt resultat](../ideer/V02.md)
- [V03 Kontroller egenskaper som skal gjelde for mange tilfeller](../ideer/V03.md)
- [V04 Finn manglende grenseverdier og negative forløp](../ideer/V04.md)
- [V05 Undersøk samtidighet og tilstandsavhengige feil](../ideer/V05.md)
- [V06 Kontroller kompatibilitet mellom produsenter og konsumenter](../ideer/V06.md)
- [V07 Sammenlign gammel og ny løsning ved migrering](../ideer/V07.md)
- [V08 Oppdag utilsiktede endringer i brukerforløp](../ideer/V08.md)

<a id="v-kategori-2"></a>

## Sikkerhet og robusthet

Prøv sikkerhetsgrenser og robusthet under representative forhold. Kontroller tilgang, agenthandlinger, avhengigheter, infrastruktur, ytelse, tilgjengelighet og avtalt databehandling.

- [V09 Kontroller autorisasjon på tvers av roller og objekter](../ideer/V09.md)
- [V10 Prøv å bryte agentens instrukser og verktøygrenser](../ideer/V10.md)
- [V11 Vurder avhengigheter og leveransens opprinnelse](../ideer/V11.md)
- [V12 Kontroller konfigurasjon og infrastruktur mot krav](../ideer/V12.md)
- [V13 Undersøk ytelse under representative belastninger](../ideer/V13.md)
- [V14 Verifiser håndtering av feil i avhengigheter](../ideer/V14.md)
- [V15 Vurder tilgjengelighet i reelle oppgaver](../ideer/V15.md)
- [V16 Kontroller at data behandles som avtalt](../ideer/V16.md)

<a id="v-kategori-3"></a>

## Spesialiserte leveranser

Tilpass verifikasjonen til det som faktisk leveres. Data, rapporter, modeller, generative svar, agenter, innebygde systemer, klienter og pakkeløsninger trenger ulike bevis.

- [V17 Verifiser datakvalitet gjennom hele pipelinen](../ideer/V17.md)
- [V18 Kontroller at rapporter uttrykker riktige forretningsbegreper](../ideer/V18.md)
- [V19 Undersøk om en modell er testet på riktig grunnlag](../ideer/V19.md)
- [V20 Test kildegrunnlag og avståelse i generative svar](../ideer/V20.md)
- [V21 Kontroller agentens handlinger gjennom hele oppgaven](../ideer/V21.md)
- [V22 Forbered verifikasjon av innebygde systemer](../ideer/V22.md)
- [V23 Planlegg tester på tvers av klientvarianter](../ideer/V23.md)
- [V24 Verifiser konfigurerte forretningsprosesser](../ideer/V24.md)

<a id="v-kategori-4"></a>

## Verifikasjonsprosess og bevis

Gjør selve kontrollarbeidet mer målrettet og etterprøvbart. Undersøk testenes evne til å finne feil, miljøets representativitet og grunnlaget for faglig godkjenning.

- [V25 Sorter testfeil etter sannsynlig årsak](../ideer/V25.md)
- [V26 Undersøk om testene faktisk oppdager feil](../ideer/V26.md)
- [V27 Gi kodegjennomgang et målrettet beslutningsgrunnlag](../ideer/V27.md)
- [V28 Prioriter testrekkefølge etter endringsrisiko](../ideer/V28.md)
- [V29 Samle etterprøvbart bevis for godkjenning](../ideer/V29.md)
- [V30 Prøv dokumentasjon som en faktisk arbeidsoppgave](../ideer/V30.md)
- [V31 Forbered realistiske tester for brukeraksept](../ideer/V31.md)
- [V32 Vurder om testmiljøet representerer målmiljøet](../ideer/V32.md)

## Bruk steget i prosjektet

Avtal hva som er et korrekt resultat og hvilke uavhengige bevis godkjenningen krever. Mål kontrollarbeidet sammen med feil som oppdages, feil som overses og unødvendige avslag.

- [Finn ideer ut fra prosjektets behov](../veiledning/behov.md).
- [Velg og mål et avgrenset forsøk](../veiledning/effektmaaling.md).
- [Bruk malene for valg og utprøving](../maler.md).
- [Les om arbeidsformer og felles forutsetninger](../veiledning/leserveiledning.md).

[Se alle 256 ideene i registeret](../register.md).

| Forrige steg i læringssløyfen | Neste steg i læringssløyfen |
| --- | --- |
| [Agentutførelse](agentutforelse.md) | [Produksjon](produksjon.md) |
