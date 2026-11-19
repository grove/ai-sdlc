# Produksjon

Gjøre en verifisert leveranse tilgjengelig for avtalt bruk med kontrollert aktivering, operativ beredskap og tydelig mottak. Produksjon kan være en kjørende tjeneste, distribuert pakke, et dataprodukt eller en godkjent beslutning som faktisk tas i bruk. KI støtter koordinering og gjennomføring innen eksplisitt mandat.

**Spørsmålet i dette steget:** Kan leveransen tas i bruk under kontroll?

**Typisk overlevering:** Riktig godkjent versjon i tilsiktet bruk, med eier, observasjon og plan for feil.

## Plass i læringssløyfen

Produksjon omfatter tilsiktet bruk også uten kjørende tjeneste: en publisert pakke, et dataprodukt, en sertifisert leveranse eller en godkjent beslutning som mottakeren faktisk bruker. Angi lokal definisjon før arbeidet starter.

Forrige steg er [Verifisering](verifisering.md). Neste steg er [Observasjon](observasjon.md). Sløyfen gjentas når erfaringene gir grunnlag for en ny forbedring.

## Finn en idé

De fire temaområdene gir ulike innganger til steget. Velg ideer som treffer prosjektets problem, og tilpass arbeidsform og målinger til risiko og tilgjengelig grunnlag. Hver idé har et eget eksempel, kontrollpunkt og forslag til effektmål.

- [Klargjøring og releasebeslutning](#r-kategori-1)
- [Utrulling og aktivering](#r-kategori-2)
- [Driftsberedskap og mottak](#r-kategori-3)
- [Kontrollert feilhåndtering og avslutning](#r-kategori-4)

<a id="r-kategori-1"></a>

## Klargjøring og releasebeslutning

Klargjør en konkret releasebeslutning med riktige eiere, godkjenninger og artefakter. Ta hensyn til berørte mottakere, avhengigheter, vinduer og en egnet utrullingsform.

- [R01 Lag et samlet grunnlag for releasebeslutningen](../ideer/R01.md)
- [R02 Synliggjør hvilke tjenester og brukere som berøres](../ideer/R02.md)
- [R03 Skriv releaseinformasjon for ulike mottakere](../ideer/R03.md)
- [R04 Planlegg rekkefølgen mellom avhengige leveranser](../ideer/R04.md)
- [R05 Foreslå gjennomførbare releasevinduer](../ideer/R05.md)
- [R06 Velg utrullingsform ut fra endringens egenskaper](../ideer/R06.md)
- [R07 Kontroller at riktig godkjenning følger riktig leveranse](../ideer/R07.md)
- [R08 Bekreft at det verifiserte artefaktet er det som leveres](../ideer/R08.md)

<a id="r-kategori-2"></a>

## Utrulling og aktivering

Planlegg og gjennomfør kontrollert overgang til den nye løsningen. Ideene dekker gradvis aktivering, databaser, plattformer, grensesnitt, klienter, firmware og konfigurasjon.

- [R09 Støtt kontrollert gradvis utrulling](../ideer/R09.md)
- [R10 Styr aktivering og livsløp for funksjonsflagg](../ideer/R10.md)
- [R11 Planlegg databaseendringer som tåler overgangsperioden](../ideer/R11.md)
- [R12 Koordiner bytte til ny datakilde eller plattform](../ideer/R12.md)
- [R13 Koordiner publisering av grensesnitt og konsumentovergang](../ideer/R13.md)
- [R14 Klargjør distribusjon gjennom app- og klientkanaler](../ideer/R14.md)
- [R15 Planlegg firmwareutrulling etter enhetsgrupper](../ideer/R15.md)
- [R16 Overfør godkjent konfigurasjon mellom miljøer](../ideer/R16.md)

<a id="r-kategori-3"></a>

## Driftsberedskap og mottak

Gjør leveransen mulig å bruke og forvalte i praksis. Sørg for driftsprosedyrer, måling, eierskap, støtte, innføring, kapasitetsgrenser og tydelig mottak av kunnskaps- og dataleveranser.

- [R17 Gjør driftsprosedyrer klare for den nye versjonen](../ideer/R17.md)
- [R18 Klargjør måling før funksjonen aktiveres](../ideer/R18.md)
- [R19 Gjennomfør tydelig overlevering til tjenesteeier](../ideer/R19.md)
- [R20 Forbered støtteapparatet på forventede spørsmål](../ideer/R20.md)
- [R21 Tilpass innføring til faktiske brukerroller](../ideer/R21.md)
- [R22 Avklar kapasitet og kostnadsgrenser ved lansering](../ideer/R22.md)
- [R23 Gjør kunnskapsleveranser klare for faktisk bruk](../ideer/R23.md)
- [R24 Klargjør kontrollert publisering av modeller og dataprodukter](../ideer/R24.md)

<a id="r-kategori-4"></a>

## Kontrollert feilhåndtering og avslutning

Forbered handlinger når innføringen feiler eller gammel løsning skal avsluttes. Skill tilbakeføring, fremoverretting, stans og gjenetablering, og rydd opp i midlertidige rettigheter og ressurser.

- [R25 Forklar feil som oppstår under utrullingen](../ideer/R25.md)
- [R26 Forbered og støtt tilbakeføring til kjent versjon](../ideer/R26.md)
- [R27 Planlegg retting når tilbakeføring ikke er mulig](../ideer/R27.md)
- [R28 Gjør stans og begrenset drift gjennomførbart](../ideer/R28.md)
- [R29 Koordiner sikker rotasjon av nøkler og sertifikater](../ideer/R29.md)
- [R30 Lukk midlertidige rettigheter og ressurser etter levering](../ideer/R30.md)
- [R31 Forbered kontrollert avvikling av gammel løsning](../ideer/R31.md)
- [R32 Lever en verifiserbar pakke for gjenetablering](../ideer/R32.md)

## Bruk steget i prosjektet

Avklar hva tilsiktet bruk betyr for leveransen, hvem som godkjenner overgangen og hvem som eier driften. Følg innføringen med målinger og en gjennomførbar plan for feil.

- [Finn ideer ut fra prosjektets behov](../veiledning/behov.md).
- [Velg og mål et avgrenset forsøk](../veiledning/effektmaaling.md).
- [Bruk malene for valg og utprøving](../maler.md).
- [Les om arbeidsformer og felles forutsetninger](../veiledning/leserveiledning.md).

[Se alle 256 ideene i registeret](../register.md).

| Forrige steg i læringssløyfen | Neste steg i læringssløyfen |
| --- | --- |
| [Verifisering](verifisering.md) | [Observasjon](observasjon.md) |
