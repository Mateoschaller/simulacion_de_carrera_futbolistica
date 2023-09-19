import random

def amarillas_selecciones(club,jugadores_sancionados,equipo_player,valoracion_player,nombre_jugador,apto):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14,0.14]           
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.2, 0.2, 0.2, 0.2, 0.2] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.25, 0.25, 0.25, 0.25 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.3, 0.3, 0.3] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.5,0.5]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0] 
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array    
    def random_generator():
        rand_num = random.random() 
        if rand_num <= 0.1:
            return 0 
        else:
            return 1 

    numeros = []
    num1 = random_generator()
    if num1 == 1:
        numeros.append(num1)
    num2 = random_generator()
    if num2 == 1:    
        numeros.append(num2)
    lat = len(numeros)
    contador = 0
    amarillas = []
    while (contador == lat):
        e1player = ["Morata","Olmo","Gavi","Aspas"]
        e2player = ["Mbappe","Giroud","Griezmann","Muani"]
        e3player = ["Depay","Weghorst","Simons","Wijnaldum"]
        e4player = ["Kane","Saka","Foden","Rashford"]
        e5player = ["Scamacca","Tonali","Jorginho","Retegui"]
        e6player = ["Perisic","Kramaric","Brozovic","Pasalic"]
        e7player = ["Lukaku","De Bruyne","Trossard","Bakayoko"]
        e8player = ["C.Ronaldo","Félix","Leão","Bruno Fernandes"]
        e9player = ["Xhaka","Okafor","Steffen","Fassnacht"]
        e10player = ["Eriksen","Braithwaite","Dolberg","Cornelius"]
        e11player = ["Lewandowski","Zielinski","Skoras","Swiderski"]
        e12player = ["Haaland","Brynhildsen","odegaard","Sorloth"]
        e13player = ["Havertz","Gündogan","Müller","Gnabry"]
        e14player = ["Bale","Ramsey","Moore","Ampadu"]
        e15player = ["Mitrovic","Jovic","Vlahovic","Tadic"]
        e16player = ["Isak","Forsberg","Elanga","Gyokeres"]
        e17player = ["Messi","MacAllister","Álvarez","Fernandez"]
        e18player = ["Núñez","Suárez","Cavani","Valverde"]
        e19player = ["Samudio","Ávalos","Cardozo","Villasanti"]
        e20player = ["Ben Brereton Díaz","Aránguiz","Vidal","Vargas"]
        e21player = ["Vaca","Chura","Sagredo","Sagredo"]
        e22player = ["Neymar","Richarlison","Firmino","Paquetá"]
        e23player = ["Lapadula","Cueva","Carrillo","Ormeño"]
        e24player = ["Luis Díaz","Borja","Borre","Zapata"]
        e25player = ["Valencia","Mena","Plata","Palacios"]
        e26player = ["Hurtado","Soteldo","Savarino","Córdova"]
        e27player = ["Lozano","Guardado","Herrera","Antuna"]
        e28player = ["Pulisic","Adams","McKennie","Reyna"]
        e29player = ["David","Larin","Wotherspoon","Davies"]
        e30player = ["Campbell","Alcocer","Tejeda","Calvo"]
        e31player = ["Paradela","Cavafe","Espino","Pozo"]
        e32player = ["Quioto","Arrada","Juanique","Leveron"]
        
        e33player = ["Salah","Mohamed","Zizo","Hamdy"]
        e34player = ["Mane","Sarr","Sarr(O.L)","Gueye"]
        e35player = ["Khazri","Jaziri","Msakni","Rafia"]
        e36player = ["Aboubakar","Siliki","Malong","Ngamaleu"]
        e37player = ["Hakimi","En-Nesyri","Amrabat","Munir"]
        e38player = ["Iheanacho","Iwobi","Awoniyi","Olayinka"]
        e39player = ["Ayew","Ayew(cp)","Partey","Paintsil"]
        e40player = ["Mahrez","Benrahma","Bounedjah","Boulaya"]
        e41player = ["Taremi","Amiri","Shekari","Gholizadeh"]
        e42player = ["Son","Min-kyu","Hee-chan","Jae-sung"]
        e43player = ["Mitoma","Kubo","Nishimura","Asano"]
        e44player = ["Lei","Elkerson","Yuning","Long"]
        e45player = ["Al-Shehri","Asiri","Sharahili","Kanno"]
        e46player = ["Solomon","Dasa","Lavi","Vitor"]
        e47player = ["McGree","Cummings","Kuol","Duke"]
        e48player = ["Alil","Afif","Muneer","Madibo"]
        if apto == 1:
            if equipo_player == "España":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e1player.insert(pos,nombre_jugador)
            elif equipo_player == "Francia":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e2player.insert(pos,nombre_jugador)
            elif equipo_player == "Holanda":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e3player.insert(pos,nombre_jugador)
            elif equipo_player == "Inglaterra":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e4player.insert(pos,nombre_jugador)
            elif equipo_player == "Italia":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e5player.insert(pos,nombre_jugador)
            elif equipo_player == "Croacia":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e6player.insert(pos,nombre_jugador)
            elif equipo_player == "Belgica":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e7player.insert(pos,nombre_jugador)
            elif equipo_player == "Portugal":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e8player.insert(pos,nombre_jugador)
            elif equipo_player == "Suiza":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e9player.insert(pos,nombre_jugador)
            elif equipo_player == "Dinamarca":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e10player.insert(pos,nombre_jugador)
            elif equipo_player == "Polonia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e11player.insert(pos,nombre_jugador)
            elif equipo_player == "Noruega":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e12player.insert(pos,nombre_jugador)
            elif equipo_player == "Alemania":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e13player.insert(pos,nombre_jugador)
            elif equipo_player == "Gales":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4      
                e14player.insert(pos,nombre_jugador)
            elif equipo_player == "Serbia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e15player.insert(pos,nombre_jugador)
            elif equipo_player == "Suecia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e16player.insert(pos,nombre_jugador)
            elif equipo_player == "Argentina":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e17player.insert(pos,nombre_jugador)
            elif equipo_player == "Uruguay":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e18player.insert(pos,nombre_jugador)
            elif equipo_player == "Paraguay":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e19player.insert(pos,nombre_jugador)
            elif equipo_player == "Chile":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e20player.insert(pos,nombre_jugador)
            elif equipo_player == "Bolivia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e21player.insert(pos,nombre_jugador)
            elif equipo_player == "Brasil":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e22player.insert(pos,nombre_jugador)
            elif equipo_player == "Peru":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e23player.insert(pos,nombre_jugador)
            elif equipo_player == "Colombia":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e24player.insert(pos,nombre_jugador)
            elif equipo_player == "Ecuador":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e25player.insert(pos,nombre_jugador)
            elif equipo_player == "Venezuela":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e26player.insert(pos,nombre_jugador)
            elif equipo_player == "Mexico":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e27player.insert(pos,nombre_jugador)     
            elif equipo_player == "Estados Unidos":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e28player.insert(pos,nombre_jugador)
            elif equipo_player == "Canada":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e29player.insert(pos,nombre_jugador)   
            elif equipo_player == "Costa Rica":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e30player.insert(pos,nombre_jugador)
            elif equipo_player == "Cuba":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e31player.insert(pos,nombre_jugador) 
            elif equipo_player == "Honduras":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e32player.insert(pos,nombre_jugador)
            elif equipo_player == "Egipto":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e33player.insert(pos,nombre_jugador)            
            elif equipo_player == "Senegal":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e34player.insert(pos,nombre_jugador)
            elif equipo_player == "Tunez":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                
                e35player.insert(pos,nombre_jugador) 
            elif equipo_player == "Camerun":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e36player.insert(pos,nombre_jugador)
            elif equipo_player == "Marruecos":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e37player.insert(pos,nombre_jugador)
            elif equipo_player == "Nigeria":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e38player.insert(pos,nombre_jugador)
            elif equipo_player == "Ghana":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e39player.insert(pos,nombre_jugador)
            elif equipo_player == "Argelia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e40player.insert(pos,nombre_jugador)
            elif equipo_player == "Iran":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e41player.insert(pos,nombre_jugador)            
            elif equipo_player == "Corea del Sur":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e42player.insert(pos,nombre_jugador)
            elif equipo_player == "Japon":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e43player.insert(pos,nombre_jugador) 
            elif equipo_player == "China":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e44player.insert(pos,nombre_jugador)
            elif equipo_player == "Arabia Saudita":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e45player.insert(pos,nombre_jugador)
            elif equipo_player == "Israel":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e46player.insert(pos,nombre_jugador)
            elif equipo_player == "Australia":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e47player.insert(pos,nombre_jugador)
            elif equipo_player == "Qatar":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e48player.insert(pos,nombre_jugador)
        
        if club == "España":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                    weigth = len(jugadores)
                else:    
                    jugadores = e1player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Francia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                    weigth = len(jugadores)
                else:
                    jugadores = e2player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Holanda":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                    weigth = len(jugadores)
                else:
                    jugadores = e3player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Inglaterra":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                    weigth = len(jugadores)
                else:
                    jugadores = e4player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Italia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                    weigth = len(jugadores)
                else:
                    jugadores = e5player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Croacia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                    weigth = len(jugadores)
                else:
                    jugadores = e6player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Belgica":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                    weigth = len(jugadores)
                else:
                    jugadores = e7player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Portugal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                    weigth = len(jugadores)
                else:
                    jugadores = e8player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Suiza":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                    weigth = len(jugadores)
                else:
                    jugadores = e9player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Dinamarca":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                    weigth = len(jugadores)
                else:
                    jugadores = e10player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Polonia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                    weigth = len(jugadores)
                else:
                    jugadores = e11player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Noruega":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                    weigth = len(jugadores)
                else:
                    jugadores = e12player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Alemania":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                    weigth = len(jugadores)
                else:
                    jugadores = e13player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Gales":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                    weigth = len(jugadores)
                else:
                    jugadores = e14player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Serbia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                    weigth = len(jugadores)
                else:
                    jugadores = e15player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Suecia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                    weigth = len(jugadores)
                else:
                    jugadores = e16player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Argentina":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                    weigth = len(jugadores)
                else:
                    jugadores = e17player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Uruguay":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                    weigth = len(jugadores)
                else:
                    jugadores = e18player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Paraguay":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                    weigth = len(jugadores)
                else:
                    jugadores = e19player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Chile":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                    weigth = len(jugadores)
                else:
                    jugadores = e20player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Bolivia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                    weigth = len(jugadores)
                else:
                    jugadores = e21player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Brasil":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                    weigth = len(jugadores)
                else:
                    jugadores = e22player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Peru":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                    weigth = len(jugadores)
                else:
                    jugadores = e23player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Colombia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                    weigth = len(jugadores)
                else:
                    jugadores = e24player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Ecuador":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                    weigth = len(jugadores)
                else:
                    jugadores = e25player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Venezuela":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                    weigth = len(jugadores)
                else:
                    jugadores = e26player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Mexico":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                    weigth = len(jugadores)
                else:
                    jugadores = e27player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Estados Unidos":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                    weigth = len(jugadores)
                else:
                    jugadores = e28player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Canada":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                    weigth = len(jugadores)
                else:
                    jugadores = e29player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Costa Rica":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                    weigth = len(jugadores)
                else:
                    jugadores = e30player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Cuba":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                    weigth = len(jugadores)
                else:
                    jugadores = e31player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Honduras":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                    weigth = len(jugadores)
                else:
                    jugadores = e32player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)
        elif club == "Egipto":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                    weigth = len(jugadores)
                else:
                    jugadores = e33player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Senegal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                    weigth = len(jugadores)
                else:
                    jugadores = e34player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Tunez":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                    weigth = len(jugadores)
                else:
                    jugadores = e35player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Camerun":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                    weigth = len(jugadores)
                else:
                    jugadores = e36player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Marruecos":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                    weigth = len(jugadores)
                else:
                    jugadores = e37player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Nigeria":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                    weigth = len(jugadores)
                else:
                    jugadores = e38player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Ghana":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                    weigth = len(jugadores)
                else:
                    jugadores = e39player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Argelia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                    weigth = len(jugadores)
                else:
                    jugadores = e40player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Iran":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                    weigth = len(jugadores)
                else:
                    jugadores = e41player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Corea del Sur":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                    weigth = len(jugadores)
                else:
                    jugadores = e42player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Japon":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                    weigth = len(jugadores)
                else:
                    jugadores = e43player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "China":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                    weigth = len(jugadores)
                else:
                    jugadores = e44player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Arabia Saudita":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                    weigth = len(jugadores)
                else:
                    jugadores = e45player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Israel":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                    weigth = len(jugadores)
                else:
                    jugadores = e46player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Australia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                    weigth = len(jugadores)
                else:
                    jugadores = e47player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Qatar":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                    weigth = len(jugadores)
                else:
                    jugadores = e48player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
                  
                
                
        contador += 1     
        amarillas.append(gol)
    if len(amarillas) != 0:   
        print(f' Amarillas {club}: ' + ', '.join(map(str, amarillas))) 
    return amarillas

def asistentes_selecciones(club,goles,jugadores_sancionados,equipo_player,valoracion_player,nombre_jugador,apto):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14,0.14]           
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.2, 0.2, 0.2, 0.2, 0.2] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.25, 0.25, 0.25, 0.25 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.3, 0.3, 0.3] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.5,0.5]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0] 
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array   
    def random_generator():
        rand_num = random.random() 
        if rand_num <= 0.3:
            return 0 
        else:
            return 1 
    
    asistencias_totales = []
    while (goles != 0):
        e1player = ["Morata","Olmo","Gavi","Aspas"]
        e2player = ["Mbappe","Giroud","Griezmann","Muani"]
        e3player = ["Depay","Weghorst","Simons","Wijnaldum"]
        e4player = ["Kane","Saka","Foden","Rashford"]
        e5player = ["Scamacca","Tonali","Jorginho","Retegui"]
        e6player = ["Perisic","Kramaric","Brozovic","Pasalic"]
        e7player = ["Lukaku","De Bruyne","Trossard","Bakayoko"]
        e8player = ["C.Ronaldo","Félix","Leão","Bruno Fernandes"]
        e9player = ["Xhaka","Okafor","Steffen","Fassnacht"]
        e10player = ["Eriksen","Braithwaite","Dolberg","Cornelius"]
        e11player = ["Lewandowski","Zielinski","Skoras","Swiderski"]
        e12player = ["Haaland","Brynhildsen","odegaard","Sorloth"]
        e13player = ["Havertz","Gündogan","Müller","Gnabry"]
        e14player = ["Bale","Ramsey","Moore","Ampadu"]
        e15player = ["Mitrovic","Jovic","Vlahovic","Tadic"]
        e16player = ["Isak","Forsberg","Elanga","Gyokeres"]
        e17player = ["Messi","MacAllister","Álvarez","Fernandez"]
        e18player = ["Núñez","Suárez","Cavani","Valverde"]
        e19player = ["Samudio","Ávalos","Cardozo","Villasanti"]
        e20player = ["Ben Brereton Díaz","Aránguiz","Vidal","Vargas"]
        e21player = ["Vaca","Chura","Sagredo","Sagredo"]
        e22player = ["Neymar","Richarlison","Firmino","Paquetá"]
        e23player = ["Lapadula","Cueva","Carrillo","Ormeño"]
        e24player = ["Luis Díaz","Borja","Borre","Zapata"]
        e25player = ["Valencia","Mena","Plata","Palacios"]
        e26player = ["Hurtado","Soteldo","Savarino","Córdova"]
        e27player = ["Lozano","Guardado","Herrera","Antuna"]
        e28player = ["Pulisic","Adams","McKennie","Reyna"]
        e29player = ["David","Larin","Wotherspoon","Davies"]
        e30player = ["Campbell","Alcocer","Tejeda","Calvo"]
        e31player = ["Paradela","Cavafe","Espino","Pozo"]
        e32player = ["Quioto","Arrada","Juanique","Leveron"]
        e33player = ["Salah","Mohamed","Zizo","Hamdy"]
        e34player = ["Mane","Sarr","Sarr(O.L)","Gueye"]
        e35player = ["Khazri","Jaziri","Msakni","Rafia"]
        e36player = ["Aboubakar","Siliki","Malong","Ngamaleu"]
        e37player = ["Hakimi","En-Nesyri","Amrabat","Munir"]
        e38player = ["Iheanacho","Iwobi","Awoniyi","Olayinka"]
        e39player = ["Ayew","Ayew(cp)","Partey","Paintsil"]
        e40player = ["Mahrez","Benrahma","Bounedjah","Boulaya"]
        e41player = ["Taremi","Amiri","Shekari","Gholizadeh"]
        e42player = ["Son","Min-kyu","Hee-chan","Jae-sung"]
        e43player = ["Mitoma","Kubo","Nishimura","Asano"]
        e44player = ["Lei","Elkerson","Yuning","Long"]
        e45player = ["Al-Shehri","Asiri","Sharahili","Kanno"]
        e46player = ["Solomon","Dasa","Lavi","Vitor"]
        e47player = ["McGree","Cummings","Kuol","Duke"]
        e48player = ["Alil","Afif","Muneer","Madibo"]
        if apto == 1:
            if equipo_player == "España":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e1player.insert(pos,nombre_jugador)
            elif equipo_player == "Francia":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e2player.insert(pos,nombre_jugador)
            elif equipo_player == "Holanda":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e3player.insert(pos,nombre_jugador)
            elif equipo_player == "Inglaterra":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e4player.insert(pos,nombre_jugador)
            elif equipo_player == "Italia":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e5player.insert(pos,nombre_jugador)
            elif equipo_player == "Croacia":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e6player.insert(pos,nombre_jugador)
            elif equipo_player == "Belgica":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e7player.insert(pos,nombre_jugador)
            elif equipo_player == "Portugal":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e8player.insert(pos,nombre_jugador)
            elif equipo_player == "Suiza":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e9player.insert(pos,nombre_jugador)
            elif equipo_player == "Dinamarca":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e10player.insert(pos,nombre_jugador)
            elif equipo_player == "Polonia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e11player.insert(pos,nombre_jugador)
            elif equipo_player == "Noruega":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e12player.insert(pos,nombre_jugador)
            elif equipo_player == "Alemania":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e13player.insert(pos,nombre_jugador)
            elif equipo_player == "Gales":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4      
                e14player.insert(pos,nombre_jugador)
            elif equipo_player == "Serbia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e15player.insert(pos,nombre_jugador)
            elif equipo_player == "Suecia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e16player.insert(pos,nombre_jugador)
            elif equipo_player == "Argentina":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e17player.insert(pos,nombre_jugador)
            elif equipo_player == "Uruguay":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e18player.insert(pos,nombre_jugador)
            elif equipo_player == "Paraguay":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e19player.insert(pos,nombre_jugador)
            elif equipo_player == "Chile":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e20player.insert(pos,nombre_jugador)
            elif equipo_player == "Bolivia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e21player.insert(pos,nombre_jugador)
            elif equipo_player == "Brasil":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e22player.insert(pos,nombre_jugador)
            elif equipo_player == "Peru":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e23player.insert(pos,nombre_jugador)
            elif equipo_player == "Colombia":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e24player.insert(pos,nombre_jugador)
            elif equipo_player == "Ecuador":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e25player.insert(pos,nombre_jugador)
            elif equipo_player == "Venezuela":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e26player.insert(pos,nombre_jugador)
            elif equipo_player == "Mexico":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e27player.insert(pos,nombre_jugador)     
            elif equipo_player == "Estados Unidos":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e28player.insert(pos,nombre_jugador)
            elif equipo_player == "Canada":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e29player.insert(pos,nombre_jugador)   
            elif equipo_player == "Costa Rica":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e30player.insert(pos,nombre_jugador)
            elif equipo_player == "Cuba":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e31player.insert(pos,nombre_jugador) 
            elif equipo_player == "Honduras":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e32player.insert(pos,nombre_jugador)
            elif equipo_player == "Egipto":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e33player.insert(pos,nombre_jugador)            
            elif equipo_player == "Senegal":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e34player.insert(pos,nombre_jugador)
            elif equipo_player == "Tunez":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                
                e35player.insert(pos,nombre_jugador) 
            elif equipo_player == "Camerun":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e36player.insert(pos,nombre_jugador)
            elif equipo_player == "Marruecos":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e37player.insert(pos,nombre_jugador)
            elif equipo_player == "Nigeria":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e38player.insert(pos,nombre_jugador)
            elif equipo_player == "Ghana":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e39player.insert(pos,nombre_jugador)
            elif equipo_player == "Argelia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e40player.insert(pos,nombre_jugador)
            elif equipo_player == "Iran":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e41player.insert(pos,nombre_jugador)            
            elif equipo_player == "Corea del Sur":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e42player.insert(pos,nombre_jugador)
            elif equipo_player == "Japon":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e43player.insert(pos,nombre_jugador) 
            elif equipo_player == "China":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e44player.insert(pos,nombre_jugador)
            elif equipo_player == "Arabia Saudita":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e45player.insert(pos,nombre_jugador)
            elif equipo_player == "Israel":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e46player.insert(pos,nombre_jugador)
            elif equipo_player == "Australia":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e47player.insert(pos,nombre_jugador)
            elif equipo_player == "Qatar":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e48player.insert(pos,nombre_jugador)
        
   
        
        numero = random_generator()
        if numero == 1:
            goles = goles -1
        else:    
            asistencia = str(goles)
            goles = goles -1
            if club == "España":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                    weigth = len(jugadores)
                else:    
                    jugadores = e1player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Francia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e2player 
                        weigth = len(jugadores)
                    gol =  get_random_player6(jugadores,weigth)
            elif club == "Holanda":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e3player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Inglaterra":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e4player 
                        weigth = len(jugadores)
                    gol =  get_random_player6(jugadores,weigth)
            elif club == "Italia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e5player 
                        weigth = len(jugadores)
                    gol =  get_random_player6(jugadores,weigth)
            elif club == "Croacia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e6player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Belgica":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e7player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Portugal":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e8player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Suiza":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e9player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Dinamarca":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e10player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Polonia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e11player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Noruega":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e12player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Alemania":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e13player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Gales":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e14player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Serbia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e15player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Suecia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e16player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Argentina":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e17player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Uruguay":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e18player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Paraguay":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e19player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Chile":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e20player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Bolivia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e21player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Brasil":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e22player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Peru":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e23player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Colombia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e24player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Ecuador":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e25player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Venezuela":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e26player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Mexico":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e27player 
                        weigth = len(jugadores)  
                    gol = get_random_player6(jugadores,weigth)      
            elif club == "Estados Unidos":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e28player 
                        weigth = len(jugadores) 
                    gol = get_random_player6(jugadores,weigth)       
            elif club == "Canada":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e29player 
                        weigth = len(jugadores)   
                    gol = get_random_player6(jugadores,weigth)     
            elif club == "Costa Rica":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e30player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Cuba":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e31player 
                        weigth = len(jugadores) 
                    gol = get_random_player6(jugadores,weigth)       
            elif club == "Honduras":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e32player 
                        weigth = len(jugadores) 
                    gol = get_random_player6(jugadores,weigth)       
            elif club == "Egipto":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                    weigth = len(jugadores)
                else:
                    jugadores = e33player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Senegal":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e34player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Tunez":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e35player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Camerun":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e36player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Marruecos":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e37player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Nigeria":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e38player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Ghana":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e39player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Argelia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e40player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Iran":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e41player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Corea del Sur":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e42player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Japon":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e43player 
                        weigth = len(jugadores)  
                    gol = get_random_player6(jugadores,weigth)      
            elif club == "China":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e44player 
                        weigth = len(jugadores) 
                    gol = get_random_player6(jugadores,weigth)       
            elif club == "Arabia Saudita":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e45player 
                        weigth = len(jugadores)   
                    gol = get_random_player6(jugadores,weigth)     
            elif club == "Israel":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e46player 
                        weigth = len(jugadores)
                    gol = get_random_player6(jugadores,weigth)
            elif club == "Australia":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e47player 
                        weigth = len(jugadores) 
                    gol = get_random_player6(jugadores,weigth)       
            elif club == "Qatar":
                    if len(jugadores_sancionados) != 0:
                        jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                        weigth = len(jugadores)
                    else:
                        jugadores = e48player 
                        weigth = len(jugadores) 
                    gol = get_random_player6(jugadores,weigth)              
                
                
                
            asistencias_totales.append(gol)    
    if len(asistencias_totales) != 0:   
        print(f' Asistencias {club}: ' + ', '.join(map(str, asistencias_totales))) 
    return asistencias_totales

