# ean13
## Wstęp
Poniższy program służy do generowania kodów kreskowych zgodnie ze standardem EAN13. Uruchomienie może zostac wykonane na dwa sposoby, opisane poniżej. 
## Instalacja poprzez pobranie spakowanego kodu
### Instalacja pakietu pillow do rysowania kodów

Po rozpakowaniu folderu .zip należy zainstalować pakiet pillow. Można dokonac tego poprzez menedżer pakietów pip ```pip install pillow``` (możliwe, że zaistnieje koniecznosć pobrania samego pipa).
Alternatywnym rozwiązaniem jest uruchomienie pipa w środowisku wirtualnym (pip domyślnie się tam znajduje): 
```
C:\Users\zofia\Downloads\ean13>python -m venv venv
C:\Users\zofia\Downloads\ean13>venv\scripts\activate
(venv) C:\Users\zofia\Downloads\ean13>
(venv) C:\Users\zofia\Downloads\ean13>pip install pillow
Collecting pillow
Using cached Pillow-9.3.0-cp310-cp310-win_amd64.whl (2.5 MB)
Installing collected packages: pillow
Successfully installed pillow-9.3.0 
```
### Uruchomienie
Uruchomienie programu następuje poprzez podanie ścieżki absolutnej do pliku ean13.py wraz z kodem jako argumentem. Jeśli długość argumentu jest niepoprawna (inna niż 12 znaków), program zakończy się niepowodzeniem oraz wyświetli błąd. 
```
(venv) C:\Users\zofia\Downloads\ean13>python C:\Users\zofia\Downloads\ean13\ean13.py 871125300120
checksum: 2, sequence: 8711253001202  
```

Przykładowy błąd:
```
(venv) C:\Users\zocha\Downloads\ean13>python C:\Users\zocha\Downloads\ean13\ean13.py 8711253001202
Len is not 12
(venv) C:\Users\zocha\Downloads\ean13>  
```
Podanie argmentu nieliczbowego spowoduje błąd i wyjście z programu:
```
(venv) C:\Users\zocha\Downloads\ean13>python C:\Users\zocha\Downloads\ean13\ean13.py abcdeghijklm
Traceback (most recent call last):
  File "C:\Users\zocha\Downloads\ean13\ean13.py", line 9, in <module>
    barcode = BarcodeGenerator(sequence=sequence)
  File "C:\Users\zocha\Downloads\ean13\ean13\barcode_generator.py", line 12, in __init__
    self.barcode = Barcode(sequence)
  File "C:\Users\zocha\Downloads\ean13\ean13\barcode.py", line 28, in __init__
    checksum = str(self._generate_checksum(code))
  File "C:\Users\zocha\Downloads\ean13\ean13\barcode.py", line 84, in _generate_checksum
    odd = [int(i) for i in code[-1::-2]]
  File "C:\Users\zocha\Downloads\ean13\ean13\barcode.py", line 84, in <listcomp>
    odd = [int(i) for i in code[-1::-2]]
ValueError: invalid literal for int() with base 10: 'm'
```
Po uruchomieniu programu na ekranie pojawi się grafika z kodem kreskowym, a w konsoli wyświetlone zostaną suma kontrolna oraz 13 cyfrowy kod. 
Grafika zostanie zapisana również w podfolderze barcodes pod nazwą będąca 13-cyfrowym kodem, w formacie png. 

## Instalacja poprzez sklonowanie repozytorium
### Klonowanie repozytorium
Aby sklonować repozytorium wymagane jest zainstalowanie git. W folderze, do którego ma być sklonowane repozytorium należy otworzyć dowolną konsolę i wykonać polecenie:
```
git clone https://github.com/zorka5/ean13.git
```
Przykładowo, jeśli projekt ma być zapisany w folderze Projects:
```
cd C:\Users\zofia\Documents\Projects\SIWP
C:\Users\zofia\Documents\Projects\SIWP>git clone https://github.com/zorka5/ean13.git
```

Rozpocznie się klonowanie repozytorium. 
```
C:\Users\zofia\Documents\Projects\SIWP>git clone https://github.com/zorka5/ean13.git
Cloning into 'ean13'...
remote: Enumerating objects: 63, done.
remote: Counting objects: 100% (63/63), done.
remote: Compressing objects: 100% (37/37), done.
remote: Total 63 (delta 26), reused 58 (delta 21), pack-reused 0
Receiving objects: 100% (63/63), 11.65 KiB | 2.91 MiB/s, done.
Resolving deltas: 100% (26/26), done.
```
Należy wejść do utworzonego folderu ean13:
```
C:\Users\zofia\Documents\Projects\SIWP>cd ean13
C:\Users\zofia\Documents\Projects\SIWP\ean13>
```
### Środowisko wirtualne
Aby nie instalować pakietów globalnie, możliwe jest uruchamianie programu w środowisku wirtualnym. W celu jego utworzenia w folderze ean13 należy wykonać:
```
C:\Users\zofia\Documents\Projects\SIWP\ean13>python -m venv venv
```
W przypadku braku narzędzi umożlwiających tworzenie środowisk wirtualnych może być konieczne zainstolowanie dodatkowych pakietów. 
Uruchomienie venv poprzez komendę venv\scripts\activate
```
C:\Users\zofia\Documents\Projects\SIWP\ean13>venv\scripts\activate
(venv) C:\Users\zofia\Documents\Projects\SIWP\ean13>
```

### Wymagane pakiety
Jedynym wymaganym pakietem do rysowania kodów kreskowych jest pakiet pillow. Można go zainstalować np poprzez pip:
```
(venv) C:\Users\zofia\Documents\Projects\SIWP\ean13>pip install pillow
Collecting pillow
  Using cached Pillow-9.3.0-cp310-cp310-win_amd64.whl (2.5 MB)
Installing collected packages: pillow
Successfully installed pillow-9.3.0
```
## Uruchomienie programu
Uruchomienie programu następuje analogicznie jak w punkcie poprzednim.
