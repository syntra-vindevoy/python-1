# Python 1 (Syntra): Think Python Chapter 1 - 9

## Les 01 - Di 13/09/2022

- Gemist (Portugal)

## Les 02 - Do 15/09/2022

### Logic gates 

- Vorige week: `AND`, `OR`, `XOR`, `NOT`, `NAND`, `NOR`, `XNOR`
- [Oefeningen (1.5)](https://issuu.com/diekeure/docs/vbtl_3-4_ns_logisch_denken_lb_proefversie)
    ```
     1: a0 b0 c0
     2: a1 b1 c1
     3: a1 b0 c1
     4: a0 b1 c1 d1 e0
     5: a0 b0 c0 d1 e0
     6: a0 b1 c1 d1 e1
     7: a0 b0 c1 d0 e0
     8: a0 b0 c1
     9: a0 b0 c0
    10: a0 b0 c0
    ```

### Virtual environments (miniconda)

- `conda create --name syntra`
- `conda activate syntra`
- `conda install python -c conda-forge`
    - [Conda Forge](https://conda-forge.org)
    - meer en recente packages (open source)
    - steeds deze source (flag `-c`) gebruiken!!

### Best Practices

- nooit whitespace in namen
- directories:  **lowercase**
- variables:    **snake_case**
- class names:  **CamelCase**
- keywords:     **lowercase** 

### Source Control (GIT)

- [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
    - `develop` = working copy van de repo
    - `master` = nadat in PRD gezet is
    - `feature` branches: ontwikkeling van nieuwe delen 
    - `(hot)fix` branches: fixes (hot = op PRD)
- Specifiek voor cursus:
    - iedereen moet names branch hebben (`jorick`)
    - 1st branch = `project-setup` (deprecated)
- Tool (all platforms): [GitKraken](https://www.gitkraken.com)
- Tool (Windows / Mac): [SourceTree](https://www.sourcetreeapp.com/)

## Les 03 - Di 20/09/2022

- Gemist (Brussel)

- Recursieve functie voor factorial
- [Nassi Schneiderman Diagram](https://en.wikipedia.org/wiki/Nassi%E2%80%93Shneiderman_diagram)

- Floor division
    ```python
    3 // 2 == 1
    -3 // 2 == -2
    ```

- Think Python oefeningen (1.1 - 1.2)

## Les 04 - Do 22/09/2022

- Think Python oefeningen (2.1 - 2.3)

- Extra oefening: swap variables
    - via tuple assignment:
        ```python
        x, y = y, x
        ```
    - via XOR: https://betterexplained.com/articles/swap-two-variables-using-xor
        ```python
        x = x ^ y
        y = x ^ y
        x = x ^ y
        ``` 
- Oefeningen mogen gepushed worden naar eigen branch: `origin/jorick`

## Les 05 - Di 27/09/2022

### Think Python Chapter 3: Functions

- *arguments* vs *parameters*
- *state diagrams* vs *stack diagrams*
- *fruitful functions* vs *void functions*
- *positional arguments* vs *keyword arguments*

### Think Python chapter 4: Interface Design

- *encapsulation*
- *generalization*
- *interface design*
- *refactoring*
- *development plan*

### Andere

```python
import math


def integer_length(n) -> int:
    """ Geeft de lengte van een getal in cijfers. """
    return int(math.log10(n)) + 1


def prime() -> int:
    """ Berekenen van een priemgetal via math.sqrt. """
    # TODO: thuis
    return -1
```

## Les 06 - Do 29/09/2022

- stack diagrams: niet te kennen
- fruitful vs void functions: vindt Yves slechte termen
- metaclasses: **TODO**: opzoeken
- Yves focust op NoneType errors: kunnen uitleggen, altijd nadenken over je type arg bij valkuilen!
- Yves gebruikt **dunder** termen expliciet bij `__name__` etc

## Les 07 - Di 04/10/2022

### Algemeen

- Mensen demo'en oplossingen van vorige week.

- Uitleg over de `if __name__ == '__main__':` check en belang bij imports

- Var "`_`" gebruiken wanneer je de waarde van de var niet nodig hebt:
    ```python
    for _ in range(5):
        # do something
    ```
- Uitleg over newline `\n` en tab `\t`; python gebruikt 4 spaties, tab wordt door editor omgezet.

- Uitleg over optionele parameters, bv. `print`:
    ```python
    print("_", end="+")    # end is \n by default 
    ```

- Oefeningen over `range`-functie (start, stop, step)

### Think Python Chapter 4

- Korte uitleg over klassen / objecten / instantiëring
    ```python
    from turtle import Turtle

    bob = Turtle()    # Instantiatie van een Turtle-object
    
    type(bob)         # turtle.Turtle
    print(bob)        # <turtle.Turtle object at 0x7f5a55af3550>
    ```

- cirkel = oneindige veelhoek: 360 x 1° draaien en 1 eenheid vooruit

### Oefeningen

- Tegen volgende week: 4.3 p.31 (5 oefeningen)

## Les 08 - Do 06/10/2022

### Think Python Chapter 4

- Test driven development
    - tests parallel scrijven met prd-code
    - ofwel via `assert` ofwel `unittest`

### Think Python Chapter 5

- if/elif wanneer de if's exclusief zijn.
    ```python
    # goed (maar verwarrend)
    if x > 3:
        ...
    elif x > 0:
        ...

    # slecht
    if x > 0:
        ...
    elif x > 3:
        ...         # wordt NOOIT uitgevoerd
    ```

- recursie herhalen, blijft belangrijk, rij van fibonacci als voorbeeld

## Les 09 - Di 11/10/2022

- Geen nota's (oefeningen)

## Les 10 - Do 13/10/2022

- Gemist (Spoedopname)

## Les 11 - Di 18/10/2022

### Think Python Chapter 5 - oefeningen

- 5.4: is dit hetzelfde als `factorial(n) + s` ?

### Think Python Chapter 6 - Theorie

- **Type hinting** (argument/return) 
    ```python
    def do_somehting(a: int):
        # take int as argument
        # only HINTING, no hard rules, IDE gaat zagen
        return an_integer

    def do_something(a: int) -> Any:
        # handig voor debugging
        return something

    def do_something(a: str) -> int | None:
        # return int OF None
        # even more pss => list(dict(...
        return something

    def do_something(a: str | int) -> str:
        # take int OF str als argument        
        return something
    ```

- Positional en keyword arguments
    - eerst positional, dan keywords, en niet overlappen
    - keyword arguments aka names parameters/arguments

- Optional en default parameters
    ```python
    def do_something(a, b, c=None):
    # Default value is None, aka optional
        pass
 
    def to_something(a=None, b):
    # Werkt niet
    # SyntaxError: non-default argument follows default argument
     pass
   ```

- Opnieuw: Yves maakt veel kleine denkoefeningetjes met None.
    ```python
    def som(a, b, c):
        # Niet laten vangen!!
        s = a + b + c
    
    print(som(1, 2, 3))    # None    
    ``` 

- Formatted strings. `f"{}"` >> `str.format()` 

- Checking types `type(a)` en `isinstance(a, int)` - combineren met `assert`

## Les 12 - Do 20/10/2022

- Eerst GIT pushes mogelijk maken voor de hele klas, daarna oef.

### Think Python Chapter 6 - Oefeningen

- 1 skippen, doorgedaan t.e.m. 8.5, best wat kalmer aan doen

## Les 13 - Di 25/20/2022

- Think Python Chapter 7 gedaan + oefeningen
- Volgende week bespreken van de oefeningen

## Les 14 - Di 08/11/2022

### Oefeningen Hs 8

- `Path(__file__).parent` uit `pathlib` 
- `logging` module
    - warnings: is error, maar ik heb dit voorzien
    - error: dit zou eigenlijk niet mogen gebeuren
- `except: pass` wil Yves niet zien. Minstens één logged line

## Les 15 - Do 10/11/2022

- Gemist (Meeting)

## Les 16 - Do 17/11/2022

- [Tomohiko Sakamoto algorithm for finding day of week](https://www.geeksforgeeks.org/tomohiko-sakamotos-algorithm-finding-day-week)
    - Aanpassen en gebruiken voor calender: 1st day is Sun, moet Mon zijn.
- `pathlib` <3 mogen we gebruiken -> +methods?
- context manager `with` gebruiken

## Les 17 - Di 22/11/2022

- GIT (zie powerpoint)

## Les 18 - Di 29/11/2022

- Gemist (Ziek)

## Les 19 - Do 01/12/2022

- Afwerken oefeningen die vorige week gegeven werden, ter voorbereiding van het examen. Ik heb er een aantal ingehaald:
  - `extra/find_number.py`
  - `extra/find_letter_bounds.py`

## Examen - Di 06/12/2022

- Zie repository op [GitHub](https://github.com/syntra-vindevoy/python1-jorick-2022-23/tree/examen-python-1)
