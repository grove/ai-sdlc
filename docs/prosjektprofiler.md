# Tilpass ideene til prosjektet

Metodikken kan være Scrum, Kanban, fossefall, et program eller forvaltning. Tilpass tidspunkt og formalisering, men behold forbindelsen mellom problem, forventet effekt, faktisk leveranse og læring. Prosjekttaggene i katalogen er søkehjelp og angir ikke uttømmende begrensninger.

| **Prosjektprofil** | **Viktig lokal tilpasning** | **Eksempler** |
| --- | --- | --- |
| Nye digitale produkter | Begynn med behov og en liten prototype. Mål faktisk brukeroppgave og læring før full bygging. | [P02](ideer/P02.md) [H06](ideer/H06.md) [A02](ideer/A02.md) [V31](ideer/V31.md) [O01](ideer/O01.md) |
| Eksisterende produkter og tjenester | Ta hensyn til brukere, kontrakter og historisk oppførsel. Mål hele flyten og etterfølgende feil. | [K02](ideer/K02.md) [A01](ideer/A01.md) [V08](ideer/V08.md) [R09](ideer/R09.md) [O09](ideer/O09.md) |
| Eldre systemer og stormaskin | Avklar faktiske regler, datatyper, batchvinduer og skjulte avhengigheter. Bruk differensiell sammenligning. | [P17](ideer/P17.md) [K03](ideer/K03.md) [A12](ideer/A12.md) [V07](ideer/V07.md) [R12](ideer/R12.md) |
| Integrasjoner og API-er | Gjør eierskap, kontrakter og konsumentovergang eksplisitt. Prøv tidsavbrudd, duplikater og delvis feil. | [K06](ideer/K06.md) [A17](ideer/A17.md) [A18](ideer/A18.md) [V06](ideer/V06.md) [R13](ideer/R13.md) |
| Data analyse og rapportering | Bevar definisjoner, dataopphav og kvalitet gjennom hele kjeden. Test mot faktiske forretningsregler. | [K04](ideer/K04.md) [A19](ideer/A19.md) [V17](ideer/V17.md) [V18](ideer/V18.md) [O22](ideer/O22.md) |
| KI og maskinlæring i produktet | Skill utviklingshjelp fra produktets modell. Evaluer data, prediksjoner eller svar og menneskelig overtakelse. | [H30](ideer/H30.md) [A21](ideer/A21.md) [A22](ideer/A22.md) [V19](ideer/V19.md) [V20](ideer/V20.md) |
| Plattform infrastruktur og DevOps | Prøv endringer i isolasjon, med policy og plan. Ta med selvbetjening, drift og gjenetablering. | [K22](ideer/K22.md) [A25](ideer/A25.md) [A26](ideer/A26.md) [V12](ideer/V12.md) [R32](ideer/R32.md) |
| Mobil klient og frakoblet bruk | Prøv enhetsvariasjon, lokal lagring, synkronisering og oppgradering. Distribusjon kan være forsinket eller uten nett. | [A06](ideer/A06.md) [V23](ideer/V23.md) [R14](ideer/R14.md) [O04](ideer/O04.md) [O30](ideer/O30.md) |
| Embedded OT og IoT | Bruk relevant maskinvare eller validert simulator, sikre stoppmodi og sporbar godkjenning. Feltoppdatering kan være dyr. | [P24](ideer/P24.md) [H31](ideer/H31.md) [A07](ideer/A07.md) [V22](ideer/V22.md) [R15](ideer/R15.md) |
| ERP hyllevare og low code | Test lokale roller, konfigurasjon og integrasjoner. Kontroller leverandørbegrensninger og fremtidig oppgradering. | [A08](ideer/A08.md) [V24](ideer/V24.md) [R16](ideer/R16.md) [O07](ideer/O07.md) [L08](ideer/L08.md) |
| Regulert eller sikkerhetskritisk arbeid | Bevar kravsporbarhet, uavhengige bevis og nødvendig signering. Utvid kontroll ut fra konsekvens ved feil. | [K12](ideer/K12.md) [K13](ideer/K13.md) [V01](ideer/V01.md) [V29](ideer/V29.md) [R07](ideer/R07.md) |
| Forskning og vitenskapelige beregninger | Bruk dimensjonsanalyse, kjente resultater, numerisk stabilitet, reproduserbarhet og uavhengig faglig vurdering. | [H05](ideer/H05.md) [A20](ideer/A20.md) [A32](ideer/A32.md) [V02](ideer/V02.md) [V03](ideer/V03.md) |
| Spill simulering og visuelle systemer | Prøv regler, tilstand, ytelse, innhold og variasjon i enheter. Kombiner automatiske kontroller med faktiske brukstester. | [A02](ideer/A02.md) [A03](ideer/A03.md) [V05](ideer/V05.md) [V08](ideer/V08.md) [V13](ideer/V13.md) |
| Dokumenter arkitektur og forprosjekt | Definer en navngitt mottaker og beslutning. Mål korrekthet, nytte i senere arbeid og redusert avklaringsbehov. | [H29](ideer/H29.md) [A29](ideer/A29.md) [A32](ideer/A32.md) [V30](ideer/V30.md) [R23](ideer/R23.md) |
| Forvaltning og beredskap | Koble support og hendelser til bekreftede feil og forebygging. Skill analyse fra autorisert produksjonsinngrep. | [P18](ideer/P18.md) [P30](ideer/P30.md) [O17](ideer/O17.md) [R26](ideer/R26.md) [L12](ideer/L12.md) |
| Migrering overtakelse og avvikling | Kartlegg avhengigheter, historikk og databevaring. Prøv overgang, avstemming og gjenoppretting før gammel løsning tas bort. | [A13](ideer/A13.md) [A16](ideer/A16.md) [V07](ideer/V07.md) [R27](ideer/R27.md) [R31](ideer/R31.md) |

