import pygame, time

pygame.mixer.pre_init(frequency=48000,size=16,channels=2,buffer=512)
pygame.mixer.init()
def cero():
    pygame.mixer.music.load("0.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def uno():
    pygame.mixer.music.load("1.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def dos():
    pygame.mixer.music.load("2.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def tres():
    pygame.mixer.music.load("3.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def cuatro():
    pygame.mixer.music.load("4.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def cinco():
    pygame.mixer.music.load("5.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def seis():
    pygame.mixer.music.load("6.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def siete():
    pygame.mixer.music.load("7.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def ocho():
    pygame.mixer.music.load("8.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
def nueve():
    pygame.mixer.music.load("9.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


primeros_decimales_De_pi= "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
pi_prueba="121"
pi_2= "5820974944 5923078164 0628620899 8628034825 3421170679"

i=0
while i <len(primeros_decimales_De_pi):
    match primeros_decimales_De_pi[i]:
        case "0":
            cero()
        case "1":
            uno()
        case "2":
            dos()
        case "3":
            tres()
        case "4":
            cuatro()
        case "5":
            cinco()
        case "6":
            seis()
        case "7":
            siete()
        case "8":
            ocho()
        case "9":
            nueve()
        case _:
            break
    i+=1

#algoritmo de prueba
"""""
texto = "hola"
i = 0

while i < len(texto):
    match texto[i]:
        case "h":
            print(f"La letra {i + 1} es h")
        case "o":
            print(f"la segunda letra{i + 1} es o")
        case _:
            break
    i += 1
#fin"""

# if len(pi) in "3":
#     print("hola")