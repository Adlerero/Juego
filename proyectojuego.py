import pygame
import time
import sys
import os

class Juego:
    def __init__(self):
        #Implementar un nuevo constructor que guarde por chekpoints las cosas

        self.nombre = ""
        self.apellido = ""
        self.genero = ""
        self.pistas = 0
        self.decision1 = 0
        self.decision2 = 0
        self.decision3 = 0
        self.llavecoche = 0
        self.carta = 0
        self.intentos = 6
        self.objetos = []
        self.inventario = []
        self.numerodeobjetosinventario = 0
        self.limiteinventario = 5
        self.comandos = {'g':self.buscar_objetos, 'i':self.revisar_inventario, 'l': self.lectura_carta, 's': self.soltar_objetos,}
        #Poner los comandos hasta arriba
        #Agregar contenido no visto a la carta despues

        self.artecarta = """
    .:*####%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%####*-.    
    .=@@#*****************************************#@@+.    
    .+@%-.........................................-%@*.    
    .*@%-...................:::::.................-%@*.    
    .*@%:..-#@@@@@@@@@@@@@@@@@@@@@@*..............-%@*.    
    .*@%:...:=*#######****#######*=...............-%@*.    
    .*@%-.........................................-%@*.    
    .*@%-.........................................-%@*.    
    .*@%-..-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=..-%@*.    
    .+@#....:+#%%%##*++++++++++++++++++*#%%%%*-...-%@*.    
    .+@#..........................................-%@*.    
    .+@*.....:::::::::::::::::::::::::::::::::....:#@*.    
  ...*@*...-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:...#@*:..  
 .*%@@@#.....:-====---------------------=====:.....*@@@@+..
.%@@@@@@+.........................................+@@@@@@%.
+@@@::*@@%=...:=+++++++*********+++++++*##*=....=%@@*-:%@@+
%@@#...:+%@%+::=#%@%%##################%@@#=::+%@%+:...#@@%
@@@+......=%@@*:...........................:*@@%=......+@@@
@@@=........=%@@*:.......................:*@@%=........=@@@
@@@=..........=%@@#-...................-#@@%=..........-@@@
@@@-............=%@@%=..:::=###+-::..=%@@@+............-@@@
@@@-..............=%@@@@@@@@%%%@@@@@@@@@*..............-@@@
@@@=..............:#@@@%=.........-%@@@#:..............=@@@
@@@=............=%@@@=...............=@@@%=............=@@@
%@@=..........=%@@#-...................=%@@@+..........=@@%
#@@+.......:+@@@#-.......................=%@@@*:.......+@@#
*@@+.....:*@@@*:...........................-#@@@#-.....+@@*
+@@+...-#@@%+:...............................:+%@@%=...+@@+
=@@+:+%@@%=.....................................=#@@%=.=@@+
-@@%@@@#-.........................................-#@@@%@@=
-@@@@@%+++++++++++++++++++++++++++++++++++++++++++++#@@@@@-
:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
        """
        self.artepaquetedechicles = """
                                     .....................................................     
                                     .#=+......................:::::::::::::--------======*..  
                         ....:----::+*--*.................................................*..  
                . .......:*-=:.........:+..................::::::::::::...................#... 
              .#**+*:----=+-=:.........-=.......:-=*##########################*+-:........#... 
      ........-*---+:::::=+-+:........:+-...:+######################################*-...:%... 
      ....+--==#---*:::::==-+:...:=*####-.=############################################*::%... 
  ...=++=++--++#---*:::=*#=-*...+#######:-###############################################=%... 
  ...+--=*+--+*#---*--####=-*...+#######..+##############################################-%... 
..:==*--=*+--+*#---*:-*###--*.....=*####...:+##########################################=.:%... 
..:==*--=#+--+*#---*:::-+#--+.........:*.......-+*################################*+:....:#... 
..:==*--=#+--+*#---*:::::+===..........+.............:-=++***##########***+==-:...........#... 
..-==*--=#+--++#---+:::::::::::::::::::+::::::::::::::::::::::::::::::....................*... 
..-==*--=#+--=+#++++::::::::::::::::::=+:::::::::::::::::::::----------------:---------::+:... 
..-==*--=*+=-+=:::::::---------------+=:::::-=++***#############################**+=::::*:...  
..-==*--=*::::-----=============----*=::*###########################################*:-#.....  
..:==*++++:::::::::::::::::::::::::*=::::=+*#################################*+=--:::++......  
..:========+++++++++++++++++++++++#=============================-----:::::::::::::::+-.......  
 ..::.=============================================================================:.........  
      ..........................:::::-----------=================================-.....      
        """

        #Cambiar arte de carta cuando ya tengas la linterna

    def ejecucion_comandos(self, query):
        query = query.lower()
        if query in self.comandos:
            self.comandos[query]()
        else:
            query = input(f"Comando '{query}' no válido. Introduce otro: ")
            self.ejecucion_comandos(query)

    def buscar_objetos(self):
        #if query == '':
         #   return
        #if query == 'g':
        if self.intentos > 0:
            self.intentos -= 1
            print("\nObjetos disponibles: ")
            print(f"{self.objetos}")
            orden = input("\nEscribe el nombre del objeto a recoger. Si quieres cancelar, escribe 'c': ")
            orden = orden.lower()
            while orden not in self.objetos and orden != "c":
                orden = input("Escriba bien: ")
                orden = orden.lower()
            if self.numerodeobjetosinventario <= self.limiteinventario:
                if orden != "c":
                    self.numerodeobjetosinventario +=1
                    self.objetos.remove(orden)
                    self.inventario.append(orden)
                    if orden == "carta":
                        print ("\n")
                        self.mostrar_arte(self.artecarta, 0.001)
                        return
                    if orden == "paquete de chicles":
                        print("\n")
                        self.mostrar_arte(self.artepaquetedechicles, 0.001)
                else:
                    return
            else:
                print("Tu inventario esta lleno. Tendras que soltar algun objeto para recoger otro.")
        else:
            print("\nNumero de intentos para buscar objetos agotado.")
        #Implementar imagenes del objeto?

    def revisar_inventario(self):
        print("\nObjetos en el inventario:")
        print(f"{self.inventario}")
        print("\n")
        print(f"Numero de objetos en el inventario: {self.numerodeobjetosinventario} \tLimite de objetos del inventario: 5")
        print("\n¿Deseas revisar algún objeto del inventario?")
        invorden = input("Escribe el nombre del objeto para revisarlo o 'c' para cancelar: ")
        invorden = invorden.lower()
        while invorden not in self.inventario and invorden != "c":
            invorden = input("Escriba bien: ")
            invorden = invorden.lower()
        if invorden == "carta":
            self.mostrar_arte(self.artecarta, 0.001)
            print("\nPresiona enter para continuar.")
            self.enter()
            return
        elif invorden == "paquete de chicles":
            self.mostrar_arte(self.artepaquetedechicles, 0.001)
            print("\nPresiona enter para continuar.")
            self.enter()
        else:
            return
    
    def soltar_objetos(self):
        print("\nObjetos en el inventario:")
        print(f"{self.inventario}")
        print("\n")
        orden = input("Escribe el nombre del objeto que quieres soltar, o presiona 'c' para cancelar: ")
        orden = orden.lower()
        while orden not in self.inventario and orden != "c":
            orden = input("Escriba bien: ")
            orden.lower()
        if orden != "c":
            self.inventario.remove(orden)
            self.numerodeobjetosinventario -= 1
        else:
            return
        

    

    def lectura_carta(self):
        if "linterna" not in self.inventario:
            if self.genero == "h":
                contenidocarta = f"""
Noirville, 30 de noviembre de 2023.

Querido {self.nombre}.

Es un placer para mí dirigirme a ti en este día especial para felicitarte por tu graduación de la Academia de Detectives. Este logro es testimonio de tu dedicación, habilidades y determinación, y estoy seguro de que has adquirido las herramientas necesarias para enfrentar los desafíos que se avecinan.

Al haber seguido tu formación con éxito, me complace expresarte mi más sincera enhorabuena. Tu entrada en el mundo de la investigación y la resolución de crímenes es un paso significativo, y estoy convencido de que harás contribuciones valiosas para hacer de Noirville un lugar más seguro.

Estoy entusiasmado por la posibilidad de trabajar juntos en el futuro. Noirville enfrenta desafíos únicos, pero con tu talento y dedicación, confío en que lograremos grandes avances en la lucha contra el crimen en nuestra querida ciudad.

Recuerda que la colaboración y la perseverancia son clave en nuestra profesión. Atravesaremos momentos difíciles, pero estoy seguro de que, con tu habilidad y ética de trabajo, podremos superar cualquier obstáculo que se presente en nuestro camino.

Te felicito nuevamente por este logro y espero con ansias verte convertirte en un detective excepcional. Estoy aquí para apoyarte en cada paso de tu camino.

Con gratitud y anticipación,

Vincent Noiré
Ministro de Justicia de Noirville
            """
            else:
                contenidocarta = f"""
Noirville, 30 de noviembre de 2023.

Querida {self.nombre}.

Es un placer para mí dirigirme a ti en este día especial para felicitarte por tu graduación de la Academia de Detectives. Este logro es testimonio de tu dedicación, habilidades y determinación, y estoy seguro de que has adquirido las herramientas necesarias para enfrentar los desafíos que se avecinan.

Al haber seguido tu formación con éxito, me complace expresarte mi más sincera enhorabuena. Tu entrada en el mundo de la investigación y la resolución de crímenes es un paso significativo, y estoy convencido de que harás contribuciones valiosas para hacer de Noirville un lugar más seguro.

Estoy entusiasmado por la posibilidad de trabajar juntos en el futuro. Noirville enfrenta desafíos únicos, pero con tu talento y dedicación, confío en que lograremos grandes avances en la lucha contra el crimen en nuestra querida ciudad.

Recuerda que la colaboración y la perseverancia son clave en nuestra profesión. Atravesaremos momentos difíciles, pero estoy seguro de que, con tu habilidad y ética de trabajo, podremos superar cualquier obstáculo que se presente en nuestro camino.

Te felicito nuevamente por este logro y espero con ansias verte convertirte en una detective excepcional. Estoy aquí para apoyarte en cada paso de tu camino.

Con gratitud y anticipación,

Vincent Noiré
Ministro de Justicia de Noirville
            """
            self.mostrar_texto(contenidocarta)
            textoenter = "Presiona enter 3 veces para continuar."
            print("\n\nPresiona enter 3 veces para continuar.")
            self.enter()
            self.enter()
            self.enter()

        else:
            pass
        #Hacer que si se lleva una linterna consigo, la carta tenga un mensaje oculto.


    #Funcion para mostrar texto
    def mostrar_texto(self, texto):
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
            #0.03 el ideal

    #Funcion para mostrar arte
    def mostrar_arte(self, texto, tiempo):
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(tiempo)

    #Funcion para parpadeo del texto
    def parpadeo(self, texto):
        tiempo_inicio = time.time()
        tiempo_limite = 3  # segundos

        while time.time() - tiempo_inicio < tiempo_limite:
            sys.stdout.write(f"\r{texto} ")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\r" + " " * len(texto) + " ")
            sys.stdout.flush()
            time.sleep(0.5)
    
    #Funcion de enter para conversaciones
    def enter(self):
        comandoenter = input()
        while comandoenter != '':
            textoenter = "Presiona enter para continuar."
            self.parpadeo(textoenter)
            comandoenter = input()


    """
    def genero(self, texto1, texto2):
        if self.genero == "h":
            return texto1
        if self.genero == "m":
            return texto2
    """

    def inicio(self):
        # Ruta de tu archivo de música
        track1 = "살인 계획 (A Murder Plan).mp3"

        pygame.mixer.music.load(track1)
        pygame.mixer.music.play()

        logo = """

@@@@@@@@@@@@%=#@@@@@@%@@%%%@%@%%%%%%%%%%%###*****************##%%%%%%%%%@@@@@@@@@@@@@@@@@##@@@%%%%%%
@@@@@%%%%@@@%-.=%@@@%%%@%%%%%@%%%%%%%%%%#####******++*********#%%%%%%%%@@@@@@@@@@@@@@%%*:.+@@@%#**#%
@@@@@%%%%@@@%-.:*@@@%%%@%%%%%%%%%%%%%%%%#####**++++**+++++*****%%%%%%%%%@@@@@@@@@%@%#-....+@@@%**%@%
@@@@@%%%%@@@%-..=%@%-:=%%%%%%%%%%%%%%%%%#####*+++**+++*+++++***#%#%%%%%%%%@@@@@@@%+....-*%@@@@%%@@%%
@@@@@@%%%@@@%-..:#@%-.:#@@%%%%%%%%%%#########****++**+++**++++*#%##%%%%%%%%%#+%@@@=..*%@@@@@@@@%@@%%
@@@@@@@@%@@@%-...-%%-.:#@%-....-+##%########**++*++++++*++**++*####%%###@@@*..%@@@=..%@@@@@@@@@%@@%%
@@@@@@@@@@@@%-....*%-.:#@*..:==:..+@%=-=%%+++++**+****+++#+++##+-=%@#..*@@@*..%@@@=..%@@@@@@@@@%@@%%
@@@@@@@@%@@@%-....:#-.:#@*..+@@%:.-%%-.:%@-......+%*..-%@*..+@%-.:%@#..*@@@*..%@@@=..%@@@%@@@@@%@%%%
@@@@@@@@%@@@%-.....=-.:#@*..+@@@-.-%%-..%@-.:#%=..#%-..*%..:%@%-.-%@#..*@@@*..%@@@=..*+:.#@@@@@%@@%%
@@@@@@@@%@@@%-.:-..::.:#@*..+@@@:.-%%-..%@-.:+*-..*@#..--..+@@%-.-%@#..*@@@*..%@@@=......#@@@@@%@@%%
@@@@@@@@%@@@%-.:+-....:#@*..+@@@:.-%%-..%@-......:%@@=....-%@@%-.-%@#..*@@@*..%@@@=...+#%@@@@@@%@@%%
@@@@@@@@%@@@%-.:**....:#@*..+@@@:.-%%-..%@-....:#@@@@%:...*@@@%-.-%@#..*@@@*..%@@@=..%@@@@@@@@@%@@%%
@@@@@@@@#@@@%:.:*%=...:#@*..+@@@:.-%%-..%@-.:=..=%@@@@*..-@@@@%-.-%@#..*@@@*..%@@@=..%@@@@@@@@@%@@%%
@@@@@@@@%@@@%-..*@#:..:#@*..+@@#..-%%-..%@-.:#+..=@@@@%=.%@@@@%-.-%@#..+%%@*..%@@@=..%@@@@@@@@@@@@%%
@@@@@@%%%@@@%-..*@@=..:#@#........+@%-.:%@-.-%@+::*@@@@#*@@@@@%-.-%@#.....#*...:*@=..%@@@@@@@@@@@@@%
@@%%@@%%@@@@%-..*@@#:.:#@@*-:-=+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%**+=-#*....+@=..-+*%@@@@@@%%#%%
@@#%%%#%@@@@%-..*@@@+-+%@@@@@@@@@@@@@@%%%%####*###*#********####%%@@@@@@@@@@@%%#%@=.......+@@@%%%%%%
@@@@@##%%%@@%-:=%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%#%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@%+:..+@@@@%%%##
@@@@@@@@%%@@@@@@@@@@@@@@@%%%%@@%@@%%@*==#=*#%++%#=##=%%#=%#+%#++%+*+#=+@@%@@@@@@@@@@@@@@@@@@@@%#*++#

        """

        for char in logo:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.005)  # Ajusta el tiempo de pausa según lo rápido que quieras que aparezcan los caracteres

        query = input("\n\tEscribe s para continuar\n\t")
        while query != "s":
            query = input()
        time.sleep(3)
        os.system('cls')
        pygame.mixer.music.stop()
        return

    def asignacion(self):
        text1 = "Comienza tu aventura."
        self.parpadeo(text1)
        print("\n¿Cual es tu nombre?")
        p.nombre = input()
        print("\n¿Cual es tu apellido?")
        p.apellido = input()
        self.genero = input("\n¿Cual es tu género? Escribe h para hombre, m para mujer: ")
        while self.genero !="h" and self.genero !="m":
            self.genero = input("\nIncorrecto. Intenta de nuevo: ")
        time.sleep(2)
        os.system('cls') 

    def tutorial(self):
        track1 = "1 Hora de Sonido de la Lluvia y Truenos  HD  Relajarse..mp3"

        pygame.mixer.music.load(track1)
        pygame.mixer.music.play()

        print("\tHora: 9.46 pm\tLocación: Estación de policia")
        print("\n")
        if self.genero == "h":
            text2 = f"La noche en Noirville está envuelta en un manto de lluvia y neón cuando el recién graduado de la academia de detectives, {p.nombre} {p.apellido}, se encuentra frente a la puerta de la sombría oficina del Capitán James Fitzgerald, su mentor."
        else:
            text2 = f"La noche en Noirville está envuelta en un manto de lluvia y neón cuando la recién graduada de la academia de detectives, {p.nombre} {p.apellido}, se encuentra frente a la puerta de la sombría oficina del Capitán James Fitzgerald, su mentor."
        self.mostrar_texto(text2)
        print("\n")
        textoenter = "Presiona enter para continuar."
        self.parpadeo(textoenter)
        self.enter()
        if self.genero == "h":
            text3 = f"Capitán Fitzgerald: Bienvenido, {p.apellido}. Pasa por favor. Lamento llamarte para un caso tan violento justo despues de tu graduación. Parece que esta ciudad no te deja descansar."
        else:
            text3 = f"Capitán Fitzgerald: Bienvenida, {p.apellido}. Pasa por favor. Lamento llamarte para un caso tan violento justo despues de tu graduación. Parece que esta ciudad no te deja descansar."
        self.mostrar_texto(text3)
        self.enter()
        text4 = f"Se que la situación es complicada, pero quiero que recuerdes todo lo que has aprendido y lo duro que has estado preparandote todos estos años."
        self.mostrar_texto(text4)
        self.enter()
        if self.genero == "h":
            text5 = f"Seguramente escuchaste por la radio todo lo que paso. Es una pena. Pero no tenemos tiempo para lamentarnos. ¿Estas listo para lo que viene?"
        else:
            text5 = f"Seguramente escuchaste por la radio todo lo que paso. Es una pena. Pero no tenemos tiempo para lamentarnos. ¿Estas lista para lo que viene?"
        self.mostrar_texto(text5)
        print("\n")
        if self.genero == "h":
            response = input("\n¿Que quieres hacer? Escribe 'a' para quedarte callado o 'b' para responder: ")
        else:
            response = input("\n¿Que quieres hacer? Escribe 'a' para quedarte callada o 'b' para responder: ")
        while response != "a" and response != "b":
            if self.genero == "h":
                response = input ("\n¿Que fue eso? Escribe 'a' para quedarte callado o 'b' para responder: ")
            if self.genero == "m":
                response = input ("\n¿Que fue eso? Escribe 'a' para quedarte callada o 'b' para responder: ")
        if response == "a":
            print("\n")
            text6 = f"Detective {self.nombre} {self.apellido}: ............"
            self.mostrar_texto(text6)
            self.enter()
            print("\n")
            if self.genero == "h":
                text7 = f"Capitan Fitzgerald: No estuviste 5 años preparandote duro para quedarte congelado en situaciones como esta. Vamos."
            else:
                text7 = f"Capitan Fitzgerald: No estuviste 5 años preparandote duro para quedarte congelada en situaciones como esta. Vamos."
            self.mostrar_texto(text7)
            self.enter()
        if response == "b":
            print("\n")
            text6 = f"Detective {self.nombre} {self.apellido}: ¡Claro que lo estoy! ¡No descansaré hasta que el crimen en esta ciudad sea completamente erradicado!"
            self.mostrar_texto(text6)
            self.enter()
            print("\n")
            if self.genero == "h":
                text7 = f"Capitan Fitzgerald: ¡Esa es la actitud novato! Me alegra saber que te he entrenado bien."
            if self.genero == "m":
                text7 = f"Capitan Fitzgerald: ¡Esa es la actitud novata! Me alegra saber que te he entrenado bien."
            self.mostrar_texto(text7)
            self.enter()
        os.system('cls')


        print("\tHora: 9:48 pm\tLocación: Estación de policia")
        print("\n")
        text8 = f"Capitan Fitzgerald: Por cierto, esta carta llego para ti el dia de ayer. ¿Quieres tomarla?"
        self.mostrar_texto(text8)
        self.objetos.append("carta")
        textocarta = input("\n\nEscribe g para buscar objetos en el lugar: ")
        while textocarta != "g":
            textocarta = input("Hay un objeto importante en este lugar. Escribe g por favor: ")
        self.ejecucion_comandos(textocarta)
        while self.numerodeobjetosinventario != 1:
            textocarta = input("Capitan Fitzgerald: ¿No entendiste? Toma la carta por favor. Escribe g: ")
            self.ejecucion_comandos(textocarta)
        print("\n")
        leercarta = input("Escribe 'l' para leer la carta: ")
        while leercarta != "l":
            if self.genero == "h":
                leercarta = input("Creo que esta carta es importante novato. Por favor, leela.")
            else:
                leercarta = input("Creo que esta carta es importante novata. Por favor, leela.")
        os.system('cls')
        pygame.mixer.music.stop()
        #print("\tHora: 9:50 pm\tLocación: Estación de policia")
        #print("\n")
        
        track2 = ("1 HORA DE LLUVIA LOFI ,SAD, RELAX CON SONIDO DE PIANO(MUSIC).mp3")
        pygame.mixer.music.load(track2)
        pygame.mixer.music.play()
        self.ejecucion_comandos(leercarta)
        os.system('cls')
        print("\tHora: 9:55 pm\tLocación: Estación de policia")
        print("\n")
        text1 = f"Detective {self.nombre} {self.apellido}: ..........."
        text2 = f"Capitan Fitzgerald: .........."
        self.mostrar_texto(text2)
        self.enter()
        print("\n")
        self.mostrar_texto(text1)
        self.enter()
        print("\n")
        text3 = f"Capitan Fitzgerald: Lo siento mucho, {self.apellido}. Es una pena que tengas que comenzar tu aventura investigando el asesinato de alguien tan importante para los dos. Lo lamento mucho."
        self.mostrar_texto(text3)
        self.enter()
        text4 = f"Ser un detective aquí en Noirville... no es para los débiles de corazón. Las calles están llenas de sombras y cada caso es un camino oscuro. Pero alguien tiene que hacerlo, alguien tiene que buscar la verdad en medio de la oscuridad."
        self.mostrar_texto(text4)
        self.enter()
        print("\n")
        response = input("¿Que quieres hacer? Escribe a para responder asustado o b para responder motivado.")
        while response != "a" and response != "b":
            response = input ("¿Que fue eso? Escribe a para responder asustado b para responder motivado.")
        if response == "a":
            print("\n")
            text5 = f"Detective {self.nombre} {self.apellido}: Comandante...." 
            self.mostrar_texto(text5)
            self.enter()
            text6 = f"Tengo miedo. ¿En que nos estamos metiendo? ¿Vamos a terminar igual que el ministro?"
            self.mostrar_texto(text6)
            self.enter()
            print("\n")
            text7 = f"Comandante Fitzgerald: No puedo decirte lo que va a pasar. Pero si no somos nosotros los que tratamos de solocuionar esto, nadie lo hara."
            self.mostrar_texto(text7)
            self.enter()
            text8 = f"El era nuestro jefe, pero también era nuestro amigo después de todo... Este crímen no puede quedar impune."
            self.mostrar_texto(text8)
            self.enter()
            print("\n")
            text9 = f"Detective {self.nombre} {self.apellido}: Si, ¡Tiene razón, llegaremos al fondo de esto! Pongamonos en marcha."
            self.mostrar_texto(text9)
            self.enter()
        if response == "b":
            print("\n")
            text5 = f"Detective {self.nombre} {self.apellido}: Comandante...."
            self.mostrar_texto(text5)
            self.enter()
            text6 = f"¡Me encargaré de encontrar quien esta detras de todo esto! El ministro era nuestro jefe, pero más que todo eso, era nuestro amigo. ¡Este crimen no quedará impune!"
            self.mostrar_texto(text6)
            self.enter()
            print("\n")
            if self.genero == "h":
                text7 = f"Comandante Fitzgerald: Solo el escucharte me pone los pelos de punta, muchacho. Quien sabe..."
            else: 
                text7 = f"Comandante Fitzgerald: Solo el escucharte me pone los pelos de punta, muchacha. Quien sabe..."
            self.mostrar_texto(text7)
            self.enter()
            text8 = f"Quizás puedas llegar a ser como Vincent en el futuro. Hacer todo el bien que el hizo."
            self.mostrar_texto(text8)
            self.enter()
            print("\n")
            text9 = f"Detective {self.nombre} {self.apellido}: No hay tiempo que perder. Pongamonos en marcha."
            self.mostrar_texto(text9)
            self.enter()
        pygame.mixer.music.stop()
        os.system('cls')

        track3 = ("The last Samurai Soundtrack, con sonido de lluvia  Meditación.mp3")
        pygame.mixer.music.load(track3)
        pygame.mixer.music.play()

        #self.inventario.append("paquete de chicles")
        print("\tHora: 10:00 pm\tLocación: Estación de policia")
        print("\n")
        if self.genero == "h":
            text1 = f"Capitan James Fitzgerald: Detente allí. Antes de partir debo enseñarte un par de cosas más. Allá afuera es diferente, niño"
        else:
            text1 = f"Capitan James Fitzgerald: Detente allí. Antes de partir debo enseñarte un par de cosas más. Allá afuera es diferente, niña"
        self.mostrar_texto(text1)
        self.enter()
        text2 = f"No es un juego, es la vida real. Cada paso que des, cada decisión que tomes, puede ser la diferencia entre la vida y la muerte. Así que mantén los ojos abiertos y la mente alerta."
        self.mostrar_texto(text2)
        self.enter()
        print("\n")
        print("\n")
        text3 = f"Capitan Fitzgerald: En primer lugar, va a ser importante el como recabes pistas. No tenemos todo el tiempo del mundo, por lo que existe un limite de intentos para buscar objetos."
        self.mostrar_texto(text3)
        self.enter()
        self.objetos.append("paquete de chicles")
        print(f"\nNumero de intentos para buscar objetos: {self.intentos}")
        text4 = input("Intenta buscar objetos ahora. Presiona 'g': ")
        text4 = text4.lower()
        while text4 != "g":
            text4 = input("Busca objetos por favor. Quiero probar mi punto. Escribe 'g': ")
            text4 = text4.lower()
        self.ejecucion_comandos(text4)
        while "paquete de chicles" not in self.inventario:
            text4 = input("Por favor, toma el paquete de chicles. Escribe g: ")
            text4 = text4.lower()
            self.ejecucion_comandos(text4)
        print(f"\nNumero de intentos para buscar objetos: {self.intentos}")
        text5 = f"\nCapitan Fitzgerald: Como podrás observar, tu número de intentos para buscar objetos se redujo. Estos intentos seran relativos al caso que estemos tratando."
        self.mostrar_texto(text5)
        self.enter()
        text6 =f"No olvides esta regla."
        self.mostrar_texto(text6)
        self.enter()
        text7 = f"Además de esto, vas a querer soltar objetos que no te sirvan, ya que el espacio de tu inventario es limitado. Solo puedes cargar con 5 objetos a la vez. Y cada objeto que sueltes será dejado atrás."
        self.mostrar_texto(text7)
        text8 = input("Escribe s para soltar objetos: ")
        while text8 != "s":
            text8 = input("Suelta objetos por favor. Quiero probar mi punto. Escribe 's': ")
            text8 = text8.lower()
        self.ejecucion_comandos(text8)
        while self.numerodeobjetosinventario == 2:
            text8 = input("Por favor, suelta un objeto. Escribe 's': ")
            text8 = text8.lower()
            self.ejecucion_comandos(text4)
        if "carta" not in self.inventario:
            text9 = f"Capitán Fitzgerald: Creí que le darías mas importancia a esa carta, {self.apellido}. Después de todo, son las ultimas palabras del ministro hacia ti. Pero está bien. Ya no podrás recogerla de nuevo. Recuerda esto."
            self.mostrar_texto(text9)
            self.enter()
        else:    
            text9 = f"Capitán Fitzgerald: Ese paquete de chicles no tenía mucha utilidad da fin de cuentas. Buena elección. Ahora tienes más espacio en tu inventario."
            self.mostrar_texto(text9)
            self.enter()
        text1 = f"Por último, debes saber que es importante revisar tu inventario para poder analizar lo que llevas encima y que hacer con las situaciones con las que te encuentres."
        self.mostrar_texto(text1)
        self.enter()
        text2 = input("\nEscribe i para revisar tu inventario: ")
        while text2 != "i":
            text2 = input("Vas a querer saber que es lo que llevas encima. Escribe i: ")
            text2 = text2.lower()
        self.ejecucion_comandos(text2)
        text3 = f"Capitán Fitzgerald: Las pistas que recabes serán cruciales para poder resolver cualquier caso o quedarnos igual que ya estamos."
        self.mostrar_texto(text3)
        self.enter()
        if self.genero == "h":
            text4 = f"No perdamos más tiempo, recien egresado y detective profesional {self.nombre} {self.apellido}. Vamos a esa escena del crimen."
        else:
            text4 = f"No perdamos más tiempo, recien egresada y detective profesional {self.nombre} {self.apellido}. Vamos a esa escena del crimen."
        self.mostrar_texto(text4)
        self.enter()
        pygame.mixer.music.stop()
        os.system('cls')
        #Ademas, vas a querer soltar objetos que no te sirvan, ya que tu inventario es limitado

        #Tutorial de limite de objetos, inventario, numero de intentos?, y soltar objetos. 
        #text5 = f"Vamos, {self.apellido}. No hay tiempo que perder. Lleguemos al fondo de esto. Toma las llaves de la patrulla y dirijamonos a la escena del crimen."
        #self.mostrar_texto(text5)
        #self.enter()
        #self.objetos.append("Llaves de patrulla")
        

        #Recuerda que tu inventario es limitado. Solo puedes cargar con 5 objetos, asi que cuida muy bien lo que llevas encima.
        #Revisar inventario
        #Presionar tal tecla para soltar algun objeto
        #Escribir el nombre del objeto a soltar
        return
    
    def camino(self):
        track1 = "살인 계획 (A Murder Plan).mp3"

        pygame.mixer.music.load(track1)
        pygame.mixer.music.play()

    def ejecucion_juego(self):
        self.inicio()
        self.asignacion()
        self.tutorial()
        self.camino()
        
        

p = Juego()
pygame.init()
os.system('cls')
p.ejecucion_juego()

#Hacer .lower donde sea necesario


#Aqui ira el tutorial de comandos
#Avanzar, tomar objetos, soltar objetos, etc.

#Comandos: Agarrar o soltar objetos. Interrogar personas.