def rojas_selecciones(club,jugadores_sancionados,equipo_player,valoracion_player,nombre_jugador,apto):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14,0.14]            
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.2, 0.2, 0.2, 0.2, 0.2] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.25, 0.25, 0.25, 0.25 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.3, 0.3, 0.3] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.5,0.5]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0]
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array    
    def random_generator():
        rand_num = random.random() 
        if rand_num <= 0.025:
            return 0 
        else:
            return 1 
    
    numeros = []
    num1 = random_generator()
    if num1 == 1:
        numeros.append(num1)
    num2 = random_generator()
    if num2 == 1:    
        numeros.append(num2)
    lat = len(numeros)
    contador = 0
    rojas = []
    while (contador == lat):
        e1player = ["Morata","Olmo","Gavi","Aspas"]
        e2player = ["Mbappe","Giroud","Griezmann","Muani"]
        e3player = ["Depay","Weghorst","Simons","Wijnaldum"]
        e4player = ["Kane","Saka","Foden","Rashford"]
        e5player = ["Scamacca","Tonali","Jorginho","Retegui"]
        e6player = ["Perisic","Kramaric","Brozovic","Pasalic"]
        e7player = ["Lukaku","De Bruyne","Trossard","Bakayoko"]
        e8player = ["C.Ronaldo","Félix","Leão","Bruno Fernandes"]
        e9player = ["Xhaka","Okafor","Steffen","Fassnacht"]
        e10player = ["Eriksen","Braithwaite","Dolberg","Cornelius"]
        e11player = ["Lewandowski","Zielinski","Skoras","Swiderski"]
        e12player = ["Haaland","Brynhildsen","odegaard","Sorloth"]
        e13player = ["Havertz","Gündogan","Müller","Gnabry"]
        e14player = ["Bale","Ramsey","Moore","Ampadu"]
        e15player = ["Mitrovic","Jovic","Vlahovic","Tadic"]
        e16player = ["Isak","Forsberg","Elanga","Gyokeres"]
        e17player = ["Messi","MacAllister","Álvarez","Fernandez"]
        e18player = ["Núñez","Suárez","Cavani","Valverde"]
        e19player = ["Samudio","Ávalos","Cardozo","Villasanti"]
        e20player = ["Ben Brereton Díaz","Aránguiz","Vidal","Vargas"]
        e21player = ["Vaca","Chura","Sagredo","Sagredo"]
        e22player = ["Neymar","Richarlison","Firmino","Paquetá"]
        e23player = ["Lapadula","Cueva","Carrillo","Ormeño"]
        e24player = ["Luis Díaz","Borja","Borre","Zapata"]
        e25player = ["Valencia","Mena","Plata","Palacios"]
        e26player = ["Hurtado","Soteldo","Savarino","Córdova"]
        e27player = ["Lozano","Guardado","Herrera","Antuna"]
        e28player = ["Pulisic","Adams","McKennie","Reyna"]
        e29player = ["David","Larin","Wotherspoon","Davies"]
        e30player = ["Campbell","Alcocer","Tejeda","Calvo"]
        e31player = ["Paradela","Cavafe","Espino","Pozo"]
        e32player = ["Quioto","Arrada","Juanique","Leveron"]
        e33player = ["Salah","Mohamed","Zizo","Hamdy"]
        e34player = ["Mane","Sarr","Sarr(O.L)","Gueye"]
        e35player = ["Khazri","Jaziri","Msakni","Rafia"]
        e36player = ["Aboubakar","Siliki","Malong","Ngamaleu"]
        e37player = ["Hakimi","En-Nesyri","Amrabat","Munir"]
        e38player = ["Iheanacho","Iwobi","Awoniyi","Olayinka"]
        e39player = ["Ayew","Ayew(cp)","Partey","Paintsil"]
        e40player = ["Mahrez","Benrahma","Bounedjah","Boulaya"]
        e41player = ["Taremi","Amiri","Shekari","Gholizadeh"]
        e42player = ["Son","Min-kyu","Hee-chan","Jae-sung"]
        e43player = ["Mitoma","Kubo","Nishimura","Asano"]
        e44player = ["Lei","Elkerson","Yuning","Long"]
        e45player = ["Al-Shehri","Asiri","Sharahili","Kanno"]
        e46player = ["Solomon","Dasa","Lavi","Vitor"]
        e47player = ["McGree","Cummings","Kuol","Duke"]
        e48player = ["Alil","Afif","Muneer","Madibo"]
        if apto == 1:
            if equipo_player == "España":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e1player.insert(pos,nombre_jugador)
            elif equipo_player == "Francia":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e2player.insert(pos,nombre_jugador)
            elif equipo_player == "Holanda":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e3player.insert(pos,nombre_jugador)
            elif equipo_player == "Inglaterra":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e4player.insert(pos,nombre_jugador)
            elif equipo_player == "Italia":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e5player.insert(pos,nombre_jugador)
            elif equipo_player == "Croacia":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e6player.insert(pos,nombre_jugador)
            elif equipo_player == "Belgica":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e7player.insert(pos,nombre_jugador)
            elif equipo_player == "Portugal":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e8player.insert(pos,nombre_jugador)
            elif equipo_player == "Suiza":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e9player.insert(pos,nombre_jugador)
            elif equipo_player == "Dinamarca":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e10player.insert(pos,nombre_jugador)
            elif equipo_player == "Polonia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e11player.insert(pos,nombre_jugador)
            elif equipo_player == "Noruega":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e12player.insert(pos,nombre_jugador)
            elif equipo_player == "Alemania":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e13player.insert(pos,nombre_jugador)
            elif equipo_player == "Gales":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4      
                e14player.insert(pos,nombre_jugador)
            elif equipo_player == "Serbia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e15player.insert(pos,nombre_jugador)
            elif equipo_player == "Suecia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e16player.insert(pos,nombre_jugador)
            elif equipo_player == "Argentina":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e17player.insert(pos,nombre_jugador)
            elif equipo_player == "Uruguay":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e18player.insert(pos,nombre_jugador)
            elif equipo_player == "Paraguay":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e19player.insert(pos,nombre_jugador)
            elif equipo_player == "Chile":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e20player.insert(pos,nombre_jugador)
            elif equipo_player == "Bolivia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e21player.insert(pos,nombre_jugador)
            elif equipo_player == "Brasil":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e22player.insert(pos,nombre_jugador)
            elif equipo_player == "Peru":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e23player.insert(pos,nombre_jugador)
            elif equipo_player == "Colombia":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e24player.insert(pos,nombre_jugador)
            elif equipo_player == "Ecuador":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e25player.insert(pos,nombre_jugador)
            elif equipo_player == "Venezuela":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e26player.insert(pos,nombre_jugador)
            elif equipo_player == "Mexico":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e27player.insert(pos,nombre_jugador)     
            elif equipo_player == "Estados Unidos":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e28player.insert(pos,nombre_jugador)
            elif equipo_player == "Canada":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e29player.insert(pos,nombre_jugador)   
            elif equipo_player == "Costa Rica":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e30player.insert(pos,nombre_jugador)
            elif equipo_player == "Cuba":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e31player.insert(pos,nombre_jugador) 
            elif equipo_player == "Honduras":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e32player.insert(pos,nombre_jugador)
            elif equipo_player == "Egipto":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e33player.insert(pos,nombre_jugador)            
            elif equipo_player == "Senegal":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e34player.insert(pos,nombre_jugador)
            elif equipo_player == "Tunez":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                
                e35player.insert(pos,nombre_jugador) 
            elif equipo_player == "Camerun":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e36player.insert(pos,nombre_jugador)
            elif equipo_player == "Marruecos":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e37player.insert(pos,nombre_jugador)
            elif equipo_player == "Nigeria":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e38player.insert(pos,nombre_jugador)
            elif equipo_player == "Ghana":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e39player.insert(pos,nombre_jugador)
            elif equipo_player == "Argelia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e40player.insert(pos,nombre_jugador)
            elif equipo_player == "Iran":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e41player.insert(pos,nombre_jugador)            
            elif equipo_player == "Corea del Sur":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e42player.insert(pos,nombre_jugador)
            elif equipo_player == "Japon":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e43player.insert(pos,nombre_jugador) 
            elif equipo_player == "China":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e44player.insert(pos,nombre_jugador)
            elif equipo_player == "Arabia Saudita":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e45player.insert(pos,nombre_jugador)
            elif equipo_player == "Israel":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e46player.insert(pos,nombre_jugador)
            elif equipo_player == "Australia":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e47player.insert(pos,nombre_jugador)
            elif equipo_player == "Qatar":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e48player.insert(pos,nombre_jugador)
        
   
        if club == "España":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                    weigth = len(jugadores)
                else:    
                    jugadores = e1player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Francia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                    weigth = len(jugadores)
                else:
                    jugadores = e2player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Holanda":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                    weigth = len(jugadores)
                else:
                    jugadores = e3player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Inglaterra":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                    weigth = len(jugadores)
                else:
                    jugadores = e4player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Italia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                    weigth = len(jugadores)
                else:
                    jugadores = e5player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Croacia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                    weigth = len(jugadores)
                else:
                    jugadores = e6player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Belgica":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                    weigth = len(jugadores)
                else:
                    jugadores = e7player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Portugal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                    weigth = len(jugadores)
                else:
                    jugadores = e8player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Suiza":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                    weigth = len(jugadores)
                else:
                    jugadores = e9player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Dinamarca":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                    weigth = len(jugadores)
                else:
                    jugadores = e10player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Polonia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                    weigth = len(jugadores)
                else:
                    jugadores = e11player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Noruega":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                    weigth = len(jugadores)
                else:
                    jugadores = e12player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Alemania":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                    weigth = len(jugadores)
                else:
                    jugadores = e13player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Gales":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                    weigth = len(jugadores)
                else:
                    jugadores = e14player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Serbia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                    weigth = len(jugadores)
                else:
                    jugadores = e15player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Suecia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                    weigth = len(jugadores)
                else:
                    jugadores = e16player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Argentina":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                    weigth = len(jugadores)
                else:
                    jugadores = e17player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Uruguay":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                    weigth = len(jugadores)
                else:
                    jugadores = e18player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Paraguay":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                    weigth = len(jugadores)
                else:
                    jugadores = e19player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Chile":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                    weigth = len(jugadores)
                else:
                    jugadores = e20player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Bolivia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                    weigth = len(jugadores)
                else:
                    jugadores = e21player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Brasil":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                    weigth = len(jugadores)
                else:
                    jugadores = e22player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Peru":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                    weigth = len(jugadores)
                else:
                    jugadores = e23player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Colombia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                    weigth = len(jugadores)
                else:
                    jugadores = e24player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Ecuador":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                    weigth = len(jugadores)
                else:
                    jugadores = e25player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Venezuela":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                    weigth = len(jugadores)
                else:
                    jugadores = e26player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Mexico":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                    weigth = len(jugadores)
                else:
                    jugadores = e27player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Estados Unidos":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                    weigth = len(jugadores)
                else:
                    jugadores = e28player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Canada":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                    weigth = len(jugadores)
                else:
                    jugadores = e29player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Costa Rica":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                    weigth = len(jugadores)
                else:
                    jugadores = e30player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Cuba":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                    weigth = len(jugadores)
                else:
                    jugadores = e31player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Honduras":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                    weigth = len(jugadores)
                else:
                    jugadores = e32player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth) 
        elif club == "Egipto":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                    weigth = len(jugadores)
                else:
                    jugadores = e33player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Senegal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                    weigth = len(jugadores)
                else:
                    jugadores = e34player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Tunez":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                    weigth = len(jugadores)
                else:
                    jugadores = e35player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Camerun":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                    weigth = len(jugadores)
                else:
                    jugadores = e36player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Marruecos":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                    weigth = len(jugadores)
                else:
                    jugadores = e37player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Nigeria":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                    weigth = len(jugadores)
                else:
                    jugadores = e38player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Ghana":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                    weigth = len(jugadores)
                else:
                    jugadores = e39player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Argelia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                    weigth = len(jugadores)
                else:
                    jugadores = e40player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Iran":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                    weigth = len(jugadores)
                else:
                    jugadores = e41player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Corea del Sur":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                    weigth = len(jugadores)
                else:
                    jugadores = e42player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Japon":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                    weigth = len(jugadores)
                else:
                    jugadores = e43player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "China":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                    weigth = len(jugadores)
                else:
                    jugadores = e44player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Arabia Saudita":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                    weigth = len(jugadores)
                else:
                    jugadores = e45player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Israel":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                    weigth = len(jugadores)
                else:
                    jugadores = e46player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Australia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                    weigth = len(jugadores)
                else:
                    jugadores = e47player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Qatar":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                    weigth = len(jugadores)
                else:
                    jugadores = e48player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)           
                          
            
            
        contador += 1     
        rojas.append(gol)
    if len(rojas) != 0:   
        print(f' rojas {club}: ' + ', '.join(map(str, rojas))) 
    return rojas

def goleadores_selecciones(club,goles,jugadores_sancionados,equipo_player,valoracion_player,nombre_jugador,apto):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.30, 0.20, 0.15, 0.10, 0.10, 0.10, 0.5]             
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.30, 0.20, 0.15, 0.15, 0.10, 0.10] 
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.3, 0.2, 0.15, 0.15, 0.1] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.35, 0.30, 0.20, 0.15 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.5, 0.3, 0.2] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.6,0.4]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0]   
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array   
    
    goles_totales = []
    while (goles != 0):
        e1player = ["Morata","Olmo","Gavi","Aspas"]
        e2player = ["Mbappe","Giroud","Griezmann","Muani"]
        e3player = ["Depay","Weghorst","Simons","Wijnaldum"]
        e4player = ["Kane","Saka","Foden","Rashford"]
        e5player = ["Scamacca","Tonali","Jorginho","Retegui"]
        e6player = ["Perisic","Kramaric","Brozovic","Pasalic"]
        e7player = ["Lukaku","De Bruyne","Trossard","Bakayoko"]
        e8player = ["C.Ronaldo","Félix","Leão","Bruno Fernandes"]
        e9player = ["Xhaka","Okafor","Steffen","Fassnacht"]
        e10player = ["Eriksen","Braithwaite","Dolberg","Cornelius"]
        e11player = ["Lewandowski","Zielinski","Skoras","Swiderski"]
        e12player = ["Haaland","Brynhildsen","odegaard","Sorloth"]
        e13player = ["Havertz","Gündogan","Müller","Gnabry"]
        e14player = ["Bale","Ramsey","Moore","Ampadu"]
        e15player = ["Mitrovic","Jovic","Vlahovic","Tadic"]
        e16player = ["Isak","Forsberg","Elanga","Gyokeres"]
        e17player = ["Messi","MacAllister","Álvarez","Fernandez"]
        e18player = ["Núñez","Suárez","Cavani","Valverde"]
        e19player = ["Samudio","Ávalos","Cardozo","Villasanti"]
        e20player = ["Ben Brereton Díaz","Aránguiz","Vidal","Vargas"]
        e21player = ["Vaca","Chura","Sagredo","Sagredo"]
        e22player = ["Neymar","Richarlison","Firmino","Paquetá"]
        e23player = ["Lapadula","Cueva","Carrillo","Ormeño"]
        e24player = ["Luis Díaz","Borja","Borre","Zapata"]
        e25player = ["Valencia","Mena","Plata","Palacios"]
        e26player = ["Hurtado","Soteldo","Savarino","Córdova"]
        e27player = ["Lozano","Guardado","Herrera","Antuna"]
        e28player = ["Pulisic","Adams","McKennie","Reyna"]
        e29player = ["David","Larin","Wotherspoon","Davies"]
        e30player = ["Campbell","Alcocer","Tejeda","Calvo"]
        e31player = ["Paradela","Cavafe","Espino","Pozo"]
        e32player = ["Quioto","Arrada","Juanique","Leveron"]
        e33player = ["Salah","Mohamed","Zizo","Hamdy"]
        e34player = ["Mane","Sarr","Sarr(O.L)","Gueye"]
        e35player = ["Khazri","Jaziri","Msakni","Rafia"]
        e36player = ["Aboubakar","Siliki","Malong","Ngamaleu"]
        e37player = ["Hakimi","En-Nesyri","Amrabat","Munir"]
        e38player = ["Iheanacho","Iwobi","Awoniyi","Olayinka"]
        e39player = ["Ayew","Ayew(cp)","Partey","Paintsil"]
        e40player = ["Mahrez","Benrahma","Bounedjah","Boulaya"]
        e41player = ["Taremi","Amiri","Shekari","Gholizadeh"]
        e42player = ["Son","Min-kyu","Hee-chan","Jae-sung"]
        e43player = ["Mitoma","Kubo","Nishimura","Asano"]
        e44player = ["Lei","Elkerson","Yuning","Long"]
        e45player = ["Al-Shehri","Asiri","Sharahili","Kanno"]
        e46player = ["Solomon","Dasa","Lavi","Vitor"]
        e47player = ["McGree","Cummings","Kuol","Duke"]
        e48player = ["Alil","Afif","Muneer","Madibo"]
        if apto == 1:
            if equipo_player == "España":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e1player.insert(pos,nombre_jugador)
            elif equipo_player == "Francia":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e2player.insert(pos,nombre_jugador)
            elif equipo_player == "Holanda":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e3player.insert(pos,nombre_jugador)
            elif equipo_player == "Inglaterra":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e4player.insert(pos,nombre_jugador)
            elif equipo_player == "Italia":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e5player.insert(pos,nombre_jugador)
            elif equipo_player == "Croacia":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e6player.insert(pos,nombre_jugador)
            elif equipo_player == "Belgica":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e7player.insert(pos,nombre_jugador)
            elif equipo_player == "Portugal":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e8player.insert(pos,nombre_jugador)
            elif equipo_player == "Suiza":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e9player.insert(pos,nombre_jugador)
            elif equipo_player == "Dinamarca":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e10player.insert(pos,nombre_jugador)
            elif equipo_player == "Polonia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e11player.insert(pos,nombre_jugador)
            elif equipo_player == "Noruega":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e12player.insert(pos,nombre_jugador)
            elif equipo_player == "Alemania":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e13player.insert(pos,nombre_jugador)
            elif equipo_player == "Gales":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4      
                e14player.insert(pos,nombre_jugador)
            elif equipo_player == "Serbia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e15player.insert(pos,nombre_jugador)
            elif equipo_player == "Suecia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e16player.insert(pos,nombre_jugador)
            elif equipo_player == "Argentina":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e17player.insert(pos,nombre_jugador)
            elif equipo_player == "Uruguay":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e18player.insert(pos,nombre_jugador)
            elif equipo_player == "Paraguay":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e19player.insert(pos,nombre_jugador)
            elif equipo_player == "Chile":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e20player.insert(pos,nombre_jugador)
            elif equipo_player == "Bolivia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e21player.insert(pos,nombre_jugador)
            elif equipo_player == "Brasil":
                if valoracion_player > 90: 
                    pos = 0
                elif valoracion_player > 80: 
                    pos = 1 
                elif valoracion_player > 70: 
                    pos = 2 
                elif valoracion_player > 60: 
                    pos = 3 
                else: pos = 4
                e22player.insert(pos,nombre_jugador)
            elif equipo_player == "Peru":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e23player.insert(pos,nombre_jugador)
            elif equipo_player == "Colombia":
                if valoracion_player > 80: 
                    pos = 0
                elif valoracion_player > 70: 
                    pos = 1 
                elif valoracion_player > 60: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e24player.insert(pos,nombre_jugador)
            elif equipo_player == "Ecuador":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e25player.insert(pos,nombre_jugador)
            elif equipo_player == "Venezuela":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e26player.insert(pos,nombre_jugador)
            elif equipo_player == "Mexico":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e27player.insert(pos,nombre_jugador)     
            elif equipo_player == "Estados Unidos":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e28player.insert(pos,nombre_jugador)
            elif equipo_player == "Canada":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e29player.insert(pos,nombre_jugador)   
            elif equipo_player == "Costa Rica":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e30player.insert(pos,nombre_jugador)
            elif equipo_player == "Cuba":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e31player.insert(pos,nombre_jugador) 
            elif equipo_player == "Honduras":
                if valoracion_player > 50: 
                    pos = 0
                elif valoracion_player > 45: 
                    pos = 1 
                elif valoracion_player > 40: 
                    pos = 2 
                elif valoracion_player > 35: 
                    pos = 3 
                else: pos = 4
                e32player.insert(pos,nombre_jugador)
            elif equipo_player == "Egipto":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e33player.insert(pos,nombre_jugador)            
            elif equipo_player == "Senegal":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e34player.insert(pos,nombre_jugador)
            elif equipo_player == "Tunez":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                
                e35player.insert(pos,nombre_jugador) 
            elif equipo_player == "Camerun":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e36player.insert(pos,nombre_jugador)
            elif equipo_player == "Marruecos":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e37player.insert(pos,nombre_jugador)
            elif equipo_player == "Nigeria":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e38player.insert(pos,nombre_jugador)
            elif equipo_player == "Ghana":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e39player.insert(pos,nombre_jugador)
            elif equipo_player == "Argelia":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e40player.insert(pos,nombre_jugador)
            elif equipo_player == "Iran":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e41player.insert(pos,nombre_jugador)            
            elif equipo_player == "Corea del Sur":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e42player.insert(pos,nombre_jugador)
            elif equipo_player == "Japon":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e43player.insert(pos,nombre_jugador) 
            elif equipo_player == "China":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e44player.insert(pos,nombre_jugador)
            elif equipo_player == "Arabia Saudita":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e45player.insert(pos,nombre_jugador)
            elif equipo_player == "Israel":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e46player.insert(pos,nombre_jugador)
            elif equipo_player == "Australia":
                if valoracion_player > 65: 
                    pos = 0
                elif valoracion_player > 60: 
                    pos = 1 
                elif valoracion_player > 55: 
                    pos = 2 
                elif valoracion_player > 50: 
                    pos = 3 
                else: pos = 4
                e47player.insert(pos,nombre_jugador)
            elif equipo_player == "Qatar":
                if valoracion_player > 60: 
                    pos = 0
                elif valoracion_player > 55: 
                    pos = 1 
                elif valoracion_player > 50: 
                    pos = 2 
                elif valoracion_player > 45: 
                    pos = 3 
                else: pos = 4
                e48player.insert(pos,nombre_jugador)
        
        gol = str(goles)
        goles = goles -1
        if club == "España":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                    weigth = len(jugadores)
                else:    
                    jugadores = e1player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Francia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                    weigth = len(jugadores)
                else:
                    jugadores = e2player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Holanda":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                    weigth = len(jugadores)
                else:
                    jugadores = e3player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Inglaterra":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                    weigth = len(jugadores)
                else:
                    jugadores = e4player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Italia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                    weigth = len(jugadores)
                else:
                    jugadores = e5player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Croacia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                    weigth = len(jugadores)
                else:
                    jugadores = e6player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Belgica":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                    weigth = len(jugadores)
                else:
                    jugadores = e7player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Portugal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                    weigth = len(jugadores)
                else:
                    jugadores = e8player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Suiza":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                    weigth = len(jugadores)
                else:
                    jugadores = e9player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Dinamarca":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                    weigth = len(jugadores)
                else:
                    jugadores = e10player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Polonia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                    weigth = len(jugadores)
                else:
                    jugadores = e11player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Noruega":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                    weigth = len(jugadores)
                else:
                    jugadores = e12player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Alemania":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                    weigth = len(jugadores)
                else:
                    jugadores = e13player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Gales":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                    weigth = len(jugadores)
                else:
                    jugadores = e14player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Serbia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                    weigth = len(jugadores)
                else:
                    jugadores = e15player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Suecia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                    weigth = len(jugadores)
                else:
                    jugadores = e16player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Argentina":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                    weigth = len(jugadores)
                else:
                    jugadores = e17player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Uruguay":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                    weigth = len(jugadores)
                else:
                    jugadores = e18player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Paraguay":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                    weigth = len(jugadores)
                else:
                    jugadores = e19player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Chile":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                    weigth = len(jugadores)
                else:
                    jugadores = e20player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Bolivia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                    weigth = len(jugadores)
                else:
                    jugadores = e21player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Brasil":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                    weigth = len(jugadores)
                else:
                    jugadores = e22player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Peru":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                    weigth = len(jugadores)
                else:
                    jugadores = e23player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Colombia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                    weigth = len(jugadores)
                else:
                    jugadores = e24player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Ecuador":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                    weigth = len(jugadores)
                else:
                    jugadores = e25player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Venezuela":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                    weigth = len(jugadores)
                else:
                    jugadores = e26player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Mexico":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                    weigth = len(jugadores)
                else:
                    jugadores = e27player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Estados Unidos":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                    weigth = len(jugadores)
                else:
                    jugadores = e28player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Canada":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                    weigth = len(jugadores)
                else:
                    jugadores = e29player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Costa Rica":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                    weigth = len(jugadores)
                else:
                    jugadores = e30player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Cuba":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                    weigth = len(jugadores)
                else:
                    jugadores = e31player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Honduras":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                    weigth = len(jugadores)
                else:
                    jugadores = e32player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)    
        elif club == "Egipto":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                    weigth = len(jugadores)
                else:
                    jugadores = e33player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Senegal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                    weigth = len(jugadores)
                else:
                    jugadores = e34player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Tunez":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                    weigth = len(jugadores)
                else:
                    jugadores = e35player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Camerun":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                    weigth = len(jugadores)
                else:
                    jugadores = e36player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Marruecos":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                    weigth = len(jugadores)
                else:
                    jugadores = e37player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Nigeria":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                    weigth = len(jugadores)
                else:
                    jugadores = e38player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Ghana":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                    weigth = len(jugadores)
                else:
                    jugadores = e39player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Argelia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                    weigth = len(jugadores)
                else:
                    jugadores = e40player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Iran":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                    weigth = len(jugadores)
                else:
                    jugadores = e41player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Corea del Sur":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                    weigth = len(jugadores)
                else:
                    jugadores = e42player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Japon":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                    weigth = len(jugadores)
                else:
                    jugadores = e43player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "China":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                    weigth = len(jugadores)
                else:
                    jugadores = e44player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Arabia Saudita":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                    weigth = len(jugadores)
                else:
                    jugadores = e45player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Israel":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                    weigth = len(jugadores)
                else:
                    jugadores = e46player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Australia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                    weigth = len(jugadores)
                else:
                    jugadores = e47player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Qatar":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                    weigth = len(jugadores)
                else:
                    jugadores = e48player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)        
                  
    
        goles_totales.append(gol)            
    numeros_aleatorios = random.sample(range(1,91), len(goles_totales))
    goles_totales.sort()
    numeros_aleatorios.sort()
    print(f'\U000026BD Goles {club}: '+', '.join([f'{gol} \u23f1 {num}\'' for gol, num in zip(goles_totales, numeros_aleatorios)]))


    return goles_totales 


