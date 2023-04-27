from datetime import datetime

from lib.modul1.moduleA import modulA
from lib.modul2.moduleB import modulB
from lib.modul3.modulC import modulC

now = datetime.now()

def timestampwykonania():
    godzina = now.strftime("%H:%M:%S")
    data = now.strftime("%m.%d.%Y")
    print("Sktypt wykonany: ", data, " o godzinie ", godzina)

modulA()
modulB()
modulC()
timestampwykonania()
