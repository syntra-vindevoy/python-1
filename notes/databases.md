# Python 1 (Syntra): Databases

## Les 21 - Di 13/12/2022

### Normalisatie

#### Brochure
- standnummer
- datum
- sessietijden
- naam v. brouwerij
- land v. brouwerij
- naam bier
- stijl bier
- %ABV
- <s>paginanummer</s>
- <s>persoonlijke score</s>

#### Methode

1. berekende gegevens niet opslaan (bij ons toch)

2. entiteiten gaan zoeken: bier, brouwer, land, festival, stijl, 
    - **Brouwerij**
        - <u>`brewery_id`</u> | PK = *Primary Key*
        - standnummer
        - naam 
        - land

3. komt een eigenschap van een entiteit >1x voor: nieuwe entiteit maken
    - **Bier** 
        - <u>`beer_id`</u>
        - brewery_id
        - naam
        - stijl
        - ABV

    - **Festival**
        - <u>`festival_id`</u>
        - naam
        - locatie

    - **FestivalDatum**
        - <u>`festivaldatum_id`</u>
        - datum
        - festival_id

    - **Sessie**
        - <u>`sessie_id`</u>
        - naam
        - festival_datum_id

    - **SessieBieren**
        - ...

#### Relaties

- **many-to-one** - default van een relationele database
- **many-to-many** - enkel op te lossen met een tussentabel

## Les 22 - Di 20/12/2022

- gemist