def lesiones(club,jugadores_sancionados,jugadores_lesionados,equipo_player,valoracion_player,nombre_jugador):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14,0.14]           
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.2, 0.2, 0.2, 0.2, 0.2] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.25, 0.25, 0.25, 0.25 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.3, 0.3, 0.3] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.5,0.5]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0] 
    for i in jugadores_lesionados:
        if i in jugadores_sancionados: pass
        else: jugadores_sancionados.append(i)
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array    
    def random_generator():
        rand_num = random.random() 
        if rand_num <= 0.05:
            return 0 
        else:
            return 1 

    numeros = []
    num1 = random_generator()
    if num1 == 1:
        numeros.append(num1)
    lat = len(numeros)
    contador = 0
    amarillas = []
    while (contador == lat):
        e1player = ["Martinelli", "Gabriel Jesus", "Havertz", "Saka", "Odegaard"]
        e2player = ["Coutinho", "Watkins", "Ramsey", "Buendía"]
        e3player = ["Semenyo","Solanke","Lerma","Christie"]
        e4player = ["Toney", "Mbeumo", "Schade", "Ghoddos"]
        e5player = ["Fati", "Welbeck", "Mitoma", "Enciso", "Ferguson"]
        e6player = ["Sterling", "Fernandez", "Nkunku", "Mudryk","Palmer"]
        e7player = ["Ayew(cp)", "Mateta", "Doucoure", "Edouard"]
        e8player = ["Beto", "McNeil", "Calvert-Lewin", "Danjuma"]
        e9player = ["Traore", "Jimenez", "Iwobi", "Willian"]
        e10player = ["Rutter","Summerville","Gnoto","Gray"]
        e11player = ["Vardy","Iheanacho","Akgün","Mavididi"]
        e12player = ["Salah", "MacAllister", "Núñez", "Luis Díaz", "Diogo Jota"]
        e13player = ["Haaland", "Foden", "Grealish", "Álvarez", "De Bruyne"]
        e14player = ["Rashford", "Mount", "Bruno Fernandes", "Martial", "Sancho"]
        e15player = ["Isak", "Guimarães", "Joelinton", "Tonali", "Murphy"]
        e16player = ["Awoniyi", "Gibbs-White", "Origi", "Danilo"]
        e17player = ["Adams","Alcaraz","Armstrong","Edozie"]
        e18player = ["Richarlison", "Son", "Sarr", "Kulusevski", "Perisic"]
        e19player = ["Antonio", "Paquetá", "Benrahma", "Ings"]
        e20player = ["Silva", "Cunha", "Kalajdzic", "Sarabia"]
        e21player = ["Foster", "Redmond", "Amdouni", "Brownhill"]
        e22player = ["Osula", "Jebbison", "Archer", "Brewster"]
        e23player = ["Adebayo", "Lokonga", "Morris", "Ogbene"]
        e24player = ["Greenwood","Silvera","Jones","Forss"]
        e25player = ["Godden","Simms","Tavares","Wright"]
        e26player = ["Clarke","Bennette","Semedo","Rigg"]
        e27player = ["Leonard","Gallagher","Ennis","Hedges"]
        e28player = ["Bradshaw","Nisbet","Watmore","Emakhu"]
        e29player = ["Dike","Wallace","Diangana","Phillips"]
        e30player = ["Lowe","Ginnelly","Cooper","Cullen"]
        e31player = ["Bayo","Martins","Healeyr","Ince"]
        e32player = ["Keane","Holmes","Riis","McCann"]
        e33player = ["Barnes","Sargent","Gibbs","Idah"]
        e34player =["Wells","Cornick","Bell","Conway"]
        e35player = ["Delap","Lokilo","Sinik","Connolly"]
        e36player = ["Gooch","Campbell","Mmaee","Gayle"]
        e37player = ["Hogan","Jutkiewicz","Roberts","Stansfield"]
        e38player = ["Koroma","Burgzorg","Ward","Hudlin"]
        e39player = ["Ugbo","Robinson","Bowler","Grant"]
        e40player = ["Dykes","Adomah","Willock","Smyth"]
        e41player = ["Mbappe","Asensio","O.Dembele","Muani","Barcola"]
        e42player = ["Lacazette","Baldé","Jeffinho","Tolisso","Tagliafico"]
        e43player = ["Martinez","Alexis Sánchez","Arnautovic","Calhanoglu","Mkhitaryan"]
        e44player = ["Vlahovic","Kean","Chiesa","Milik","Pogba"]
        e45player = ["Giroud","Leão","Pulisic","Jović","Romero"]
        e46player = ["Osimhen","Raspadori","Simeone","Politano","Kvaratskhelia"]
        e47player = ["Dybala","Belotti","El Shaarawy","Lukaku","Pellegrini"]
        e48player = ["Griezmann","Morata","de Paul","Koke","Lemar"]
        e49player = ["Lewandowski","Gavi","Felix","Raphinha","Torres"]
        e50player = ["Bellingham","Vinicius","Rodrygo","Modric","Tchouameni"]
        e51player =["Haller","Moukoko","Adeyemi","Reus","Reyna"]
        e52player = ["Kane","Gnabry","Müller","Musiala","Sané"]
        e53player = ["Tella","Hložek","Hofmann","Adli","Boniface"]
        e54player = ["Taremi","Galeno","Evanilson","Jaime","Grujic"]
        e55player = ["Paulinho","Trincao","Edwards","Santos","Goncalves"]
        e56player = ["Götze","Marmoush","Ngankam","Alario","Rode"]
        e57player = ["Aubameyang","Sarr(M)","Correa","Ndiaye","Gueye"]
        e58player = ["Zakharyan","En-Nesyri","Suso","Ocampos","Rakitić"]
        e59player = ["Neres","Rafa","Di María","Musa","Gouveia"]
        e60player = ["Poulsen","Werner","Sesko","Olmo","Openda"]
        e61player = ["Bergwijn","Akpom","Mikautadze","Godts","Tahirovic"]
        e62player = ["Ben Yedder","Martins(M)","Embolo","Seghir","Camara"]
        e63player = ["Traore","Sikan","Petryak","Zubkov","Bondarenko"]
        e64player = ["Buchanan","Nusa","Jutglà","Vermant","Olsen"]
        e65player = ["de Jong","Bakayoko","Til","Veerman","Lang"]
        e66player = ["Sadiq","Oyarzabal","Andre Silva","Kubo","Zakharyan"]
        e67player = ["Immobile","Anderson","Pedro(L)","Basic","Isaksen"]
        e68player = ["Muriel","Scamacca","Pasalic","Lookman","Adopo"]
        e69player = ["N.Gonzalez","Arthur","Beltrán","Sottil","Kouamé"]
        e70player = ["Karlsson","Ndoye","Orsolini","Hooijdonk"]
        e71player = ["Pellegri","Radonjic","Sanabria","Vlasic"]
        e72player = ["Carvalho","Colombo","Maric","Ciurria"]
        e73player = ["Deulofeu","Thauvin","Brenner"," Success"]
        e74player = ["Berardi","Lauriente","Mulattieri","Pinamonti"]
        e75player = ["Caputo","Cambiaghi","Gyasi","Destro"]
        e76player = ["Botheim","Candreva","Ikwuemesi","Maggiore"]
        e77player = ["Piccoli","Krstovic","Banda","Burnete"]
        e78player = ["Mboula","Djuric","Braaf","Ngonge"]
        e79player = ["Moro","Krollis","Verde","Elia"]
        e80player = ["Ciofani","Buonaiuto","Coda","Zanimacchia"]
        e81player = ["Estanis","Borini","Gumina","Monache"]
        e82player = ["Cheddira","Kvernadze","Soule","Cuni"] 
        e83player = ["Retegui","Gudmundsson","Ekuban","Fini"]
        e84player = ["Diaw","Nasti","Maita","Sibilli"]
        e85player = ["Colak","Benedyczak","Begic","Mihaila"]
        e86player = ["Lapadula","Pavoletti","Petagna","Zito"]
        e87player = ["Rover","Odogwu","Pecorino","Cisco"]
        e88player = ["Gondo","Lanini","Pettinari","Vido"]
        e89player =["Johsen","Pierini","Tessmann","Pohjanpalo"]
        e90player = ["Mancuso","Brunori","Soleri","Segre"]
        e91player = ["Falcinelli","Manconi","Giovannini","Gerli"]
        e92player = ["Mlakar","Torregrossa","Tramoni","Nagy"]
        e93player = ["Pedro Mendes","Millico","Nestorovski","Caligara"]
        e94player = ["Cutrone","Gabrielloni","Baselli","Cerri"]
        e95player = ["Favili","Dionisi","Raimondo","Proietti"]
        e96player = ["Moncini","Bianchi","Bisoli","Ferro"]
        e97player = ["Magrassi","Maistrello","Pittarello","Danzi"]
        e98player = ["Forte","Tutino","Novello","Crespi"]
        e99player =["Matos","Cudrig","Julitanmo","Seghetti"]
        e100player = ["Antenucci","Dalmonte","Siligardi","Rabbi"]
        e101player = ["Improta","Ciano","Marotta","Bolsius"]
        if equipo_player == "Arsenal":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e1player.insert(pos,nombre_jugador)
        elif equipo_player == "Aston Villa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e2player.insert(pos,nombre_jugador)
        elif equipo_player == "Bournemouth":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e3player.insert(pos,nombre_jugador)
        elif equipo_player == "Brentford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e4player.insert(pos,nombre_jugador)
        elif equipo_player == "Brigthon":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1 
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e5player.insert(pos,nombre_jugador)
        elif equipo_player == "Chelsea":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e6player.insert(pos,nombre_jugador)
        elif equipo_player == "Crystal Palace":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e7player.insert(pos,nombre_jugador)
        elif equipo_player == "Everton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e8player.insert(pos,nombre_jugador)
        elif equipo_player == "Fulham":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e9player.insert(pos,nombre_jugador)
        elif equipo_player == "Leeds United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e10player.insert(pos,nombre_jugador)
        elif equipo_player == "Leicester City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e11player.insert(pos,nombre_jugador)
        elif equipo_player == "Liverpool":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e12player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester City":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e13player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester United":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            elif valoracion_player > 30: 
                pos = 6
            else: pos = 7         
            e14player.insert(pos,nombre_jugador)
        elif equipo_player == "Newcastle":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e15player.insert(pos,nombre_jugador)
        elif equipo_player == "Nottingham Forest":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e16player.insert(pos,nombre_jugador)
        elif equipo_player == "Southampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e17player.insert(pos,nombre_jugador)
        elif equipo_player == "Tottenham":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e18player.insert(pos,nombre_jugador)
        elif equipo_player == "West ham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e19player.insert(pos,nombre_jugador)
        elif equipo_player == "Wolverhampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e20player.insert(pos,nombre_jugador)
        elif equipo_player == "Burnley":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e21player.insert(pos,nombre_jugador)
        elif equipo_player == "Sheffield United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e22player.insert(pos,nombre_jugador)
        elif equipo_player == "Luton Town":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e23player.insert(pos,nombre_jugador)
        elif equipo_player == "Middlesbrough":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e24player.insert(pos,nombre_jugador)
        elif equipo_player == "Coventry City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e25player.insert(pos,nombre_jugador)
        elif equipo_player == "Sunderland":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e26player.insert(pos,nombre_jugador)
        elif equipo_player == "Blackburn Rovers":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e27player.insert(pos,nombre_jugador)     
        elif equipo_player == "Millwall":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e28player.insert(pos,nombre_jugador)
        elif equipo_player == "West Bromwich Albion":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e29player.insert(pos,nombre_jugador)   
        elif equipo_player == "Swansea":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e30player.insert(pos,nombre_jugador)
        elif equipo_player == "Watford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e31player.insert(pos,nombre_jugador) 
        elif equipo_player == "Preston North End":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e32player.insert(pos,nombre_jugador)     
        elif equipo_player == "Norwich":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e33player.insert(pos,nombre_jugador)            
        elif equipo_player == "Bristol City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e34player.insert(pos,nombre_jugador)
        elif equipo_player == "Hull City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            
            e35player.insert(pos,nombre_jugador) 
        elif equipo_player == "Stoke City":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e36player.insert(pos,nombre_jugador)
        elif equipo_player == "Birmingham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e37player.insert(pos,nombre_jugador)
        elif equipo_player == "Huddersfield Town":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e38player.insert(pos,nombre_jugador)
        elif equipo_player == "Cardiff City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e39player.insert(pos,nombre_jugador)
        elif equipo_player == "Queens Park Rangers":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e40player.insert(pos,nombre_jugador)
        
        elif equipo_player == "Inter":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e43player.insert(pos,nombre_jugador)
        elif equipo_player == "Juventus":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e44player.insert(pos,nombre_jugador)
        elif equipo_player == "Milan":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e45player.insert(pos,nombre_jugador)
        elif equipo_player == "Napoli":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e46player.insert(pos,nombre_jugador)
        elif equipo_player == "Roma":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e47player.insert(pos,nombre_jugador)
        elif equipo_player == "Lazio":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e67player.insert(pos,nombre_jugador)
        elif equipo_player == "Atalanta":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e68player.insert(pos,nombre_jugador)
        elif equipo_player == "Fiorentina":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e68player.insert(pos,nombre_jugador)
        elif equipo_player == "Bologna":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e70player.insert(pos,nombre_jugador)
        elif equipo_player == "Torino":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e71player.insert(pos,nombre_jugador)
        elif equipo_player == "Sassuolo":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e74player.insert(pos,nombre_jugador)
        elif equipo_player == "Udinese":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e73player.insert(pos,nombre_jugador)
        elif equipo_player == "Monza":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e72player.insert(pos,nombre_jugador)
        elif equipo_player == "Empoli":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e75player.insert(pos,nombre_jugador)
        elif equipo_player == "Salernitana":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e76player.insert(pos,nombre_jugador)
        elif equipo_player == "Lecce":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e77player.insert(pos,nombre_jugador)
        elif equipo_player == "Hellas Verona":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e78player.insert(pos,nombre_jugador)
        elif equipo_player == "Spezia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e79player.insert(pos,nombre_jugador)
        elif equipo_player == "Cremonese":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e80player.insert(pos,nombre_jugador)
        elif equipo_player == "Sampdoria":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e81player.insert(pos,nombre_jugador)
        elif equipo_player == "Genoa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e83player.insert(pos,nombre_jugador)
        elif equipo_player == "Frosinone":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e82player.insert(pos,nombre_jugador)
        elif equipo_player == "Bari":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e84player.insert(pos,nombre_jugador)
        elif equipo_player == "Parma":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e85player.insert(pos,nombre_jugador)
        elif equipo_player == "Cagliari":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e86player.insert(pos,nombre_jugador)
        elif equipo_player == "Sudtirol":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e87player.insert(pos,nombre_jugador)
        elif equipo_player == "Reggina":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e88player.insert(pos,nombre_jugador)
        elif equipo_player == "Venezia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e89player.insert(pos,nombre_jugador)
        elif equipo_player == "Palermo":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e90player.insert(pos,nombre_jugador)
        elif equipo_player == "Modena":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e91player.insert(pos,nombre_jugador)
        elif equipo_player == "Pisa":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e92player.insert(pos,nombre_jugador)
        elif equipo_player == "Ascoli":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e93player.insert(pos,nombre_jugador)
        elif equipo_player == "Como":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e94player.insert(pos,nombre_jugador)
        elif equipo_player == "Ternana":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e95player.insert(pos,nombre_jugador)
        elif equipo_player == "Brescia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e96player.insert(pos,nombre_jugador)
        elif equipo_player == "Cittadella":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e97player.insert(pos,nombre_jugador)
        elif equipo_player == "Spal":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e100player.insert(pos,nombre_jugador)
        elif equipo_player == "Benevento":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e101player.insert(pos,nombre_jugador)
        elif equipo_player == "Cosenza":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e98player.insert(pos,nombre_jugador)
        elif equipo_player == "Perugia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e99player.insert(pos,nombre_jugador)
        
        
        
        
        
        
   
        if club == "Arsenal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                    weigth = len(jugadores)
                else:    
                    jugadores = e1player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Aston Villa":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                    weigth = len(jugadores)
                else:
                    jugadores = e2player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Bournemouth":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                    weigth = len(jugadores)
                else:
                    jugadores = e3player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Brentford":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                    weigth = len(jugadores)
                else:
                    jugadores = e4player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Brigthon":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                    weigth = len(jugadores)
                else:
                    jugadores = e5player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Chelsea":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                    weigth = len(jugadores)
                else:
                    jugadores = e6player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Crystal Palace":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                    weigth = len(jugadores)
                else:
                    jugadores = e7player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Everton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                    weigth = len(jugadores)
                else:
                    jugadores = e8player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Fulham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                    weigth = len(jugadores)
                else:
                    jugadores = e9player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Leeds United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                    weigth = len(jugadores)
                else:
                    jugadores = e10player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Leicester City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                    weigth = len(jugadores)
                else:
                    jugadores = e11player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Liverpool":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                    weigth = len(jugadores)
                else:
                    jugadores = e12player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Manchester City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                    weigth = len(jugadores)
                else:
                    jugadores = e13player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Manchester United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                    weigth = len(jugadores)
                else:
                    jugadores = e14player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Newcastle":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                    weigth = len(jugadores)
                else:
                    jugadores = e15player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Nottingham Forest":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                    weigth = len(jugadores)
                else:
                    jugadores = e16player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Southampton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                    weigth = len(jugadores)
                else:
                    jugadores = e17player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Tottenham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                    weigth = len(jugadores)
                else:
                    jugadores = e18player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "West ham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                    weigth = len(jugadores)
                else:
                    jugadores = e19player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Wolverhampton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                    weigth = len(jugadores)
                else:
                    jugadores = e20player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Burnley":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                    weigth = len(jugadores)
                else:
                    jugadores = e21player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Sheffield United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                    weigth = len(jugadores)
                else:
                    jugadores = e22player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Luton Town":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                    weigth = len(jugadores)
                else:
                    jugadores = e23player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Middlesbrough":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                    weigth = len(jugadores)
                else:
                    jugadores = e24player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Coventry City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                    weigth = len(jugadores)
                else:
                    jugadores = e25player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Sunderland":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                    weigth = len(jugadores)
                else:
                    jugadores = e26player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Blackburn Rovers":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                    weigth = len(jugadores)
                else:
                    jugadores = e27player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Millwall":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                    weigth = len(jugadores)
                else:
                    jugadores = e28player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "West Bromwich Albion":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                    weigth = len(jugadores)
                else:
                    jugadores = e29player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Swansea":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                    weigth = len(jugadores)
                else:
                    jugadores = e30player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Watford":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                    weigth = len(jugadores)
                else:
                    jugadores = e31player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Preston North End":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                    weigth = len(jugadores)
                else:
                    jugadores = e32player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Norwich":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                    weigth = len(jugadores)
                else:
                    jugadores = e33player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)             
        elif club == "Bristol City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                    weigth = len(jugadores)
                else:
                    jugadores = e34player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Hull City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                    weigth = len(jugadores)
                else:
                    jugadores = e35player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Stoke City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                    weigth = len(jugadores)
                else:
                    jugadores = e36player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Birmingham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                    weigth = len(jugadores)
                else:
                    jugadores = e37player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Huddersfield Town":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                    weigth = len(jugadores)
                else:
                    jugadores = e38player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Cardiff City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                    weigth = len(jugadores)
                else:
                    jugadores = e39player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Queens Park Rangers":   
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                    weigth = len(jugadores)
                else:
                    jugadores = e40player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "PSG":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                weigth = len(jugadores)
            else:
                jugadores = e41player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "O.Lyon":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                weigth = len(jugadores)
            else:
                jugadores = e42player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Inter":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                weigth = len(jugadores)
            else:
                jugadores = e43player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Juventus":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                weigth = len(jugadores)
            else:
                jugadores = e44player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Milan":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                weigth = len(jugadores)
            else:
                jugadores = e45player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Napoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                weigth = len(jugadores)
            else:
                jugadores = e46player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Roma":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                weigth = len(jugadores)
            else:
                jugadores = e47player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Atl.Madrid":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                weigth = len(jugadores)
            else:
                jugadores = e48player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Barcelona":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e49player)
                weigth = len(jugadores)
            else:
                jugadores = e49player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Real Madrid":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e50player)
                weigth = len(jugadores)
            else:
                jugadores = e50player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "B.Dortmund":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e51player)
                weigth = len(jugadores)
            else:
                jugadores = e51player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Bayern Munich":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e52player)
                weigth = len(jugadores)
            else:
                jugadores = e52player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "B.Leverkusen":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e53player)
                weigth = len(jugadores)
            else:
                jugadores = e53player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Porto":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e54player)
                weigth = len(jugadores)
            else:
                jugadores = e54player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Sporting Lisboa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e55player)
                weigth = len(jugadores)
            else:
                jugadores = e55player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Frankfurt":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e56player)
                weigth = len(jugadores)
            else:
                jugadores = e56player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "O.Marsella":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e57player)
                weigth = len(jugadores)
            else:
                jugadores = e57player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)   
        elif club == "Sevilla":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e58player)
                weigth = len(jugadores)
            else:
                jugadores = e58player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Benfica":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e59player)
                weigth = len(jugadores)
            else:
                jugadores = e59player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Leipzig":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e60player)
                weigth = len(jugadores)
            else:
                jugadores = e60player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Ajax":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e61player)
                weigth = len(jugadores)
            else:
                jugadores = e61player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Monaco":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e62player)
                weigth = len(jugadores)
            else:
                jugadores = e62player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Shakhtar":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e63player)
                weigth = len(jugadores)
            else:
                jugadores = e63player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Brugge":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e64player)
                weigth = len(jugadores)
            else:
                jugadores = e64player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "PSV":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e65player)
                weigth = len(jugadores)
            else:
                jugadores = e65player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Real Sociedad":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e66player)
                weigth = len(jugadores)
            else:
                jugadores = e66player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)                        
        elif club == "Lazio":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e67player)
                weigth = len(jugadores)
            else:
                jugadores = e67player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Atalanta":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e68player)
                weigth = len(jugadores)
            else:
                jugadores = e68player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Fiorentina":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e69player)
                weigth = len(jugadores)
            else:
                jugadores = e69player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Bologna":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e70player)
                weigth = len(jugadores)
            else:
                jugadores = e70player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Torino":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e71player)
                weigth = len(jugadores)
            else:
                jugadores = e71player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Monza":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e72player)
                weigth = len(jugadores)
            else:
                jugadores = e72player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Udinese":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e73player)
                weigth = len(jugadores)
            else:
                jugadores = e73player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Sassuolo":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e74player)
                weigth = len(jugadores)
            else:
                jugadores = e74player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Empoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e75player)
                weigth = len(jugadores)
            else:
                jugadores = e75player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Salernitana":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e76player)
                weigth = len(jugadores)
            else:
                jugadores = e76player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Lecce":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e77player)
                weigth = len(jugadores)
            else:
                jugadores = e77player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Hellas Verona":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e78player)
                weigth = len(jugadores)
            else:
                jugadores = e78player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Spezia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e79player)
                weigth = len(jugadores)
            else:
                jugadores = e79player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cremonese":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e80player)
                weigth = len(jugadores)
            else:
                jugadores = e80player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Sampdoria":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e81player)
                weigth = len(jugadores)
            else:
                jugadores = e81player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Frosinone":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e82player)
                weigth = len(jugadores)
            else:
                jugadores = e82player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Genoa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e83player)
                weigth = len(jugadores)
            else:
                jugadores = e83player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Bari":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e84player)
                weigth = len(jugadores)
            else:
                jugadores = e84player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Parma":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e85player)
                weigth = len(jugadores)
            else:
                jugadores = e85player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cagliari":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e86player)
                weigth = len(jugadores)
            else:
                jugadores = e86player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)         
        elif club == "Sudtirol":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e87player)
                weigth = len(jugadores)
            else:
                jugadores = e87player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Reggina":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e88player)
                weigth = len(jugadores)
            else:
                jugadores = e88player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Venezia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e89player)
                weigth = len(jugadores)
            else:
                jugadores = e89player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Palermo":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e90player)
                weigth = len(jugadores)
            else:
                jugadores = e90player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Modena":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e91player)
                weigth = len(jugadores)
            else:
                jugadores = e91player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Pisa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e92player)
                weigth = len(jugadores)
            else:
                jugadores = e92player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Ascoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e93player)
                weigth = len(jugadores)
            else:
                jugadores = e93player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Como":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e94player)
                weigth = len(jugadores)
            else:
                jugadores = e94player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Ternana":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e95player)
                weigth = len(jugadores)
            else:
                jugadores = e95player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Brescia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e96player)
                weigth = len(jugadores)
            else:
                jugadores = e96player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cittadella":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e97player)
                weigth = len(jugadores)
            else:
                jugadores = e97player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Cosenza":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e98player)
                weigth = len(jugadores)
            else:
                jugadores = e98player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Perugia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e99player)
                weigth = len(jugadores)
            else:
                jugadores = e99player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Spal":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e100player)
                weigth = len(jugadores)
            else:
                jugadores = e100player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Benevento":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e101player)
                weigth = len(jugadores)
            else:
                jugadores = e101player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)         
        contador += 1     
        secuencia = [1, 2, 3, 4, 5]
        lesionn = random.choice(secuencia)
        amarillas.append([gol,lesionn])
    if len(amarillas) != 0:   
        for i in amarillas:
            print(f"lesionado {i[0]}, {i[1]} partidos")
    return amarillas

