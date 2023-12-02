#Importante tener instalado pygame para poder ejecutar el juego. Pygame me sirvio para agregar musica.
#Si no se tiene instalado, abrir la terminal y escribir "pip install pygame". Asegurese de estar usando el interprete
#de python correcto en su entorno de trabajo.

#Cada funcion que requiere escribir un query lo transforma a minusculas, para que no haya distincion si escribes mayusculas o minusculas.

import pygame
import time
import sys
import os
import random

class Juego:
    #Constructores. Contienen nombre, apellido, genero, arte de objetos, inventario, comandos, numero de intentos, limite de objetos,
    #arrays de objetos en tutorial, biblioteca, baño, dormitorio, array de locaciones, entre otros mas
    #Son constructores ya que es importante que permanezcan durante todo el codigo, y sean modificables a lo largo de este.
    def __init__(self):
        self.locationorden = ""
        self.locations = []
        self.nombre = ""
        self.apellido = ""
        self.genero = ""
        self.pistas = 0
        self.decision1 = False
        self.llavecoche = 0
        self.carta = 0
        self.intentos = 10
        self.objetos = []
        self.objetossala = []
        self.objetosdormitorio = []
        self.objetosbaño = []
        self.objetosbiblioteca = []
        self.inventario = []
        self.inventariorespaldo1 = []
        self.mayordomointento = False
        self.mayordomovaso = False
        self.numerodeobjetosinventario = 0
        self.numerodeobjetosinventariorespaldo1 = 0
        self.limiteinventario = 5
        self.comandos = {'g':self.buscar_objetos, 'i':self.revisar_inventario_tutorial, 'l': self.lectura_carta, 's': self.soltar_objetos,}
        #Comandos que se ejecuten al escribir alguna de las letras cuando se pone la funcion ejecucion_comandos

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

        #Poner otro arte para carta anonima

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
        self.artesobrededinero = """                                           
                                      ......                                      
                                    ..::--::..                                    
                                ...:----------:...                                
                             ...:----------------:...                             
                          ...:----------------------:...                          
                      ....:----------------------------:....                      
                    ...:----------------------------------:...                    
                  .::----------------------------------------::..                 
         .......::------------------------------------====================-..     
         .=+++++*****************++++++++++++++++++++++++++++++++++++++++++..     
      ...=+++++*****************+++++++++++++++++++++++++++++++++++++++++++..     
    ...:=+++++=:::::::::::..........................................=++++++:..    
    :=-=+++++++============++++++++++++++++++++++++++++++++++++++++++++++*+==:.   
   .::-+*++++===========--------:::::::::::::::::::...............=++++***+-::..  
   .:---::+*=:......................:++++++-:......................-+**+::---:..  
   .:------::-=:.................=++++++++++++=:..................-=--:------:..  
   .:---------::-=:............-+++++++--+++++++-.............:-=-::---------:..  
   .:------------::-=-:.......-++++++=-...-=+++++=.........:-=-::------------:..  
   .:---------------::-=-....-++++++..:::=::++++++=......-=-::---------------:..  
   .:------------------::---:=++++++..-::++++++++++:.:---:-------------------:..  
   .:---------------------::-+*+=++++-...:=++++++++=--::---------------------:..  
   .:------------------------::-+*++=++:::..+++***-:-------------------------:..  
   .:----------------------------:-+*+=::=..**+-:----------------------------:..  
   .:-------------------------------::-=--==-:-------------------------------:..  
   .:------------------------------------::----------------------------------:..  
   .:---------------------------------::-------------------------------------:..  
   .:------------------------------::----------------------------------------:..  
   .:---------------------------::-------------------------------------------:..  
   .:------------------------::----------------------------------------------:..  
   .:--------------------::--------------------------------------------------:..  
   .:-----------------::-----------------------------------------------------:..  
   .:--------------::--------------------------------------------------------:..  
   .:-----------::-----------------------------------------------------------:..  
   .:--------::--------------------------------------------------------------:..  
   .:-----::-----------------------------------------------------------------:..  
    ..:::------------------------------------------------------------------:..    
     ........................................................................     
                                                                                  
        """
        self.artevaso = """                     
                              ........:::::::::......                             
                   ..-+++====-----------:::::::----::-===+++-..                   
                   =%%=....                             ...=#%=.                  
                  .:#..:=*#%%%#*==--::::::::----=+*#%%%%#+:..#-                   
                   .%:......:-=--------:::::::::::::::....:::#:                   
                   .%::                                .---+-%.                   
                   .#::                                .---*:%.                   
                    +-:                                .---+:*.                   
                    =+..                               .--====.                   
                    -#..                               .--+-+-                    
                    :#..                               .--+-#-                    
                    :#..                               .--+-#:                    
                    .#:.                               :-==:#:                    
                    .#=.:-=+****++==--:::...::--+*####*++++-#.                    
                    .#**...                           :#*:#=#.                    
                    .+**%%%###*=:................-=+**##%%#*#.                    
                     -#+%%--==..::--===========--:.....*#%**+.                    
                     :#-%%+-+=:.                      .*#%+*-                     
                     .%-%%*=+=:.                      .+#%=#:                     
                     .%-%%#=+=:.                      .=#%-%.                     
                     .*-#%#=+=:                       .=%%-%.                     
                      ==+%#=+=:                       .-%%-*.                     
                      -#=%#=+=:.                      ..%*==                      
                      -%-%%=+=:.                      ..%=*-                      
                      :%:%%++=:.                      .:%-#-                      
                      .#=#%=+=:.                      .-%:%:                      
                      .#*#%===:.                      .=%-#.                      
                      .***%+==:.                      .*#+#.                      
                      .-#+%+==:.                      .##**.                      
                       .%-%++=..           .  ..     .:%+#-                       
                       .%=#%#****#####%%%%#######****#%%-%.                       
                        +%*#%%%%#*++===-----==++*#%%%%#=%#.                       
                        -%*%++##%%#+=-::::--=+*#%%##+=%%#=.                       
                        :%#%%%%%%%%%%%####%%%%%%%%%%%%%*%-                        
                        .#%*%%%+.....    ..    ...-#%%###.                        
                         .-*#*######******##########*#*=.                         
                               ......::::::.......  ..                                                              
        """
        self.artecucaracha = """
.....................................................%..........................
...................................................:@=..........................
...................................................@@...........................
.............................-@%**=--:............**+...........................
................................+%#*%%%*.........:%%............................
.....................................-#*#*.......+@@............................
.......................................+#*@......**#............................
........................................+@%*.....#*#............................
........................................-*%......**#............................
............::......:*%%%@*@+...........**.......%#@.............*..............
..............%@@%%%-@%=..-@*#%........=##......@*@.............:#..............
.............................*%#%:.....##-....:%#*...............*:.............
..............................:*##@:..#*#.....%#+................:+.............
...................=#@%##***####%%%####*##%@#%%+................-%..............
................+@**@%######@@@@@@%*************%#.%%*........:@-...............
...............:#@#*#%@%@************************#@****#@@-:#%..................
.............%#*****#%@@%******************%@@@@@**%*****#*.....................
............=#*******@%*****#@@@@@@%%%@@@#***@@****@*****#%:....................
.............-@#*#@#****************************@*%*****@@-.-@=.................
................#%******************************%%#@%@#........%+...............
..................-+@@%%%******************%%@@=................:%..............
............................:-++*@%@++%%=.....@*%................*..............
...............................+%##....%*......#*%-..............%..............
.............................%#*%......*#-......*#*@.............%..............
..............-=#%%%@##+++*@*#%:.......:%#........%%@...........................
.............-.....:+@@@@@@@:...........**@.......#*@...........................
.........................................@*%......#*@...........................
.........................................:#*-.....:@@:..........................
..........................................+*%:.....@#:..........................
...........................................%@=.....#*-..........................
..........................................**%:......@%..........................
..........................................@@.........%*.........................
..........................................@...........#%........................
..........................................-.....................................
        """
        self.artecepillodedientes = """
               ...:------:.                                                                    
       .*@@@@%+*==*+*#%#%##@@.                                                                 
       .@.*.+:.+.*.-..%-..#.#-                                                                 
      .-@:#.*:.+.*.-..%-. #-%+.                                                                
      ..@.%.#..*.*.-..%-. #.%:.                         ...................::::::::::::...     
      .*@.%.#..*.*.=..%-. #.@@%=...........::-==+*#%@@@@@@@@@@%%%%%%%%%%@@@%%####******@@..    
     .@:@=%.*.:=.*.=..#-. %:@::::::+@@*+++++++++++=====================================##@.    
     -#::::=*%@@@%*#*#@@@%*-::::::+##===================================================*@.    
     .@:-::::::::::::::::::::::==--=@*%+=============**++++======================++*%+=+%*.    
     .+@@@+-*%@%#+===+#@%+%@@@:...............::=+#%@@@@@@@@@@@@@@@%%%%%#####%%%%@@@@@@@..     
         .....:--=====-:....                                           ..  ..       ..         
        """
        self.arteplaca = """
         @@@@@@              @@@@              @@@@@@         
       @@@%**%@@@@@@     @@@@@##@@@@@     @@@@@@%**%@@@       
     @@@%*=---=+#%@@@@@@@@@%+=---+#@@@@@@@@@%#+=---=*%@@@     
    @@@*--==*+==------------==++==------------==+*+=--*@@@    
    @@#=-=*@%%@@%#*==---=+*%@@@@@@%*+=---==+#%@@@%@*=-=#@@    
     @@#-=+@#--=+*#%@@@@@%#+=----=+#%@@@@@%#*+=--#@+=-#@@@    
     @@@+-=#%+----------------------------------+%#=-+@@@     
      @@#-=*@*----------------------------------*@*=-*@@      
      @@#-=*@*-----------=+*######*+=-----------*@*=-#@@      
      @@*-=*@*--------+#@@%#**++**#%@@#+--------+@#=-*@@      
     @@@=-+%%=------*@@#+=----------==#@@*------=%%+-=%@@     
     @@*-=*@#-----+%@*=------=#%=------=+#+------*@*=-*@@@    
    @@#--+@%=----*@#=--------%@@%--------=*@*----=%@+--#@@    
   @@%=-=%%+----+@#=--------#@**@#--------=#@*----+%%+-=%@@   
  @@@=-=#@*----=%%+--==++*#%@*--*@%#*++==--+%%+----+@#=-=%@@  
  @@+-=*@#-----+@*=-=%@@%#**+----+**#%@@%+-=*@*-----*@*=-+@@  
 @@%=-+@%------*@*---=*@%+----------+%@#=---+@#------#@+-=%@@ 
 @@#-=*@*------*@*-----=#@%=-------%@#=-----+@#------*@*=-*@@ 
 @@*-=#@+------+@*=-----=%@=-------@%=-----=*@*------+@#=-*@@ 
 @@*-=*@*------=#%+-----+@%--+%%+--%@+-----+%%=------+@*=-*@@ 
 @@%-=+@#-------+%%+----*@@@@@**@@@@@*----=%@+-------#@+=-#@@ 
  @@+-=#@*-------+%%+=--#@#==----==#@#--=+%%+-------+@#=-+@@  
  @@%=-=%@+-------=#@#+=-=----------=-==#@%=-------+%%+-=%@@  
   @@#===#@*--------=#@%*==--------==*%@%=--------*@%+==#@@   
    @@#=-=*@%*--------=+#@@%%####%%@@#+=--------+%@*=-=#@@    
     @@@*=-=*%@#*=---------=++**++=---------=+#@%*=-=+%@@     
      @@@%+--=+*%@@@%#+=--------------=+*%@@@%#+=-=+%@@@      
        @@#+*+=---==+#%@@%*=------=*%@@%#+==---=+*@@@@        
           @@@@%*+====--=*%@@*--*@@%*=--====+*%@@@@           
               @@@@@@@#==---+@@@@+---==#@@@@@@@               
                    @@@@@%*=-====-=+%@@@@@                    
                        @@@@#=--=#@@@@                        
                           @@@##@@@                           
                             @@@@                             
        """
        self.artereloj = """
                                                  
                .......::::::.....                
           .=%@@@@@@@%%######%@@@%.               
           .#@+%++++++++++++++#**@.               
           .#%+*++++++++++++++##*@.               
            =@+%#+++++++++++++##*@.               
            -@+++++++++++++++++**@.               
            :@*@%+++++++++++++*@*@:               
            .@#++++++++++++++++++%-               
            .@###++++++++++++++@*%+..             
         .#@@@#++++++++++++++++++%@%@+.           
         .@*=@##%++#%@@@@@@@#*+%%%@-%*.           
         .##-@@@@%#*+****+===+#%@@@+%*..          
          +@@%+=#@@%+-::::=*%@@@%+=*@@-.          
       .-%%++#@*-:.....-=.:::::::+@#==#@-.        
     .-@%==@%:::::.....%%::.....:-:-%%=-%#.       
    .*%==%%-:::-@#......:::....+%-:.:=%+=#@:.     
   .#@=*@=:.....::...................::@%=*#.     
   +@=*@-:...........................:=:%*=#+     
  -@+=%=:#@*:.::.................:=%-*-.-@=+@:    
 .%#=*#:.::-:.:#%=.............:%#-:.:..:#%-%*.   
 :@+-@+.........:*@#:......:=*%=..::.....+@=+@@@. 
 -@==@=...........:=@%:..:#@=:..........:=@=-@%@- 
 -@=+@-=++=..........:##@#:...........:++=@+-%#@= 
 :@++@=::.:.........:@%:-@@:.............=@=-@#@+ 
 .@#=@+:............:::...:-:............+@=+%+=. 
  =%=*#:.................................##-%*.   
  .#*=%=...-+:.....................-*-..=%=+@:.   
  .-@++@=:##-......................:-#=-@+=%=..   
  ..=@++@*:..........................:+@+-%+.     
    .-@*=#@-:...=+.............*#:..:#%==%=..     
     ..%@+=@%:.=%:.....:-=......-::+@+-#%:...     
        :%%+*%%+-.......-*.....:=%@*=#%-..        
        ..@@@=-=%@@%*-::=+*#@@@@+-=@@@-.          
         .@*=%@#+=-==++++===---+#@@#-@=.          
         .@*-+@*@@@@@@@@%%%@@@%*@*@#-%=.          
         .#@@@%+%*++++++++++++++*+@@@@-.          
             -@*++++++++++++++++*+@*....          
             :@*%#++++++++++++++%*%*.             
             :@*++++++++++++++++*+%*.             
             :@*#*++++++++++++++####.             
             .%*#*++++++++++++++++*#.             
             .#*++++++++++++++++##+%:             
             .#*@#++++++++++++++++#%.             
             .%*%#**************%@@*.             
             .:-----------------:...              
        """
        self.artelinterna = """
.....................................................................
.....................................-##-............................
....................................=@*+#@%=.........................
...................................+@+***+=#@%=......................
..................................+@+-=*+-+#%+#@%=:..................
.................................*@+------*#+-=**#%%+:...............
................................*%=----------=*#*--##%%*-............
...............................+@@%*--------------%+#==*%@*-.........
...............................*@+=*@@#------------=--#=%=%#:........
...............................+@+====*@@#------------=#-%%:.........
...............................+@+=======*%@#=---------=@%...........
..............................:%@@@#+=======*%@#+-----=@#............
.............................-%%--=#@@#*=======+#@%+-+@+.............
............................-%#------=*@@%*=======+#@@=..............
...........................-%*----------=*@@@*===*@@#-...............
..........................-@*---------------+@@@@=...................
.........................=@*-----------------%#:.....................
........................*@+----------------=@*.......................
.......................*@=----------------+@*........................
.....................:*%=----------------+@+.........................
....................:#%=----+@@@%=------*@=..........................
....................%%=----*@=.:@#-----*@=...........................
..................:@#-----*@=.-@%-----#%-............................
.................-@#------#%++@#-----#%-.............................
................=@*--------=**+----=%%:..............................
...............=@+----------------=%#................................
..............=@+----------------=%*:................................
.............*@+----------------=@*..................................
............#@*----------------=@*...................................
..........:#@*%@%+------------+@+....................................
..........*@++++*#@%*=-------*@-.....................................
..........*%++++++++#%%*=---*%-......................................
..........:%@#+++++++++*@@##%-.......................................
............:+@@#+++++++++%%-........................................
................+@@#+++++@%:.........................................
...................=%@@@%+...........................................
.....................................................................
        """
        self.artecorbata = """
..................................................
.............-*+++++++++++++++-=+++++:............
.............-*************+-:+*****+:............
..............=#*********+-:=*******-.............
...............+*******+=:=+*******=..............
................+****+=:=+********-...............
.................:**+:-+*******#=.................
...................**%@%%%%%%##:..................
..................=*************..................
.................:**************=.................
.................+************+:=:................
................=***********+:-+*+................
...............:+*********+:-+****-...............
...............=********+--+******+...............
..............:+******+-:=+********-..............
..............=*****+=:=+**********+:.............
.............:****+=:=+*************-.............
.............=#*+=:=+***************=.............
............:**=:-+******************:............
............-*--++****************+==-............
............+-++*****************+:-+*:...........
...........:#+*****************+-:++*#-...........
...........=*****************+-:+*****+...........
...........****************+-:+*******#...........
..........:#*************+=:=+********#-..........
..........=************+=:=+***********+..........
..........***********+=--+*************#..........
..........%*********+--+***************%..........
.........:#*******+-:+*****************#-.........
.........=******+-:=******************+++.........
.........+****+=:=+*****************+=:-*.........
.........***+=:=+*****************+=:-+**.........
.........**=:-+******************+::++**#.........
.........*:-+******************+-:=+****#.........
.........*+******************+-:=+******#.........
.........#*****************+-.=+*********.........
.........****************+-:=+**********+.........
.........+**************=:-+***********#-.........
..........-#**********+:-+**************..........
............+#******+::+*************+:...........
.............:+***+::+**************:.............
...............-*-:=**************:...............
.................=**************:.................
...................=**********:...................
.....................:+*+*+-......................
        """
        
        #Cambiar arte de carta cuando ya tengas la linterna

    #Funcion que toma un query como parametro, que si se encuentra en self.comandos manda a dicha funcion, y si no
    #pone un while hasta que se escriba un comando valido.
    def ejecucion_comandos(self, query):
        query = query.lower()
        if query in self.comandos:
            self.comandos[query]()
        else:
            query = input(f"Comando '{query}' no válido. Introduce otro: ")
            self.ejecucion_comandos(query)

    #Game over durante el caso 1. Muestra el arte y reinicia el caso si presionas a o el juego si presionas b.
    #Usa auxiliar guardado para reinciar los datos a como estaban cuando empezaste el caso.
    def gameovercaso1(self):
        os.system('cls')
        track1 = "풀리지 않는 의문 Unanswered question.mp3"
        pygame.mixer.music.load(track1)
        pygame.mixer.music.play()
        text = """
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                           
        """
        self.mostrar_arte(text, 0.01)
        self.enter()
        text1 = "Agotaste tu numero de intentos sin tener los objetos necesarios en tu inventario."
        print("\n")
        self.mostrar_texto(text1)
        self.enter()
        orden = input("\n¿Que deseas hacer? Escribe a para reiniciar el caso, b para terminar la partida. ")
        orden = orden.lower()
        while orden != "a" and orden != "b":
            orden = input("\nEscriba bien. ")
            orden = orden.lower()
        if orden == "a":
            os.system('cls')
            self.auxiliarguardado()
            self.caso1()
            self.resolucion_caso()
            #escribir lo que este abajo en ejecucionjuego
            sys.exit()
        if orden == "b":
            os.system('cls')
            self.inicio()
            self.asignacion()
            self.tutorial()
            self.camino()
            self.auxiliarguardado()
            self.caso1()
            self.resolucion_caso()
            sys.exit()

    def gameoverresolucion(self):
        os.system('cls')
        track1 = "풀리지 않는 의문 Unanswered question.mp3"
        pygame.mixer.music.load(track1)
        pygame.mixer.music.play()
        text = """
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                           
        """
        self.mostrar_arte(text, 0.01)
        self.enter()
        text1 = "Arrestaste a la persona equivocada."
        print("\n")
        self.mostrar_texto(text1)
        self.enter()
        orden = input("\n¿Que deseas hacer? Escribe a para reiniciar el caso, b para terminar la partida. ")
        orden = orden.lower()
        while orden != "a" and orden != "b":
            orden = input("\nEscriba bien. ")
            orden = orden.lower()
        if orden == "a":
            text = "Revisa bien las pistas y descripciones que se te dan en esta ocasión."
            self.parpadeo(text, 5)
            os.system('cls')
            self.auxiliarguardado()
            self.caso1()
            self.resolucion_caso()
            #escribir lo que este abajo en ejecucionjuego
            sys.exit()
        if orden == "b":
            os.system('cls')
            self.inicio()
            self.asignacion()
            self.tutorial()
            self.camino()
            self.auxiliarguardado()
            self.caso1()
            self.resolucion_caso()
            sys.exit()

    

        #Estas funciones despliegan las descripciones de los 4 lugares, dependiendo de cual sea llamada.
    def descripcionbaño(self):
        text = """
El lugar exhibe una elegancia simple con azulejos blancos y detalles bien ordenados. La suave luz realza el orden y la limpieza, con toallas dobladas y una agradable fragancia en el aire.

Pero al mirar el espejo sobre el lavamanos, algo parece fuera de lugar. Las imágenes reflejadas se distorsionan sutilmente, creando una sensación de inquietud. En la penumbra, las sombras danzan de manera intrigante, sugiriendo que quizás hay más en este espejo de lo que parece a simple vista.
        """
        print("\n")
        print(text)
        print("\n")

    def descripcionsala(self):
        text = """
El lugar lleva las cicatrices de un acto violento. Aunque el cuerpo del Ministro ha sido retirado, el ambiente conserva la pesadez de los eventos recientes. Manchas de sangre que se aferran tenazmente a la alfombra y a los muebles, resistiéndose a ser olvidadas.

El mobiliario elegante yacía desplazado, como si la sala hubiera sido escenario de un conflicto interno. La luz tenue, filtrándose por las cortinas cerradas, acentúa la solemnidad del lugar. Huellas de la investigación policial son visibles, marcadas por cintas amarillas que delimitan áreas de interés.

A pesar de los esfuerzos por limpiar y restaurar la normalidad, la sala de estar sigue resonando con el eco del crimen. El susurro de la tragedia persiste en las sombras, invitando a la reflexión sobre lo que una vez fue un espacio de confort, ahora manchado por la violencia.
        """
        print("\n")
        print(text)
        print("\n")

    def descripciondormitorio(self):
        text = """
Una estancia opulenta que refleja la elegancia y el poder que caracterizaban la posición del ministro. Las paredes están revestidas con una rica tapicería, y una cama majestuosa, coronada por dosel, ocupa el centro del espacio.

En el rincón del dormitorio, el mayordomo del ministro se encuentra discretamente en espera, listo para atender cualquier necesidad que pueda surgir. Su presencia, siempre vigilante, agrega una capa de misterio a la lujosa atmósfera del dormitorio.
        """
        print("\n")
        print(text)
        print("\n")

    def descripcionbiblioteca(self):
        text = """
Llegó a ser un rincón de conocimiento ordenado, ahora yace en un estado caótico. Montones de libros yacen desplomados en el suelo, sus páginas revelando la huella de un caos reciente. Entre las estanterías desorganizadas, títulos respetados yacen dispersos, como testigos silenciosos de un disturbio literario.

En el centro de la sala, la caja fuerte, símbolo de secretos bien guardados, ha sido violentamente forzada. Las marcas de intentos desesperados por abrirla son evidentes, todo para que esta fuera cerrada de nuevo.

En tus manos está recabar las pistas necesarias. Parece ser que este es un lugar importante.
        """
        print("\n")
        print(text)
        print("\n")


    #Permite cambiar de locacion en el caso. Hay tantos ifs ya que programa comandos diferentes para cada locacion.
    #Entra en un bucle que repite ejecucion de comandos hasta que se tienen los 3 objetos necesarios.
    #Además, llama a la funcion gameover si se acaban tus intentos y aun no tienes los items necesarios.
    def cambiar_posicion(self):
        print("\nLocaciones disponibles:")
        print(f"{self.locations}")
        print("\n")
        self.locationorden = input("Escribe una locacion a la que cambiar: ")
        self.locationorden = self.locationorden.lower()
        while self.locationorden not in self.locations:
            self.locationorden = input("Escriba bien. ")
        if self.locationorden == "sala de estar":
            os.system('cls')
            print("\tUbicacion: Sala del departamento del ministro\tHora: 10:30 pm")
            print("\nRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tHablar con el capitan = c")
            print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
            print("\n")
            self.descripcionsala()
            self.comandos = {'i':self.revisar_inventario, 's': self.soltar_objetos, 'p': self.cambiar_posicion, 'c': self.hablarconcapitan,}
            query = input("¿Que quieres hacer? Escribe un comando: ")
            query = query.lower()
            self.ejecucion_comandos(query)
            while "carta anonima" not in self.inventario or "sobre con dinero" not in self.inventario or "vaso de cristal" not in self.inventario:
                if "carta anonima" in self.inventario and "sobre con dinero" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Sala del departamento del ministro\tHora: 10:30 pm")
                    print("\nRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tHablar con el capitan = c")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "carta anonima" in self.inventario and "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Sala del departamento del ministro\tHora: 10:30 pm")
                    print("\nRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tHablar con el capitan = c")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "sobre con dinero" in self.inventario and "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Sala del departamento del ministro\tHora: 10:30 pm")
                    print("\nRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tHablar con el capitan = c")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "carta anonima" in self.inventario or "sobre con dinero" in self.inventario or "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Sala del departamento del ministro\tHora: 10:30 pm")
                    print("\nRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tHablar con el capitan = c")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás mas cerca de resolver este caso. ¿Qué quieres hacer?")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if self.intentos <= 0:
                    self.gameovercaso1()
                if self.decision1 == True:
                    return
                else: 
                    os.system('cls')
                    print("\tUbicacion: Sala del departamento del ministro\tHora: 10:30 pm")
                    print("\nRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tHablar con el capitan = c")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
            os.system('cls')
            text = "Haz recabado las pistas necesarias. Dirigete con el capitán Fitzgerald."
            self.mostrar_texto(text)
            self.enter()
            query = input()
            self.ejecucion_comandos(query)
        
        if self.locationorden == "biblioteca":
            os.system('cls')
            print("\tUbicacion: Biblioteca del departamento del ministro\tHora: 10:30 pm")
            print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
            print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
            print("\n")
            self.descripcionbiblioteca()
            self.comandos = {'g':self.buscar_objetos_biblioteca, 'i':self.revisar_inventario, 's': self.soltar_objetos, 'p': self.cambiar_posicion,}    
            query = input("¿Que quieres hacer? Escribe un comando: ")
            query = query.lower()
            self.ejecucion_comandos(query)
            while "carta anonima" not in self.inventario or "sobre con dinero" not in self.inventario or "vaso de cristal" not in self.inventario:
                if "carta anonima" in self.inventario and "sobre con dinero" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Biblioteca del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "carta anonima" in self.inventario and "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Biblioteca del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "sobre con dinero" in self.inventario and "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Biblioteca del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "carta anonima" in self.inventario or "sobre con dinero" in self.inventario or "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Biblioteca del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás mas cerca de resolver este caso. ¿Qué quieres hacer?")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if self.intentos <= 0:
                    self.gameovercaso1()
                else: 
                    os.system('cls')
                    print("\tUbicacion: Biblioteca del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
            os.system('cls')
            text = "Haz recabado las pistas necesarias. Dirigete con el capitán Fitzgerald."
            self.mostrar_texto(text)
            self.enter()
            query = input()
            self.ejecucion_comandos(query)
        
        if self.locationorden == "dormitorio":
            #Puedes interrogar al mayordomo. Este te dice que ese dia era su descanso. Este se pone nervioso si le preguntas por el vaso.
            #Objetos: vaso, linterna, traje del ministro
            os.system('cls')
            print("\tUbicacion: Dormitorio del departamento del ministro\tHora: 10:30 pm")
            print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tInterrogar al mayordomo = m")
            print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
            print("\n")
            self.descripciondormitorio()
            self.comandos = {'g':self.buscar_objetos_dormitorio, 'i':self.revisar_inventario, 's': self.soltar_objetos, 'p': self.cambiar_posicion, 'm': self.interrogarmayordomo,}    
            query = input("¿Que quieres hacer? Escribe un comando: ")
            query = query.lower()
            self.ejecucion_comandos(query)
            while "carta anonima" not in self.inventario or "sobre con dinero" not in self.inventario or "vaso de cristal" not in self.inventario:
                if "carta anonima" in self.inventario and "sobre con dinero" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Dormitorio del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tInterrogar al mayordomo = m")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "carta anonima" in self.inventario and "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Dormitorio del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tInterrogar al mayordomo = m")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "sobre con dinero" in self.inventario and "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Dormitorio del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tInterrogar al mayordomo = m")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "carta anonima" in self.inventario or "sobre con dinero" in self.inventario or "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Dormitorio del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tInterrogar al mayordomo = m")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás mas cerca de resolver este caso. ¿Qué quieres hacer?")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if self.intentos <= 0:
                    self.gameovercaso1()
                else: 
                    os.system('cls')
                    print("\tUbicacion: Dormitorio del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p\tInterrogar al mayordomo = m")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
            os.system('cls')
            text = "Haz recabado las pistas necesarias. Dirigete con el capitán Fitzgerald."
            self.mostrar_texto(text)
            self.enter()
            query = input()
            self.ejecucion_comandos(query)
        
        
        if self.locationorden == "baño":
            os.system('cls')
            print("\tUbicacion: Baño del departamento del ministro\tHora: 10:30 pm")
            print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
            print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
            self.descripcionbaño()
            self.comandos = {'g':self.buscar_objetos_baño, 'i':self.revisar_inventario, 's': self.soltar_objetos, 'p': self.cambiar_posicion,}    
            query = input("¿Que quieres hacer? Escribe un comando: ")
            query = query.lower()
            self.ejecucion_comandos(query)
            while "carta anonima" not in self.inventario or "sobre con dinero" not in self.inventario or "vaso de cristal" not in self.inventario:
                if "carta anonima" in self.inventario and "sobre con dinero" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Baño del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "carta anonima" in self.inventario and "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Baño del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "sobre con dinero" in self.inventario and "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Baño del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás a punto de resolver el caso. Sigue recabando pistas. ¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if "carta anonima" in self.inventario or "sobre con dinero" in self.inventario or "vaso de cristal" in self.inventario:
                    os.system('cls')
                    print("\tUbicacion: Baño del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("Estás mas cerca de resolver este caso. ¿Qué quieres hacer?")
                    query = query.lower()
                    self.ejecucion_comandos(query)
                if self.intentos <= 0:
                    self.gameovercaso1()
                else: 
                    os.system('cls')
                    print("\tUbicacion: Baño del departamento del ministro\tHora: 10:30 pm")
                    print("\nBuscar objetos = g\tRevisar inventario = i\tSoltar objetos = s\tCambiar de locacion = p")
                    print(f"\nIntentos para buscar objetos restantes = {self.intentos}")
                    print("\n")
                    query = input("¿Qué quieres hacer? ")
                    query = query.lower()
                    self.ejecucion_comandos(query)
            os.system('cls')
            text = "Haz recabado las pistas necesarias. Dirigete con el capitán Fitzgerald."
            self.mostrar_texto(text)
            self.enter()
            query = input()
            self.ejecucion_comandos(query)
        
            #definir comandos con otras funciones, que trabajen con self.objetossala de estar y asi
            #Tambien inspeccionar objetos a otra funcion, que tenga sus respectivos minijuegis, o no

    #Funcion de buscar objetos. Trabaja durante el tutorial. Va reduciendo intentos cada que la usas.
    #Si escoges recoger un objeto, lo pone en tu inventario y lo quita de self.objetos
    def buscar_objetos(self):
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


    def buscar_objetos_dormitorio(self):
        if self.intentos > 0:
            self.intentos -= 1
            print("\nObjetos disponibles: ")
            print(f"{self.objetosdormitorio}")
            orden = input("\nEscribe el nombre del objeto a recoger. Si quieres cancelar, escribe 'c': ")
            orden = orden.lower()
            while orden not in self.objetosdormitorio and orden != "c":
                orden = input("Escriba bien: ")
                orden = orden.lower()
            if self.numerodeobjetosinventario <= 5:
                if orden != "c":
                    self.numerodeobjetosinventario +=1
                    self.objetosdormitorio.remove(orden)
                    self.inventario.append(orden)
                    if orden == "vaso de cristal":
                        print ("\n")
                        self.mostrar_arte(self.artevaso, 0.001)
                        if self.mayordomovaso == True:
                            text = "Un vaso de cristal con agua, manchado. Parecen huellas dactilares."
                        else:
                            text = "Un vaso de cristal con agua."
                        print("\n\n",text)
                        self.enter()
                    if orden == "corbata":
                        print("\n")
                        self.mostrar_arte(self.artecorbata, 0.001)
                        print ("\n\nCorbata que pertenecía al ministro.")
                        self.enter()
                    if orden == "linterna":
                        print("\n")
                        self.mostrar_arte(self.artelinterna, 0.001)
                        print("\n\nUna simple linterna.")
                        self.enter()
                else:
                    pass
            else:
                print("Tu inventario esta lleno. Tendras que soltar algun objeto para recoger otro.")
                  
        else:
            print("\nNumero de intentos para buscar objetos agotado.")


    #Funcion de buscar objetos enfocada a la biblioteca. Trabaja con los objetos de ese lugar y pone el juego deL mensaje del espejo.
    def buscar_objetos_baño(self):
        if self.intentos > 0:
            self.intentos -= 1
            if self.espejo():
                text = "Buscando debajo de la alcantarilla."
                self.parpadeo(text, 5)
                print("\nObjetos disponibles: ")
                print(f"{self.objetosbaño}")
                orden = input("\nEscribe el nombre del objeto a recoger. Si quieres cancelar, escribe 'c': ")
                orden = orden.lower()
                while orden not in self.objetosbaño and orden != "c":
                    orden = input("Escriba bien: ")
                    orden = orden.lower()
                if self.numerodeobjetosinventario <= 5:
                    if orden != "c":
                        self.numerodeobjetosinventario +=1
                        self.objetosbaño.remove(orden)
                        self.inventario.append(orden)
                        if orden == "sobre con dinero":
                            print ("\n")
                            self.mostrar_arte(self.artesobrededinero, 0.001)
                            print ("\n\nEs sospechoso...")
                            self.enter()
                            print ("\n¿Por qué habria un sobre con dinero escondido aqui?")
                            self.enter()
                            return
                        if orden == "cepillo de dientes":
                            print("\n")
                            self.mostrar_arte(self.artecepillodedientes, 0.001)
                            print("\n\n¿Este cepillo pertenecia al ministro?...")
                            self.enter()
                            return
                        if orden == "cucaracha":
                            print("\n")
                            self.mostrar_arte(self.artecucaracha, 0.001)
                            print("\n\nAsqueroso.")
                            self.enter()
                            return
                    else:
                        pass
                else:
                    print("Tu inventario esta lleno. Tendras que soltar algun objeto para recoger otro.")
            else:
                pass        
        else:
            print("\nNumero de intentos para buscar objetos agotado.")
        

    #Funcion de buscar objetos enfocada a la biblioteca. Trabaja con los objetos de ese lugar y pone el juego de la caja fuerte.
    def buscar_objetos_biblioteca(self):
        if self.intentos > 0:
            self.intentos -= 1
            if self.jugar_adivina_el_numero():
                print("\nObjetos disponibles: ")
                print(f"{self.objetosbiblioteca}")
                orden = input("\nEscribe el nombre del objeto a recoger. Si quieres cancelar, escribe 'c': ")
                orden = orden.lower()
                while orden not in self.objetosbiblioteca and orden != "c":
                    orden = input("Escriba bien: ")
                    orden = orden.lower()
                if self.numerodeobjetosinventario <= 5:
                    if orden != "c":
                        self.numerodeobjetosinventario +=1
                        self.objetosbiblioteca.remove(orden)
                        self.inventario.append(orden)
                        if orden == "carta anonima":
                            print ("\n")
                            self.mostrar_arte(self.artecarta, 0.001)
                            print ("\n\nRevisa la carta anonima en tu inventario si quieres leerla.")
                            self.enter()
                            return
                        if orden == "reloj costoso":
                            print("\n")
                            self.mostrar_arte(self.artereloj, 0.001)
                            print ("\n\nReloj marca Tag Heuer.")
                            self.enter()
                        if orden == "placa":
                            print("\n")
                            self.mostrar_arte(self.arteplaca, 0.001)
                            print("\n\n¿El ministro tenía una placa?")
                            self.enter()
                    else:
                        pass
                else:
                    print("Tu inventario esta lleno. Tendras que soltar algun objeto para recoger otro.")
            else:
                pass        
        else:
            print("\nNumero de intentos para buscar objetos agotado.")
        


        #Monton de libros tirados y desorden. Y en medio de todo, la caja fuerte. Esto revela que pudo ser abierta recientemente.

    def jugar_adivina_el_numero(self):
        numero_secreto = random.randint(1, 100)
        intentos = 0
        max_intentos = 7

        print("\n\nSera necesario que adivines la contraseña para inspeccionar la caja fuerte. Esta solo admite un numero entre el 1 y 100.")
        self.enter()
        print(f"Prueba con diferentes numeros. Llevas contigo un sistema que detectara si nos estamos acercando o no.")
        self.enter()
        print(f"Tienes {max_intentos} antes de que la caja fuerte se bloquee. En dicho caso, tendras que volver a intentarlo y gastar otro intento de buscar objetos.")
        self.enter()

        while intentos < max_intentos:
            try:
                intento = int(input("Ingrese la contraseña: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue  # Vuelve al inicio del bucle para solicitar una entrada válida

            if intento == numero_secreto:
                print(f"Contraseña correcta. Bienvenido señor Noiré. Aqui estan sus elementos.")
                return True
            elif intento < numero_secreto:
                print(f"La contraseña es mayor. Te quedan {max_intentos-intentos} intentos.")
            else:
                print(f"La contraseña es menor. Te quedan {max_intentos-intentos} intentos.")

            intentos += 1

        if intentos == max_intentos:
            print(f"\nCaja fuerte bloqueada después de {max_intentos} intentos fallidos.")
            return False
        

    #Minijuego del espejo. El mensaje correcto es revisa debajo de la alcantarilla. En el espejo aparece con
    #las silabas cambiadas. Si lo adivinas, puedes buscar los objetos debajo de la alcantarilla y pierdes
    #un intento. Si no lo adivinas, no puedes revisar y pierdes un intento.    
    def espejo (self):
        print("\nEste espejo es bastante extraño....\n")
        arteespejo = """
 .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+. 
(      ▌ ▐·▪  .▄▄ ·  ▄▄▄· ▄▄▄  ▄▄▄ .    ▄▄▄▄·  ▄▄▄· ·▄▄▄▄  ▄▄▄ . ▐▄▄▄          ·▄▄▄▄  ▄▄▄ .       )
 )    ▪█·█▌██ ▐█ ▀. ▐█ ▀█ ▀▄ █·▀▄.▀·    ▐█ ▀█▪▐█ ▀█ ██▪ ██ ▀▄.▀·  ·██▪         ██▪ ██ ▀▄.▀·      ( 
(     ▐█▐█•▐█·▄▀▀▀█▄▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄    ▐█▀▀█▄▄█▀▀█ ▐█· ▐█▌▐▀▀▪▄▪▄ ██ ▄█▀▄     ▐█· ▐█▌▐▀▀▪▄       )
 )     ███ ▐█▌▐█▄▪▐█▐█ ▪▐▌▐█•█▌▐█▄▄▌    ██▄▪▐█▐█ ▪▐▌██. ██ ▐█▄▄▌▐▌▐█▌▐█▌.▐▌    ██. ██ ▐█▄▄▌      ( 
(     . ▀  ▀▀▀ ▀▀▀▀  ▀  ▀ .▀  ▀ ▀▀▀     ·▀▀▀▀  ▀  ▀ ▀▀▀▀▀•  ▀▀▀  ▀▀▀• ▀█▄▀▪    ▀▀▀▀▀•  ▀▀▀        )
 )    ▄▄▌   ▄▄▄·      ▄▄·  ▄▄▄·  ▐ ▄  ▄▄▄· ▄▄▌  ▄▄▄  ▪  ▄▄▄▄▄ ▄▄▄· ▄▄▌  ▄▄▌   ▄▄▄·               ( 
(     ██•  ▐█ ▀█     ▐█ ▌▪▐█ ▀█ •█▌▐█▐█ ▀█ ██•  ▀▄ █·██ •██  ▐█ ▀█ ██•  ██•  ▐█ ▀█                )
 )    ██▪  ▄█▀▀█     ██ ▄▄▄█▀▀█ ▐█▐▐▌▄█▀▀█ ██▪  ▐▀▀▄ ▐█· ▐█.▪▄█▀▀█ ██▪  ██▪  ▄█▀▀█               ( 
(     ▐█▌▐▌▐█ ▪▐▌    ▐███▌▐█ ▪▐▌██▐█▌▐█ ▪▐▌▐█▌▐▌▐█•█▌▐█▌ ▐█▌·▐█ ▪▐▌▐█▌▐▌▐█▌▐▌▐█ ▪▐▌               )
 )    .▀▀▀  ▀  ▀     ·▀▀▀  ▀  ▀ ▀▀ █▪ ▀  ▀ .▀▀▀ .▀  ▀▀▀▀ ▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀  ▀  ▀               ( 
(                                                                                                 )
 "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+" 
        """
        self.mostrar_arte(arteespejo, 0.001)
        self.enter()
        print("\nNo tiene nada de extraño. Mas bien contiene un mensaje cifrado. ¿Eres capaz de descifrarlo?")
        query = input("\nEscribe el mensaje descifrado: ")
        query = query.lower()
        if query == "revisa debajo de la alcantarilla":
            print("\nMensaje descifrado.")
            self.enter()
            os.system('cls')
            return True
        else: 
            print("\nMensaje incorrecto.")
            self.enter()
            os.system('cls')
            return False


    def hablarconcapitan(self):
        if "sobre con dinero" in self.inventario and "vaso de cristal" in self.inventario and "carta anonima" in self.inventario:
            self.decision1 = True
            print("\n")
            text = f"Me sorprende el nivel de percepción que tienes, detective {self.apellido}. Lograste recabar las pistas necesarias. Acompañame, vamos a descifrar todo esto."
            self.mostrar_texto(text)
            self.enter()
            self.resolucion_caso()
            

        if "carta anonima" in self.inventario and "sobre con dinero" in self.inventario:
            print("\n")
            text = f"Tienes 2 pistas necesarias para resolver este caso, detective {self.apellido}. Te falta una. Sigue buscando."
            self.mostrar_texto(text)
            self.enter()
            return
        if "carta anonima" in self.inventario and "vaso de cristal" in self.inventario:
            print("\n")
            text = f"Tienes 2 pistas necesarias para resolver este caso, detective {self.apellido}. Te falta una. Sigue buscando."
            self.mostrar_texto(text)
            self.enter()
            return
        if "sobre con dinero" in self.inventario and "vaso de cristal" in self.inventario:
            print("\n")
            text = f"Tienes 2 pistas necesarias para resolver este caso, detective {self.apellido}. Te falta una. Sigue buscando."
            self.mostrar_texto(text)
            self.enter()
            return
        if "carta anonima" in self.inventario or "sobre con dinero" in self.inventario or "vaso de cristal" in self.inventario:
            print("\n")
            if self.genero == "h":
                text = f"Tienes 1 pista necesaria para resolver este caso, novato. No tenemos todo el tiempo del mundo. Sigue buscando por más pistas."
            else:
                text = f"Tienes 1 pista necesaria para resolver este caso, novata. No tenemos todo el tiempo del mundo. Sigue buscando por más pistas."
            self.mostrar_texto(text)
            self.enter()
            return
        
            
        else: 
            print("\n")
            text = f"Deja de perder el tiempo, {self.apellido}. Ponte a recabar las pistas que necesitemos."
            self.mostrar_texto(text)
            self.enter()
            return
            


    def interrogarmayordomo(self):
        print("\n")
        text1 = f"Detective {self.nombre} {self.apellido}: Buenas noches, señor mayordomo. Quisiera hacerle unas preguntas para avanzar en la resolucion del caso. ¿Quiere cooperar conmigo?"
        self.mostrar_texto(text1)
        self.enter()
        print("\n")
        text2 = f"Mayordomo: .........."
        self.mostrar_texto(text2)
        self.enter()
        print("\n")
        text3 = f"Detective {self.nombre} {self.apellido}: Le pido una disculpa. Se que esto puede resultar duro para usted, pero necesito de su cooperacion para avanzar en la resolución de este caso."
        self.mostrar_texto(text3)
        self.enter()
        print("\n")
        text4 = f"Mayordomo: S..s....s..si...está bien...pregunte lo que sea necesario, señor oficial."
        self.mostrar_texto(text4)
        self.enter()
        print("\n")
        text5 = f"Detective {self.nombre} {self.apellido}: ¿Cómo se llama para empezar?"
        self.mostrar_texto(text5)
        self.enter()
        print("\n")
        text6 = f"Mayordomo: Mi nombre es Sebastian. Sebastian Blackwell."
        self.mostrar_texto(text6)
        self.enter()
        print("\n")
        text7 = f"Detective {self.nombre} {self.apellido}: Muy bien, Sebastian. Procedamos con esto."
        self.mostrar_texto(text7)
        self.enter()
        print("\n")
        print("\n")
        text8 = f"----Posees de preguntas diferentes para hacerle al mayordomo, pero solo podrás seleccionar 2. Piensa cautelosamente lo que vayas a preguntar, ya que estos son tus unicos 2 intentos."
        self.mostrar_texto(text8)
        print("\nPresiona enter 3 veces para continuar.")
        self.enter()
        self.enter()
        self.enter()
        os.system('cls')
        print("Escribe a para preguntar sobre su relación con el ministro")
        #Habla sobre los cercanos que eran y como hoy era su dia libre.
        #print("\nEscribe b para preguntar sobre el vaso de cristal en la repisa.")
        #Se pone nervioso ya que el no se encontraba allí, pero tiene sus huellas. Poner en true self.mayordomo
        print("\nEscribe b para preguntar sobre el atentado y donde se encontraba el cuando ocurrió.")
        #Hoy era su dia libre
        print("\nEscribe c para preguntar si sabe si el ministro había recibido amenazas.")
        #No
        query = input("\nEscribe una opcion: ")
        while query != "a" and query != "b" and query != "c":
            query = input("Escriba bien. ")
        if query == "a":
            text2 = f"Mayordomo Sebastian Blackwell: He sido su mayordomo desde hace más de 10 años. Siento que en cierta medida, llegue a ser como un hermano para él. Pero todo esto tuvo que pasar justo hoy, en mi día de descanso."
            print("\n")
            self.mostrar_texto(text2)
            self.enter()
            text3 = f"Desearía haber podido hacer más."
            self.mostrar_texto(text3)
            self.enter()
            print("\n")
            print("Escribe a para preguntar sobre el vaso de agua en la repisa.")
            print("\nEscribe b para preguntar si sabe si el ministro había recibido amenazas.")
            query = input("\nEscribe una opcion: ")
            while query != "a" and query != "b":
                query = input("Escriba bien. ")
            if query == "a":
                text2 = f"Detective {self.nombre} {self.apellido}: Ese vaso de agua, ¿Ya estaba aquí cuando llegaste?"
                print("\n")
                self.mostrar_texto(text2)
                self.enter()
                text3 = f"Mayordomo Sebastian Blackwell: No tiene nada de importante. Yo no lo revisaría si fuera tu. En serio, no es nada..."
                self.mostrar_texto(text3)
                self.enter()
                print("\n")
                self.mayordomointento = True
                self.mayordomovaso = True
            if query == "b":
                print("\n")
                text2 = f"Mayordomo Sebastian Blackwell: No que yo supiera. El ministro nunca me contó nada sobre una posible conspiración en su contra, o sobre haber recibido amenazas."
                self.mostrar_texto(text2)
                self.enter()
                text3 = f"Tampoco parecía que alguien del departamento de policia o del gobierno estuviera en su contra. No tengo idea de quien pueda estar detrás de esto..."
                self.mostrar_texto(text3)
                self.enter()
                print("\n")  
                self.mayordomointento = True
        if query == "b":
            print("\n")
            text2 = f"Mayordomo Sebastian Blackwell: Lo que sucedió es una pena. Fue repentino, inesperado. Hoy era mi día libre, y no me encontraba aquí cuando sucedió. Aún no lo puedo creer."
            self.mostrar_texto(text2)
            self.enter()
            text3 = f"Desearía haber podido hacer más, desearía haber estado aquí para haberlo ayudado."
            self.mostrar_texto(text3)
            self.enter()
            print("\n")
            print("Escribe a para preguntar sobre el vaso de agua en la repisa.")
            print("\nEscribe b para preguntar si sabe si el ministro había recibido amenazas.")
            query = input("\nEscribe una opcion: ")
            while query != "a" and query != "b":
                query = input("Escriba bien. ")
            if query == "a":
                print("\n")
                text2 = f"Detective {self.nombre} {self.apellido}: Ese vaso de agua, ¿Ya estaba aquí cuando llegaste?"
                self.mostrar_texto(text2)
                self.enter()
                text3 = f"Mayordomo Sebastian Blackwell: No tiene nada de importante. Yo no lo revisaría si fuera tu. En serio, no es nada..."
                self.mostrar_texto(text3)
                self.enter()
                print("\n")
                self.mayordomointento = True
                self.mayordomovaso = True
            if query == "b":
                text2 = f"Mayordomo Sebastian Blackwell: No que yo supiera. El ministro nunca me contó nada sobre una posible conspiración en su contra, o sobre haber recibido amenazas."
                print("\n")
                self.mostrar_texto(text2)
                self.enter()
                text3 = f"Tampoco parecía que alguien del departamento de policia o del gobierno estuviera en su contra. No tengo idea de quien pueda estar detrás de esto..."
                self.mostrar_texto(text3)
                self.enter()
                print("\n") 
                self.mayordomointento = True
        if query == "c":
            text2 = f"Mayordomo Sebastian Blackwell: No que yo supiera. El ministro nunca me contó nada sobre una posible conspiración en su contra, o sobre haber recibido amenazas."
            print("\n")
            self.mostrar_texto(text2)
            self.enter()
            text3 = f"Tampoco parecía que alguien del departamento de policia o del gobierno estuviera en su contra. No tengo idea de quien pueda estar detrás de esto..."
            self.mostrar_texto(text3)
            self.enter()
            print("\n")
            print("Escribe a para preguntar sobre su relación con el ministro")
            print("\nEscribe b para preguntar sobre el atentado y donde se encontraba el cuando ocurrió.")
            query = input("\nEscribe una opcion: ")
            while query != "a" and query != "b":
                query = input("Escriba bien. ")
            if query == "a":
                text2 = f"Mayordomo Sebastian Blackwell: He sido su mayordomo desde hace más de 10 años. Siento que en cierta medida, llegue a ser como un hermano para él. Pero todo esto tuvo que pasar justo hoy, en mi día de descanso."
                print("\n")
                self.mostrar_texto(text2)
                self.enter()
                text3 = f"Desearía haber podido hacer más."
                self.mostrar_texto(text3)
                self.enter()
                print("\n")
                self.mayordomointento = True
            if query == "b":
                text2 = f"Mayordomo Sebastian Blackwell: Lo que sucedió es una pena. Fue repentino, inesperado. Hoy era mi día libre, y no me encontraba aquí cuando sucedió. Aún no lo puedo creer."
                print("\n")
                self.mostrar_texto(text2)
                self.enter()
                text3 = f"Desearía haber podido hacer más, desearía haber estado aquí para haberlo ayudado."
                self.mostrar_texto(text3)
                self.enter()
                print("\n")
                self.mayordomointento = True



    #Funcion para revisar inventario durante el tutorial. Es diferente a revisar_inventario ya que el tutorial te permite leer la
    #carta del ministro estando fuera del inventario. Mientras que el durante el juego, puedes leerla desde el inventario.
    #Solo tiene los 2 objetos que aparecen en el tutorial
    def revisar_inventario_tutorial(self):
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
            print("\nLas ultimas palabras que te dejo el ministro.")
            print("\nPresiona enter para continuar.")
            self.enter()
            return
        elif invorden == "paquete de chicles":
            self.mostrar_arte(self.artepaquetedechicles, 0.001)
            print("\nUn paquete de chicles comun y corriente.")
            print("\nPresiona enter para continuar.")
            self.enter()
        else:
            return
        

    #Funcion para revisar el inventario. Al seleccionar un objeto te muestra su imagen y una breve descripcion de este. Los artes que
    # muestra son constructores que se encuentran al principio del juego.  
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
            print("\nLas ultimas palabras que te dejo el ministro.")
            ordencarta = input("\nPresiona l para leer la carta o c para continuar: ")
            ordencarta = ordencarta.lower()
            while ordencarta != "c" and ordencarta != "l":
                ordencarta = input("Escriba bien: ")
                ordencarta = ordencarta.lower()
            if ordencarta == "l":
                self.lectura_carta()
            else:
                pass
        elif invorden == "paquete de chicles":
            self.mostrar_arte(self.artepaquetedechicles, 0.001)
            print("\nUn paquete de chicles comun y corriente.")
            self.enter()
        elif invorden == "carta anonima":
            self.mostrar_arte(self.artecarta, 0.001)
            print("\nUna carta dejada por un desconocido.")
            ordencarta = input("\nPresiona l para leer la carta o c para continuar: ")
            while ordencarta != "c" and ordencarta != "l":
                ordencarta = input("Escriba bien: ")
                ordencarta = ordencarta.lower()
            if ordencarta == "l":
                self.lecturacartaanonima()
            else:
                pass
        elif invorden == "reloj costoso":
            print("\n")
            self.mostrar_arte(self.artereloj, 0.001)
            print ("\n\nReloj marca Tag Heuer.")
            self.enter()
        elif invorden == "placa":
            print("\n")
            self.mostrar_arte(self.arteplaca, 0.001)
            print("\n\n¿El ministro tenía una placa?")
            self.enter()
        elif invorden == "cucaracha":
            self.mostrar_arte(self.artecucaracha, 0.001)
            print("\nAsqueroso")
            self.enter()
        elif invorden == "cepillo de dientes":
            self.mostrar_arte(self.artecepillodedientes, 0.001)
            print("\n¿Será que este cepillo le pertenecía al ministro?")
            self.enter()
        elif invorden == "corbata":
            print("\n")
            self.mostrar_arte(self.artecorbata, 0.001)
            print ("\n\nCorbata que pertenecía al ministro.")
            self.enter()
        elif invorden == "linterna":
            print("\n")
            self.mostrar_arte(self.artelinterna, 0.001)
            print("\n\nUna simple linterna.")
            self.enter()
        elif invorden == "vaso de cristal":
            print ("\n")
            self.mostrar_arte(self.artevaso, 0.001)
            if self.mayordomovaso == True:
                text = "Un vaso de cristal con agua, manchado. Parecen huellas dactilares."
            else:
                text = "Un vaso de cristal con agua."
            print("\n\n",text)
            self.enter()

        else:
            return
    

    #Funcion que permite soltar objetos al usuario. Verifica si esta la orden en el inventario y luego usa .remove para quitarla.
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
        
    
    #Muestra el texto de la carrta. Si tienes la linterna, muestra un texto diferente.
    def lectura_carta(self):
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
        if "linterna" not in self.inventario:
            self.mostrar_arte(contenidocarta, 0.005)
            textoenter = "Presiona enter 3 veces para continuar."
            print("\n\nPresiona enter 3 veces para continuar.")
            self.enter()
            self.enter()
            self.enter()

        else:
            self.mostrar_arte(contenidocarta, 0.001)
            self.enter()
            self.mostrar_arte(self.artelinterna, 0.001)
            self.enter()
            self.mostrar_texto("................")
            print("\n")
            self.mostrar_texto("La carta posee algo extraño si se le apunta con luz. Parece desplegar un mensaje.")
            arte = """
╔═╗┌─┐┌┬┐┌─┐┬ ┬  ┌─┐┬┌─┐┌┐┌┌┬┐┌─┐  ┌─┐┌┬┐┌─┐┌┐┌┌─┐┌─┐┌─┐┌┬┐┌─┐   ╔═╗┬       
║╣ └─┐ │ │ │└┬┘  └─┐│├┤ │││ │││ │  ├─┤│││├┤ │││├─┤┌─┘├─┤ │││ │   ║╣ │       
╚═╝└─┘ ┴ └─┘ ┴   └─┘┴└─┘┘└┘─┴┘└─┘  ┴ ┴┴ ┴└─┘┘└┘┴ ┴└─┘┴ ┴─┴┘└─┘o  ╚═╝┴─┘     
┌─┐┬ ┬┬  ┌─┐┌─┐┌┐ ┬  ┌─┐  ┌┬┐┌─┐  ┌┬┐┌─┐┌┬┐┌─┐  ┌─┐┌─┐┌┬┐┌─┐  ┌─┐┌─┐  ┌─┐┬  
│  │ ││  ├─┘├─┤├┴┐│  ├┤    ││├┤    │ │ │ │││ │  ├┤ └─┐ │ │ │  ├┤ └─┐  ├┤ │  
└─┘└─┘┴─┘┴  ┴ ┴└─┘┴─┘└─┘  ─┴┘└─┘   ┴ └─┘─┴┘└─┘  └─┘└─┘ ┴ └─┘  └─┘└─┘  └─┘┴─┘
┌─┐┌─┐┬┌─┐┬┌─┐┬     ╦┌─┐┬─┐┬─┐┌─┐┌┬┐  ╔╗ ┌─┐┬─┐┬┌─┬  ┌─┐┬ ┬                 
│ │├┤ ││  │├─┤│     ║├─┤├┬┘├┬┘├┤  ││  ╠╩╗├─┤├┬┘├┴┐│  ├┤ └┬┘                 
└─┘└  ┴└─┘┴┴ ┴┴─┘  ╚╝┴ ┴┴└─┴└─└─┘─┴┘  ╚═╝┴ ┴┴└─┴ ┴┴─┘└─┘ ┴                  
            """
            self.mostrar_arte(arte, 0.001)
            self.enter()
            print("\n")
            self.mostrar_texto("................")
            self.enter()

        

    #Muestra el texto de la carta anonima encontrada en la caja fuerte.
    def lecturacartaanonima(self):
        os.system('cls')
        text = """
Estimado Capitán Fitzgerald.

Espero que esta carta encuentre su camino a sus manos, ya que la información que estoy a punto de revelar es de suma importancia para la integridad del departamento y la seguridad de todos.

Primero que todo, permítame presentarme como un miembro leal del departamento. Mi conciencia no me permite mantener en secreto lo que sé. No es fácil traicionar la confianza de aquellos con los que he servido, pero la verdad debe salir a la luz.

He descubierto una red de conspiraciones que involucra a ciertos individuos dentro del departamento. Nombres como la secretaria del ministro, Victoria Ramos y el contador Arthur Mitchell, residentes de este edificio, están implicados en actividades que comprometen nuestra misión y la seguridad de la ciudad. Detrás de las apariencias, hay una trama más grande que se extiende más allá de lo que podemos imaginar.

La información que estoy proporcionando puede poner mi vida en peligro, pero estoy dispuesto a arriesgarme por la verdad. Se avecinan eventos que amenazan con socavar la integridad de nuestro trabajo. Preparémonos para lo que está por venir.

Le ruego, Capitán, que actúe con extrema cautela y discreción al abordar este asunto. La verdad está ahí afuera, pero la lealtad y la traición se entrelazan en formas inesperadas.

Atentamente,

Un aliado en las sombras.
        """
        self.mostrar_texto(text)
        print("\n\n\tPresiona enter 3 veces para continuar")
        self.enter()
        self.enter()
        self.enter()


    #Funcion para mostrar texto
    def mostrar_texto(self, texto):
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
            #0.03 el ideal

    #Funcion para mostrar arte. Misma que el texto, pero permite poner tu el tiempo cuando la llamas.
    def mostrar_arte(self, texto, tiempo):
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(tiempo)

    #Funcion para parpadeo del texto
    def parpadeo(self, texto, limite):
        tiempo_inicio = time.time()
        tiempo_limite = limite  # segundos

        while time.time() - tiempo_inicio < tiempo_limite:
            sys.stdout.write(f"\r{texto} ")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\r" + " " * len(texto) + " ")
            sys.stdout.flush()
            time.sleep(0.5)
    
    #Funcion de enter para conversaciones. Si no escribes enter, muestra un mensaje parpadeando.
    def enter(self):
        comandoenter = input()
        while comandoenter != '':
            textoenter = "Presiona enter para continuar."
            self.parpadeo(textoenter, 3)
            comandoenter = input()


    #Funcion que muestra el titulo del juego. Presionas s para continuar. Usa musica con pygame.
    def inicio(self):
        # Ruta de tu archivo de música
        track1 = "살인 계획 (A Murder Plan).mp3"

        pygame.mixer.music.load(track1)
        pygame.mixer.music.play(-1)

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

    #Permite introducir tu nombre, apellido y genero, que se guardan en un constructor.
    def asignacion(self):
        text1 = "Comienza tu aventura."
        self.parpadeo(text1, 3)
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
        self.parpadeo(textoenter, 3)
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
        self.mostrar_texto(text2)
        self.enter()
        print("\n")
        text2 = f"Capitan Fitzgerald: .........."
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

        self.comandos = {'g':self.buscar_objetos, 'i':self.revisar_inventario, 's': self.soltar_objetos,}

        track3 = ("The last Samurai Soundtrack, con sonido de lluvia  Meditación.mp3")
        pygame.mixer.music.load(track3)
        pygame.mixer.music.play()

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
        track1 = "x2mate.com - Sirena de Policia (efecto de Sonido) (320 kbps).mp3"
        pygame.mixer.music.load(track1)
        pygame.mixer.music.play()
        patrulla = """
...............................................................................................
...............................................................................................
.............................................:##+*####-........................................
.............................................%++++****%........................................
......................................:=+**##%@@@@@%%%%##**+==-:+%*:...........................
....................................:#...........+.:::------..    ..%:.........................
...................................:+.:*.......#:+-.........:*...   .+-........................
..................................--.-+....:--=#:+-....:--===+*.    ..=-.......................
.................................=:.=+..:-=====#:+-..:========+:.   ..:+:......................
................................*:.+=.:========#:+=.-==========#.. .::::*-.....................
...............................#-:+::==========#:*==============%..::::::*-....................
.............................:%-:*@%@==========#-*===============+.:::::::+-...................
............................:#::####%*=========#-*===============+*::::::::=-..................
...........................:*::%%%%%@==========@-*================*-::::::::+=.................
.....................::*@@#::::::::::::::::::::::*:::::::::::::::::::::::::::*%%%%%@@@*:.......
...............:=*@%####**+.                    .+       .....              .=##########@:.....
..........*#%%#********###..                    .+  .......::......          -#********##+.....
........-@################  -**-=**.*=:*.**+=*+..+  ...::::::::::..          .##########@+.....
........#--*%#############  -#:#*+#-#=:#+#:#*#-..+    ..::::::::...          .########%%*=.....
.......++=*%##############  -#. *+#:#+:#+#:#*#...+    ..::::::::...          .########%+*-.....
......:#=*%###############...:. .-:.::.:.:-.:::..+  ...::::::::::.............#######%#+*-.....
....:+%%%########%@%%####%%*..                  .+  ... ...::.  ..-#%%####%%*:#######%++#-.....
..+#+++++++*###@#############%..                .+       .......*%############%%#####%%%%:.....
..%##########%%###@-.....:@#####.            .. .+....::::::::=@###@+......#%###@##########%+..
..@#####%%%%%%##%:........::%###*        .....:::*:::::::::::-@##%+.........:*%##@########%%@..
..#%%%%%%%%%@##@:...:*%*-::::%##%-.....::::::::::*:::::::::::###%=....=%#-::::+###%##%%%%%%%*..
..=%%%%%%%%%%##*....%%%%@-:::+###*:::::::::::::::*:::::::::::%##@....*%%%%*:::-@##@%%%%%%%%%:..
..:%%%%%%%%%%###....*%%%%::::+##%@%%%%%%%%%%%%%%%@%%%%%%%%%%%@##@....=@%%@-:::=%##@%%%%%%%%#...
...#%%%%%%%%@##%=..:::::::::-@##@%%%%%%%%%%%%%%%%@%%%%%%%%%%%@###+...:::::::::###%%%%%%%%%@:...
............:@##%*:::::::::=%##%=.............................#####:::::::::-%###*.............
.............:%###%%*=-=*%%###@:...............................*%###%#+==+#%###%=..............
...............:%%##########@=..................................:#%##########@*................
..................:+%@@@@*:........................................:-#@@@@#-...................
...............................................................................................
...............................................................................................
        """
        self.parpadeo(patrulla, 7)
        textoenter = "Presiona enter 3 veces para continuar."
        self.parpadeo(textoenter, 3)
        self.enter()
        self.enter()
        self.enter()
        pygame.mixer.music.stop()
        os.system('cls')
    
    def guardadoprev1(self):
        self.inventariorespaldo1 = self.inventario
        self.numerodeobjetosinventariorespaldo1 = self.numerodeobjetosinventario

    def auxiliar1(self):
        self.inventario.append("carta")
        self.numerodeobjetosinventario = 1

    def auxiliarguardado(self):
        self.inventario = self.inventariorespaldo1
        self.numerodeobjetosinventario = self.numerodeobjetosinventariorespaldo1
        self.locations = []
        self.objetosbiblioteca = []
        self.objetosbaño = []
        self.objetosdormitorio = []
        self.mayordomointento = False
        self.mayordomovaso = False
        self.decision1 = False

    def caso1(self):
        track1 = "The Clue.mp3"
        pygame.mixer.music.load(track1)
        pygame.mixer.music.play(-1)
        self.intentos = 5
        self.locations.append("sala de estar")
        self.locations.append("dormitorio")
        self.locations.append("baño")
        self.locations.append("biblioteca")
        self.objetosbiblioteca.append("carta anonima")
        self.objetosbiblioteca.append("reloj costoso")
        self.objetosbiblioteca.append("placa")
        self.objetosbaño.append("sobre con dinero")
        self.objetosbaño.append("cepillo de dientes")
        self.objetosbaño.append("cucaracha")
        self.objetosdormitorio.append("vaso de cristal")
        self.objetosdormitorio.append("linterna")
        self.objetosdormitorio.append("corbata")
        
        
        print("\n")
        text1 = f"Capitán Fitzgerald: Buenas noches, oficial Barkley. ¿Cuál es la situación aquí?"
        self.mostrar_texto(text1)
        self.enter()
        print("\n")
        text2 = "Oficial Jarred Barkley: Capitán, encontramos al Ministro sin vida hace aproximadamente 2 horas. La escena es bastante desordenada."
        self.mostrar_texto(text2)
        self.enter()
        print("\n")
        text3 = "Capitán Fitzgerald: ¿Algún indicio de cómo pudo haber sucedido? ¿Una causa de muerte clara?"
        self.mostrar_texto(text3)
        self.enter()
        print("\n")
        text4 = "Oficial Jarred Barkley: Sí, Capitán. El Ministro tiene una herida de arma blanca en el estómago. Parece ser la causa de su fallecimiento."
        self.mostrar_texto(text4)
        self.enter()
        print("\n")
        text5 = "Capitán Fitzgerald: Esto es grave. Necesitamos descubrir quién pudo haber hecho esto. ¿Alguna pista o testigo?"
        self.mostrar_texto(text5)
        self.enter()
        print("\n")
        text6 = "Oficial Jarred Barkley: Estamos revisando la zona, pero hasta ahora no hay testigos. Encontramos algunos objetos fuera de lugar y un desorden en la biblioteca. Además, el mayordomo del ministro acaba de llegar, por si quieren hablar con él."
        self.mostrar_texto(text6)
        self.enter()
        print("\n")
        text7 = "Capitán Fitzgerald: La caja fuerte, ¿contenía algo importante?"
        self.mostrar_texto(text7)
        self.enter()
        print("\n")
        text8 = "Oficial Jarred Barkley: Eso es algo que aún estamos investigando, Capitán."
        self.mostrar_texto(text8)
        self.enter()
        print("\n")
        text9 = "Capitán Fitzgerald: Bien, manténme informado de cualquier desarrollo. Vamos a encontrar al responsable de esto."
        self.mostrar_texto(text9)
        self.enter()
        print("\n")
        if self.genero == "h":
            text10 = f"Novato, por favor dirigete a las demas locaciones a recabar pistas. Yo me encargaré de revisar la sala de estar. Buscame si necesitas algo o si crees que has recabado las pistas suficientes."
        else:
            text10 = f"Novata, por favor dirigete a las demas locaciones a recabar pistas. Yo me encargaré de revisar la sala de estar. Buscame si necesitas algo o si crees que has recabado las pistas suficientes."
        self.mostrar_texto(text10)
        self.enter()
        print("\n")
        self.comandos = {'g':self.buscar_objetos, 'i':self.revisar_inventario, 'l': self.lectura_carta, 's': self.soltar_objetos, 'p': self.cambiar_posicion,}
        text1 = input("Escribe 'p' para elegir una locación en la que empezar: ")
        while text1 != 'p':
            text1 = input("\nElige una locacion con la que empezar. Escribe 'p'. ")
        self.ejecucion_comandos(text1)
        pygame.mixer.music.stop()
        
    
    def resolucion_caso(self):
        os.system('cls')
        track1 = "살인 계획 (A Murder Plan).mp3"

        pygame.mixer.music.load(track1)
        pygame.mixer.music.play(-1)

        text = "\tUbicación: Estacion de policia \tHora: 12:30 pm"
        print("\n")
        self.mostrar_texto(text)
        self.enter()
        print("\n")
        text1 = "Capitán Fitzgerald: Buenas noches, Detective. Después de estar revisando las pruebas por un tiempo, conseguimos las siguientes premisas.."
        self.mostrar_texto(text1)
        self.enter()
        print("\n")
        text2 = "El sobre con dinero encontrado en la alcantarilla parece estar vinculado a una conspiración más grande en contra del ministro. A continuación te explicaré los detalles."
        self.mostrar_texto(text2)
        self.enter()
        print("\n")
        text3 = "Se encontraron huellas dactilares en el vaso, y sin del mayordomo Sebastian Blackwell. Era su día libre y ese vaso estaba allí desde antes de que el llegara a la escena. Esto lo coloca como un sospechoso directo."
        self.mostrar_texto(text3)
        self.enter()
        print("\n")
        text4 = "En cuanto a la carta anónima, contiene información comprometedora sobre Victoria Alonso y Arthur Mitchell."
        self.mostrar_texto(text4)
        self.enter()
        print("\n")
        text5 = "Pruebas contra Victoria Alonso:"
        self.mostrar_texto(text5)
        self.enter()
        text6 = "- Documentos financieros que la vinculan al sobre con dinero."
        self.mostrar_texto(text6)
        self.enter()
        text7 = "- Testimonios que la sitúan cerca de la escena del crimen."
        self.mostrar_texto(text7)
        self.enter()
        text8 = "Pruebas contra Arthur Mitchell:"
        self.mostrar_texto(text8)
        self.enter()
        text9 = "- Registros telefónicos que lo conectan con la conspiración mencionada en la carta."
        self.mostrar_texto(text9)
        self.enter()
        text10 = "- Un objeto personal encontrado en la escena del crimen."
        self.mostrar_texto(text10)
        self.enter()
        print("\n")
        text5 = f"Capitán Fitzgerald: Tendremos que tomar una decisión sobre a quién arrestar. Las pruebas estan en su contra, pero es por algo que te estuvimos entrenando por tantos años en la academia, {self.apellido}. Confiamos en ti para resolver este caso."
        self.mostrar_texto(text5)
        self.enter()
        print("\n")
        text6 = f"Se que tienes ese don para ver más alla de las cosas."
        self.mostrar_texto(text6)
        self.enter()
        print("\n")
        text7 = f"Hemos reunido a todos los sospechosos en diferentes salas. La resolución a la que llegues, esos sospechosos serán arrestados y daremos el caso como cerrado por el momento."
        self.mostrar_texto(text7)
        self.enter()
        text8 = f"Perdóname por someterte a esta presión novato. Pero es algo que tienes que hacer. Meditalo muy bien y dime tu decisión."
        self.mostrar_texto(text8)
        self.enter()
        print("\n")

        decision = input("Presiona 'a' para arrestar a Victoria Alonso y Arthur Mitchell, presiona 'b' para arrestar al mayordomo Sebastian Blackwell, presiona 'c' para arrestar al oficial Jarred Barkley, presiona 'd' para arrestar al capitán: ")
        decision = decision.lower()
        while decision != "a" and decision != "b" and decision != "c" and decision != "d":
            decision = input("Escriba bien. ")
            decision = decision.lower()
        if decision == 'a':
            print("\n")
            text6 = "Capitán Fitzgerald: Has decidido arrestar a Victoria Alonso y a Arthur Mitchell. Es una decisión difícil, pero confiamos en tu juicio. Veremos cómo se desarrolla la investigación."
            self.mostrar_texto(text6)
            self.enter()
            os.system('cls')
            pygame.mixer.music.stop()
            time.sleep(3)
            text6 = "Victoria y Arthur no eran los culpables."
            self.mostrar_arte(text6, 0.7)
            self.enter()
            self.gameoverresolucion()
        elif decision == 'b':
            print("\n")
            text6 = "Capitán Fitzgerald: Has decidido arrestar a Sebastian Blackwell. Es una decisión difícil, pero confiamos en tu juicio. Veremos cómo se desarrolla la investigación."
            self.mostrar_texto(text6)
            self.enter()
            os.system('cls')
            pygame.mixer.music.stop()
            time.sleep(3)
            text6 = "El mayordomo Sebastian no era el culpable."
            self.mostrar_arte(text6, 0.7)
            self.enter()
            self.gameoverresolucion()
        elif decision == 'c':
            print("\n")
            text6 = f"Capitán Fitzgerald: Me sorprende tu decision, {self.apellido}. Pero confio en tu criterio. El oficial Barkley sera arrestado y llevado a juicio. Confío en tu criterio."
            self.mostrar_texto(text6)
            self.enter()
            os.system('cls')
            time.sleep(3)
            text6 = "El oficial Jarred Barkley era el culpable."
            self.mostrar_arte(text6, 0.7)
            self.enter()
            print("\n")
            arte = """
   █████████                        █████                 
  ███░░░░░███                      ░░███                  
 ███     ░░░   ██████   ██████   ███████                  
░███          ███░░███ ███░░███ ███░░███                  
░███    █████░███ ░███░███ ░███░███ ░███                  
░░███  ░░███ ░███ ░███░███ ░███░███ ░███                  
 ░░█████████ ░░██████ ░░██████ ░░████████                 
  ░░░░░░░░░   ░░░░░░   ░░░░░░   ░░░░░░░░                  
                                                          
                                                          
                                                          
 ██████████                █████  ███                     
░░███░░░░░█               ░░███  ░░░                      
 ░███  █ ░  ████████    ███████  ████  ████████    ███████
 ░██████   ░░███░░███  ███░░███ ░░███ ░░███░░███  ███░░███
 ░███░░█    ░███ ░███ ░███ ░███  ░███  ░███ ░███ ░███ ░███
 ░███ ░   █ ░███ ░███ ░███ ░███  ░███  ░███ ░███ ░███ ░███
 ██████████ ████ █████░░████████ █████ ████ █████░░███████
░░░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░███
                                                  ███ ░███
                                                 ░░██████ 
                                                  ░░░░░░  
            """
            self.mostrar_arte(arte, 0.001)
            print("\n\n")
            text = """
Jarred Barkley había concebido meticulosamente un plan para establecer una red criminal. Su primer paso fue eliminar al Ministro, una figura clave en sus planes. Forzó la caja fuerte para sembrar caos y desvió sospechas, dejando un indicio inadvertido: su placa policial.

Continuando con su astuta estrategia, Barkley elaboró una carta anónima incriminatoria, apuntando falsamente hacia Victoria Alonso y Arthur Mitchell. Colocó la carta estratégicamente en la caja fuerte, asegurándose de dejar su placa para señalar hacia sus propios crímenes.

Amenazó al mayordomo Sebastian Blackwell para que dejara sus huellas dactilares en el vaso, fabricando así evidencia que lo incriminaba. Barkley había urdido un enredo de engaños para hacer caer sobre Sebastian la sombra de la culpabilidad.

Finalmente, para sellar su maquinación, colocó un sobre con dinero procedente de Victoria Alonso y Arthur Mitchell en la alcantarilla. Esta artimaña apuntaba a inculpar a ambos, cerrando así el círculo de su red criminal.

            """
            self.mostrar_texto(text)
            print("\nPresiona enter 3 veces para continuar.")
            self.enter()
            self.enter()
            self.enter()
            os.system('cls')
            if self.genero == "h":
                text6 = "Capitán Fitzgerald: Te lo dije muchacho. Siempre hubo algo dentro de ti. Contigo en nuestro equipo, podremos desentrañar todas las verdades ocultas a la ley que esconde esta ciudad."
            else:
                text6 = "Capitán Fitzgerald: Te lo dije muchacha. Siempre hubo algo dentro de ti. Contigo en nuestro equipo, podremos desentrañar todas las verdades ocultas a la ley que esconde esta ciudad."
            self.mostrar_texto(text6)
            self.enter()
            text7 = "Ven, vamos a celebrar. Esta va por Vincent."
            self.mostrar_texto(text6)
            self.enter()
            print("\n")
            self.mostrar_arte(arte, 0.001)
            sys.exit()


            
        else:
            pygame.mixer.music.stop()
            os.system('cls')
            text6 = "Capitán Fitzgerald: .............."
            self.mostrar_texto(text6)
            self.enter()
            text6 = "¿Por qué?"
            self.mostrar_arte(text6, 0.6)
            self.enter()
            os.system('cls')
            time.sleep(3)
            text6 = "El capitán Fitzgerald no era el culpable."
            self.mostrar_arte(text6, 0.7)
            self.enter()
            self.gameoverresolucion()


       

    def ejecucion_juego(self):
        #self.inicio()
        #self.asignacion()
        #self.tutorial()
        #self.camino()
        self.auxiliar1()
        self.caso1()
        
        
        

p = Juego()
pygame.init()
os.system('cls')
p.ejecucion_juego()

#Hacer .lower donde sea necesario


#Aqui ira el tutorial de comandos
#Avanzar, tomar objetos, soltar objetos, etc.

#Comandos: Agarrar o soltar objetos. Interrogar personas.

#Propuesta para final: que las huellas en el vaso sean del mayordomo, pero no haya dicho nada porque estaba siendo amenazado.