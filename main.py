from ia import IA
from audio import voz

def main():

    while True:  

        promt = voz()
        if(promt != "salir" or promt !="Salir" or promt != "salír" or promt != "Salír"):
            IA(promt)
        else:
            break

        
main()