def amarillas(club,jugadores_sancionados,jugadores_lesionados,equipo_player,valoracion_player,nombre_jugador):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14,0.14]           
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.2, 0.2, 0.2, 0.2, 0.2] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.25, 0.25, 0.25, 0.25 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.3, 0.3, 0.3] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.5,0.5]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0] 
    
    if len(jugadores_lesionados) != 0:
        for i in jugadores_lesionados:
            if i in jugadores_sancionados: pass
            else: jugadores_sancionados.append(i)
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array    
    def random_generator():
        rand_num = random.random() 
        if rand_num <= 0.1:
            return 0 
        else:
            return 1 

    numeros = []
    num1 = random_generator()
    if num1 == 1:
        numeros.append(num1)
    num2 = random_generator()
    if num1 == 1:    
        numeros.append(num2)
    lat = len(numeros)
    contador = 0
    amarillas = []
    while (contador == lat): 
        e1player = ["Martinelli", "Gabriel Jesus", "Havertz", "Saka", "Odegaard"]
        e2player = ["Coutinho", "Watkins", "Ramsey", "Buendía"]
        e3player = ["Semenyo","Solanke","Lerma","Christie"]
        e4player = ["Toney", "Mbeumo", "Schade", "Ghoddos"]
        e5player = ["Fati", "Welbeck", "Mitoma", "Enciso", "Ferguson"]
        e6player = ["Sterling", "Fernandez", "Nkunku", "Mudryk","Palmer"]
        e7player = ["Ayew(cp)", "Mateta", "Doucoure", "Edouard"]
        e8player = ["Beto", "McNeil", "Calvert-Lewin", "Danjuma"]
        e9player = ["Traore", "Jimenez", "Iwobi", "Willian"]
        e10player = ["Rutter","Summerville","Gnoto","Gray"]
        e11player = ["Vardy","Iheanacho","Akgün","Mavididi"]
        e12player = ["Salah", "MacAllister", "Núñez", "Luis Díaz", "Diogo Jota"]
        e13player = ["Haaland", "Foden", "Grealish", "Álvarez", "De Bruyne"]
        e14player = ["Rashford", "Mount", "Bruno Fernandes", "Martial", "Sancho"]
        e15player = ["Isak", "Guimarães", "Joelinton", "Tonali", "Murphy"]
        e16player = ["Awoniyi", "Gibbs-White", "Origi", "Danilo"]
        e17player = ["Adams","Alcaraz","Armstrong","Edozie"]
        e18player = ["Richarlison", "Son", "Sarr", "Kulusevski", "Perisic"]
        e19player = ["Antonio", "Paquetá", "Benrahma", "Ings"]
        e20player = ["Silva", "Cunha", "Kalajdzic", "Sarabia"]
        e21player = ["Foster", "Redmond", "Amdouni", "Brownhill"]
        e22player = ["Osula", "Jebbison", "Archer", "Brewster"]
        e23player = ["Adebayo", "Lokonga", "Morris", "Ogbene"]
        e24player = ["Greenwood","Silvera","Jones","Forss"]
        e25player = ["Godden","Simms","Tavares","Wright"]
        e26player = ["Clarke","Bennette","Semedo","Rigg"]
        e27player = ["Leonard","Gallagher","Ennis","Hedges"]
        e28player = ["Bradshaw","Nisbet","Watmore","Emakhu"]
        e29player = ["Dike","Wallace","Diangana","Phillips"]
        e30player = ["Lowe","Ginnelly","Cooper","Cullen"]
        e31player = ["Bayo","Martins","Healeyr","Ince"]
        e32player = ["Keane","Holmes","Riis","McCann"]
        e33player = ["Barnes","Sargent","Gibbs","Idah"]
        e34player =["Wells","Cornick","Bell","Conway"]
        e35player = ["Delap","Lokilo","Sinik","Connolly"]
        e36player = ["Gooch","Campbell","Mmaee","Gayle"]
        e37player = ["Hogan","Jutkiewicz","Roberts","Stansfield"]
        e38player = ["Koroma","Burgzorg","Ward","Hudlin"]
        e39player = ["Ugbo","Robinson","Bowler","Grant"]
        e40player = ["Dykes","Adomah","Willock","Smyth"]
        e41player = ["Mbappe","Asensio","O.Dembele","Muani","Barcola"]
        e42player = ["Lacazette","Baldé","Jeffinho","Tolisso","Tagliafico"]
        e43player = ["Martinez","Alexis Sánchez","Arnautovic","Calhanoglu","Mkhitaryan"]
        e44player = ["Vlahovic","Kean","Chiesa","Milik","Pogba"]
        e45player = ["Giroud","Leão","Pulisic","Jović","Romero"]
        e46player = ["Osimhen","Raspadori","Simeone","Politano","Kvaratskhelia"]
        e47player = ["Dybala","Belotti","El Shaarawy","Lukaku","Pellegrini"]
        e48player = ["Griezmann","Morata","de Paul","Koke","Lemar"]
        e49player = ["Lewandowski","Gavi","Felix","Raphinha","Torres"]
        e50player = ["Bellingham","Vinicius","Rodrygo","Modric","Tchouameni"]
        e51player =["Haller","Moukoko","Adeyemi","Reus","Reyna"]
        e52player = ["Kane","Gnabry","Müller","Musiala","Sané"]
        e53player = ["Tella","Hložek","Hofmann","Adli","Boniface"]
        e54player = ["Taremi","Galeno","Evanilson","Jaime","Grujic"]
        e55player = ["Paulinho","Trincao","Edwards","Santos","Goncalves"]
        e56player = ["Götze","Marmoush","Ngankam","Alario","Rode"]
        e57player = ["Aubameyang","Sarr(M)","Correa","Ndiaye","Gueye"]
        e58player = ["Zakharyan","En-Nesyri","Suso","Ocampos","Rakitić"]
        e59player = ["Neres","Rafa","Di María","Musa","Gouveia"]
        e60player = ["Poulsen","Werner","Sesko","Olmo","Openda"]
        e61player = ["Bergwijn","Akpom","Mikautadze","Godts","Tahirovic"]
        e62player = ["Ben Yedder","Martins(M)","Embolo","Seghir","Camara"]
        e63player = ["Traore","Sikan","Petryak","Zubkov","Bondarenko"]
        e64player = ["Buchanan","Nusa","Jutglà","Vermant","Olsen"]
        e65player = ["de Jong","Bakayoko","Til","Veerman","Lang"]
        e66player = ["Sadiq","Oyarzabal","Andre Silva","Kubo","Zakharyan"]
        e67player = ["Immobile","Anderson","Pedro(L)","Basic","Isaksen"]
        e68player = ["Muriel","Scamacca","Pasalic","Lookman","Adopo"]
        e69player = ["N.Gonzalez","Arthur","Beltrán","Sottil","Kouamé"]
        e70player = ["Karlsson","Ndoye","Orsolini","Hooijdonk"]
        e71player = ["Pellegri","Radonjic","Sanabria","Vlasic"]
        e72player = ["Carvalho","Colombo","Maric","Ciurria"]
        e73player = ["Deulofeu","Thauvin","Brenner"," Success"]
        e74player = ["Berardi","Lauriente","Mulattieri","Pinamonti"]
        e75player = ["Caputo","Cambiaghi","Gyasi","Destro"]
        e76player = ["Botheim","Candreva","Ikwuemesi","Maggiore"]
        e77player = ["Piccoli","Krstovic","Banda","Burnete"]
        e78player = ["Mboula","Djuric","Braaf","Ngonge"]
        e79player = ["Moro","Krollis","Verde","Elia"]
        e80player = ["Ciofani","Buonaiuto","Coda","Zanimacchia"]
        e81player = ["Estanis","Borini","Gumina","Monache"]
        e82player = ["Cheddira","Kvernadze","Soule","Cuni"] 
        e83player = ["Retegui","Gudmundsson","Ekuban","Fini"]
        e84player = ["Diaw","Nasti","Maita","Sibilli"]
        e85player = ["Colak","Benedyczak","Begic","Mihaila"]
        e86player = ["Lapadula","Pavoletti","Petagna","Zito"]
        e87player = ["Rover","Odogwu","Pecorino","Cisco"]
        e88player = ["Gondo","Lanini","Pettinari","Vido"]
        e89player =["Johsen","Pierini","Tessmann","Pohjanpalo"]
        e90player = ["Mancuso","Brunori","Soleri","Segre"]
        e91player = ["Falcinelli","Manconi","Giovannini","Gerli"]
        e92player = ["Mlakar","Torregrossa","Tramoni","Nagy"]
        e93player = ["Pedro Mendes","Millico","Nestorovski","Caligara"]
        e94player = ["Cutrone","Gabrielloni","Baselli","Cerri"]
        e95player = ["Favili","Dionisi","Raimondo","Proietti"]
        e96player = ["Moncini","Bianchi","Bisoli","Ferro"]
        e97player = ["Magrassi","Maistrello","Pittarello","Danzi"]
        e98player = ["Forte","Tutino","Novello","Crespi"]
        e99player =["Matos","Cudrig","Julitanmo","Seghetti"]
        e100player = ["Antenucci","Dalmonte","Siligardi","Rabbi"]
        e101player = ["Improta","Ciano","Marotta","Bolsius"]
        if equipo_player == "Arsenal":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e1player.insert(pos,nombre_jugador)
        elif equipo_player == "Aston Villa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e2player.insert(pos,nombre_jugador)
        elif equipo_player == "Bournemouth":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e3player.insert(pos,nombre_jugador)
        elif equipo_player == "Brentford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e4player.insert(pos,nombre_jugador)
        elif equipo_player == "Brigthon":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1 
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e5player.insert(pos,nombre_jugador)
        elif equipo_player == "Chelsea":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e6player.insert(pos,nombre_jugador)
        elif equipo_player == "Crystal Palace":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e7player.insert(pos,nombre_jugador)
        elif equipo_player == "Everton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e8player.insert(pos,nombre_jugador)
        elif equipo_player == "Fulham":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e9player.insert(pos,nombre_jugador)
        elif equipo_player == "Leeds United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e10player.insert(pos,nombre_jugador)
        elif equipo_player == "Leicester City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e11player.insert(pos,nombre_jugador)
        elif equipo_player == "Liverpool":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e12player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester City":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e13player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester United":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            elif valoracion_player > 30: 
                pos = 6
            else: pos = 7         
            e14player.insert(pos,nombre_jugador)
        elif equipo_player == "Newcastle":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e15player.insert(pos,nombre_jugador)
        elif equipo_player == "Nottingham Forest":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e16player.insert(pos,nombre_jugador)
        elif equipo_player == "Southampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e17player.insert(pos,nombre_jugador)
        elif equipo_player == "Tottenham":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e18player.insert(pos,nombre_jugador)
        elif equipo_player == "West ham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e19player.insert(pos,nombre_jugador)
        elif equipo_player == "Wolverhampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e20player.insert(pos,nombre_jugador)
        elif equipo_player == "Burnley":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e21player.insert(pos,nombre_jugador)
        elif equipo_player == "Sheffield United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e22player.insert(pos,nombre_jugador)
        elif equipo_player == "Luton Town":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e23player.insert(pos,nombre_jugador)
        elif equipo_player == "Middlesbrough":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e24player.insert(pos,nombre_jugador)
        elif equipo_player == "Coventry City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e25player.insert(pos,nombre_jugador)
        elif equipo_player == "Sunderland":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e26player.insert(pos,nombre_jugador)
        elif equipo_player == "Blackburn Rovers":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e27player.insert(pos,nombre_jugador)     
        elif equipo_player == "Millwall":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e28player.insert(pos,nombre_jugador)
        elif equipo_player == "West Bromwich Albion":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e29player.insert(pos,nombre_jugador)   
        elif equipo_player == "Swansea":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e30player.insert(pos,nombre_jugador)
        elif equipo_player == "Watford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e31player.insert(pos,nombre_jugador) 
        elif equipo_player == "Preston North End":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e32player.insert(pos,nombre_jugador)     
        elif equipo_player == "Norwich":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e33player.insert(pos,nombre_jugador)            
        elif equipo_player == "Bristol City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e34player.insert(pos,nombre_jugador)
        elif equipo_player == "Hull City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            
            e35player.insert(pos,nombre_jugador) 
        elif equipo_player == "Stoke City":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e36player.insert(pos,nombre_jugador)
        elif equipo_player == "Birmingham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e37player.insert(pos,nombre_jugador)
        elif equipo_player == "Huddersfield Town":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e38player.insert(pos,nombre_jugador)
        elif equipo_player == "Cardiff City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e39player.insert(pos,nombre_jugador)
        elif equipo_player == "Queens Park Rangers":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e40player.insert(pos,nombre_jugador)
        
        elif equipo_player == "Inter":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e43player.insert(pos,nombre_jugador)
        elif equipo_player == "Juventus":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e44player.insert(pos,nombre_jugador)
        elif equipo_player == "Milan":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e45player.insert(pos,nombre_jugador)
        elif equipo_player == "Napoli":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e46player.insert(pos,nombre_jugador)
        elif equipo_player == "Roma":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e47player.insert(pos,nombre_jugador)
        elif equipo_player == "Lazio":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e67player.insert(pos,nombre_jugador)
        elif equipo_player == "Atalanta":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e68player.insert(pos,nombre_jugador)
        elif equipo_player == "Fiorentina":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e69player.insert(pos,nombre_jugador)
        elif equipo_player == "Bologna":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e70player.insert(pos,nombre_jugador)
        elif equipo_player == "Torino":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e71player.insert(pos,nombre_jugador)
        elif equipo_player == "Sassuolo":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e74player.insert(pos,nombre_jugador)
        elif equipo_player == "Udinese":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e73player.insert(pos,nombre_jugador)
        elif equipo_player == "Monza":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e72player.insert(pos,nombre_jugador)
        elif equipo_player == "Empoli":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e75player.insert(pos,nombre_jugador)
        elif equipo_player == "Salernitana":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e76player.insert(pos,nombre_jugador)
        elif equipo_player == "Lecce":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e77player.insert(pos,nombre_jugador)
        elif equipo_player == "Hellas Verona":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e78player.insert(pos,nombre_jugador)
        elif equipo_player == "Spezia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e79player.insert(pos,nombre_jugador)
        elif equipo_player == "Cremonese":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e80player.insert(pos,nombre_jugador)
        elif equipo_player == "Sampdoria":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e81player.insert(pos,nombre_jugador)
        elif equipo_player == "Genoa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e83player.insert(pos,nombre_jugador)
        elif equipo_player == "Frosinone":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e82player.insert(pos,nombre_jugador)
        elif equipo_player == "Bari":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e84player.insert(pos,nombre_jugador)
        elif equipo_player == "Parma":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e85player.insert(pos,nombre_jugador)
        elif equipo_player == "Cagliari":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e86player.insert(pos,nombre_jugador)
        elif equipo_player == "Sudtirol":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e87player.insert(pos,nombre_jugador)
        elif equipo_player == "Reggina":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e88player.insert(pos,nombre_jugador)
        elif equipo_player == "Venezia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e89player.insert(pos,nombre_jugador)
        elif equipo_player == "Palermo":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e90player.insert(pos,nombre_jugador)
        elif equipo_player == "Modena":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e91player.insert(pos,nombre_jugador)
        elif equipo_player == "Pisa":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e92player.insert(pos,nombre_jugador)
        elif equipo_player == "Ascoli":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e93player.insert(pos,nombre_jugador)
        elif equipo_player == "Como":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e94player.insert(pos,nombre_jugador)
        elif equipo_player == "Ternana":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e95player.insert(pos,nombre_jugador)
        elif equipo_player == "Brescia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e96player.insert(pos,nombre_jugador)
        elif equipo_player == "Cittadella":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e97player.insert(pos,nombre_jugador)
        elif equipo_player == "Spal":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e100player.insert(pos,nombre_jugador)
        elif equipo_player == "Benevento":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e101player.insert(pos,nombre_jugador)
        elif equipo_player == "Cosenza":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e98player.insert(pos,nombre_jugador)
        elif equipo_player == "Perugia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e99player.insert(pos,nombre_jugador)
        
        
        
        
        
        
   
        if club == "Arsenal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                    weigth = len(jugadores)
                else:    
                    jugadores = e1player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Aston Villa":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                    weigth = len(jugadores)
                else:
                    jugadores = e2player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Bournemouth":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                    weigth = len(jugadores)
                else:
                    jugadores = e3player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Brentford":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                    weigth = len(jugadores)
                else:
                    jugadores = e4player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Brigthon":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                    weigth = len(jugadores)
                else:
                    jugadores = e5player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
        elif club == "Chelsea":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                    weigth = len(jugadores)
                else:
                    jugadores = e6player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Crystal Palace":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                    weigth = len(jugadores)
                else:
                    jugadores = e7player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Everton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                    weigth = len(jugadores)
                else:
                    jugadores = e8player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Fulham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                    weigth = len(jugadores)
                else:
                    jugadores = e9player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Leeds United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                    weigth = len(jugadores)
                else:
                    jugadores = e10player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Leicester City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                    weigth = len(jugadores)
                else:
                    jugadores = e11player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Liverpool":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                    weigth = len(jugadores)
                else:
                    jugadores = e12player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Manchester City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                    weigth = len(jugadores)
                else:
                    jugadores = e13player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Manchester United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                    weigth = len(jugadores)
                else:
                    jugadores = e14player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Newcastle":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                    weigth = len(jugadores)
                else:
                    jugadores = e15player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Nottingham Forest":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                    weigth = len(jugadores)
                else:
                    jugadores = e16player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Southampton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                    weigth = len(jugadores)
                else:
                    jugadores = e17player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Tottenham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                    weigth = len(jugadores)
                else:
                    jugadores = e18player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "West ham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                    weigth = len(jugadores)
                else:
                    jugadores = e19player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Wolverhampton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                    weigth = len(jugadores)
                else:
                    jugadores = e20player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Burnley":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                    weigth = len(jugadores)
                else:
                    jugadores = e21player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Sheffield United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                    weigth = len(jugadores)
                else:
                    jugadores = e22player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Luton Town":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                    weigth = len(jugadores)
                else:
                    jugadores = e23player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Middlesbrough":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                    weigth = len(jugadores)
                else:
                    jugadores = e24player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Coventry City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                    weigth = len(jugadores)
                else:
                    jugadores = e25player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Sunderland":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                    weigth = len(jugadores)
                else:
                    jugadores = e26player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Blackburn Rovers":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                    weigth = len(jugadores)
                else:
                    jugadores = e27player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Millwall":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                    weigth = len(jugadores)
                else:
                    jugadores = e28player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "West Bromwich Albion":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                    weigth = len(jugadores)
                else:
                    jugadores = e29player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Swansea":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                    weigth = len(jugadores)
                else:
                    jugadores = e30player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Watford":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                    weigth = len(jugadores)
                else:
                    jugadores = e31player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Preston North End":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                    weigth = len(jugadores)
                else:
                    jugadores = e32player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Norwich":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                    weigth = len(jugadores)
                else:
                    jugadores = e33player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)             
        elif club == "Bristol City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                    weigth = len(jugadores)
                else:
                    jugadores = e34player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Hull City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                    weigth = len(jugadores)
                else:
                    jugadores = e35player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Stoke City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                    weigth = len(jugadores)
                else:
                    jugadores = e36player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
        elif club == "Birmingham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                    weigth = len(jugadores)
                else:
                    jugadores = e37player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
        elif club == "Huddersfield Town":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                    weigth = len(jugadores)
                else:
                    jugadores = e38player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "Cardiff City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                    weigth = len(jugadores)
                else:
                    jugadores = e39player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
        elif club == "Queens Park Rangers":   
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                    weigth = len(jugadores)
                else:
                    jugadores = e40player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
        elif club == "PSG":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                weigth = len(jugadores)
            else:
                jugadores = e41player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "O.Lyon":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                weigth = len(jugadores)
            else:
                jugadores = e42player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Inter":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                weigth = len(jugadores)
            else:
                jugadores = e43player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Juventus":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                weigth = len(jugadores)
            else:
                jugadores = e44player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Milan":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                weigth = len(jugadores)
            else:
                jugadores = e45player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Napoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                weigth = len(jugadores)
            else:
                jugadores = e46player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Roma":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                weigth = len(jugadores)
            else:
                jugadores = e47player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Atl.Madrid":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                weigth = len(jugadores)
            else:
                jugadores = e48player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Barcelona":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e49player)
                weigth = len(jugadores)
            else:
                jugadores = e49player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Real Madrid":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e50player)
                weigth = len(jugadores)
            else:
                jugadores = e50player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "B.Dortmund":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e51player)
                weigth = len(jugadores)
            else:
                jugadores = e51player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Bayern Munich":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e52player)
                weigth = len(jugadores)
            else:
                jugadores = e52player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "B.Leverkusen":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e53player)
                weigth = len(jugadores)
            else:
                jugadores = e53player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Porto":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e54player)
                weigth = len(jugadores)
            else:
                jugadores = e54player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Sporting Lisboa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e55player)
                weigth = len(jugadores)
            else:
                jugadores = e55player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Frankfurt":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e56player)
                weigth = len(jugadores)
            else:
                jugadores = e56player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "O.Marsella":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e57player)
                weigth = len(jugadores)
            else:
                jugadores = e57player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)   
        elif club == "Sevilla":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e58player)
                weigth = len(jugadores)
            else:
                jugadores = e58player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Benfica":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e59player)
                weigth = len(jugadores)
            else:
                jugadores = e59player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Leipzig":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e60player)
                weigth = len(jugadores)
            else:
                jugadores = e60player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Ajax":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e61player)
                weigth = len(jugadores)
            else:
                jugadores = e61player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Monaco":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e62player)
                weigth = len(jugadores)
            else:
                jugadores = e62player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Shakhtar":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e63player)
                weigth = len(jugadores)
            else:
                jugadores = e63player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Brugge":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e64player)
                weigth = len(jugadores)
            else:
                jugadores = e64player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "PSV":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e65player)
                weigth = len(jugadores)
            else:
                jugadores = e65player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Real Sociedad":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e66player)
                weigth = len(jugadores)
            else:
                jugadores = e66player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)                        
        elif club == "Lazio":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e67player)
                weigth = len(jugadores)
            else:
                jugadores = e67player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Atalanta":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e68player)
                weigth = len(jugadores)
            else:
                jugadores = e68player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Fiorentina":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e69player)
                weigth = len(jugadores)
            else:
                jugadores = e69player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Bologna":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e70player)
                weigth = len(jugadores)
            else:
                jugadores = e70player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Torino":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e71player)
                weigth = len(jugadores)
            else:
                jugadores = e71player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Monza":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e72player)
                weigth = len(jugadores)
            else:
                jugadores = e72player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Udinese":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e73player)
                weigth = len(jugadores)
            else:
                jugadores = e73player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Sassuolo":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e74player)
                weigth = len(jugadores)
            else:
                jugadores = e74player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Empoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e75player)
                weigth = len(jugadores)
            else:
                jugadores = e75player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Salernitana":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e76player)
                weigth = len(jugadores)
            else:
                jugadores = e76player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Lecce":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e77player)
                weigth = len(jugadores)
            else:
                jugadores = e77player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Hellas Verona":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e78player)
                weigth = len(jugadores)
            else:
                jugadores = e78player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Spezia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e79player)
                weigth = len(jugadores)
            else:
                jugadores = e79player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cremonese":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e80player)
                weigth = len(jugadores)
            else:
                jugadores = e80player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Sampdoria":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e81player)
                weigth = len(jugadores)
            else:
                jugadores = e81player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Frosinone":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e82player)
                weigth = len(jugadores)
            else:
                jugadores = e82player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Genoa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e83player)
                weigth = len(jugadores)
            else:
                jugadores = e83player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Bari":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e84player)
                weigth = len(jugadores)
            else:
                jugadores = e84player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Parma":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e85player)
                weigth = len(jugadores)
            else:
                jugadores = e85player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cagliari":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e86player)
                weigth = len(jugadores)
            else:
                jugadores = e86player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)         
        elif club == "Sudtirol":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e87player)
                weigth = len(jugadores)
            else:
                jugadores = e87player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Reggina":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e88player)
                weigth = len(jugadores)
            else:
                jugadores = e88player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Venezia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e89player)
                weigth = len(jugadores)
            else:
                jugadores = e89player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Palermo":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e90player)
                weigth = len(jugadores)
            else:
                jugadores = e90player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Modena":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e91player)
                weigth = len(jugadores)
            else:
                jugadores = e91player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Pisa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e92player)
                weigth = len(jugadores)
            else:
                jugadores = e92player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Ascoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e93player)
                weigth = len(jugadores)
            else:
                jugadores = e93player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Como":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e94player)
                weigth = len(jugadores)
            else:
                jugadores = e94player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Ternana":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e95player)
                weigth = len(jugadores)
            else:
                jugadores = e95player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Brescia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e96player)
                weigth = len(jugadores)
            else:
                jugadores = e96player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cittadella":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e97player)
                weigth = len(jugadores)
            else:
                jugadores = e97player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Cosenza":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e98player)
                weigth = len(jugadores)
            else:
                jugadores = e98player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Perugia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e99player)
                weigth = len(jugadores)
            else:
                jugadores = e99player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Spal":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e100player)
                weigth = len(jugadores)
            else:
                jugadores = e100player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Benevento":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e101player)
                weigth = len(jugadores)
            else:
                jugadores = e101player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)         
        contador += 1     
        amarillas.append(gol)
    if len(amarillas) != 0:   
        print(f' Amarillas {club}: ' + ', '.join(map(str, amarillas))) 
    return amarillas