<a id="avsnitt-arbeidsbetingelser-som-endrer-oppsettet"></a>

## Arbeidsbetingelser som endrer oppsettet

| **Betingelse** | **Tilpass på denne måten** |
| --- | --- |
| Sensitive data eller miljø uten nett | Bruk bare godkjent behandlingssted og data. Forbered lokale kildepakker, pakkearkiv og verktøy uten å anta nettilgang. |
| Lite historikk eller få leveranser | Start med oppgaveprøver og kvalitative funn. Vis usikkerheten og planlegg lengre observasjon i stedet for å hevde sikker effekt. |
| Store leveranser med få produksjonsvinduer | Prøv deler av sløyfen i simulator eller representativt miljø. Ta med integrasjon og observasjon etter den faktiske innføringen. |
| Mange team og eksterne leverandører | Avklar datarettigheter, kontrakter, grenseflater og hvem som eier målinger. Ikke flytt gevinst eller risiko til mottakeren uten å følge den. |
| Tilgjengelighet og flere språk | Bruk faktisk relevante brukere og hjelpemidler, og faglig kontrollerte oversettelser. En automatisk sjekk dekker ikke alle brukerbehov. [7](kilder.md#kilde-7) |
| Lang levetid eller sjelden bruk | Planlegg kontroll av arkiv, gjenetablering, utløpte avhengigheter og sjeldne arbeidsforløp også etter at prosjektet er avsluttet. |

<a id="avsnitt-utvid-en-id-med-en-konkret-variant"></a>

## Utvid en idé med en konkret variant

Kombiner arbeidsoppgave, artefakt, brukergruppe og risikobetingelse. [A29](ideer/A29.md) kan for eksempel bli vedlikehold av en installasjonsguide for et frakoblet kundemiljø. [V03](ideer/V03.md) kan bli kontroll av bevaringslover i en simulator. [A24](ideer/A24.md) kan bli syntetiske geografiske datasett eller hendelsesstrømmer. Behold samme krav til grunnlag, kontroll og effektmåling som i den opprinnelige ideen.

[Til katalogens start](index.md) · [Alle ideene](register.md)
