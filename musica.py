import pygame, time
"""
# 🎵 Proyecto: "PI Music Generator"

Este proyecto combina **matemática, música y programación**.  
La idea se inspira en el concepto del *mono infinito*, pero en lugar de texto, 
utilizamos el número **π (pi)** o **e (Euler)** para generar melodías.

---

## 🧠 Concepto

El número pi es infinito y contiene todos los posibles patrones de números.  
Entonces, si asignamos una **nota musical a cada dígito del 0 al 9**, podríamos,
 en teoría, reproducir **todas las canciones que existen**… incluso aquellas que aún no fueron creadas.

Cada número se convierte en una nota, y al recorrer los decimales de pi o e, el programa toca una melodía única.

---

## 🧩 Cómo funciona

1. Grabé 10 notas con mi guitarra, una para cada número del 0 al 9.
2. Edité los sonidos con Audacity y los guardé como archivos WAV:  
   `0.wav`, `1.wav`, `2.wav`, … `9.wav`
3. Usé **Python** con la librería **Pygame** para reproducir los sonidos.
4. El programa lee una cadena con los primeros decimales de **π** o **e**.
5. Por cada número, ejecuta la función correspondiente (ej. si ve un "3", toca `3.wav`).
6. Así se genera una secuencia sonora basada directamente en una constante matemática.

---

## 🧮 Ejemplo

Si los primeros decimales de pi son: 14159265358979323846264338


El programa reproducirá:  
🎵 nota3 → nota1 → nota4 → nota1 → nota5 → nota9 → nota2 → nota6 → nota5

---

## 🚀 Cómo usarlo

1. Asegúrate de tener **Python** y **Pygame** instalados:

2. Guarda tus sonidos (`0.wav` a `9.wav`) en la misma carpeta que el script.
3. Ejecuta el archivo:

4. Disfrutá la melodía infinita generada por los números.

---

## 💡 Idea del video (si lo querés mostrar)

> “¿Puede pi tocar todas las canciones del mundo?”
>
> Este experimento combina programación, música y filosofía del infinito.  
> Usando los decimales de pi como base, cada número se traduce en una nota musical.  
> Si pi es infinito… entonces, dentro de su secuencia, podrían existir todas las melodías posibles.

---

## ⚙️ Autor

**Dante Nicolás Rodríguez**  
GitHub: [TecnicoD](https://github.com/TecnicoD)  
Inspirado por la relación entre el infinito, la música y la programación 🎸💻
"""

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