def asistentes(club,goles,jugadores_sancionados,jugadores_lesionados,equipo_player,valoracion_player,nombre_jugador):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14,0.14]           
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.2, 0.2, 0.2, 0.2, 0.2] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.25, 0.25, 0.25, 0.25 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.3, 0.3, 0.3] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.5,0.5]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0] 
    for i in jugadores_lesionados:
        if i in jugadores_sancionados: pass
        else: jugadores_sancionados.append(i)
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array   
    def random_generator():
        rand_num = random.random() 
        if rand_num <= 0.3:
            return 0 
        else:
            return 1 
    
    asistencias_totales = []
    while (goles != 0):
        e1player = ["Martinelli", "Gabriel Jesus", "Havertz", "Saka", "Odegaard"]
        e2player = ["Coutinho", "Watkins", "Ramsey", "Buendía"]
        e3player = ["Semenyo","Solanke","Lerma","Christie"]
        e4player = ["Toney", "Mbeumo", "Schade", "Ghoddos"]
        e5player = ["Fati", "Welbeck", "Mitoma", "Enciso", "Ferguson"]
        e6player = ["Sterling", "Fernandez", "Nkunku", "Mudryk","Palmer"]
        e7player = ["Ayew(cp)", "Mateta", "Doucoure", "Edouard"]
        e8player = ["Beto", "McNeil", "Calvert-Lewin", "Danjuma"]
        e9player = ["Traore", "Jimenez", "Iwobi", "Willian"]
        e10player = ["Rutter","Summerville","Gnoto","Gray"]
        e11player = ["Vardy","Iheanacho","Akgün","Mavididi"]
        e12player = ["Salah", "MacAllister", "Núñez", "Luis Díaz", "Diogo Jota"]
        e13player = ["Haaland", "Foden", "Grealish", "Álvarez", "De Bruyne"]
        e14player = ["Rashford", "Mount", "Bruno Fernandes", "Martial", "Sancho"]
        e15player = ["Isak", "Guimarães", "Joelinton", "Tonali", "Murphy"]
        e16player = ["Awoniyi", "Gibbs-White", "Origi", "Danilo"]
        e17player = ["Adams","Alcaraz","Armstrong","Edozie"]
        e18player = ["Richarlison", "Son", "Sarr", "Kulusevski", "Perisic"]
        e19player = ["Antonio", "Paquetá", "Benrahma", "Ings"]
        e20player = ["Silva", "Cunha", "Kalajdzic", "Sarabia"]
        e21player = ["Foster", "Redmond", "Amdouni", "Brownhill"]
        e22player = ["Osula", "Jebbison", "Archer", "Brewster"]
        e23player = ["Adebayo", "Lokonga", "Morris", "Ogbene"]
        e24player = ["Greenwood","Silvera","Jones","Forss"]
        e25player = ["Godden","Simms","Tavares","Wright"]
        e26player = ["Clarke","Bennette","Semedo","Rigg"]
        e27player = ["Leonard","Gallagher","Ennis","Hedges"]
        e28player = ["Bradshaw","Nisbet","Watmore","Emakhu"]
        e29player = ["Dike","Wallace","Diangana","Phillips"]
        e30player = ["Lowe","Ginnelly","Cooper","Cullen"]
        e31player = ["Bayo","Martins","Healeyr","Ince"]
        e32player = ["Keane","Holmes","Riis","McCann"]
        e33player = ["Barnes","Sargent","Gibbs","Idah"]
        e34player =["Wells","Cornick","Bell","Conway"]
        e35player = ["Delap","Lokilo","Sinik","Connolly"]
        e36player = ["Gooch","Campbell","Mmaee","Gayle"]
        e37player = ["Hogan","Jutkiewicz","Roberts","Stansfield"]
        e38player = ["Koroma","Burgzorg","Ward","Hudlin"]
        e39player = ["Ugbo","Robinson","Bowler","Grant"]
        e40player = ["Dykes","Adomah","Willock","Smyth"]
        e41player = ["Mbappe","Asensio","O.Dembele","Muani","Barcola"]
        e42player = ["Lacazette","Baldé","Jeffinho","Tolisso","Tagliafico"]
        e43player = ["Martinez","Alexis Sánchez","Arnautovic","Calhanoglu","Mkhitaryan"]
        e44player = ["Vlahovic","Kean","Chiesa","Milik","Pogba"]
        e45player = ["Giroud","Leão","Pulisic","Jović","Romero"]
        e46player = ["Osimhen","Raspadori","Simeone","Politano","Kvaratskhelia"]
        e47player = ["Dybala","Belotti","El Shaarawy","Lukaku","Pellegrini"]
        e48player = ["Griezmann","Morata","de Paul","Koke","Lemar"]
        e49player = ["Lewandowski","Gavi","Felix","Raphinha","Torres"]
        e50player = ["Bellingham","Vinicius","Rodrygo","Modric","Tchouameni"]
        e51player =["Haller","Moukoko","Adeyemi","Reus","Reyna"]
        e52player = ["Kane","Gnabry","Müller","Musiala","Sané"]
        e53player = ["Tella","Hložek","Hofmann","Adli","Boniface"]
        e54player = ["Taremi","Galeno","Evanilson","Jaime","Grujic"]
        e55player = ["Paulinho","Trincao","Edwards","Santos","Goncalves"]
        e56player = ["Götze","Marmoush","Ngankam","Alario","Rode"]
        e57player = ["Aubameyang","Sarr(M)","Correa","Ndiaye","Gueye"]
        e58player = ["Zakharyan","En-Nesyri","Suso","Ocampos","Rakitić"]
        e59player = ["Neres","Rafa","Di María","Musa","Gouveia"]
        e60player = ["Poulsen","Werner","Sesko","Olmo","Openda"]
        e61player = ["Bergwijn","Akpom","Mikautadze","Godts","Tahirovic"]
        e62player = ["Ben Yedder","Martins(M)","Embolo","Seghir","Camara"]
        e63player = ["Traore","Sikan","Petryak","Zubkov","Bondarenko"]
        e64player = ["Buchanan","Nusa","Jutglà","Vermant","Olsen"]
        e65player = ["de Jong","Bakayoko","Til","Veerman","Lang"]
        e66player = ["Sadiq","Oyarzabal","Andre Silva","Kubo","Zakharyan"]
        e67player = ["Immobile","Anderson","Pedro(L)","Basic","Isaksen"]
        e68player = ["Muriel","Scamacca","Pasalic","Lookman","Adopo"]
        e69player = ["N.Gonzalez","Arthur","Beltrán","Sottil","Kouamé"]
        e70player = ["Karlsson","Ndoye","Orsolini","Hooijdonk"]
        e71player = ["Pellegri","Radonjic","Sanabria","Vlasic"]
        e72player = ["Berardi","Lauriente","Mulattieri","Pinamonti"]
        e73player = ["Deulofeu","Thauvin","Brenner"," Success"]
        e74player = ["Carvalho","Colombo","Maric","Ciurria"]
        e75player = ["Caputo","Cambiaghi","Gyasi","Destro"]
        e76player = ["Botheim","Candreva","Ikwuemesi","Maggiore"]
        e77player = ["Piccoli","Krstovic","Banda","Burnete"]
        e78player = ["Mboula","Djuric","Braaf","Ngonge"]
        e79player = ["Moro","Krollis","Verde","Elia"]
        e80player = ["Ciofani","Buonaiuto","Coda","Zanimacchia"]
        e81player = ["Estanis","Borini","Gumina","Monache"]
        e82player = ["Cheddira","Kvernadze","Soule","Cuni"] 
        e83player = ["Retegui","Gudmundsson","Ekuban","Fini"]
        e84player = ["Diaw","Nasti","Maita","Sibilli"]
        e85player = ["Colak","Benedyczak","Begic","Mihaila"]
        e86player = ["Lapadula","Pavoletti","Petagna","Zito"]
        e87player = ["Rover","Odogwu","Pecorino","Cisco"]
        e88player = ["Gondo","Lanini","Pettinari","Vido"]
        e89player =["Johsen","Pierini","Tessmann","Pohjanpalo"]
        e90player = ["Mancuso","Brunori","Soleri","Segre"]
        e91player = ["Falcinelli","Manconi","Giovannini","Gerli"]
        e92player = ["Mlakar","Torregrossa","Tramoni","Nagy"]
        e93player = ["Pedro Mendes","Millico","Nestorovski","Caligara"]
        e94player = ["Cutrone","Gabrielloni","Baselli","Cerri"]
        e95player = ["Favili","Dionisi","Raimondo","Proietti"]
        e96player = ["Moncini","Bianchi","Bisoli","Ferro"]
        e97player = ["Magrassi","Maistrello","Pittarello","Danzi"]
        e98player = ["Antenucci","Dalmonte","Siligardi","Rabbi"]
        e99player =["Matos","Julitanmo","Cudrig","Seghetti"]
        e100player = ["Forte","Tutino","Novello","Crespi"]
        e101player = ["Improta","Ciano","Marotta","Bolsius"]
        if equipo_player == "Arsenal":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e1player.insert(pos,nombre_jugador)
        elif equipo_player == "Aston Villa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e2player.insert(pos,nombre_jugador)
        elif equipo_player == "Bournemouth":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e3player.insert(pos,nombre_jugador)
        elif equipo_player == "Brentford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e4player.insert(pos,nombre_jugador)
        elif equipo_player == "Brigthon":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1 
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e5player.insert(pos,nombre_jugador)
        elif equipo_player == "Chelsea":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e6player.insert(pos,nombre_jugador)
        elif equipo_player == "Crystal Palace":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e7player.insert(pos,nombre_jugador)
        elif equipo_player == "Everton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e8player.insert(pos,nombre_jugador)
        elif equipo_player == "Fulham":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e9player.insert(pos,nombre_jugador)
        elif equipo_player == "Leeds United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e10player.insert(pos,nombre_jugador)
        elif equipo_player == "Leicester City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e11player.insert(pos,nombre_jugador)
        elif equipo_player == "Liverpool":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e12player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester City":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e13player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester United":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            elif valoracion_player > 30: 
                pos = 6
            else: pos = 7         
            e14player.insert(pos,nombre_jugador)
        elif equipo_player == "Newcastle":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e15player.insert(pos,nombre_jugador)
        elif equipo_player == "Nottingham Forest":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e16player.insert(pos,nombre_jugador)
        elif equipo_player == "Southampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e17player.insert(pos,nombre_jugador)
        elif equipo_player == "Tottenham":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e18player.insert(pos,nombre_jugador)
        elif equipo_player == "West ham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e19player.insert(pos,nombre_jugador)
        elif equipo_player == "Wolverhampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e20player.insert(pos,nombre_jugador)
        elif equipo_player == "Burnley":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e21player.insert(pos,nombre_jugador)
        elif equipo_player == "Sheffield United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e22player.insert(pos,nombre_jugador)
        elif equipo_player == "Luton Town":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e23player.insert(pos,nombre_jugador)
        elif equipo_player == "Middlesbrough":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e24player.insert(pos,nombre_jugador)
        elif equipo_player == "Coventry City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e25player.insert(pos,nombre_jugador)
        elif equipo_player == "Sunderland":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e26player.insert(pos,nombre_jugador)
        elif equipo_player == "Blackburn Rovers":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e27player.insert(pos,nombre_jugador)     
        elif equipo_player == "Millwall":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e28player.insert(pos,nombre_jugador)
        elif equipo_player == "West Bromwich Albion":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e29player.insert(pos,nombre_jugador)   
        elif equipo_player == "Swansea":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e30player.insert(pos,nombre_jugador)
        elif equipo_player == "Watford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e31player.insert(pos,nombre_jugador) 
        elif equipo_player == "Preston North End":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e32player.insert(pos,nombre_jugador)     
        elif equipo_player == "Norwich":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e33player.insert(pos,nombre_jugador)            
        elif equipo_player == "Bristol City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e34player.insert(pos,nombre_jugador)
        elif equipo_player == "Hull City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            
            e35player.insert(pos,nombre_jugador) 
        elif equipo_player == "Stoke City":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e36player.insert(pos,nombre_jugador)
        elif equipo_player == "Birmingham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e37player.insert(pos,nombre_jugador)
        elif equipo_player == "Huddersfield Town":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e38player.insert(pos,nombre_jugador)
        elif equipo_player == "Cardiff City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e39player.insert(pos,nombre_jugador)
        elif equipo_player == "Queens Park Rangers":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e40player.insert(pos,nombre_jugador)
        elif equipo_player == "Inter":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e43player.insert(pos,nombre_jugador)
        elif equipo_player == "Juventus":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e44player.insert(pos,nombre_jugador)
        elif equipo_player == "Milan":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e45player.insert(pos,nombre_jugador)
        elif equipo_player == "Napoli":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e46player.insert(pos,nombre_jugador)
        elif equipo_player == "Roma":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e47player.insert(pos,nombre_jugador)
        elif equipo_player == "Lazio":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e67player.insert(pos,nombre_jugador)
        elif equipo_player == "Atalanta":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e68player.insert(pos,nombre_jugador)
        elif equipo_player == "Fiorentina":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e69player.insert(pos,nombre_jugador)
        elif equipo_player == "Bologna":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e70player.insert(pos,nombre_jugador)
        elif equipo_player == "Torino":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e71player.insert(pos,nombre_jugador)
        elif equipo_player == "Sassuolo":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e74player.insert(pos,nombre_jugador)
        elif equipo_player == "Udinese":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e73player.insert(pos,nombre_jugador)
        elif equipo_player == "Monza":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e72player.insert(pos,nombre_jugador)
        elif equipo_player == "Empoli":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e75player.insert(pos,nombre_jugador)
        elif equipo_player == "Salernitana":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e76player.insert(pos,nombre_jugador)
        elif equipo_player == "Lecce":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e77player.insert(pos,nombre_jugador)
        elif equipo_player == "Hellas Verona":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e78player.insert(pos,nombre_jugador)
        elif equipo_player == "Spezia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e79player.insert(pos,nombre_jugador)
        elif equipo_player == "Cremonese":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e80player.insert(pos,nombre_jugador)
        elif equipo_player == "Sampdoria":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e81player.insert(pos,nombre_jugador)
        elif equipo_player == "Genoa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e83player.insert(pos,nombre_jugador)
        elif equipo_player == "Frosinone":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e82player.insert(pos,nombre_jugador)
        elif equipo_player == "Bari":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e84player.insert(pos,nombre_jugador)
        elif equipo_player == "Parma":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e85player.insert(pos,nombre_jugador)
        elif equipo_player == "Cagliari":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e86player.insert(pos,nombre_jugador)
        elif equipo_player == "Sudtirol":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e87player.insert(pos,nombre_jugador)
        elif equipo_player == "Reggina":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e88player.insert(pos,nombre_jugador)
        elif equipo_player == "Venezia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e89player.insert(pos,nombre_jugador)
        elif equipo_player == "Palermo":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e90player.insert(pos,nombre_jugador)
        elif equipo_player == "Modena":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e91player.insert(pos,nombre_jugador)
        elif equipo_player == "Pisa":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e92player.insert(pos,nombre_jugador)
        elif equipo_player == "Ascoli":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e93player.insert(pos,nombre_jugador)
        elif equipo_player == "Como":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e94player.insert(pos,nombre_jugador)
        elif equipo_player == "Ternana":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e95player.insert(pos,nombre_jugador)
        elif equipo_player == "Brescia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e96player.insert(pos,nombre_jugador)
        elif equipo_player == "Cittadella":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e97player.insert(pos,nombre_jugador)
        elif equipo_player == "Spal":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e100player.insert(pos,nombre_jugador)
        elif equipo_player == "Benevento":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e101player.insert(pos,nombre_jugador)
        elif equipo_player == "Cosenza":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e98player.insert(pos,nombre_jugador)
        elif equipo_player == "Perugia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e99player.insert(pos,nombre_jugador)
        
        
        numero = random_generator()
        if numero == 1:
            goles = goles -1
        else:    
            asistencia = str(goles)
            goles = goles -1
            if club == "Arsenal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                    weigth = len(jugadores)
                else:    
                    jugadores = e1player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Aston Villa":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                    weigth = len(jugadores)
                else:
                    jugadores = e2player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
            elif club == "Bournemouth":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                    weigth = len(jugadores)
                else:
                    jugadores = e3player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Brentford":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                    weigth = len(jugadores)
                else:
                    jugadores = e4player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
            elif club == "Brigthon":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                    weigth = len(jugadores)
                else:
                    jugadores = e5player 
                    weigth = len(jugadores)
                gol =  get_random_player6(jugadores,weigth)
            elif club == "Chelsea":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                    weigth = len(jugadores)
                else:
                    jugadores = e6player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Crystal Palace":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                    weigth = len(jugadores)
                else:
                    jugadores = e7player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Everton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                    weigth = len(jugadores)
                else:
                    jugadores = e8player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Fulham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                    weigth = len(jugadores)
                else:
                    jugadores = e9player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Leeds United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                    weigth = len(jugadores)
                else:
                    jugadores = e10player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Leicester City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                    weigth = len(jugadores)
                else:
                    jugadores = e11player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Liverpool":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                    weigth = len(jugadores)
                else:
                    jugadores = e12player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Manchester City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                    weigth = len(jugadores)
                else:
                    jugadores = e13player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Manchester United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                    weigth = len(jugadores)
                else:
                    jugadores = e14player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Newcastle":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                    weigth = len(jugadores)
                else:
                    jugadores = e15player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Nottingham Forest":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                    weigth = len(jugadores)
                else:
                    jugadores = e16player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Southampton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                    weigth = len(jugadores)
                else:
                    jugadores = e17player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Tottenham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                    weigth = len(jugadores)
                else:
                    jugadores = e18player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "West ham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                    weigth = len(jugadores)
                else:
                    jugadores = e19player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Wolverhampton":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                    weigth = len(jugadores)
                else:
                    jugadores = e20player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Burnley":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                    weigth = len(jugadores)
                else:
                    jugadores = e21player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Sheffield United":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                    weigth = len(jugadores)
                else:
                    jugadores = e22player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Luton Town":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                    weigth = len(jugadores)
                else:
                    jugadores = e23player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Middlesbrough":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                    weigth = len(jugadores)
                else:
                    jugadores = e24player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Coventry City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                    weigth = len(jugadores)
                else:
                    jugadores = e25player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Sunderland":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                    weigth = len(jugadores)
                else:
                    jugadores = e26player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Blackburn Rovers":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                    weigth = len(jugadores)
                else:
                    jugadores = e27player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
            elif club == "Millwall":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                    weigth = len(jugadores)
                else:
                    jugadores = e28player 
                    weigth = len(jugadores)    
                gol = get_random_player6(jugadores,weigth)    
            elif club == "West Bromwich Albion":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                    weigth = len(jugadores)
                else:
                    jugadores = e29player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
            elif club == "Swansea":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                    weigth = len(jugadores)
                else:
                    jugadores = e30player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Watford":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                    weigth = len(jugadores)
                else:
                    jugadores = e31player 
                    weigth = len(jugadores)  
                gol = get_random_player6(jugadores,weigth)      
            elif club == "Preston North End":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                    weigth = len(jugadores)
                else:
                    jugadores = e32player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
            elif club == "Norwich":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                    weigth = len(jugadores)
                else:
                    jugadores = e33player 
                    weigth = len(jugadores)     
                gol = get_random_player6(jugadores,weigth)           
            elif club == "Bristol City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                    weigth = len(jugadores)
                else:
                    jugadores = e34player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Hull City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                    weigth = len(jugadores)
                else:
                    jugadores = e35player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
            elif club == "Stoke City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                    weigth = len(jugadores)
                else:
                    jugadores = e36player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)       
            elif club == "Birmingham":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                    weigth = len(jugadores)
                else:
                    jugadores = e37player 
                    weigth = len(jugadores)   
                gol = get_random_player6(jugadores,weigth)     
            elif club == "Huddersfield Town":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                    weigth = len(jugadores)
                else:
                    jugadores = e38player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Cardiff City":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                    weigth = len(jugadores)
                else:
                    jugadores = e39player 
                    weigth = len(jugadores)      
                gol = get_random_player6(jugadores,weigth)  
            elif club == "Queens Park Rangers":   
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                    weigth = len(jugadores)
                else:
                    jugadores = e40player 
                    weigth = len(jugadores) 
                gol = get_random_player6(jugadores,weigth)   
            elif club == "PSG":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                    weigth = len(jugadores)
                else:
                    jugadores = e41player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "O.Lyon":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                    weigth = len(jugadores)
                else:
                    jugadores = e42player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Inter":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                    weigth = len(jugadores)
                else:
                    jugadores = e43player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Juventus":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                    weigth = len(jugadores)
                else:
                    jugadores = e44player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Milan":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                    weigth = len(jugadores)
                else:
                    jugadores = e45player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Napoli":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                    weigth = len(jugadores)
                else:
                    jugadores = e46player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Roma":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                    weigth = len(jugadores)
                else:
                    jugadores = e47player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Atl.Madrid":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                    weigth = len(jugadores)
                else:
                    jugadores = e48player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Barcelona":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e49player)
                    weigth = len(jugadores)
                else:
                    jugadores = e49player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Real Madrid":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e50player)
                    weigth = len(jugadores)
                else:
                    jugadores = e50player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "B.Dortmund":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e51player)
                    weigth = len(jugadores)
                else:
                    jugadores = e51player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Bayern Munich":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e52player)
                    weigth = len(jugadores)
                else:
                    jugadores = e52player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "B.Leverkusen":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e53player)
                    weigth = len(jugadores)
                else:
                    jugadores = e53player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Porto":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e54player)
                    weigth = len(jugadores)
                else:
                    jugadores = e54player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Sporting Lisboa":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e55player)
                    weigth = len(jugadores)
                else:
                    jugadores = e55player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Frankfurt":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e56player)
                    weigth = len(jugadores)
                else:
                    jugadores = e56player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "O.Marsella":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e57player)
                    weigth = len(jugadores)
                else:
                    jugadores = e57player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)   
            elif club == "Sevilla":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e58player)
                    weigth = len(jugadores)
                else:
                    jugadores = e58player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Benfica":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e59player)
                    weigth = len(jugadores)
                else:
                    jugadores = e59player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Leipzig":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e60player)
                    weigth = len(jugadores)
                else:
                    jugadores = e60player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Ajax":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e61player)
                    weigth = len(jugadores)
                else:
                    jugadores = e61player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Monaco":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e62player)
                    weigth = len(jugadores)
                else:
                    jugadores = e62player 
                    weigth = len(jugadores)
                gol =get_random_player6(jugadores,weigth)            
            elif club == "Shakhtar":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e63player)
                    weigth = len(jugadores)
                else:
                    jugadores = e63player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Brugge":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e64player)
                    weigth = len(jugadores)
                else:
                    jugadores = e64player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "PSV":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e65player)
                    weigth = len(jugadores)
                else:
                    jugadores = e65player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Real Sociedad":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e66player)
                    weigth = len(jugadores)
                else:
                    jugadores = e66player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)                    
            elif club == "Lazio":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e67player)
                    weigth = len(jugadores)
                else:
                    jugadores = e67player 
                    weigth = len(jugadores)
                gol =get_random_player6(jugadores,weigth)            
            elif club == "Atalanta":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e68player)
                    weigth = len(jugadores)
                else:
                    jugadores = e68player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Fiorentina":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e69player)
                    weigth = len(jugadores)
                else:
                    jugadores = e69player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Bologna":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e70player)
                    weigth = len(jugadores)
                else:
                    jugadores = e70player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Torino":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e71player)
                    weigth = len(jugadores)
                else:
                    jugadores = e71player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)
            elif club == "Monza":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e72player)
                    weigth = len(jugadores)
                else:
                    jugadores = e72player 
                    weigth = len(jugadores)
                gol =get_random_player6(jugadores,weigth)            
            elif club == "Udinese":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e73player)
                    weigth = len(jugadores)
                else:
                    jugadores = e73player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Sassuolo":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e74player)
                    weigth = len(jugadores)
                else:
                    jugadores = e74player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Empoli":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e75player)
                    weigth = len(jugadores)
                else:
                    jugadores = e75player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Salernitana":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e76player)
                    weigth = len(jugadores)
                else:
                    jugadores = e76player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Lecce":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e77player)
                    weigth = len(jugadores)
                else:
                    jugadores = e77player 
                    weigth = len(jugadores)
                gol =get_random_player6(jugadores,weigth)            
            elif club == "Hellas Verona":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e78player)
                    weigth = len(jugadores)
                else:
                    jugadores = e78player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Spezia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e79player)
                    weigth = len(jugadores)
                else:
                    jugadores = e79player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Cremonese":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e80player)
                    weigth = len(jugadores)
                else:
                    jugadores = e80player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Sampdoria":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e81player)
                    weigth = len(jugadores)
                else:
                    jugadores = e81player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Frosinone":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e82player)
                    weigth = len(jugadores)
                else:
                    jugadores = e82player 
                    weigth = len(jugadores)
                gol =get_random_player6(jugadores,weigth)            
            elif club == "Genoa":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e83player)
                    weigth = len(jugadores)
                else:
                    jugadores = e83player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Bari":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e84player)
                    weigth = len(jugadores)
                else:
                    jugadores = e84player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Parma":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e85player)
                    weigth = len(jugadores)
                else:
                    jugadores = e85player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Cagliari":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e86player)
                    weigth = len(jugadores)
                else:
                    jugadores = e86player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)         
            elif club == "Sudtirol":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e87player)
                    weigth = len(jugadores)
                else:
                    jugadores = e87player 
                    weigth = len(jugadores)
                gol =get_random_player6(jugadores,weigth)            
            elif club == "Reggina":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e88player)
                    weigth = len(jugadores)
                else:
                    jugadores = e88player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Venezia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e89player)
                    weigth = len(jugadores)
                else:
                    jugadores = e89player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Palermo":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e90player)
                    weigth = len(jugadores)
                else:
                    jugadores = e90player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Modena":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e91player)
                    weigth = len(jugadores)
                else:
                    jugadores = e91player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Pisa":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e92player)
                    weigth = len(jugadores)
                else:
                    jugadores = e92player 
                    weigth = len(jugadores)
                gol =get_random_player6(jugadores,weigth)            
            elif club == "Ascoli":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e93player)
                    weigth = len(jugadores)
                else:
                    jugadores = e93player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Como":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e94player)
                    weigth = len(jugadores)
                else:
                    jugadores = e94player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Ternana":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e95player)
                    weigth = len(jugadores)
                else:
                    jugadores = e95player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Brescia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e96player)
                    weigth = len(jugadores)
                else:
                    jugadores = e96player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Cittadella":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e97player)
                    weigth = len(jugadores)
                else:
                    jugadores = e97player 
                    weigth = len(jugadores)
                gol =get_random_player6(jugadores,weigth)            
            elif club == "Cosenza":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e98player)
                    weigth = len(jugadores)
                else:
                    jugadores = e98player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)    
            elif club == "Perugia":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e99player)
                    weigth = len(jugadores)
                else:
                    jugadores = e99player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Spal":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e100player)
                    weigth = len(jugadores)
                else:
                    jugadores = e100player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth) 
            elif club == "Benevento":
                if len(jugadores_sancionados) != 0:
                    jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e101player)
                    weigth = len(jugadores)
                else:
                    jugadores = e101player 
                    weigth = len(jugadores)
                gol = get_random_player6(jugadores,weigth)       
                
                
            asistencias_totales.append(gol)    
    if len(asistencias_totales) != 0:   
        print(f' Asistencias {club}: ' + ', '.join(map(str, asistencias_totales))) 
    return asistencias_totales

def rojas(club,jugadores_sancionados,jugadores_lesionados,equipo_player,valoracion_player,nombre_jugador):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.14, 0.14, 0.14, 0.14, 0.14, 0.14,0.14]            
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.16, 0.16, 0.16, 0.16, 0.16, 0.16]
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.2, 0.2, 0.2, 0.2, 0.2] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.25, 0.25, 0.25, 0.25 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.3, 0.3, 0.3] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.5,0.5]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0]
    if len(jugadores_lesionados) != 0:
        for i in jugadores_lesionados:
            if i in jugadores_sancionados: pass
            else: jugadores_sancionados.append(i)
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array    
    def random_generator():
        rand_num = random.random() 
        if rand_num <= 0.025:
            return 0 
        else:
            return 1 
    
    numeros = []
    num1 = random_generator()
    if num1 == 1:
        numeros.append(num1)
    num2 = random_generator()
    if num1 == 1:    
        numeros.append(num2)
    lat = len(numeros)
    contador = 0
    rojas = []
    while (contador == lat):
        e1player = ["Martinelli", "Gabriel Jesus", "Havertz", "Saka", "Odegaard"]
        e2player = ["Coutinho", "Watkins", "Ramsey", "Buendía"]
        e3player = ["Semenyo","Solanke","Lerma","Christie"]
        e4player = ["Toney", "Mbeumo", "Schade", "Ghoddos"]
        e5player = ["Fati", "Welbeck", "Mitoma", "Enciso", "Ferguson"]
        e6player = ["Sterling", "Fernandez", "Nkunku", "Mudryk","Palmer"]
        e7player = ["Ayew(cp)", "Mateta", "Doucoure", "Edouard"]
        e8player = ["Beto", "McNeil", "Calvert-Lewin", "Danjuma"]
        e9player = ["Traore", "Jimenez", "Iwobi", "Willian"]
        e10player = ["Rutter","Summerville","Gnoto","Gray"]
        e11player = ["Vardy","Iheanacho","Akgün","Mavididi"]
        e12player = ["Salah", "MacAllister", "Núñez", "Luis Díaz", "Diogo Jota"]
        e13player = ["Haaland", "Foden", "Grealish", "Álvarez", "De Bruyne"]
        e14player = ["Rashford", "Mount", "Bruno Fernandes", "Martial", "Sancho"]
        e15player = ["Isak", "Guimarães", "Joelinton", "Tonali", "Murphy"]
        e16player = ["Awoniyi", "Gibbs-White", "Origi", "Danilo"]
        e17player = ["Adams","Alcaraz","Armstrong","Edozie"]
        e18player = ["Richarlison", "Son", "Sarr", "Kulusevski", "Perisic"]
        e19player = ["Antonio", "Paquetá", "Benrahma", "Ings"]
        e20player = ["Silva", "Cunha", "Kalajdzic", "Sarabia"]
        e21player = ["Foster", "Redmond", "Amdouni", "Brownhill"]
        e22player = ["Osula", "Jebbison", "Archer", "Brewster"]
        e23player = ["Adebayo", "Lokonga", "Morris", "Ogbene"]
        e24player = ["Greenwood","Silvera","Jones","Forss"]
        e25player = ["Godden","Simms","Tavares","Wright"]
        e26player = ["Clarke","Bennette","Semedo","Rigg"]
        e27player = ["Leonard","Gallagher","Ennis","Hedges"]
        e28player = ["Bradshaw","Nisbet","Watmore","Emakhu"]
        e29player = ["Dike","Wallace","Diangana","Phillips"]
        e30player = ["Lowe","Ginnelly","Cooper","Cullen"]
        e31player = ["Bayo","Martins","Healeyr","Ince"]
        e32player = ["Keane","Holmes","Riis","McCann"]
        e33player = ["Barnes","Sargent","Gibbs","Idah"]
        e34player =["Wells","Cornick","Bell","Conway"]
        e35player = ["Delap","Lokilo","Sinik","Connolly"]
        e36player = ["Gooch","Campbell","Mmaee","Gayle"]
        e37player = ["Hogan","Jutkiewicz","Roberts","Stansfield"]
        e38player = ["Koroma","Burgzorg","Ward","Hudlin"]
        e39player = ["Ugbo","Robinson","Bowler","Grant"]
        e40player = ["Dykes","Adomah","Willock","Smyth"]
        e41player = ["Mbappe","Asensio","O.Dembele","Muani","Barcola"]
        e42player = ["Lacazette","Baldé","Jeffinho","Tolisso","Tagliafico"]
        e43player = ["Martinez","Alexis Sánchez","Arnautovic","Calhanoglu","Mkhitaryan"]
        e44player = ["Vlahovic","Kean","Chiesa","Milik","Pogba"]
        e45player = ["Giroud","Leão","Pulisic","Jović","Romero"]
        e46player = ["Osimhen","Raspadori","Simeone","Politano","Kvaratskhelia"]
        e47player = ["Dybala","Belotti","El Shaarawy","Lukaku","Pellegrini"]
        e48player = ["Griezmann","Morata","de Paul","Koke","Lemar"]
        e49player = ["Lewandowski","Gavi","Felix","Raphinha","Torres"]
        e50player = ["Bellingham","Vinicius","Rodrygo","Modric","Tchouameni"]
        e51player =["Haller","Moukoko","Adeyemi","Reus","Reyna"]
        e52player = ["Kane","Gnabry","Müller","Musiala","Sané"]
        e53player = ["Tella","Hložek","Hofmann","Adli","Boniface"]
        e54player = ["Taremi","Galeno","Evanilson","Jaime","Grujic"]
        e55player = ["Paulinho","Trincao","Edwards","Santos","Goncalves"]
        e56player = ["Götze","Marmoush","Ngankam","Alario","Rode"]
        e57player = ["Aubameyang","Sarr(M)","Correa","Ndiaye","Gueye"]
        e58player = ["Zakharyan","En-Nesyri","Suso","Ocampos","Rakitić"]
        e59player = ["Neres","Rafa","Di María","Musa","Gouveia"]
        e60player = ["Poulsen","Werner","Sesko","Olmo","Openda"]
        e61player = ["Bergwijn","Akpom","Mikautadze","Godts","Tahirovic"]
        e62player = ["Ben Yedder","Martins(M)","Embolo","Seghir","Camara"]
        e63player = ["Traore","Sikan","Petryak","Zubkov","Bondarenko"]
        e64player = ["Buchanan","Nusa","Jutglà","Vermant","Olsen"]
        e65player = ["de Jong","Bakayoko","Til","Veerman","Lang"]
        e66player = ["Sadiq","Oyarzabal","Andre Silva","Kubo","Zakharyan"]
        e67player = ["Immobile","Anderson","Pedro(L)","Basic","Isaksen"]
        e68player = ["Muriel","Scamacca","Pasalic","Lookman","Adopo"]
        e69player = ["N.Gonzalez","Arthur","Beltrán","Sottil","Kouamé"]
        e70player = ["Karlsson","Ndoye","Orsolini","Hooijdonk"]
        e71player = ["Pellegri","Radonjic","Sanabria","Vlasic"]
        e72player = ["Carvalho","Colombo","Maric","Ciurria"]
        e73player = ["Deulofeu","Thauvin","Brenner"," Success"]
        e74player = ["Berardi","Lauriente","Mulattieri","Pinamonti"]
        e75player = ["Caputo","Cambiaghi","Gyasi","Destro"]
        e76player = ["Botheim","Candreva","Ikwuemesi","Maggiore"]
        e77player = ["Piccoli","Krstovic","Banda","Burnete"]
        e78player = ["Mboula","Djuric","Braaf","Ngonge"]
        e79player = ["Moro","Krollis","Verde","Elia"]
        e80player = ["Ciofani","Buonaiuto","Coda","Zanimacchia"]
        e81player = ["Estanis","Borini","Gumina","Monache"]
        e82player = ["Retegui","Gudmundsson","Ekuban","Fini"]
        e83player = ["Cheddira","Kvernadze","Soule","Cuni"]
        e84player = ["Diaw","Nasti","Maita","Sibilli"]
        e85player = ["Colak","Benedyczak","Begic","Mihaila"]
        e86player = ["Lapadula","Pavoletti","Petagna","Zito"]
        e87player = ["Rover","Odogwu","Pecorino","Cisco"]
        e88player = ["Gondo","Lanini","Pettinari","Vido"]
        e89player =["Johsen","Pierini","Tessmann","Pohjanpalo"]
        e90player = ["Mancuso","Brunori","Soleri","Segre"]
        e91player = ["Falcinelli","Manconi","Giovannini","Gerli"]
        e92player = ["Mlakar","Torregrossa","Tramoni","Nagy"]
        e93player = ["Pedro Mendes","Millico","Nestorovski","Caligara"]
        e94player = ["Cutrone","Gabrielloni","Baselli","Cerri"]
        e95player = ["Favili","Dionisi","Raimondo","Proietti"]
        e96player = ["Moncini","Bianchi","Bisoli","Ferro"]
        e97player = ["Magrassi","Maistrello","Pittarello","Danzi"]
        e98player = ["Forte","Tutino","Novello","Crespi"]
        e99player =["Matos","Cudrig","Julitanmo","Seghetti"]
        e100player = ["Antenucci","Dalmonte","Siligardi","Rabbi"]
        e101player = ["Improta","Ciano","Marotta","Bolsius"]
        if equipo_player == "Arsenal":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e1player.insert(pos,nombre_jugador)
        elif equipo_player == "Aston Villa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e2player.insert(pos,nombre_jugador)
        elif equipo_player == "Bournemouth":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e3player.insert(pos,nombre_jugador)
        elif equipo_player == "Brentford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e4player.insert(pos,nombre_jugador)
        elif equipo_player == "Brigthon":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1 
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e5player.insert(pos,nombre_jugador)
        elif equipo_player == "Chelsea":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e6player.insert(pos,nombre_jugador)
        elif equipo_player == "Crystal Palace":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e7player.insert(pos,nombre_jugador)
        elif equipo_player == "Everton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e8player.insert(pos,nombre_jugador)
        elif equipo_player == "Fulham":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e9player.insert(pos,nombre_jugador)
        elif equipo_player == "Leeds United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e10player.insert(pos,nombre_jugador)
        elif equipo_player == "Leicester City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e11player.insert(pos,nombre_jugador)
        elif equipo_player == "Liverpool":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e12player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester City":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e13player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester United":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            elif valoracion_player > 30: 
                pos = 6
            else: pos = 7         
            e14player.insert(pos,nombre_jugador)
        elif equipo_player == "Newcastle":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e15player.insert(pos,nombre_jugador)
        elif equipo_player == "Nottingham Forest":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e16player.insert(pos,nombre_jugador)
        elif equipo_player == "Southampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e17player.insert(pos,nombre_jugador)
        elif equipo_player == "Tottenham":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e18player.insert(pos,nombre_jugador)
        elif equipo_player == "West ham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e19player.insert(pos,nombre_jugador)
        elif equipo_player == "Wolverhampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e20player.insert(pos,nombre_jugador)
        elif equipo_player == "Burnley":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e21player.insert(pos,nombre_jugador)
        elif equipo_player == "Sheffield United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e22player.insert(pos,nombre_jugador)
        elif equipo_player == "Luton Town":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e23player.insert(pos,nombre_jugador)
        elif equipo_player == "Middlesbrough":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e24player.insert(pos,nombre_jugador)
        elif equipo_player == "Coventry City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e25player.insert(pos,nombre_jugador)
        elif equipo_player == "Sunderland":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e26player.insert(pos,nombre_jugador)
        elif equipo_player == "Blackburn Rovers":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e27player.insert(pos,nombre_jugador)     
        elif equipo_player == "Millwall":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e28player.insert(pos,nombre_jugador)
        elif equipo_player == "West Bromwich Albion":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e29player.insert(pos,nombre_jugador)   
        elif equipo_player == "Swansea":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e30player.insert(pos,nombre_jugador)
        elif equipo_player == "Watford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e31player.insert(pos,nombre_jugador) 
        elif equipo_player == "Preston North End":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e32player.insert(pos,nombre_jugador)     
        elif equipo_player == "Norwich":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e33player.insert(pos,nombre_jugador)            
        elif equipo_player == "Bristol City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e34player.insert(pos,nombre_jugador)
        elif equipo_player == "Hull City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            
            e35player.insert(pos,nombre_jugador) 
        elif equipo_player == "Stoke City":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e36player.insert(pos,nombre_jugador)
        elif equipo_player == "Birmingham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e37player.insert(pos,nombre_jugador)
        elif equipo_player == "Huddersfield Town":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e38player.insert(pos,nombre_jugador)
        elif equipo_player == "Cardiff City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e39player.insert(pos,nombre_jugador)
        elif equipo_player == "Queens Park Rangers":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e40player.insert(pos,nombre_jugador)
        elif equipo_player == "Inter":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e43player.insert(pos,nombre_jugador)
        elif equipo_player == "Juventus":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e44player.insert(pos,nombre_jugador)
        elif equipo_player == "Milan":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e45player.insert(pos,nombre_jugador)
        elif equipo_player == "Napoli":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e46player.insert(pos,nombre_jugador)
        elif equipo_player == "Roma":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e47player.insert(pos,nombre_jugador)
        elif equipo_player == "Lazio":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e67player.insert(pos,nombre_jugador)
        elif equipo_player == "Atalanta":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e68player.insert(pos,nombre_jugador)
        elif equipo_player == "Fiorentina":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e69player.insert(pos,nombre_jugador)
        elif equipo_player == "Bologna":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e70player.insert(pos,nombre_jugador)
        elif equipo_player == "Torino":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e71player.insert(pos,nombre_jugador)
        elif equipo_player == "Sassuolo":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e74player.insert(pos,nombre_jugador)
        elif equipo_player == "Udinese":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e73player.insert(pos,nombre_jugador)
        elif equipo_player == "Monza":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e72player.insert(pos,nombre_jugador)
        elif equipo_player == "Empoli":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e75player.insert(pos,nombre_jugador)
        elif equipo_player == "Salernitana":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e76player.insert(pos,nombre_jugador)
        elif equipo_player == "Lecce":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e77player.insert(pos,nombre_jugador)
        elif equipo_player == "Hellas Verona":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e78player.insert(pos,nombre_jugador)
        elif equipo_player == "Spezia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e79player.insert(pos,nombre_jugador)
        elif equipo_player == "Cremonese":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e80player.insert(pos,nombre_jugador)
        elif equipo_player == "Sampdoria":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e81player.insert(pos,nombre_jugador)
        elif equipo_player == "Genoa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e83player.insert(pos,nombre_jugador)
        elif equipo_player == "Frosinone":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e82player.insert(pos,nombre_jugador)
        elif equipo_player == "Bari":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e84player.insert(pos,nombre_jugador)
        elif equipo_player == "Parma":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e85player.insert(pos,nombre_jugador)
        elif equipo_player == "Cagliari":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e86player.insert(pos,nombre_jugador)
        elif equipo_player == "Sudtirol":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e87player.insert(pos,nombre_jugador)
        elif equipo_player == "Reggina":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e88player.insert(pos,nombre_jugador)
        elif equipo_player == "Venezia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e89player.insert(pos,nombre_jugador)
        elif equipo_player == "Palermo":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e90player.insert(pos,nombre_jugador)
        elif equipo_player == "Modena":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e91player.insert(pos,nombre_jugador)
        elif equipo_player == "Pisa":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e92player.insert(pos,nombre_jugador)
        elif equipo_player == "Ascoli":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e93player.insert(pos,nombre_jugador)
        elif equipo_player == "Como":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e94player.insert(pos,nombre_jugador)
        elif equipo_player == "Ternana":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e95player.insert(pos,nombre_jugador)
        elif equipo_player == "Brescia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e96player.insert(pos,nombre_jugador)
        elif equipo_player == "Cittadella":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e97player.insert(pos,nombre_jugador)
        elif equipo_player == "Spal":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e100player.insert(pos,nombre_jugador)
        elif equipo_player == "Benevento":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e101player.insert(pos,nombre_jugador)
        elif equipo_player == "Cosenza":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e98player.insert(pos,nombre_jugador)
        elif equipo_player == "Perugia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e99player.insert(pos,nombre_jugador)
        
   
        if club == "Arsenal":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                weigth = len(jugadores)
            else:    
                jugadores = e1player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Aston Villa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                weigth = len(jugadores)
            else:
                jugadores = e2player 
                weigth = len(jugadores)
            gol =  get_random_player6(jugadores,weigth)
        elif club == "Bournemouth":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                weigth = len(jugadores)
            else:
                jugadores = e3player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Brentford":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                weigth = len(jugadores)
            else:
                jugadores = e4player 
                weigth = len(jugadores)
            gol =  get_random_player6(jugadores,weigth)
        elif club == "Brigthon":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                weigth = len(jugadores)
            else:
                jugadores = e5player 
                weigth = len(jugadores)
            gol =  get_random_player6(jugadores,weigth)
        elif club == "Chelsea":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                weigth = len(jugadores)
            else:
                jugadores = e6player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Crystal Palace":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                weigth = len(jugadores)
            else:
                jugadores = e7player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Everton":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                weigth = len(jugadores)
            else:
                jugadores = e8player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Fulham":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                weigth = len(jugadores)
            else:
                jugadores = e9player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Leeds United":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                weigth = len(jugadores)
            else:
                jugadores = e10player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Leicester City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                weigth = len(jugadores)
            else:
                jugadores = e11player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Liverpool":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                weigth = len(jugadores)
            else:
                jugadores = e12player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Manchester City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                weigth = len(jugadores)
            else:
                jugadores = e13player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Manchester United":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                weigth = len(jugadores)
            else:
                jugadores = e14player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Newcastle":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                weigth = len(jugadores)
            else:
                jugadores = e15player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Nottingham Forest":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                weigth = len(jugadores)
            else:
                jugadores = e16player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Southampton":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                weigth = len(jugadores)
            else:
                jugadores = e17player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Tottenham":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                weigth = len(jugadores)
            else:
             jugadores = e18player 
             weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "West ham":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                weigth = len(jugadores)
            else:
                jugadores = e19player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Wolverhampton":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                weigth = len(jugadores)
            else:
                jugadores = e20player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Burnley":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                weigth = len(jugadores)
            else:
                jugadores = e21player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Sheffield United":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                weigth = len(jugadores)
            else:
                jugadores = e22player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Luton Town":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                weigth = len(jugadores)
            else:
                jugadores = e23player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Middlesbrough":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                weigth = len(jugadores)
            else:
                jugadores = e24player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Coventry City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                weigth = len(jugadores)
            else:
                jugadores = e25player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Sunderland":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                weigth = len(jugadores)
            else:
                jugadores = e26player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Blackburn Rovers":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                weigth = len(jugadores)
            else:
                jugadores = e27player 
                weigth = len(jugadores)  
            gol = get_random_player6(jugadores,weigth)      
        elif club == "Millwall":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                weigth = len(jugadores)
            else:
                jugadores = e28player 
                weigth = len(jugadores) 
            gol = get_random_player6(jugadores,weigth)       
        elif club == "West Bromwich Albion":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                weigth = len(jugadores)
            else:
                jugadores = e29player 
                weigth = len(jugadores)  
            gol = get_random_player6(jugadores,weigth)      
        elif club == "Swansea":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                weigth = len(jugadores)
            else:
                jugadores = e30player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Watford":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                weigth = len(jugadores)
            else:
                jugadores = e31player 
                weigth = len(jugadores)   
            gol = get_random_player6(jugadores,weigth)     
        elif club == "Preston North End":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                weigth = len(jugadores)
            else:
                jugadores = e32player 
                weigth = len(jugadores)   
            gol = get_random_player6(jugadores,weigth)     
        elif club == "Norwich":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                weigth = len(jugadores)
            else:
                jugadores = e33player 
                weigth = len(jugadores)   
            gol = get_random_player6(jugadores,weigth)             
        elif club == "Bristol City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                weigth = len(jugadores)
            else:
                jugadores = e34player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Hull City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                weigth = len(jugadores)
            else:
                jugadores = e35player 
                weigth = len(jugadores) 
            gol = get_random_player6(jugadores,weigth)       
        elif club == "Stoke City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                weigth = len(jugadores)
            else:
                jugadores = e36player 
                weigth = len(jugadores)   
            gol = get_random_player6(jugadores,weigth)     
        elif club == "Birmingham":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                weigth = len(jugadores)
            else:
                jugadores = e37player 
                weigth = len(jugadores) 
            gol = get_random_player6(jugadores,weigth)       
        elif club == "Huddersfield Town":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                weigth = len(jugadores)
            else:
                jugadores = e38player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Cardiff City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                weigth = len(jugadores)
            else:
                jugadores = e39player 
                weigth = len(jugadores)  
            gol = get_random_player6(jugadores,weigth)      
        elif club == "Queens Park Rangers":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                weigth = len(jugadores)
            else:
                jugadores = e40player 
                weigth = len(jugadores) 
            gol = get_random_player6(jugadores,weigth)  
        elif club == "PSG":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                weigth = len(jugadores)
            else:
                jugadores = e41player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "O.Lyon":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                weigth = len(jugadores)
            else:
                jugadores = e42player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Inter":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                weigth = len(jugadores)
            else:
                jugadores = e43player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Juventus":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                weigth = len(jugadores)
            else:
                jugadores = e44player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Milan":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                weigth = len(jugadores)
            else:
                jugadores = e45player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Napoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                weigth = len(jugadores)
            else:
                jugadores = e46player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Roma":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                weigth = len(jugadores)
            else:
                jugadores = e47player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Atl.Madrid":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                weigth = len(jugadores)
            else:
                jugadores = e48player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Barcelona":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e49player)
                weigth = len(jugadores)
            else:
                jugadores = e49player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Real Madrid":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e50player)
                weigth = len(jugadores)
            else:
                jugadores = e50player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "B.Dortmund":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e51player)
                weigth = len(jugadores)
            else:
                jugadores = e51player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Bayern Munich":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e52player)
                weigth = len(jugadores)
            else:
                jugadores = e52player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "B.Leverkusen":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e53player)
                weigth = len(jugadores)
            else:
                jugadores = e53player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Porto":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e54player)
                weigth = len(jugadores)
            else:
                jugadores = e54player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Sporting Lisboa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e55player)
                weigth = len(jugadores)
            else:
                jugadores = e55player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Frankfurt":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e56player)
                weigth = len(jugadores)
            else:
                jugadores = e56player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "O.Marsella":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e57player)
                weigth = len(jugadores)
            else:
                jugadores = e57player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)   
        elif club == "Sevilla":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e58player)
                weigth = len(jugadores)
            else:
                jugadores = e58player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Benfica":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e59player)
                weigth = len(jugadores)
            else:
                jugadores = e59player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Leipzig":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e60player)
                weigth = len(jugadores)
            else:
                jugadores = e60player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Ajax":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e61player)
                weigth = len(jugadores)
            else:
                jugadores = e61player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Monaco":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e62player)
                weigth = len(jugadores)
            else:
                jugadores = e62player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Shakhtar":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e63player)
                weigth = len(jugadores)
            else:
                jugadores = e63player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Brugge":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e64player)
                weigth = len(jugadores)
            else:
                jugadores = e64player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "PSV":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e65player)
                weigth = len(jugadores)
            else:
                jugadores = e65player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Real Sociedad":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e66player)
                weigth = len(jugadores)
            else:
                jugadores = e66player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)                    
        elif club == "Lazio":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e67player)
                weigth = len(jugadores)
            else:
                jugadores = e67player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Atalanta":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e68player)
                weigth = len(jugadores)
            else:
                jugadores = e68player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Fiorentina":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e69player)
                weigth = len(jugadores)
            else:
                jugadores = e69player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Bologna":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e70player)
                weigth = len(jugadores)
            else:
                jugadores = e70player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Torino":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e71player)
                weigth = len(jugadores)
            else:
                jugadores = e71player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Monza":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e72player)
                weigth = len(jugadores)
            else:
                jugadores = e72player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Udinese":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e73player)
                weigth = len(jugadores)
            else:
                jugadores = e73player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Sassuolo":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e74player)
                weigth = len(jugadores)
            else:
                jugadores = e74player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Empoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e75player)
                weigth = len(jugadores)
            else:
                jugadores = e75player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Salernitana":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e76player)
                weigth = len(jugadores)
            else:
                jugadores = e76player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Lecce":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e77player)
                weigth = len(jugadores)
            else:
                jugadores = e77player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Hellas Verona":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e78player)
                weigth = len(jugadores)
            else:
                jugadores = e78player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Spezia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e79player)
                weigth = len(jugadores)
            else:
                jugadores = e79player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cremonese":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e80player)
                weigth = len(jugadores)
            else:
                jugadores = e80player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Sampdoria":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e81player)
                weigth = len(jugadores)
            else:
                jugadores = e81player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Frosinone":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e82player)
                weigth = len(jugadores)
            else:
                jugadores = e82player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Genoa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e83player)
                weigth = len(jugadores)
            else:
                jugadores = e83player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Bari":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e84player)
                weigth = len(jugadores)
            else:
                jugadores = e84player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Parma":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e85player)
                weigth = len(jugadores)
            else:
                jugadores = e85player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cagliari":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e86player)
                weigth = len(jugadores)
            else:
                jugadores = e86player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)         
        elif club == "Sudtirol":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e87player)
                weigth = len(jugadores)
            else:
                jugadores = e87player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Reggina":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e88player)
                weigth = len(jugadores)
            else:
                jugadores = e88player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Venezia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e89player)
                weigth = len(jugadores)
            else:
                jugadores = e89player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Palermo":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e90player)
                weigth = len(jugadores)
            else:
                jugadores = e90player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Modena":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e91player)
                weigth = len(jugadores)
            else:
                jugadores = e91player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Pisa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e92player)
                weigth = len(jugadores)
            else:
                jugadores = e92player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Ascoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e93player)
                weigth = len(jugadores)
            else:
                jugadores = e93player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Como":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e94player)
                weigth = len(jugadores)
            else:
                jugadores = e94player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Ternana":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e95player)
                weigth = len(jugadores)
            else:
                jugadores = e95player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Brescia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e96player)
                weigth = len(jugadores)
            else:
                jugadores = e96player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cittadella":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e97player)
                weigth = len(jugadores)
            else:
                jugadores = e97player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Cosenza":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e98player)
                weigth = len(jugadores)
            else:
                jugadores = e98player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Perugia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e99player)
                weigth = len(jugadores)
            else:
                jugadores = e99player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Spal":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e100player)
                weigth = len(jugadores)
            else:
                jugadores = e100player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Benevento":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e101player)
                weigth = len(jugadores)
            else:
                jugadores = e101player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)       
            
        contador += 1     
        rojas.append(gol)
    if len(rojas) != 0:   
        print(f' rojas {club}: ' + ', '.join(map(str, rojas))) 
    return rojas

def goleadores(club,goles,jugadores_sancionados,jugadores_lesionados,equipo_player,valoracion_player,nombre_jugador):
    def get_random_player6(jugadores,weigth):
        if weigth == 7:
            weights7 = [0.30, 0.20, 0.15, 0.10, 0.10, 0.10, 0.5]             
            return random.choices(jugadores, weights=weights7)[0]
        elif weigth == 6:
            weights6 = [0.30, 0.20, 0.15, 0.15, 0.10, 0.10] 
            return random.choices(jugadores, weights=weights6)[0]
        elif weigth == 5:
            weights5 = [0.3, 0.2, 0.15, 0.15, 0.1] 
            return random.choices(jugadores, weights=weights5)[0]
        elif weigth == 4:
            weights4 = [0.35, 0.30, 0.20, 0.15 ] 
            return random.choices(jugadores, weights=weights4)[0]
        elif weigth == 3:
            weights3 = [0.5, 0.3, 0.2] 
            return random.choices(jugadores, weights=weights3)[0]    
        elif weigth == 2:
            weights2 = [0.6,0.4]
            return random.choices(jugadores, weights=weights2)[0]
        else:
            weights1 = [1]
            return random.choices(jugadores, weights=weights1)[0]   
    for i in jugadores_lesionados:
        if i in jugadores_sancionados: pass
        else: jugadores_sancionados.append(i)
    def jugadores_sancionados_sacar(jugadores_sancionados,player):
        array = player
        if len(jugadores_sancionados) != 0:
            for i in jugadores_sancionados:
                if i in array:
                    array.remove(i)
            return array
        else:
            return array   
    
    goles_totales = []
    while (goles != 0):
        e1player = ["Martinelli", "Gabriel Jesus", "Havertz", "Saka", "Odegaard"]
        e2player = ["Coutinho", "Watkins", "Ramsey", "Buendía"]
        e3player = ["Semenyo","Solanke","Lerma","Christie"]
        e4player = ["Toney", "Mbeumo", "Schade", "Ghoddos"]
        e5player = ["Fati", "Welbeck", "Mitoma", "Enciso", "Ferguson"]
        e6player = ["Sterling", "Fernandez", "Nkunku", "Mudryk","Palmer"]
        e7player = ["Ayew(cp)", "Mateta", "Doucoure", "Edouard"]
        e8player = ["Beto", "McNeil", "Calvert-Lewin", "Danjuma"]
        e9player = ["Traore", "Jimenez", "Iwobi", "Willian"]
        e10player = ["Rutter","Summerville","Gnoto","Gray"]
        e11player = ["Vardy","Iheanacho","Akgün","Mavididi"]
        e12player = ["Salah", "MacAllister", "Núñez", "Luis Díaz", "Diogo Jota"]
        e13player = ["Haaland", "Foden", "Grealish", "Álvarez", "De Bruyne"]
        e14player = ["Rashford", "Mount", "Bruno Fernandes", "Martial", "Sancho"]
        e15player = ["Isak", "Guimarães", "Joelinton", "Tonali", "Murphy"]
        e16player = ["Awoniyi", "Gibbs-White", "Origi", "Danilo"]
        e17player = ["Adams","Alcaraz","Armstrong","Edozie"]
        e18player = ["Richarlison", "Son", "Sarr", "Kulusevski", "Perisic"]
        e19player = ["Antonio", "Paquetá", "Benrahma", "Ings"]
        e20player = ["Silva", "Cunha", "Kalajdzic", "Sarabia"]
        e21player = ["Foster", "Redmond", "Amdouni", "Brownhill"]
        e22player = ["Osula", "Jebbison", "Archer", "Brewster"]
        e23player = ["Adebayo", "Lokonga", "Morris", "Ogbene"]
        e24player = ["Greenwood","Silvera","Jones","Forss"]
        e25player = ["Godden","Simms","Tavares","Wright"]
        e26player = ["Clarke","Bennette","Semedo","Rigg"]
        e27player = ["Leonard","Gallagher","Ennis","Hedges"]
        e28player = ["Bradshaw","Nisbet","Watmore","Emakhu"]
        e29player = ["Dike","Wallace","Diangana","Phillips"]
        e30player = ["Lowe","Ginnelly","Cooper","Cullen"]
        e31player = ["Bayo","Martins","Healeyr","Ince"]
        e32player = ["Keane","Holmes","Riis","McCann"]
        e33player = ["Barnes","Sargent","Gibbs","Idah"]
        e34player =["Wells","Cornick","Bell","Conway"]
        e35player = ["Delap","Lokilo","Sinik","Connolly"]
        e36player = ["Gooch","Campbell","Mmaee","Gayle"]
        e37player = ["Hogan","Jutkiewicz","Roberts","Stansfield"]
        e38player = ["Koroma","Burgzorg","Ward","Hudlin"]
        e39player = ["Ugbo","Robinson","Bowler","Grant"]
        e40player = ["Dykes","Adomah","Willock","Smyth"]
        e41player = ["Mbappe","Asensio","O.Dembele","Muani","Barcola"]
        e42player = ["Lacazette","Baldé","Jeffinho","Tolisso","Tagliafico"]
        e43player = ["Martinez","Alexis Sánchez","Arnautovic","Calhanoglu","Mkhitaryan"]
        e44player = ["Vlahovic","Kean","Chiesa","Milik","Pogba"]
        e45player = ["Giroud","Leão","Pulisic","Jović","Romero"]
        e46player = ["Osimhen","Raspadori","Simeone","Politano","Kvaratskhelia"]
        e47player = ["Dybala","Belotti","El Shaarawy","Lukaku","Pellegrini"]
        e48player = ["Griezmann","Morata","de Paul","Koke","Lemar"]
        e49player = ["Lewandowski","Gavi","Felix","Raphinha","Torres"]
        e50player = ["Bellingham","Vinicius","Rodrygo","Modric","Tchouameni"]
        e51player =["Haller","Moukoko","Adeyemi","Reus","Reyna"]
        e52player = ["Kane","Gnabry","Müller","Musiala","Sané"]
        e53player = ["Tella","Hložek","Hofmann","Adli","Boniface"]
        e54player = ["Taremi","Galeno","Evanilson","Jaime","Grujic"]
        e55player = ["Paulinho","Trincao","Edwards","Santos","Goncalves"]
        e56player = ["Götze","Marmoush","Ngankam","Alario","Rode"]
        e57player = ["Aubameyang","Sarr(M)","Correa","Ndiaye","Gueye"]
        e58player = ["Zakharyan","En-Nesyri","Suso","Ocampos","Rakitić"]
        e59player = ["Neres","Rafa","Di María","Musa","Gouveia"]
        e60player = ["Poulsen","Werner","Sesko","Olmo","Openda"]
        e61player = ["Bergwijn","Akpom","Mikautadze","Godts","Tahirovic"]
        e62player = ["Ben Yedder","Martins(M)","Embolo","Seghir","Camara"]
        e63player = ["Traore","Sikan","Petryak","Zubkov","Bondarenko"]
        e64player = ["Buchanan","Nusa","Jutglà","Vermant","Olsen"]
        e65player = ["de Jong","Bakayoko","Til","Veerman","Lang"]
        e66player = ["Sadiq","Oyarzabal","Andre Silva","Kubo","Zakharyan"]
        e67player = ["Immobile","Anderson","Pedro(L)","Basic","Isaksen"]
        e68player = ["Muriel","Scamacca","Pasalic","Lookman","Adopo"]
        e69player = ["N.Gonzalez","Arthur","Beltrán","Sottil","Kouamé"]
        e70player = ["Karlsson","Ndoye","Orsolini","Hooijdonk"]
        e71player = ["Pellegri","Radonjic","Sanabria","Vlasic"]
        e72player = ["Carvalho","Colombo","Maric","Ciurria"]
        e73player = ["Deulofeu","Thauvin","Brenner"," Success"]
        e74player = ["Berardi","Lauriente","Mulattieri","Pinamonti"]
        e75player = ["Caputo","Cambiaghi","Gyasi","Destro"]
        e76player = ["Botheim","Candreva","Ikwuemesi","Maggiore"]
        e77player = ["Piccoli","Krstovic","Banda","Burnete"]
        e78player = ["Mboula","Djuric","Braaf","Ngonge"]
        e79player = ["Moro","Krollis","Verde","Elia"]
        e80player = ["Ciofani","Buonaiuto","Coda","Zanimacchia"]
        e81player = ["Estanis","Borini","Gumina","Monache"]
        e82player = ["Cheddira","Kvernadze","Soule","Cuni"] 
        e83player = ["Retegui","Gudmundsson","Ekuban","Fini"]
        e84player = ["Diaw","Nasti","Maita","Sibilli"]
        e85player = ["Colak","Benedyczak","Begic","Mihaila"]
        e86player = ["Lapadula","Pavoletti","Petagna","Zito"]
        e87player = ["Rover","Odogwu","Pecorino","Cisco"]
        e88player = ["Gondo","Lanini","Pettinari","Vido"]
        e89player =["Johsen","Pierini","Tessmann","Pohjanpalo"]
        e90player = ["Mancuso","Brunori","Soleri","Segre"]
        e91player = ["Falcinelli","Manconi","Giovannini","Gerli"]
        e92player = ["Mlakar","Torregrossa","Tramoni","Nagy"]
        e93player = ["Pedro Mendes","Millico","Nestorovski","Caligara"]
        e94player = ["Cutrone","Gabrielloni","Baselli","Cerri"]
        e95player = ["Favili","Dionisi","Raimondo","Proietti"]
        e96player = ["Moncini","Bianchi","Bisoli","Ferro"]
        e97player = ["Magrassi","Maistrello","Pittarello","Danzi"]
        e98player = ["Forte","Tutino","Novello","Crespi"]
        e99player =["Matos","Cudrig","Julitanmo","Seghetti"]
        e100player = ["Antenucci","Dalmonte","Siligardi","Rabbi"]
        e101player = ["Improta","Ciano","Marotta","Bolsius"]
        if equipo_player == "Arsenal":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e1player.insert(pos,nombre_jugador)
        elif equipo_player == "Aston Villa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e2player.insert(pos,nombre_jugador)
        elif equipo_player == "Bournemouth":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e3player.insert(pos,nombre_jugador)
        elif equipo_player == "Brentford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e4player.insert(pos,nombre_jugador)
        elif equipo_player == "Brigthon":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1 
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e5player.insert(pos,nombre_jugador)
        elif equipo_player == "Chelsea":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e6player.insert(pos,nombre_jugador)
        elif equipo_player == "Crystal Palace":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e7player.insert(pos,nombre_jugador)
        elif equipo_player == "Everton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e8player.insert(pos,nombre_jugador)
        elif equipo_player == "Fulham":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e9player.insert(pos,nombre_jugador)
        elif equipo_player == "Leeds United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e10player.insert(pos,nombre_jugador)
        elif equipo_player == "Leicester City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e11player.insert(pos,nombre_jugador)
        elif equipo_player == "Liverpool":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e12player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester City":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e13player.insert(pos,nombre_jugador)
        elif equipo_player == "Manchester United":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            elif valoracion_player > 30: 
                pos = 6
            else: pos = 7         
            e14player.insert(pos,nombre_jugador)
        elif equipo_player == "Newcastle":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e15player.insert(pos,nombre_jugador)
        elif equipo_player == "Nottingham Forest":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e16player.insert(pos,nombre_jugador)
        elif equipo_player == "Southampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e17player.insert(pos,nombre_jugador)
        elif equipo_player == "Tottenham":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e18player.insert(pos,nombre_jugador)
        elif equipo_player == "West ham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e19player.insert(pos,nombre_jugador)
        elif equipo_player == "Wolverhampton":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e20player.insert(pos,nombre_jugador)
        elif equipo_player == "Burnley":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e21player.insert(pos,nombre_jugador)
        elif equipo_player == "Sheffield United":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e22player.insert(pos,nombre_jugador)
        elif equipo_player == "Luton Town":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e23player.insert(pos,nombre_jugador)
        elif equipo_player == "Middlesbrough":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e24player.insert(pos,nombre_jugador)
        elif equipo_player == "Coventry City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e25player.insert(pos,nombre_jugador)
        elif equipo_player == "Sunderland":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e26player.insert(pos,nombre_jugador)
        elif equipo_player == "Blackburn Rovers":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e27player.insert(pos,nombre_jugador)     
        elif equipo_player == "Millwall":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e28player.insert(pos,nombre_jugador)
        elif equipo_player == "West Bromwich Albion":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e29player.insert(pos,nombre_jugador)   
        elif equipo_player == "Swansea":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e30player.insert(pos,nombre_jugador)
        elif equipo_player == "Watford":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e31player.insert(pos,nombre_jugador) 
        elif equipo_player == "Preston North End":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e32player.insert(pos,nombre_jugador)     
        elif equipo_player == "Norwich":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e33player.insert(pos,nombre_jugador)            
        elif equipo_player == "Bristol City":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e34player.insert(pos,nombre_jugador)
        elif equipo_player == "Hull City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            
            e35player.insert(pos,nombre_jugador) 
        elif equipo_player == "Stoke City":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e36player.insert(pos,nombre_jugador)
        elif equipo_player == "Birmingham":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e37player.insert(pos,nombre_jugador)
        elif equipo_player == "Huddersfield Town":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e38player.insert(pos,nombre_jugador)
        elif equipo_player == "Cardiff City":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e39player.insert(pos,nombre_jugador)
        elif equipo_player == "Queens Park Rangers":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e40player.insert(pos,nombre_jugador)
        elif equipo_player == "Inter":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e43player.insert(pos,nombre_jugador)
        elif equipo_player == "Juventus":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e44player.insert(pos,nombre_jugador)
        elif equipo_player == "Milan":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e45player.insert(pos,nombre_jugador)
        elif equipo_player == "Napoli":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e46player.insert(pos,nombre_jugador)
        elif equipo_player == "Roma":
            if valoracion_player > 90: 
                pos = 0
            elif valoracion_player > 80: 
                pos = 1 
            elif valoracion_player > 70: 
                pos = 2 
            elif valoracion_player > 60: 
                pos = 3 
            elif valoracion_player > 50: 
                pos = 4 
            elif valoracion_player > 40: 
                pos = 5
            else: pos = 6
            e47player.insert(pos,nombre_jugador)
        elif equipo_player == "Lazio":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e67player.insert(pos,nombre_jugador)
        elif equipo_player == "Atalanta":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e68player.insert(pos,nombre_jugador)
        elif equipo_player == "Fiorentina":
            if valoracion_player > 80: 
                pos = 0
            elif valoracion_player > 70: 
                pos = 1
            elif valoracion_player > 60:
                pos = 2
            elif valoracion_player > 50: 
                pos = 3 
            elif valoracion_player > 40: 
                pos = 4 
            elif valoracion_player > 30: 
                pos = 5
            else: pos = 6
            e69player.insert(pos,nombre_jugador)
        elif equipo_player == "Bologna":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e70player.insert(pos,nombre_jugador)
        elif equipo_player == "Torino":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e71player.insert(pos,nombre_jugador)
        elif equipo_player == "Sassuolo":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e74player.insert(pos,nombre_jugador)
        elif equipo_player == "Udinese":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e73player.insert(pos,nombre_jugador)
        elif equipo_player == "Monza":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e72player.insert(pos,nombre_jugador)
        elif equipo_player == "Empoli":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e75player.insert(pos,nombre_jugador)
        elif equipo_player == "Salernitana":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e76player.insert(pos,nombre_jugador)
        elif equipo_player == "Lecce":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e77player.insert(pos,nombre_jugador)
        elif equipo_player == "Hellas Verona":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e78player.insert(pos,nombre_jugador)
        elif equipo_player == "Spezia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e79player.insert(pos,nombre_jugador)
        elif equipo_player == "Cremonese":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e80player.insert(pos,nombre_jugador)
        elif equipo_player == "Sampdoria":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e81player.insert(pos,nombre_jugador)
        elif equipo_player == "Genoa":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e83player.insert(pos,nombre_jugador)
        elif equipo_player == "Frosinone":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e82player.insert(pos,nombre_jugador)
        elif equipo_player == "Bari":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e84player.insert(pos,nombre_jugador)
        elif equipo_player == "Parma":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e85player.insert(pos,nombre_jugador)
        elif equipo_player == "Cagliari":
            if valoracion_player > 60: 
                pos = 0
            elif valoracion_player > 55:
                pos = 1 
            elif valoracion_player > 50:
                pos = 2
            elif valoracion_player > 45: 
                pos = 3 
            else: pos = 4
            e86player.insert(pos,nombre_jugador)
        elif equipo_player == "Sudtirol":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e87player.insert(pos,nombre_jugador)
        elif equipo_player == "Reggina":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e88player.insert(pos,nombre_jugador)
        elif equipo_player == "Venezia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e89player.insert(pos,nombre_jugador)
        elif equipo_player == "Palermo":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e90player.insert(pos,nombre_jugador)
        elif equipo_player == "Modena":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e91player.insert(pos,nombre_jugador)
        elif equipo_player == "Pisa":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e92player.insert(pos,nombre_jugador)
        elif equipo_player == "Ascoli":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e93player.insert(pos,nombre_jugador)
        elif equipo_player == "Como":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e94player.insert(pos,nombre_jugador)
        elif equipo_player == "Ternana":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e95player.insert(pos,nombre_jugador)
        elif equipo_player == "Brescia":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e96player.insert(pos,nombre_jugador)
        elif equipo_player == "Cittadella":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e97player.insert(pos,nombre_jugador)
        elif equipo_player == "Spal":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e100player.insert(pos,nombre_jugador)
        elif equipo_player == "Benevento":
            if valoracion_player > 50: 
                pos = 0
            elif valoracion_player > 45:
                pos = 1 
            elif valoracion_player > 40: 
                pos = 2
            elif valoracion_player > 30:
                pos = 3 
            elif valoracion_player > 25: 
                pos = 4
            else: pos = 5
            e101player.insert(pos,nombre_jugador)
        elif equipo_player == "Cosenza":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e98player.insert(pos,nombre_jugador)
        elif equipo_player == "Perugia":
            if valoracion_player > 40:
                pos = 0
            elif valoracion_player > 35:
                pos = 1 
            elif valoracion_player > 30:
                pos = 2 
            elif valoracion_player > 25: 
                pos = 3 
            else: pos = 4
            e99player.insert(pos,nombre_jugador)
        
        gol = str(goles)
        goles = goles -1
        if club == "Arsenal":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e1player)
                weigth = len(jugadores)
            else:    
                jugadores = e1player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Aston Villa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e2player)
                weigth = len(jugadores)
            else:
                jugadores = e2player 
                weigth = len(jugadores)
            gol =  get_random_player6(jugadores,weigth)
        elif club == "Bournemouth":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e3player)
                weigth = len(jugadores)
            else:
                jugadores = e3player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Brentford":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e4player)
                weigth = len(jugadores)
            else:
                jugadores = e4player 
                weigth = len(jugadores)
            gol =  get_random_player6(jugadores,weigth)
        elif club == "Brigthon":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e5player)
                weigth = len(jugadores)
            else:
                jugadores = e5player 
                weigth = len(jugadores)
            gol =  get_random_player6(jugadores,weigth)
        elif club == "Chelsea":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e6player)
                weigth = len(jugadores)
            else:
                jugadores = e6player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Crystal Palace":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e7player)
                weigth = len(jugadores)
            else:
                jugadores = e7player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Everton":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e8player)
                weigth = len(jugadores)
            else:
                jugadores = e8player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Fulham":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e9player)
                weigth = len(jugadores)
            else:
                jugadores = e9player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Leeds United":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e10player)
                weigth = len(jugadores)
            else:
                jugadores = e10player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Leicester City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e11player)
                weigth = len(jugadores)
            else:
                jugadores = e11player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Liverpool":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e12player)
                weigth = len(jugadores)
            else:
                jugadores = e12player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Manchester City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e13player)
                weigth = len(jugadores)
            else:
                jugadores = e13player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Manchester United":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e14player)
                weigth = len(jugadores)
            else:
                jugadores = e14player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Newcastle":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e15player)
                weigth = len(jugadores)
            else:
                jugadores = e15player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Nottingham Forest":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e16player)
                weigth = len(jugadores)
            else:
                jugadores = e16player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Southampton":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e17player)
                weigth = len(jugadores)
            else:
                jugadores = e17player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Tottenham":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e18player)
                weigth = len(jugadores)
            else:
             jugadores = e18player 
             weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "West ham":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e19player)
                weigth = len(jugadores)
            else:
                jugadores = e19player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Wolverhampton":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e20player)
                weigth = len(jugadores)
            else:
                jugadores = e20player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Burnley":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e21player)
                weigth = len(jugadores)
            else:
                jugadores = e21player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Sheffield United":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e22player)
                weigth = len(jugadores)
            else:
                jugadores = e22player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Luton Town":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e23player)
                weigth = len(jugadores)
            else:
                jugadores = e23player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Middlesbrough":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e24player)
                weigth = len(jugadores)
            else:
                jugadores = e24player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Coventry City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e25player)
                weigth = len(jugadores)
            else:
                jugadores = e25player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Sunderland":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e26player)
                weigth = len(jugadores)
            else:
                jugadores = e26player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Blackburn Rovers":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e27player)
                weigth = len(jugadores)
            else:
                jugadores = e27player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)        
        elif club == "Millwall":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e28player)
                weigth = len(jugadores)
            else:
                jugadores = e28player 
                weigth = len(jugadores)     
            gol = get_random_player6(jugadores,weigth)   
        elif club == "West Bromwich Albion":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e29player)
                weigth = len(jugadores)
            else:
                jugadores = e29player 
                weigth = len(jugadores)   
            gol = get_random_player6(jugadores,weigth)     
        elif club == "Swansea":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e30player)
                weigth = len(jugadores)
            else:
                jugadores = e30player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Watford":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e31player)
                weigth = len(jugadores)
            else:
                jugadores = e31player 
                weigth = len(jugadores)  
            gol = get_random_player6(jugadores,weigth)      
        elif club == "Preston North End":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e32player)
                weigth = len(jugadores)
            else:
                jugadores = e32player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)        
        elif club == "Norwich":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e33player)
                weigth = len(jugadores)
            else:
                jugadores = e33player 
                weigth = len(jugadores)  
            gol = get_random_player6(jugadores,weigth)              
        elif club == "Bristol City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e34player)
                weigth = len(jugadores)
            else:
                jugadores = e34player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Hull City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e35player)
                weigth = len(jugadores)
            else:
                jugadores = e35player 
                weigth = len(jugadores)  
            gol = get_random_player6(jugadores,weigth)      
        elif club == "Stoke City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e36player)
                weigth = len(jugadores)
            else:
                jugadores = e36player 
                weigth = len(jugadores) 
            gol = get_random_player6(jugadores,weigth)       
        elif club == "Birmingham":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e37player)
                weigth = len(jugadores)
            else:
                jugadores = e37player 
                weigth = len(jugadores)   
            gol = get_random_player6(jugadores,weigth)     
        elif club == "Huddersfield Town":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e38player)
                weigth = len(jugadores)
            else:
                jugadores = e38player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Cardiff City":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e39player)
                weigth = len(jugadores)
            else:
                jugadores = e39player 
                weigth = len(jugadores)    
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Queens Park Rangers":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e40player)
                weigth = len(jugadores)
            else:
                jugadores = e40player 
                weigth = len(jugadores)                                      
            gol = get_random_player6(jugadores,weigth)
        elif club == "PSG":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e41player)
                weigth = len(jugadores)
            else:
                jugadores = e41player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "O.Lyon":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e42player)
                weigth = len(jugadores)
            else:
                jugadores = e42player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Inter":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e43player)
                weigth = len(jugadores)
            else:
                jugadores = e43player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Juventus":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e44player)
                weigth = len(jugadores)
            else:
                jugadores = e44player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Milan":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e45player)
                weigth = len(jugadores)
            else:
                jugadores = e45player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Napoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e46player)
                weigth = len(jugadores)
            else:
                jugadores = e46player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Roma":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e47player)
                weigth = len(jugadores)
            else:
                jugadores = e47player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Atl.Madrid":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e48player)
                weigth = len(jugadores)
            else:
                jugadores = e48player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Barcelona":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e49player)
                weigth = len(jugadores)
            else:
                jugadores = e49player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Real Madrid":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e50player)
                weigth = len(jugadores)
            else:
                jugadores = e50player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "B.Dortmund":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e51player)
                weigth = len(jugadores)
            else:
                jugadores = e51player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Bayern Munich":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e52player)
                weigth = len(jugadores)
            else:
                jugadores = e52player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "B.Leverkusen":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e53player)
                weigth = len(jugadores)
            else:
                jugadores = e53player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Porto":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e54player)
                weigth = len(jugadores)
            else:
                jugadores = e54player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Sporting Lisboa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e55player)
                weigth = len(jugadores)
            else:
                jugadores = e55player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Frankfurt":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e56player)
                weigth = len(jugadores)
            else:
                jugadores = e56player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "O.Marsella":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e57player)
                weigth = len(jugadores)
            else:
                jugadores = e57player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)   
        elif club == "Sevilla":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e58player)
                weigth = len(jugadores)
            else:
                jugadores = e58player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Benfica":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e59player)
                weigth = len(jugadores)
            else:
                jugadores = e59player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Leipzig":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e60player)
                weigth = len(jugadores)
            else:
                jugadores = e60player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Ajax":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e61player)
                weigth = len(jugadores)
            else:
                jugadores = e61player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Monaco":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e62player)
                weigth = len(jugadores)
            else:
                jugadores = e62player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Shakhtar":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e63player)
                weigth = len(jugadores)
            else:
                jugadores = e63player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Brugge":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e64player)
                weigth = len(jugadores)
            else:
                jugadores = e64player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "PSV":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e65player)
                weigth = len(jugadores)
            else:
                jugadores = e65player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Real Sociedad":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e66player)
                weigth = len(jugadores)
            else:
                jugadores = e66player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)                
        elif club == "Lazio":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e67player)
                weigth = len(jugadores)
            else:
                jugadores = e67player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Atalanta":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e68player)
                weigth = len(jugadores)
            else:
                jugadores = e68player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Fiorentina":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e69player)
                weigth = len(jugadores)
            else:
                jugadores = e69player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Bologna":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e70player)
                weigth = len(jugadores)
            else:
                jugadores = e70player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Torino":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e71player)
                weigth = len(jugadores)
            else:
                jugadores = e71player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)
        elif club == "Monza":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e72player)
                weigth = len(jugadores)
            else:
                jugadores = e72player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Udinese":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e73player)
                weigth = len(jugadores)
            else:
                jugadores = e73player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Sassuolo":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e74player)
                weigth = len(jugadores)
            else:
                jugadores = e74player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Empoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e75player)
                weigth = len(jugadores)
            else:
                jugadores = e75player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Salernitana":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e76player)
                weigth = len(jugadores)
            else:
                jugadores = e76player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Lecce":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e77player)
                weigth = len(jugadores)
            else:
                jugadores = e77player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Hellas Verona":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e78player)
                weigth = len(jugadores)
            else:
                jugadores = e78player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Spezia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e79player)
                weigth = len(jugadores)
            else:
                jugadores = e79player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cremonese":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e80player)
                weigth = len(jugadores)
            else:
                jugadores = e80player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Sampdoria":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e81player)
                weigth = len(jugadores)
            else:
                jugadores = e81player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Frosinone":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e82player)
                weigth = len(jugadores)
            else:
                jugadores = e82player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Genoa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e83player)
                weigth = len(jugadores)
            else:
                jugadores = e83player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Bari":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e84player)
                weigth = len(jugadores)
            else:
                jugadores = e84player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Parma":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e85player)
                weigth = len(jugadores)
            else:
                jugadores = e85player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cagliari":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e86player)
                weigth = len(jugadores)
            else:
                jugadores = e86player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)         
        elif club == "Sudtirol":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e87player)
                weigth = len(jugadores)
            else:
                jugadores = e87player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Reggina":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e88player)
                weigth = len(jugadores)
            else:
                jugadores = e88player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Venezia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e89player)
                weigth = len(jugadores)
            else:
                jugadores = e89player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Palermo":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e90player)
                weigth = len(jugadores)
            else:
                jugadores = e90player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Modena":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e91player)
                weigth = len(jugadores)
            else:
                jugadores = e91player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Pisa":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e92player)
                weigth = len(jugadores)
            else:
                jugadores = e92player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Ascoli":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e93player)
                weigth = len(jugadores)
            else:
                jugadores = e93player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Como":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e94player)
                weigth = len(jugadores)
            else:
                jugadores = e94player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Ternana":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e95player)
                weigth = len(jugadores)
            else:
                jugadores = e95player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Brescia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e96player)
                weigth = len(jugadores)
            else:
                jugadores = e96player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Cittadella":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e97player)
                weigth = len(jugadores)
            else:
                jugadores = e97player 
                weigth = len(jugadores)
            gol =get_random_player6(jugadores,weigth)            
        elif club == "Cosenza":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e98player)
                weigth = len(jugadores)
            else:
                jugadores = e98player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)    
        elif club == "Perugia":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e99player)
                weigth = len(jugadores)
            else:
                jugadores = e99player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Spal":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e100player)
                weigth = len(jugadores)
            else:
                jugadores = e100player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth) 
        elif club == "Benevento":
            if len(jugadores_sancionados) != 0:
                jugadores = jugadores_sancionados_sacar(jugadores_sancionados,e101player)
                weigth = len(jugadores)
            else:
                jugadores = e101player 
                weigth = len(jugadores)
            gol = get_random_player6(jugadores,weigth)   
        goles_totales.append(gol)            
    numeros_aleatorios = random.sample(range(1,91), len(goles_totales))
    goles_totales.sort()
    numeros_aleatorios.sort()
    print(f'\U000026BD Goles {club}: '+', '.join([f'{gol} \u23f1 {num}\'' for gol, num in zip(goles_totales, numeros_aleatorios)]))


    return goles_totales 