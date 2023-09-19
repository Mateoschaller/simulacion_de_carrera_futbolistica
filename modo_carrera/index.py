import random
from tabulate import tabulate
import arch as taq
import json
import functions as fct

def sumar_gol(nombre_jugador):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador["goles"] += 1
            jugador["mvpcontrol"] += 2
            jugador["MVP"] += 2
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.5
            break
def sumar_asistencia(nombre_jugador):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador["asistencias"] += 1
            jugador["mvpcontrol"] += 1
            jugador["MVP"] += 1
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.25
            break        

def actualizar_rustico(nombre_jugador,ama,roja):
    if ama == 1:
        for jugador in jugadores:
            if jugador["nombre"] == nombre_jugador:
                jugador["amarillas"] += 1
                jugador["sancion"] += 1
                jugador["mvpcontrol"] -= 1
                jugador["MVP"] -= 1
                if jugador["sancion"] >= 3:
                    jugador["sancionado"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.25
    if roja == 1:  
        for jugador in jugadores:
            if jugador["nombre"] == nombre_jugador:
                jugador["rojas"] += 1    
                jugador["sancion"] = 3
                jugador["mvpcontrol"] -= 3
                jugador["MVP"] -= 3
                jugador["sancionado"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.5
def sancionados(club):
    jugadores_sancionados = []
    for jugador in jugadores:
        if jugador["equipo"] == club:
            if jugador["sancionado"] == True:
                sancionado = jugador["nombre"]
                jugadores_sancionados.append(sancionado)
            if jugador["nombre"] == nombre_del_jugador:
                if jugador["sancionado"] == False:
                    jugador["partidos"] +=1
    return jugadores_sancionados 
def desancionar(club):
    for jugador in jugadores:
        if jugador["equipo"] == club:
            jugador["sancionado"] = False

def actualizar_lesionados(nombre_jugador,duracion):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            if jugador["division"] == "champions":
                pass
            else:
                jugador["lesionado"] = True
                jugador["lesion"] = duracion

def lesionados(club):
    jugadores_lesionados = []
    for jugador in jugadores:
        if jugador["equipo"] == club:
            if jugador["lesionado"] == True:
                lesion = jugador["nombre"]
                jugadores_lesionados.append(lesion)
                if jugador["nombre"] == nombre_del_jugador:
                    if jugador["sancionado"] == False:
                        jugador["partidos"] -=1
    return jugadores_lesionados 

def deslesionar(club):
    for jugador in jugadores:
        if jugador["equipo"] == club:
            if jugador["lesion"] != 0:
                jugador["lesion"] -= 1
            if jugador["lesion"] == 0:
                jugador["lesionado"] = False

def sancionados_carabao(club):
    jugadores_sancionados = []
    for jugador in jugadores:
        if jugador["equipo"] == club:
            if jugador["sancionado_carabao"] == True:
                sancionado = jugador["nombre"]
                jugadores_sancionados.append(sancionado)
            if jugador["nombre"] == nombre_del_jugador:
                if jugador["sancionado_carabao"] == False:
                    jugador["partidos"] +=1
                
                
                
    return jugadores_sancionados 

def desancionar_carabao(club):
    for jugador in jugadores:
        if jugador["equipo"] == club:
            jugador["sancionado_carabao"] = False

def actualizar_rustico_carabao(nombre_jugador,ama,roja):
    if ama == 1:
        for jugador in jugadores:
            if jugador["nombre"] == nombre_jugador:
                jugador["amarillas_carabao"] += 1
                jugador["sancion_carabao"] += 1
                jugador["MVP"] -= 1
                if jugador["sancion_carabao"] >= 3:
                    jugador["sancionado_carabao"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.25
    if roja == 1:  
        for jugador in jugadores:
            if jugador["nombre"] == nombre_jugador:
                jugador["rojas_carabao"] += 1    
                jugador["sancion_carabao"] = 3
                jugador["MVP"] -= 3
                jugador["sancionado_carabao"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.5

def sumar_gol_carabao(nombre_jugador):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador["goles_carabao"] += 1
            jugador["MVP"] += 2
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.5
            break

def sumar_asistencia_carabao(nombre_jugador):
    for jugador in jugadores:
       if jugador["nombre"] == nombre_jugador:
           jugador["asistencias_carabao"] += 1
           jugador["MVP"] += 1
           if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.25
           break  

def goleadores_totales(division):
    if division == "p":
        division = "premier"
    elif division == "c":
        division = "championship" 
    elif division == "sa":
        division = "serie A"
    elif division == "sb":
        division = "serie B"  
    input("mostrar tabla de goleadores")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
def asistentes_totales(division):
    if division == "p":
        division = "premier"
    elif division == "c":
        division = "championship"    
    elif division == "sa":
        division = "serie A"
    elif division == "sb":
        division = "serie B"
    input("mostrar tabla de asistentes")  
    print("")
    contador = 0
    asistentes_ordenados = sorted(jugadores, key=lambda j: j["asistencias"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(asistentes_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("")        

def lesionados_totales(division):
    if division == "p":
        division = "premier"
    elif division == "c":
        division = "championship" 
    elif division == "sa":
        division = "serie A"
    elif division == "sb":
        division = "serie B"  
    input("mostrar tabla de lesionados")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["lesion"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['lesion']} - {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['lesion']} - {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 

def rojas_totales(division):
    if division == "p":
        division = "premier"
    elif division == "c":
        division = "championship"
    elif division == "sa":
        division = "serie A"
    elif division == "sb":
        division = "serie B"
    input("mostrar tabla de rojas")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["rojas"], reverse=True)
    import colorama
    colorama.init()
    contador = 0
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['rojas']} {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['rojas']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
def amarillas_totales(division):
    if division == "p":
        division = "premier"
    elif division == "c":
        division = "championship"  
    elif division == "sa":
        division = "serie A"
    elif division == "sb":
        division = "serie B"
    input("mostrar tabla de amarillas")  
    print("")
    asistentes_ordenados = sorted(jugadores, key=lambda j: j["amarillas"], reverse=True)
    import colorama
    colorama.init()
    contador = 0
    for i, j in enumerate(asistentes_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['amarillas']} {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['amarillas']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("")

def generar_partido(club1,club2,tabla):
    jugadores_sancionados_locales = sancionados(club1)
    jugadores_sancionados_visitantes = sancionados(club2)
    desancionar(club1)
    desancionar(club2)
    jugadores_lesionados_locales = lesionados(club1)
    jugadores_lesionados_visitantes = lesionados(club2)
    deslesionar(club1)
    deslesionar(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totales:
            sumar_gol(i)
        asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia(i)
    amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    rojas_locales = taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_locales) != 0:
        for i in lesionados_locales:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totalesv:
            sumar_gol(i)
        asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia(i)
    amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_visitantes) != 0:
        for i in lesionados_visitantes:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico(i,0,1) 
    if goallocal > goalsvisitor:
        fct.actualizar_tabla(tabla,club1,3,goallocal,goalsvisitor,1,0,0)
        fct.actualizar_tabla(tabla,club2,0,goalsvisitor,goallocal,0,0,1)
        sumar_ranking_club(club1,3)
        sumar_ranking_club(club2,0)
    elif goallocal < goalsvisitor:
        fct.actualizar_tabla(tabla,club1,0,goallocal,goalsvisitor,0,0,1)
        fct.actualizar_tabla(tabla,club2,3,goalsvisitor,goallocal,1,0,0)
        sumar_ranking_club(club1,0)
        sumar_ranking_club(club2,3)
    else:
        fct.actualizar_tabla(tabla,club1,1,goallocal,goalsvisitor,0,1,0)
        fct.actualizar_tabla(tabla,club2,1,goalsvisitor,goallocal,0,1,0)
        sumar_ranking_club(club1,1)
        sumar_ranking_club(club2,1)

def sumar_ranking_club(club,pts):
    for i in equipo_rankinkg:
        if i["nombre"] == club:
            i["partidos"] +=1 
            i["puntos"] += pts 
def sumar_ranking_selecion(club,pts):
    for i in selecciones_ranking:
        if i["nombre"] == club:
            i["partidos"] +=1 
            i["puntos"] += pts 

def resetear_tabla():
    Arsenal["tabla"] = {'Arsenal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Aston_Villa["tabla"] = {'Aston Villa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bournemouth["tabla"] = {'Bournemouth':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brentford["tabla"] = {'Brentford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brigthon["tabla"] = {'Brigthon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Chelsea["tabla"] = {'Chelsea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Crystal_Palace["tabla"] = {'Crystal Palace':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Everton["tabla"] = {'Everton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Fulham["tabla"] = {'Fulham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Leeds_United["tabla"] = {'Leeds United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Leicester_City["tabla"] = {'Leicester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Liverpool["tabla"] = {'Liverpool':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Manchester_City["tabla"] = {'Manchester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Manchester_United["tabla"] = {'Manchester United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Newcastle["tabla"] = {'Newcastle':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Nottingham_Forest["tabla"] = {'Nottingham Forest':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Southampton["tabla"] = {'Southampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Tottenham["tabla"] = {'Tottenham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    West_ham["tabla"] = {'West ham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Wolverhampton["tabla"] = {'Wolverhampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Burnley["tabla"] = {'Burnley':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sheffield_United["tabla"] = {'Sheffield United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Luton_Town["tabla"] = {'Luton Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Middlesbrough["tabla"] = {'Middlesbrough':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Coventry_City["tabla"] = {'Coventry City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sunderland["tabla"] = {'Sunderland':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Blackburn_Rovers["tabla"] = {'Blackburn Rovers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Millwall["tabla"] = {'Millwall':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    West_Bromwich_Albion["tabla"] = {'West Bromwich Albion':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Swansea["tabla"] = {'Swansea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Watford["tabla"] = {'Watford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Preston_North_End["tabla"] = {'Preston North End':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Norwich["tabla"] = {'Norwich':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bristol_City["tabla"] = {'Bristol City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Hull_City["tabla"] = {'Hull City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Stoke_City["tabla"] = {'Stoke City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Birmingham["tabla"] = {'Birmingham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Huddersfield_Town["tabla"] = {'Huddersfield Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cardiff_City["tabla"] = {'Cardiff City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Queens_Park_Rangers["tabla"] = {'Queens Park Rangers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    
    Napoli["tabla"] = {'Napoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Lazio["tabla"] = {'Lazio':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Inter["tabla"] = {'Inter':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Milan["tabla"] = {'Milan':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Atalanta["tabla"] = {'Atalanta':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Roma["tabla"] = {'Roma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Juventus["tabla"] = {'Juventus':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Fiorentina["tabla"] = {'Fiorentina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bologna["tabla"] = {'Bologna':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Torino["tabla"] = {'Torino':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Monza["tabla"] = {'Monza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Udinese["tabla"] = {'Udinese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sassuolo["tabla"] = {'Sassuolo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Empoli["tabla"] = {'Empoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Benevento["tabla"] = {'Benevento':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Salernitana["tabla"] = {'Salernitana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Lecce["tabla"] = {'Lecce':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Hellas_Verona["tabla"] = {'Hellas Verona':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Spezia["tabla"] = {'Spezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cremonese["tabla"] = {'Cremonese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sampdoria["tabla"] = {'Sampdoria':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Frosinone["tabla"] = {'Frosinone':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Genoa["tabla"] = {'Genoa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bari["tabla"] = {'Bari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Parma["tabla"] = {'Parma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cagliari["tabla"] = {'Cagliari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sudtirol["tabla"] = {'Sudtirol':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Reggina["tabla"] = {'Reggina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Venezia["tabla"] = {'Venezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Palermo["tabla"] = {'Palermo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Modena["tabla"] = {'Modena':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Pisa["tabla"] = {'Pisa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ascoli["tabla"] = {'Ascoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Como["tabla"] = {'Como':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ternana["tabla"] = {'Ternana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brescia["tabla"] = {'Brescia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cittadella["tabla"] = {'Cittadella':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cosenza["tabla"] = {'Cosenza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Perugia["tabla"] = {'Perugia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Spal["tabla"] = {'Spal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    
    Arsenal["tabla premier"] = {'Arsenal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Aston_Villa["tabla premier"] = {'Aston Villa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bournemouth["tabla premier"] = {'Bournemouth':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brentford["tabla premier"] = {'Brentford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brigthon["tabla premier"] = {'Brigthon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Chelsea["tabla premier"] = {'Chelsea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Crystal_Palace["tabla premier"] = {'Crystal Palace':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Everton["tabla premier"] = {'Everton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Fulham["tabla premier"] = {'Fulham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Leeds_United["tabla premier"] = {'Leeds United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Leicester_City["tabla premier"] = {'Leicester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Liverpool["tabla premier"] = {'Liverpool':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Manchester_City["tabla premier"] = {'Manchester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Manchester_United["tabla premier"] = {'Manchester United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Newcastle["tabla premier"] = {'Newcastle':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Nottingham_Forest["tabla premier"] = {'Nottingham Forest':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Southampton["tabla premier"] = {'Southampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Tottenham["tabla premier"] = {'Tottenham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    West_ham["tabla premier"] = {'West ham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Wolverhampton["tabla premier"] = {'Wolverhampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Burnley["tabla premier"] = {'Burnley':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sheffield_United["tabla premier"] = {'Sheffield United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Luton_Town["tabla premier"] = {'Luton Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Middlesbrough["tabla premier"] = {'Middlesbrough':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Coventry_City["tabla premier"] = {'Coventry City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sunderland["tabla premier"] = {'Sunderland':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Blackburn_Rovers["tabla premier"] = {'Blackburn Rovers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Millwall["tabla premier"] = {'Millwall':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    West_Bromwich_Albion["tabla premier"] = {'West Bromwich Albion':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Swansea["tabla premier"] = {'Swansea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Watford["tabla premier"] = {'Watford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Preston_North_End["tabla premier"] = {'Preston North End':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Norwich["tabla premier"] = {'Norwich':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bristol_City["tabla premier"] = {'Bristol City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Hull_City["tabla premier"] = {'Hull City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Stoke_City["tabla premier"] = {'Stoke City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Birmingham["tabla premier"] = {'Birmingham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Huddersfield_Town["tabla premier"] = {'Huddersfield Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cardiff_City["tabla premier"] = {'Cardiff City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Queens_Park_Rangers["tabla premier"] = {'Queens Park Rangers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    
    Napoli["tabla premier"] = {'Napoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Lazio["tabla premier"] = {'Lazio':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Inter["tabla premier"] = {'Inter':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Milan["tabla premier"] = {'Milan':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Atalanta["tabla premier"] = {'Atalanta':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Roma["tabla premier"] = {'Roma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Juventus["tabla premier"] = {'Juventus':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Fiorentina["tabla premier"] = {'Fiorentina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bologna["tabla premier"] = {'Bologna':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Torino["tabla premier"] = {'Torino':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Monza["tabla premier"] = {'Monza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Udinese["tabla premier"] = {'Udinese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sassuolo["tabla premier"] = {'Sassuolo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Empoli["tabla premier"] = {'Empoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Benevento["tabla premier"] = {'Benevento':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Salernitana["tabla premier"] = {'Salernitana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Lecce["tabla premier"] = {'Lecce':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Hellas_Verona["tabla premier"] = {'Hellas Verona':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Spezia["tabla premier"] = {'Spezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cremonese["tabla premier"] = {'Cremonese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sampdoria["tabla premier"] = {'Sampdoria':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Frosinone["tabla premier"] = {'Frosinone':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Genoa["tabla premier"] = {'Genoa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bari["tabla premier"] = {'Bari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Parma["tabla premier"] = {'Parma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cagliari["tabla premier"] = {'Cagliari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sudtirol["tabla premier"] = {'Sudtirol':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Reggina["tabla premier"] = {'Reggina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Venezia["tabla premier"] = {'Venezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Palermo["tabla premier"] = {'Palermo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Modena["tabla premier"] = {'Modena':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Pisa["tabla premier"] = {'Pisa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ascoli["tabla premier"] = {'Ascoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Como["tabla premier"] = {'Como':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ternana["tabla premier"] = {'Ternana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brescia["tabla premier"] = {'Brescia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cittadella["tabla premier"] = {'Cittadella':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cosenza["tabla premier"] = {'Cosenza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Perugia["tabla premier"] = {'Perugia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Spal["tabla premier"] = {'Spal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    
    Arsenal["tabla europa"] = {'Arsenal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Aston_Villa["tabla europa"] = {'Aston Villa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bournemouth["tabla europa"] = {'Bournemouth':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brentford["tabla europa"] = {'Brentford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brigthon["tabla europa"] = {'Brigthon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Chelsea["tabla europa"] = {'Chelsea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Crystal_Palace["tabla europa"] = {'Crystal Palace':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Everton["tabla europa"] = {'Everton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Fulham["tabla europa"] = {'Fulham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Leeds_United["tabla europa"] = {'Leeds United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Leicester_City["tabla europa"] = {'Leicester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Liverpool["tabla europa"] = {'Liverpool':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Manchester_City["tabla europa"] = {'Manchester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Manchester_United["tabla europa"] = {'Manchester United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Newcastle["tabla europa"] = {'Newcastle':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Nottingham_Forest["tabla europa"] = {'Nottingham Forest':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Southampton["tabla europa"] = {'Southampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Tottenham["tabla europa"] = {'Tottenham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    West_ham["tabla europa"] = {'West ham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Wolverhampton["tabla europa"] = {'Wolverhampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Burnley["tabla europa"] = {'Burnley':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sheffield_United["tabla europa"] = {'Sheffield United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Luton_Town["tabla europa"] = {'Luton Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Middlesbrough["tabla europa"] = {'Middlesbrough':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Coventry_City["tabla europa"] = {'Coventry City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sunderland["tabla europa"] = {'Sunderland':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Blackburn_Rovers["tabla europa"] = {'Blackburn Rovers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Millwall["tabla europa"] = {'Millwall':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    West_Bromwich_Albion["tabla europa"] = {'West Bromwich Albion':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Swansea["tabla europa"] = {'Swansea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Watford["tabla europa"] = {'Watford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Preston_North_End["tabla europa"] = {'Preston North End':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Norwich["tabla europa"] = {'Norwich':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bristol_City["tabla europa"] = {'Bristol City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Hull_City["tabla europa"] = {'Hull City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Stoke_City["tabla europa"] = {'Stoke City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Birmingham["tabla europa"] = {'Birmingham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Huddersfield_Town["tabla europa"] = {'Huddersfield Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cardiff_City["tabla europa"] = {'Cardiff City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Queens_Park_Rangers["tabla europa"] = {'Queens Park Rangers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Napoli["tabla europa"] = {'Napoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Lazio["tabla europa"] = {'Lazio':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Inter["tabla europa"] = {'Inter':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Milan["tabla europa"] = {'Milan':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Atalanta["tabla europa"] = {'Atalanta':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Roma["tabla europa"] = {'Roma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Juventus["tabla europa"] = {'Juventus':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Fiorentina["tabla europa"] = {'Fiorentina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bologna["tabla europa"] = {'Bologna':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Torino["tabla europa"] = {'Torino':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Monza["tabla europa"] = {'Monza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Udinese["tabla europa"] = {'Udinese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sassuolo["tabla europa"] = {'Sassuolo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Empoli["tabla europa"] = {'Empoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Benevento["tabla europa"] = {'Benevento':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Salernitana["tabla europa"] = {'Salernitana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Lecce["tabla europa"] = {'Lecce':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Hellas_Verona["tabla europa"] = {'Hellas Verona':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Spezia["tabla europa"] = {'Spezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cremonese["tabla europa"] = {'Cremonese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sampdoria["tabla europa"] = {'Sampdoria':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Frosinone["tabla europa"] = {'Frosinone':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Genoa["tabla europa"] = {'Genoa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bari["tabla europa"] = {'Bari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Parma["tabla europa"] = {'Parma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cagliari["tabla europa"] = {'Cagliari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sudtirol["tabla europa"] = {'Sudtirol':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Reggina["tabla europa"] = {'Reggina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Venezia["tabla europa"] = {'Venezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Palermo["tabla europa"] = {'Palermo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Modena["tabla europa"] = {'Modena':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Pisa["tabla europa"] = {'Pisa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ascoli["tabla europa"] = {'Ascoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Como["tabla europa"] = {'Como':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ternana["tabla europa"] = {'Ternana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brescia["tabla europa"] = {'Brescia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cittadella["tabla europa"] = {'Cittadella':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cosenza["tabla europa"] = {'Cosenza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Perugia["tabla europa"] = {'Perugia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Spal["tabla europa"] = {'Spal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    
    psv["tabla europa"] = {'PSV':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Frankfurt["tabla europa"] = {'Frankfurt':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Marsella["tabla europa"] = {'O.Marsella':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sporting_Lisboa["tabla europa"] = {'Sporting Lisboa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    B_Leverkusen["tabla europa"] = {'B.Leverkusen':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Sevilla["tabla europa"] = {'Sevilla':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Leipzig["tabla europa"] = {'Leipzig':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Monaco["tabla europa"] = {'Monaco':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Real_Sociedad["tabla europa"] = {'Real Sociedad':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brugge["tabla europa"] = {'Brugge':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    psg["tabla premier"] = {'PSG':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Barcelona["tabla premier"] = {'Barcelona':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Real_Madrid["tabla premier"] = {'Real Madrid':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    B_Dortmund["tabla premier"] = {'B.Dortmund':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bayern_Munich["tabla premier"] = {'Bayern Munich':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ajax["tabla premier"] = {'Ajax':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Shakhtar["tabla premier"] = {'Shakhtar':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Lyon["tabla premier"] = {'O.Lyon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Benfica["tabla premier"] = {'Benfica':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Atl_Madrid["tabla premier"] = {'Atl.Madrid':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    
    España["tabla"] = {'España':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Francia["tabla"] = {'Francia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Holanda["tabla"] = {'Holanda':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Inglaterra["tabla"] = {'Inglaterra':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Italia["tabla"] = {'Italia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Croacia["tabla"] = {'Croacia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Belgica["tabla"] = {'Belgica':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Portugal["tabla"] = {'Portugal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Suiza["tabla"] = {'Suiza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Dinamarca["tabla"] = {'Dinamarca':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Polonia["tabla"] = {'Polonia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Noruega["tabla"] = {'Noruega':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Alemania["tabla"] ={'Alemania':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Gales["tabla"] = {'Gales':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Serbia["tabla"] = {'Serbia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Suecia["tabla"] = {'Suecia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Argentina["tabla"] = {'Argentina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Uruguay["tabla"] = {'Uruguay':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Paraguay["tabla"] = {'Paraguay':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Chile["tabla"] = {'Chile':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Bolivia["tabla"] = {'Bolivia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Brasil["tabla"] = {'Brasil':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Peru["tabla"] = {'Peru':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Colombia["tabla"] = {'Colombia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ecuador["tabla"] = {'Ecuador':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Venezuela["tabla"] = {'Venezuela':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Mexico["tabla"] = {'Mexico':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Estados_Unidos["tabla"] = {'Estados Unidos':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Canada["tabla"] = {'Canada':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Costa_Rica["tabla"] = {'Costa Rica':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Cuba["tabla"] = {'Cuba':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Honduras["tabla"] ={'Honduras':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Iran["tabla"] = {'Iran':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Corea_del_Sur["tabla"] = {'Corea del Sur':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Japon["tabla"] = {'Japon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    China["tabla"] = {'China':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Arabia_Saudita["tabla"] ={'Arabia Saudita':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Israel["tabla"] = {'Israel':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Australia["tabla"] = {'Australia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Qatar["tabla"] = {'Qatar':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Egipto["tabla"] = {'Egipto':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Senegal["tabla"] = {'Senegal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Tunez["tabla"] = {'Tunez':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Camerun["tabla"] = {'Camerun':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Marruecos["tabla"] = {'Marruecos':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Nigeria["tabla"] = {'Nigeria':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Ghana["tabla"] ={'Ghana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}
    Argelia["tabla"] = {'Argelia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},}

    
    for jugador in jugadores:
        jugador["goles"] = 0
        jugador["asistencias"] = 0
        jugador["MVP"] = 0
        jugador["amarillas"] = 0
        jugador["rojas"] = 0
        jugador["sancion"] = 0
        jugador["sancionado"] = False
        jugador["MVP de la fecha"] = 0
        jugador["mvpcontrol"] = 0
        jugador["goles_carabao"] = 0
        jugador["amarillas_carabao"] = 0
        jugador["asistencias_carabao"] = 0
        jugador["rojas_carabao"] = 0
        jugador["sancion_carabao"] = False
        jugador["sancionado_champions"] = False
        jugador["goles_champions"] = 0
        jugador["asistencias_champions"] = 0
        jugador["sancion_champions"] = 0
        jugador["rojas_champions"] = 0
        jugador["amarillas_champions"] = 0
        jugador["sancionado_europa"] = False
        jugador["goles_europa"] = 0
        jugador["asistencias_europa"] = 0
        jugador["sancion_europa"] = 0
        jugador["rojas_europa"] = 0
        jugador["amarillas_europa"] = 0
        jugador["lesion"] = 0
        jugador["lesionado"] = False
        
    for jugador in jugadores_selecciones:
        jugador["goles"] = 0
        jugador["asistencias"] = 0
        jugador["amarillas"] = 0
        jugador["rojas"] = 0
        jugador["sancion"] = 0
        jugador["sancionado"] = False
        
def actualizar_jugadores_divisiones(club,division):
    if division == "p":
        divisione = "premier"
    if division == "c":
        divisione = "championship"    
    if division == "sb":
        divisione = "serie A"
    if division == "sa":
        divisione = "serie B"  
    for jugador in jugadores:
        if jugador["equipo"] == club:
            jugador["division"] = divisione

def divisionacomodar(tabla_premier,tabla_championship):
    sky_by_championship_equipos = []
    premier_league_equipos = []
    equipos_ordenados = sorted(tabla_premier, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        club = list(equipo.keys())[0]
        if i <= 17:
            if club == "Arsenal":
                premier_league_equipos.append(Arsenal)
            elif club == "Aston Villa":
                premier_league_equipos.append(Aston_Villa)
            elif club == "Bournemouth":
                premier_league_equipos.append(Bournemouth)
            elif club == "Brentford":
                premier_league_equipos.append(Brentford)
            elif club == "Brigthon":
                premier_league_equipos.append(Brigthon)
            elif club == "Chelsea":
                premier_league_equipos.append(Chelsea)
            elif club == "Crystal Palace":
                premier_league_equipos.append(Crystal_Palace)
            elif club == "Everton":
                premier_league_equipos.append(Everton)
            elif club == "Fulham":
                premier_league_equipos.append(Fulham)
            elif club == "Leeds United":
                premier_league_equipos.append(Leeds_United)
            elif club == "Leicester City":
                premier_league_equipos.append(Leicester_City)
            elif club == "Liverpool":
                premier_league_equipos.append(Liverpool)
            elif club == "Manchester City":
                premier_league_equipos.append(Manchester_City)
            elif club == "Manchester United":
                premier_league_equipos.append(Manchester_United)
            elif club == "Newcastle":
                premier_league_equipos.append(Newcastle)
            elif club == "Nottingham Forest":
                premier_league_equipos.append(Nottingham_Forest)
            elif club == "Southampton":
                premier_league_equipos.append(Southampton)
            elif club == "Tottenham":
                premier_league_equipos.append(Tottenham)
            elif club == "West ham":
                premier_league_equipos.append(West_ham)
            elif club == "Wolverhampton":
                premier_league_equipos.append(Wolverhampton)
            elif club == "Burnley":
                premier_league_equipos.append(Burnley)
            elif club == "Sheffield United":
                premier_league_equipos.append(Sheffield_United)
            elif club == "Luton Town":
                premier_league_equipos.append(Luton_Town)
            elif club == "Middlesbrough":
                premier_league_equipos.append(Middlesbrough)
            elif club == "Coventry City":
                premier_league_equipos.append(Coventry_City)
            elif club == "Sunderland":
                premier_league_equipos.append(Sunderland)
            elif club == "Blackburn Rovers":
                premier_league_equipos.append(Blackburn_Rovers)     
            elif club == "Millwall":
                premier_league_equipos.append(Millwall)
            elif club == "West Bromwich Albion":
                premier_league_equipos.append(West_Bromwich_Albion)   
            elif club == "Swansea":
                premier_league_equipos.append(Swansea)
            elif club == "Watford":
                premier_league_equipos.append(Watford)  
            elif club == "Preston North End":
                premier_league_equipos.append(Preston_North_End)      
            elif club == "Norwich":
                premier_league_equipos.append(Norwich)              
            elif club == "Bristol City":
                premier_league_equipos.append(Bristol_City)
            elif club == "Hull City":
                premier_league_equipos.append(Hull_City)   
            elif club == "Stoke City":
                premier_league_equipos.append(Stoke_City)      
            elif club == "Birmingham":
                premier_league_equipos.append(Birmingham)   
            elif club == "Huddersfield Town":
                premier_league_equipos.append(Huddersfield_Town)
            elif club == "Cardiff City":
                premier_league_equipos.append(Cardiff_City)  
            elif club == "Queens Park Rangers":
                premier_league_equipos.append(Queens_Park_Rangers)
        else:
            if club == "Arsenal":
                sky_by_championship_equipos.append(Arsenal)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Aston Villa":
                sky_by_championship_equipos.append(Aston_Villa)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Bournemouth":
                sky_by_championship_equipos.append(Bournemouth)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Brentford":
                sky_by_championship_equipos.append(Brentford)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Brigthon":
                sky_by_championship_equipos.append(Brigthon)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Chelsea":
                sky_by_championship_equipos.append(Chelsea)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Crystal Palace":
                sky_by_championship_equipos.append(Crystal_Palace)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Everton":
                sky_by_championship_equipos.append(Everton)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Fulham":
                sky_by_championship_equipos.append(Fulham)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Leeds United":
                sky_by_championship_equipos.append(Leeds_United)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Leicester City":
                sky_by_championship_equipos.append(Leicester_City)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Liverpool":
                sky_by_championship_equipos.append(Liverpool)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Manchester City":
                sky_by_championship_equipos.append(Manchester_City)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Manchester United":
                sky_by_championship_equipos.append(Manchester_United)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Newcastle":
                sky_by_championship_equipos.append(Newcastle)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Nottingham Forest":
                sky_by_championship_equipos.append(Nottingham_Forest)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Southampton":
                sky_by_championship_equipos.append(Southampton)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Tottenham":
                sky_by_championship_equipos.append(Tottenham)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "West ham":
                sky_by_championship_equipos.append(West_ham)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Wolverhampton":
                sky_by_championship_equipos.append(Wolverhampton)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Burnley":
                sky_by_championship_equipos.append(Burnley)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Sheffield United":
                sky_by_championship_equipos.append(Sheffield_United)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Luton Town":
                sky_by_championship_equipos.append(Luton_Town)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Middlesbrough":
                sky_by_championship_equipos.append(Middlesbrough)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Coventry City":
                sky_by_championship_equipos.append(Coventry_City)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Sunderland":
                sky_by_championship_equipos.append(Sunderland)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Blackburn Rovers":
                sky_by_championship_equipos.append(Blackburn_Rovers)    
                actualizar_jugadores_divisiones(club,"c") 
            elif club == "Millwall":
                sky_by_championship_equipos.append(Millwall)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "West Bromwich Albion":
                sky_by_championship_equipos.append(West_Bromwich_Albion) 
                actualizar_jugadores_divisiones(club,"c")  
            elif club == "Swansea":
                sky_by_championship_equipos.append(Swansea)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Watford":
                sky_by_championship_equipos.append(Watford)  
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Preston North End":
                sky_by_championship_equipos.append(Preston_North_End)    
                actualizar_jugadores_divisiones(club,"c")  
            elif club == "Norwich":
                sky_by_championship_equipos.append(Norwich)       
                actualizar_jugadores_divisiones(club,"c")       
            elif club == "Bristol City":
                sky_by_championship_equipos.append(Bristol_City)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Hull City":
                sky_by_championship_equipos.append(Hull_City)   
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Stoke City":
                sky_by_championship_equipos.append(Stoke_City)     
                actualizar_jugadores_divisiones(club,"c") 
            elif club == "Birmingham":
                sky_by_championship_equipos.append(Birmingham)   
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Huddersfield Town":
                sky_by_championship_equipos.append(Huddersfield_Town)
                actualizar_jugadores_divisiones(club,"c")
            elif club == "Cardiff City":
                sky_by_championship_equipos.append(Cardiff_City) 
                actualizar_jugadores_divisiones(club,"c") 
            elif club == "Queens Park Rangers":
                sky_by_championship_equipos.append(Queens_Park_Rangers)
                actualizar_jugadores_divisiones(club,"c")
    equipos_ordenados = sorted(tabla_championship, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        club = list(equipo.keys())[0]    
        if i >= 4:
            if club == "Arsenal":
                sky_by_championship_equipos.append(Arsenal)
            elif club == "Aston Villa":
                sky_by_championship_equipos.append(Aston_Villa)
            elif club == "Bournemouth":
                sky_by_championship_equipos.append(Bournemouth)
            elif club == "Brentford":
                sky_by_championship_equipos.append(Brentford)
            elif club == "Brigthon":
                sky_by_championship_equipos.append(Brigthon)
            elif club == "Chelsea":
                sky_by_championship_equipos.append(Chelsea)
            elif club == "Crystal Palace":
                sky_by_championship_equipos.append(Crystal_Palace)
            elif club == "Everton":
                sky_by_championship_equipos.append(Everton)
            elif club == "Fulham":
                sky_by_championship_equipos.append(Fulham)
            elif club == "Leeds United":
                sky_by_championship_equipos.append(Leeds_United)
            elif club == "Leicester City":
                sky_by_championship_equipos.append(Leicester_City)
            elif club == "Liverpool":
                sky_by_championship_equipos.append(Liverpool)
            elif club == "Manchester City":
                sky_by_championship_equipos.append(Manchester_City)
            elif club == "Manchester United":
                sky_by_championship_equipos.append(Manchester_United)
            elif club == "Newcastle":
                sky_by_championship_equipos.append(Newcastle)
            elif club == "Nottingham Forest":
                sky_by_championship_equipos.append(Nottingham_Forest)
            elif club == "Southampton":
                sky_by_championship_equipos.append(Southampton)
            elif club == "Tottenham":
                sky_by_championship_equipos.append(Tottenham)
            elif club == "West ham":
                sky_by_championship_equipos.append(West_ham)
            elif club == "Wolverhampton":
                sky_by_championship_equipos.append(Wolverhampton)
            elif club == "Burnley":
                sky_by_championship_equipos.append(Burnley)
            elif club == "Sheffield United":
                sky_by_championship_equipos.append(Sheffield_United)
            elif club == "Luton Town":
                sky_by_championship_equipos.append(Luton_Town)
            elif club == "Middlesbrough":
                sky_by_championship_equipos.append(Middlesbrough)
            elif club == "Coventry City":
                sky_by_championship_equipos.append(Coventry_City)
            elif club == "Sunderland":
                sky_by_championship_equipos.append(Sunderland)
            elif club == "Blackburn Rovers":
                sky_by_championship_equipos.append(Blackburn_Rovers)     
            elif club == "Millwall":
                sky_by_championship_equipos.append(Millwall)
            elif club == "West Bromwich Albion":
                sky_by_championship_equipos.append(West_Bromwich_Albion)   
            elif club == "Swansea":
                sky_by_championship_equipos.append(Swansea)
            elif club == "Watford":
                sky_by_championship_equipos.append(Watford)  
            elif club == "Preston North End":
                sky_by_championship_equipos.append(Preston_North_End)      
            elif club == "Norwich":
                sky_by_championship_equipos.append(Norwich)              
            elif club == "Bristol City":
                sky_by_championship_equipos.append(Bristol_City)
            elif club == "Hull City":
                sky_by_championship_equipos.append(Hull_City)   
            elif club == "Stoke City":
                sky_by_championship_equipos.append(Stoke_City)      
            elif club == "Birmingham":
                sky_by_championship_equipos.append(Birmingham)   
            elif club == "Huddersfield Town":
                sky_by_championship_equipos.append(Huddersfield_Town)
            elif club == "Cardiff City":
                sky_by_championship_equipos.append(Cardiff_City)  
            elif club == "Queens Park Rangers":
                sky_by_championship_equipos.append(Queens_Park_Rangers)
        else:
            if club == "Arsenal":
                premier_league_equipos.append(Arsenal)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Aston Villa":
                premier_league_equipos.append(Aston_Villa)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Bournemouth":
                premier_league_equipos.append(Bournemouth)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Brentford":
                premier_league_equipos.append(Brentford)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Brigthon":
                premier_league_equipos.append(Brigthon)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Chelsea":
                premier_league_equipos.append(Chelsea)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Crystal Palace":
                premier_league_equipos.append(Crystal_Palace)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Everton":
                premier_league_equipos.append(Everton)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Fulham":
                premier_league_equipos.append(Fulham)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Leeds United":
                premier_league_equipos.append(Leeds_United)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Leicester City":
                premier_league_equipos.append(Leicester_City)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Liverpool":
                premier_league_equipos.append(Liverpool)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Manchester City":
                premier_league_equipos.append(Manchester_City)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Manchester United":
                premier_league_equipos.append(Manchester_United)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Newcastle":
                premier_league_equipos.append(Newcastle)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Nottingham Forest":
                premier_league_equipos.append(Nottingham_Forest)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Southampton":
                premier_league_equipos.append(Southampton)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Tottenham":
                premier_league_equipos.append(Tottenham)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "West ham":
                premier_league_equipos.append(West_ham)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Wolverhampton":
                premier_league_equipos.append(Wolverhampton)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Burnley":
                premier_league_equipos.append(Burnley)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Sheffield United":
                premier_league_equipos.append(Sheffield_United)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Luton Town":
                premier_league_equipos.append(Luton_Town)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Middlesbrough":
                premier_league_equipos.append(Middlesbrough)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Coventry City":
                premier_league_equipos.append(Coventry_City)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Sunderland":
                premier_league_equipos.append(Sunderland)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Blackburn Rovers":
                premier_league_equipos.append(Blackburn_Rovers)  
                actualizar_jugadores_divisiones(club,"p")   
            elif club == "Millwall":
                premier_league_equipos.append(Millwall)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "West Bromwich Albion":
                premier_league_equipos.append(West_Bromwich_Albion) 
                actualizar_jugadores_divisiones(club,"p")  
            elif club == "Swansea":
                premier_league_equipos.append(Swansea)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Watford":
                premier_league_equipos.append(Watford)  
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Preston North End":
                premier_league_equipos.append(Preston_North_End)     
                actualizar_jugadores_divisiones(club,"p") 
            elif club == "Norwich":
                premier_league_equipos.append(Norwich)          
                actualizar_jugadores_divisiones(club,"p")    
            elif club == "Bristol City":
                premier_league_equipos.append(Bristol_City)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Hull City":
                premier_league_equipos.append(Hull_City)   
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Stoke City":
                premier_league_equipos.append(Stoke_City)    
                actualizar_jugadores_divisiones(club,"p")  
            elif club == "Birmingham":
                premier_league_equipos.append(Birmingham)   
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Huddersfield Town":
                premier_league_equipos.append(Huddersfield_Town)
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Cardiff City":
                premier_league_equipos.append(Cardiff_City)  
                actualizar_jugadores_divisiones(club,"p")
            elif club == "Queens Park Rangers":
                premier_league_equipos.append(Queens_Park_Rangers)
                actualizar_jugadores_divisiones(club,"p")
    return sky_by_championship_equipos,premier_league_equipos     

def divisionacomodar_i(tabla_serieA,tabla_serieB):
    serieA_equipos = []
    serieB_equipos = []
    equipos_ordenados = sorted(tabla_serieA, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        club = list(equipo.keys())[0]
        if i <= 17:
            if club == "Napoli":
                serieA_equipos.append(Napoli)
            elif club == "Lazio":
                serieA_equipos.append(Lazio)
            elif club == "Inter":
                serieA_equipos.append(Inter)
            elif club == "Milan":
                serieA_equipos.append(Milan)
            elif club == "Atalanta":
                serieA_equipos.append(Atalanta)
            elif club == "Roma":
                serieA_equipos.append(Roma)
            elif club == "Juventus":
                serieA_equipos.append(Juventus)
            elif club == "Fiorentina":
                serieA_equipos.append(Fiorentina)
            elif club == "Bologna":
                serieA_equipos.append(Bologna)
            elif club == "Torino":
                serieA_equipos.append(Torino)
            elif club == "Monza":
                serieA_equipos.append(Monza)
            elif club == "Sassuolo":
                serieA_equipos.append(Sassuolo)
            elif club == "Udinese":
                serieA_equipos.append(Udinese)
            elif club == "Empoli":
                serieA_equipos.append(Empoli)
            elif club == "Salernitana":
                serieA_equipos.append(Salernitana)
            elif club == "Lecce":
                serieA_equipos.append(Lecce)
            elif club == "Hellas Verona":
                serieA_equipos.append(Hellas_Verona)
            elif club == "Spezia":
                serieA_equipos.append(Spezia)
            elif club == "Cremonese":
                serieA_equipos.append(Cremonese)
            elif club == "Sampdoria":
                serieA_equipos.append(Sampdoria)
            elif club == "Frosinone":
                serieA_equipos.append(Frosinone)
            elif club == "Genoa":
                serieA_equipos.append(Genoa)
            elif club == "Bari":
                serieA_equipos.append(Bari)
            elif club == "Parma":
                serieA_equipos.append(Parma)
            elif club == "Cagliari":
                serieA_equipos.append(Cagliari)
            elif club == "Sudtirol":
                serieA_equipos.append(Sudtirol)
            elif club == "Reggina":
                serieA_equipos.append(Reggina)     
            elif club == "Venezia":
                serieA_equipos.append(Venezia)
            elif club == "Palermo":
                serieA_equipos.append(Palermo)   
            elif club == "Modena":
                serieA_equipos.append(Modena)
            elif club == "Pisa":
                serieA_equipos.append(Pisa)  
            elif club == "Ascoli":
                serieA_equipos.append(Ascoli)      
            elif club == "Como":
                serieA_equipos.append(Como)              
            elif club == "Ternana":
                serieA_equipos.append(Ternana)
            elif club == "Brescia":
                serieA_equipos.append(Brescia)   
            elif club == "Cittadella":
                serieA_equipos.append(Cittadella)      
            elif club == "Cosenza":
                serieA_equipos.append(Cosenza)   
            elif club == "Spal":
                serieA_equipos.append(Spal)
            elif club == "Perugia":
                serieA_equipos.append(Perugia)  
            elif club == "Benevento":
                serieA_equipos.append(Benevento)
        else:
            if club == "Napoli":
                serieB_equipos.append(Napoli)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Lazio":
                serieB_equipos.append(Lazio)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Inter":
                serieB_equipos.append(Inter)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Milan":
                serieB_equipos.append(Milan)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Monza":
                serieB_equipos.append(Monza)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Atalanta":
                serieB_equipos.append(Atalanta)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Roma":
                serieB_equipos.append(Roma)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Juventus":
                serieB_equipos.append(Juventus)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Fiorentina":
                serieB_equipos.append(Fiorentina)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Bologna":
                serieB_equipos.append(Bologna)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Torino":
                serieB_equipos.append(Torino)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Udinese":
                serieB_equipos.append(Udinese)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Sassuolo":
                serieB_equipos.append(Sassuolo)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Empoli":
                serieB_equipos.append(Empoli)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Salernitana":
                serieB_equipos.append(Salernitana)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Lecce":
                serieB_equipos.append(Lecce)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Hellas Verona":
                serieB_equipos.append(Hellas_Verona)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Spezia":
                serieB_equipos.append(Spezia)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Cremonese":
                serieB_equipos.append(Cremonese)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Sampdoria":
                serieB_equipos.append(Sampdoria)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Frosinone":
                serieB_equipos.append(Frosinone)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Genoa":
                serieB_equipos.append(Genoa)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Bari":
                serieB_equipos.append(Bari)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Parma":
                serieB_equipos.append(Parma)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Cagliari":
                serieB_equipos.append(Cagliari)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Sudtirol":
                serieB_equipos.append(Sudtirol)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Reggina":
                serieB_equipos.append(Reggina)    
                actualizar_jugadores_divisiones(club,"sa") 
            elif club == "Venezia":
                serieB_equipos.append(Venezia)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Palermo":
                serieB_equipos.append(Palermo) 
                actualizar_jugadores_divisiones(club,"sa")  
            elif club == "Modena":
                serieB_equipos.append(Modena)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Pisa":
                serieB_equipos.append(Pisa)  
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Ascoli":
                serieB_equipos.append(Ascoli)    
                actualizar_jugadores_divisiones(club,"sa")  
            elif club == "Como":
                serieB_equipos.append(Como)       
                actualizar_jugadores_divisiones(club,"sa")       
            elif club == "Ternana":
                serieB_equipos.append(Ternana)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Brescia":
                serieB_equipos.append(Brescia)   
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Cittadella":
                serieB_equipos.append(Cittadella)     
                actualizar_jugadores_divisiones(club,"sa") 
            elif club == "Cosenza":
                serieB_equipos.append(Cosenza)   
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Perugia":
                serieB_equipos.append(Perugia)
                actualizar_jugadores_divisiones(club,"sa")
            elif club == "Spal":
                serieB_equipos.append(Spal) 
                actualizar_jugadores_divisiones(club,"sa") 
            elif club == "Benevento":
                serieB_equipos.append(Benevento)
                actualizar_jugadores_divisiones(club,"sa")
    equipos_ordenados = sorted(tabla_serieB, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        club = list(equipo.keys())[0]    
        if i >= 4:
            if club == "Napoli":
                serieB_equipos.append(Napoli)
            elif club == "Lazio":
                serieB_equipos.append(Lazio)
            elif club == "Inter":
                serieB_equipos.append(Inter)
            elif club == "Milan":
                serieB_equipos.append(Milan)
            elif club == "Atalanta":
                serieB_equipos.append(Atalanta)
            elif club == "Roma":
                serieB_equipos.append(Roma)
            elif club == "Juventus":
                serieB_equipos.append(Juventus)
            elif club == "Fiorentina":
                serieB_equipos.append(Fiorentina)
            elif club == "Bologna":
                serieB_equipos.append(Bologna)
            elif club == "Torino":
                serieB_equipos.append(Torino)
            elif club == "Monza":
                serieB_equipos.append(Monza)
            elif club == "Sassuolo":
                serieB_equipos.append(Sassuolo)
            elif club == "Udinese":
                serieB_equipos.append(Udinese)
            elif club == "Empoli":
                serieB_equipos.append(Empoli)
            elif club == "Salernitana":
                serieB_equipos.append(Salernitana)
            elif club == "Lecce":
                serieB_equipos.append(Lecce)
            elif club == "Hellas Verona":
                serieB_equipos.append(Hellas_Verona)
            elif club == "Spezia":
                serieB_equipos.append(Spezia)
            elif club == "Cremonese":
                serieB_equipos.append(Cremonese)
            elif club == "Sampdoria":
                serieB_equipos.append(Sampdoria)
            elif club == "Frosinone":
                serieB_equipos.append(Frosinone)
            elif club == "Genoa":
                serieB_equipos.append(Genoa)
            elif club == "Bari":
                serieB_equipos.append(Bari)
            elif club == "Parma":
                serieB_equipos.append(Parma)
            elif club == "Cagliari":
                serieB_equipos.append(Cagliari)
            elif club == "Sudtirol":
                serieB_equipos.append(Sudtirol)
            elif club == "Reggina":
                serieB_equipos.append(Reggina)     
            elif club == "Venezia":
                serieB_equipos.append(Venezia)
            elif club == "Palermo":
                serieB_equipos.append(Palermo)   
            elif club == "Modena":
                serieB_equipos.append(Modena)
            elif club == "Pisa":
                serieB_equipos.append(Pisa)  
            elif club == "Ascoli":
                serieB_equipos.append(Ascoli)      
            elif club == "Como":
                serieB_equipos.append(Como)              
            elif club == "Ternana":
                serieB_equipos.append(Ternana)
            elif club == "Brescia":
                serieB_equipos.append(Brescia)   
            elif club == "Cittadella":
                serieB_equipos.append(Cittadella)      
            elif club == "Cosenza":
                serieB_equipos.append(Cosenza)   
            elif club == "Spal":
                serieB_equipos.append(Spal)
            elif club == "Perugia":
                serieB_equipos.append(Perugia)  
            elif club == "Benevento":
                serieB_equipos.append(Benevento)
        else:
            if club == "Napoli":
                serieA_equipos.append(Napoli)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Lazio":
                serieA_equipos.append(Lazio)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Inter":
                serieA_equipos.append(Inter)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Milan":
                serieA_equipos.append(Milan)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Monza":
                serieA_equipos.append(Monza)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Atalanta":
                serieA_equipos.append(Atalanta)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Roma":
                serieA_equipos.append(Roma)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Juventus":
                serieA_equipos.append(Juventus)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Fiorentina":
                serieA_equipos.append(Fiorentina)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Bologna":
                serieA_equipos.append(Bologna)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Torino":
                serieA_equipos.append(Torino)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Udinese":
                serieA_equipos.append(Udinese)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Sassuolo":
                serieA_equipos.append(Sassuolo)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Empoli":
                serieA_equipos.append(Empoli)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Salernitana":
                serieA_equipos.append(Salernitana)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Lecce":
                serieA_equipos.append(Lecce)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Hellas Verona":
                serieA_equipos.append(Hellas_Verona)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Spezia":
                serieA_equipos.append(Spezia)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Cremonese":
                serieA_equipos.append(Cremonese)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Sampdoria":
                serieA_equipos.append(Sampdoria)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Frosinone":
                serieA_equipos.append(Frosinone)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Genoa":
                serieA_equipos.append(Genoa)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Bari":
                serieA_equipos.append(Bari)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Parma":
                serieA_equipos.append(Parma)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Cagliari":
                serieA_equipos.append(Cagliari)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Sudtirol":
                serieA_equipos.append(Sudtirol)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Reggina":
                serieA_equipos.append(Reggina)    
                actualizar_jugadores_divisiones(club,"sb") 
            elif club == "Venezia":
                serieA_equipos.append(Venezia)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Palermo":
                serieA_equipos.append(Palermo) 
                actualizar_jugadores_divisiones(club,"sb")  
            elif club == "Modena":
                serieA_equipos.append(Modena)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Pisa":
                serieA_equipos.append(Pisa)  
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Ascoli":
                serieA_equipos.append(Ascoli)    
                actualizar_jugadores_divisiones(club,"sb")  
            elif club == "Como":
                serieA_equipos.append(Como)       
                actualizar_jugadores_divisiones(club,"sb")       
            elif club == "Ternana":
                serieA_equipos.append(Ternana)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Brescia":
                serieA_equipos.append(Brescia)   
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Cittadella":
                serieA_equipos.append(Cittadella)     
                actualizar_jugadores_divisiones(club,"sb") 
            elif club == "Cosenza":
                serieA_equipos.append(Cosenza)   
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Perugia":
                serieA_equipos.append(Perugia)
                actualizar_jugadores_divisiones(club,"sb")
            elif club == "Spal":
                serieA_equipos.append(Spal) 
                actualizar_jugadores_divisiones(club,"sb") 
            elif club == "Benevento":
                serieA_equipos.append(Benevento)
                actualizar_jugadores_divisiones(club,"sb")
    return serieA_equipos,serieB_equipos     

def playoff_carabao(club1,club2):
    print("")
    input("")
    jugadores_sancionados_locales = sancionados_carabao(club1)
    jugadores_sancionados_visitantes = sancionados_carabao(club2)
    desancionar_carabao(club1)
    desancionar_carabao(club2)
    jugadores_lesionados_locales = lesionados(club1)
    jugadores_lesionados_visitantes = lesionados(club2)
    deslesionar(club1)
    deslesionar(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totales:
            sumar_gol_carabao(i)
        asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_carabao(i)
    amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    rojas_locales = taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_locales) != 0:
        for i in lesionados_locales:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_carabao(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_carabao(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totalesv:
            sumar_gol_carabao(i)
        asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_carabao(i)
    amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_visitantes) != 0:
        for i in lesionados_visitantes:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_carabao(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_carabao(i,0,1) 
    if goallocal > goalsvisitor:
        ganador = club1
        sumar_ranking_club(club1,3)
        sumar_ranking_club(club2,0)
    elif goallocal < goalsvisitor:
        ganador = club2
        sumar_ranking_club(club1,0)
        sumar_ranking_club(club2,3)
    else:
        
        sumar_ranking_club(club1,1)
        sumar_ranking_club(club2,1)
        print("PENALES")
        input("")
        penaleslocal = fct.numero_random()
        penales_visitor = fct.numero_random()
        if penaleslocal == penales_visitor:
            penales_visitor -= 1
        print(f'{club1} {penaleslocal}-{penales_visitor} {club2}')
        if penaleslocal > penales_visitor:
            ganador = club1
        else: ganador = club2    
    return ganador

def mostrar_datos_carabao():   
    jugadores_carabao = [j for j in jugadores if j["division"] in ["premier", "championship"]]
    input("mostrar la tabla de los goleadores de la carabao cup")
    print("")
    print("Tabla de goleadores de la carabao cup")
    print("")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["goles_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['goles_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['goles_carabao']} {j['nombre']} - {j['equipo']}")
    input("mostrar tabla de asistentes de la carabao cup")
    print("")
    print("Tabla de asistentes de la carabao cup")
    print("")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["asistencias_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['asistencias_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['asistencias_carabao']} {j['nombre']} - {j['equipo']}")
    input("mostrar tabla de amarillas de la carabao cup")  
    print("")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["amarillas_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['amarillas_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['amarillas_carabao']} {j['nombre']} - {j['equipo']}")
    print("")
    input("mostrar tabla de rojas de la carabao cup")  
    print("")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["rojas_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['rojas_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['rojas_carabao']} {j['nombre']} - {j['equipo']}")

def mostrar_datos_copa_italia():   
    jugadores_carabao = [j for j in jugadores if j["division"] in ["serie A", "serie B"]]
    input("mostrar la tabla de los goleadores de la Copa Italia")
    print("")
    print("Tabla de goleadores de la Copa Italia")
    print("")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["goles_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['goles_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['goles_carabao']} {j['nombre']} - {j['equipo']}")
    input("mostrar tabla de asistentes de la Copa Italia")
    print("")
    print("Tabla de asistentes de la Copa Italia")
    print("")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["asistencias_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['asistencias_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['asistencias_carabao']} {j['nombre']} - {j['equipo']}")
    input("mostrar tabla de amarillas de la Copa Italia")  
    print("")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["amarillas_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['amarillas_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['amarillas_carabao']} {j['nombre']} - {j['equipo']}")
    print("")
    input("mostrar tabla de rojas de la Copa Italia")  
    print("")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["rojas_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['rojas_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['rojas_carabao']} {j['nombre']} - {j['equipo']}")

def mostrar_campeones_totales():
    input("")
    print("campeones de la premier league")
    contador_premier = 2022
    for i in campeones_premier:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la championship")
    contador_premier = 2022 
    for i in campeones_championship:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la carabao cup")
    contador_premier = 2022 
    for i in campeones_carabao:
        contador_premier += 1
        print(f"{contador_premier}. {i}")  
    input("")
    print("campeones de la community")
    contador_premier = 2022 
    for i in campeones_comunity:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la Serie A")
    contador_premier = 2022
    for i in campeones_serieA:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la Serie B")
    contador_premier = 2022 
    for i in campeones_serieB:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la Copa Italia")
    contador_premier = 2022 
    for i in campeones_copa_italia:
        contador_premier += 1
        print(f"{contador_premier}. {i}")  
    input("")
    print("campeones de la Recopa Italiana")
    contador_premier = 2022 
    for i in campeones_recopa_italia:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la champions league")
    contador_premier = 2022 
    for i in campeones_champions:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la europa league")
    contador_premier = 2022 
    for i in campeones_europa:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la recopa de europa")
    contador_premier = 2022 
    for i in campeones_recopa:
        contador_premier += 1
        print(f"{contador_premier}. {i}")
    input("")
    print("campeones de la eurocpa")
    print(f'''
2023. {campeon_eurocopa1}
2025. {campeon_eurocopa2}
2027. {campeon_eurocopa3}
2029. {campeon_eurocopa4}
2031. {campeon_eurocopa5}
2033. {campeon_eurocopa6}
2035. {campeon_eurocopa7}
2037. {campeon_eurocopa8}
2039. {campeon_eurocopa9}
2041. {campeon_eurocopa10}
''')
    input("")
    print("campeones de la copa america")
    print(f'''
2023. {campeon_copa_america1}
2025. {campeon_copa_america2}
2027. {campeon_copa_america3}
2029. {campeon_copa_america4}
2031. {campeon_copa_america5}
2033. {campeon_copa_america6}
2035. {campeon_copa_america7}
2037. {campeon_copa_america8}
2039. {campeon_copa_america9}
2041. {campeon_copa_america10}
''')
    
    input("")
    print("campeones de la copa asiatica")
    print(f'''
2023. {campeon_copa_asia1}
2025. {campeon_copa_asia2}
2027. {campeon_copa_asia3}
2029. {campeon_copa_asia4}
2031. {campeon_copa_asia5}
2033. {campeon_copa_asia6}
2035. {campeon_copa_asia7}
2037. {campeon_copa_asia8}
2039. {campeon_copa_asia9}
2041. {campeon_copa_asia10}
''')
    
    input("")
    print("campeones de la copa africana")
    print(f'''
2023. {campeon_copa_africa1}
2025. {campeon_copa_africa2}
2027. {campeon_copa_africa3}
2029. {campeon_copa_africa4}
2031. {campeon_copa_africa5}
2033. {campeon_copa_africa6}
2035. {campeon_copa_africa7}
2037. {campeon_copa_africa8}
2039. {campeon_copa_africa9}
2041. {campeon_copa_africa10}
''')
    input("")
    print("campeones de la finalissima")
    print(f'''
2023. {campeon_finalisima1}
2025. {campeon_finalisima2}
2027. {campeon_finalisima3}
2029. {campeon_finalisima4}
2031. {campeon_finalisima5}
2033. {campeon_finalisima6}
2035. {campeon_finalisima7}
2037. {campeon_finalisima8}
2039. {campeon_finalisima9}
2041. {campeon_finalisima10}
''')
    input("")
    print("campeones del mundial")
    print(f'''
2026. {campeon_mundial1}
2030. {campeon_mundial2}
2034. {campeon_mundial3}
2038. {campeon_mundial4}
2042. {campeon_mundial5}
''')

def mostrar_goleadores_asistentes(): 
    logros = []
    input("Goleador de la premier league") 
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == "premier":
            if contador == 1:
                break
            if contador == 0:
                print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                if j['nombre'] == player["nombre"]:
                    logro = 'goleador de la Premier League'
                    logros.append(logro)
                    player["valoracion"] += 2
                    player["dinero"] += 500000
            else:
                print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
    input("asistente de la premier league") 
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["asistencias"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == "premier":
            if contador == 1:
                break
            if contador == 0:
                print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                if j['nombre'] == player["nombre"]:
                    logro = 'asistente de la Premier League'
                    logros.append(logro)
                    player["valoracion"] += 1
                    player["dinero"] += 250000
            else:
                print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
    input("Goleador de la championship")  
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == "championship":
            if contador == 1:
                break
            if contador == 0:
                print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                if j['nombre'] == player["nombre"]:
                    logro = 'goleador de la Championship'
                    logros.append(logro)
                    player["valoracion"] += 2
                    player["dinero"] += 500000
            else:
                print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
    input("asistente de la championship") 
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["asistencias"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == "championship":
            if contador == 1:
                break
            if contador == 0:
                print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                if j['nombre'] == player["nombre"]:
                    logro = 'asistente de la Championship'
                    logros.append(logro)
                    player["valoracion"] += 1
                    player["dinero"] += 250000
            else:
                print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
    
    jugadores_carabao = [j for j in jugadores if j["division"] in ["premier", "championship"]]
    input("goleador de la carabao cup")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["goles_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['goles_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = 'goleador de la Carabo Cup'
                logros.append(logro)
                player["valoracion"] += 2
                player["dinero"] += 500000
        else:
            print(f" {j['goles_carabao']} {j['nombre']} - {j['equipo']}")
    print("")
    input("asistente de la carabao cup")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["asistencias_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['asistencias_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = 'asistente de la Carabo Cup'
                logros.append(logro)
                player["valoracion"] += 1
                player["dinero"] += 250000
        else:
            print(f" {j['asistencias_carabao']} {j['nombre']} - {j['equipo']}")
    print("")
    print("") 
    input("Goleador de la Serie A")  
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == "serie A":
            if contador == 1:
                break
            if contador == 0:
                print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                if j['nombre'] == player["nombre"]:
                    logro = 'goleador de la Serie A'
                    logros.append(logro)
                    player["valoracion"] += 2
                    player["dinero"] += 500000
            else:
                print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
    input("asistente de la Serie A") 
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["asistencias"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == "serie A":
            if contador == 1:
                break
            if contador == 0:
                print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                if j['nombre'] == player["nombre"]:
                    logro = 'asistente de la Serie A'
                    logros.append(logro)
                    player["valoracion"] += 1
                    player["dinero"] += 250000
            else:
                print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
    print("") 
    input("Goleador de la Serie B")  
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == "serie B":
            if contador == 1:
                break
            if contador == 0:
                print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                if j['nombre'] == player["nombre"]:
                    logro = 'goleador de la Serie B'
                    logros.append(logro)
                    player["valoracion"] += 2
                    player["dinero"] += 500000
            else:
                print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
    input("asistente de la Serie B") 
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["asistencias"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == "serie B":
            if contador == 1:
                break
            if contador == 0:
                print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                if j['nombre'] == player["nombre"]:
                    logro = 'asistente de la Serie B'
                    logros.append(logro)
                    player["valoracion"] += 1
                    player["dinero"] += 250000
            else:
                print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
    jugadores_carabao = [j for j in jugadores if j["division"] in ["serie A", "serie B"]]
    input("goleador de la Copa Italia")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["goles_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['goles_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = 'goleador de la Copa Italia'
                logros.append(logro)
                player["valoracion"] += 2
                player["dinero"] += 500000
        else:
            print(f" {j['goles_carabao']} {j['nombre']} - {j['equipo']}")
    print("")
    input("asistente de la Copa Italia")
    jugadores_ordenados = sorted(jugadores_carabao, key=lambda j: j["asistencias_carabao"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['asistencias_carabao']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = 'asistente de la Copa Italia'
                logros.append(logro)
                player["valoracion"] += 1
                player["dinero"] += 250000
        else:
            print(f" {j['asistencias_carabao']} {j['nombre']} - {j['equipo']}")
    print("")
    input("goleador de la champions league")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles_champions"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['goles_champions']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = 'goleador de la Champions League'
                logros.append(logro)
                player["valoracion"] += 2
                player["dinero"] += 500000
        else:
            print(f" {j['goles_champions']} {j['nombre']} - {j['equipo']}")        
    print("")
    input("asistente de la champions league")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["asistencias_champions"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['asistencias_champions']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = 'asistente de la Champions League'
                logros.append(logro)
                player["valoracion"] += 1
                player["dinero"] += 250000
        else:
            print(f" {j['asistencias_champions']} {j['nombre']} - {j['equipo']}")          
    print("")
    input("goleador de la europa league")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles_europa"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['goles_europa']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = 'goleador de la Europa League'
                logros.append(logro)
                player["valoracion"] += 2
                player["dinero"] += 500000
        else:
            print(f" {j['goles_europa']} {j['nombre']} - {j['equipo']}")        
    print("")
    input("asistente de la europa league")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["asistencias_europa"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['asistencias_europa']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = 'asistente de la Europa League'
                logros.append(logro)
                player["valoracion"] += 1
                player["dinero"] += 250000
        else:
            print(f" {j['asistencias_europa']} {j['nombre']} - {j['equipo']}")   
    return logros     
def actualizar_mvp(nombre_jugador):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador["MVP de la fecha"] += 1
            if jugador["nombre"] == player["nombre"]:
                player["valoracion"] += 0.75
            break

def recetearmvp():
    for jugador in jugadores:
       jugador["mvpcontrol"] = 0

def ver_mvp_fecha_premier():
    print("")  
    jugadores_premier = [j for j in jugadores if j['division'] == 'premier']
    max_mvpcontrol = max(jugadores_premier, key=lambda j: j['mvpcontrol'])['mvpcontrol']
    jugadores_max_mvpcontrol = [j for j in jugadores_premier if j['mvpcontrol'] == max_mvpcontrol]
    num = len(jugadores_max_mvpcontrol)
    if num != 1: numerorandom = random.randint(0,num - 1)
    else: numerorandom = 0    
    mvp_de_la_fecha = []
    mvp_de_la_fecha.append(jugadores_max_mvpcontrol[numerorandom])
    for jugador in mvp_de_la_fecha:
        print(f"El MVP de la fecha es: {jugador['nombre']}")
        nombre = jugador["nombre"]
        actualizar_mvp(nombre)
    input("")    
    jugadores_ordenados = sorted(jugadores_premier, key=lambda j: j["MVP de la fecha"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f"{j['MVP de la fecha']} {j['nombre']} - {j['equipo']}")
        else:
            print(f"{j['MVP de la fecha']} {j['nombre']} - {j['equipo']}")
    print("") 

def ver_mvp_fecha_championship():
    print("")  
    jugadores_championship = [j for j in jugadores if j['division'] == 'championship']
    max_mvpcontrol = max(jugadores_championship, key=lambda j: j['mvpcontrol'])['mvpcontrol']
    jugadores_max_mvpcontrol = [j for j in jugadores_championship if j['mvpcontrol'] == max_mvpcontrol]
    num = len(jugadores_max_mvpcontrol)
    if num != 1: numerorandom = random.randint(0,num - 1)
    else: numerorandom = 0    
    mvp_de_la_fecha = []
    mvp_de_la_fecha.append(jugadores_max_mvpcontrol[numerorandom])
    for jugador in mvp_de_la_fecha:
        print(f"El MVP de la fecha es: {jugador['nombre']}")
        nombre = jugador["nombre"]
        actualizar_mvp(nombre)
    print("")     
    input("")    
    jugadores_ordenados = sorted(jugadores_championship, key=lambda j: j["MVP de la fecha"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f"{j['MVP de la fecha']} {j['nombre']} - {j['equipo']}")
        else:
            print(f"{j['MVP de la fecha']} {j['nombre']} - {j['equipo']}")
    print("") 

def ver_mvp_fecha_seriea():
    print("")  
    jugadores_championship = [j for j in jugadores if j['division'] == 'serie A']
    max_mvpcontrol = max(jugadores_championship, key=lambda j: j['mvpcontrol'])['mvpcontrol']
    jugadores_max_mvpcontrol = [j for j in jugadores_championship if j['mvpcontrol'] == max_mvpcontrol]
    num = len(jugadores_max_mvpcontrol)
    if num != 1: numerorandom = random.randint(0,num - 1)
    else: numerorandom = 0    
    mvp_de_la_fecha = []
    mvp_de_la_fecha.append(jugadores_max_mvpcontrol[numerorandom])
    for jugador in mvp_de_la_fecha:
        print(f"El MVP de la fecha es: {jugador['nombre']}")
        nombre = jugador["nombre"]
        actualizar_mvp(nombre)
    print("")     
    input("")    
    jugadores_ordenados = sorted(jugadores_championship, key=lambda j: j["MVP de la fecha"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f"{j['MVP de la fecha']} {j['nombre']} - {j['equipo']}")
        else:
            print(f"{j['MVP de la fecha']} {j['nombre']} - {j['equipo']}")
    print("") 

def ver_mvp_fecha_serieb():
    print("")  
    jugadores_championship = [j for j in jugadores if j['division'] == 'serie B']
    max_mvpcontrol = max(jugadores_championship, key=lambda j: j['mvpcontrol'])['mvpcontrol']
    jugadores_max_mvpcontrol = [j for j in jugadores_championship if j['mvpcontrol'] == max_mvpcontrol]
    num = len(jugadores_max_mvpcontrol)
    if num != 1: numerorandom = random.randint(0,num - 1)
    else: numerorandom = 0    
    mvp_de_la_fecha = []
    mvp_de_la_fecha.append(jugadores_max_mvpcontrol[numerorandom])
    for jugador in mvp_de_la_fecha:
        print(f"El MVP de la fecha es: {jugador['nombre']}")
        nombre = jugador["nombre"]
        actualizar_mvp(nombre)
    print("")     
    input("")    
    jugadores_ordenados = sorted(jugadores_championship, key=lambda j: j["MVP de la fecha"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f"{j['MVP de la fecha']} {j['nombre']} - {j['equipo']}")
        else:
            print(f"{j['MVP de la fecha']} {j['nombre']} - {j['equipo']}")
    print("") 

def mvp_del_año():
    mvp = []
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["MVP"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        print(f"EL JUGADOR MVP ES: {j['nombre']} - {j['equipo']} ({j['MVP']} pts)")
        if j["nombre"] == player["nombre"]: 
            player["mvp del año anuales"].append(1)
            premio = 'mvp del año'
            player["dinero"] += 5000000
            mvp.append(premio)
        else: player["mvp del año anuales"].append(0)
    return mvp 

def ver_datos_player():
    for jugador in jugadores_selecciones:
        if jugador["nombre"] == nombre_del_jugador:
            goles_seleccion = jugador["goles"]
            asistencias_seleccion = jugador["asistencias"]
            amarillas_seleccion = jugador["amarillas"]
            rojas_seleccion = jugador["rojas"]
    for jugador in jugadores:
        if jugador["nombre"] == nombre_del_jugador:
            goles = jugador["goles"] 
            asistencias = jugador["asistencias"]  
            amarillas = jugador["amarillas"]
            rojas = jugador["rojas"]
            mvp_de_la_fecha = jugador["MVP de la fecha"]
            goles_carabao = jugador["goles_carabao"]
            asistencias_carabao = jugador["asistencias_carabao"]
            amarillas_carabao = jugador["amarillas_carabao"]
            rojas_carabao = jugador["rojas_carabao"]
            partidos = jugador["partidos"]
            goles_champions = jugador["goles_champions"]
            asistencias_champions = jugador["asistencias_champions"]
            amarillas_champions = jugador["amarillas_champions"]
            rojas_champions = jugador["rojas_champions"]
            goles_europa = jugador["goles_europa"]
            asistencias_europa = jugador["asistencias_europa"]
            amarillas_europa = jugador["amarillas_europa"]
            rojas_europa = jugador["rojas_europa"]
            
    input("ver datos del jugador")
    print("")
    print(f'''
datos del jugador
partidos: {partidos}
goles en liga: {goles}
asistencias en liga: {asistencias}
amarillas en liga: {amarillas}
rojas en liga: {rojas}
mvp de la fecha: {mvp_de_la_fecha}
goles en la carabao: {goles_carabao}
asistencias en la carabao: {asistencias_carabao}
amarillas en la carabao: {amarillas_carabao}
rojas en la carabao: {rojas_carabao}
goles en la seleccion: {goles_seleccion}
asistencias en la seleccion: {asistencias_seleccion}
amarillas en la seleccion: {amarillas_seleccion}
rojas en la seleccion: {rojas_seleccion}
goles en la champions league: {goles_champions}
asistencias en la champions league: {asistencias_champions}
amarillas en la champions league: {amarillas_champions}
rojas en la champions league: {rojas_champions}
goles en la europa league: {goles_europa}
asistencias en la europa league: {asistencias_europa}
amarillas en la europa league: {amarillas_europa}
rojas en la europa league: {rojas_europa}
total de goles: {goles + goles_carabao + goles_champions + goles_europa + goles_seleccion}
total de asistencias: {asistencias + asistencias_carabao + asistencias_champions+ asistencias_europa + asistencias_seleccion}
total de amarillas: {amarillas+amarillas_carabao + amarillas_champions + amarillas_europa + amarillas_seleccion}
total de rojas: {rojas + rojas_carabao + rojas_champions + rojas_europa + rojas_seleccion}
''')
    input("")

def guardar_datos_anuales(vitrina,logros_anuales):
    for jugador in jugadores_selecciones:
        if jugador["nombre"] == nombre_del_jugador:
            goles_seleccion = jugador["goles"]
            asistencias_seleccion = jugador["asistencias"]
            amarillas_seleccion = jugador["amarillas"]
            rojas_seleccion = jugador["rojas"]
    for jugador in jugadores:
        if jugador["nombre"] == nombre_del_jugador:
            goles = jugador["goles"]
            asistencias = jugador["asistencias"]
            amarillas = jugador["amarillas"]
            rojas = jugador["rojas"]
            mvp_de_la_fecha = jugador["MVP de la fecha"]
            goles_carabao = jugador["goles_carabao"]
            asistencias_carabao = jugador["asistencias_carabao"]
            amarillas_carabao = jugador["amarillas_carabao"]
            rojas_carabao = jugador["rojas_carabao"]
            partidos = jugador["partidos"]
            goles_champions = jugador["goles_champions"]
            asistencias_champions = jugador["asistencias_champions"]
            amarillas_champions = jugador["amarillas_champions"]
            rojas_champions = jugador["rojas_champions"]
            goles_europa = jugador["goles_europa"]
            asistencias_europa = jugador["asistencias_europa"]
            amarillas_europa = jugador["amarillas_europa"]
            rojas_europa = jugador["rojas_europa"]
            player["goles anuales"].append(goles + goles_carabao + goles_champions + goles_europa + goles_seleccion)
            player["asistencias anuales"].append(asistencias + asistencias_carabao + asistencias_champions + asistencias_europa + asistencias_seleccion)
            player["amarillas anuales"].append(amarillas + amarillas_carabao + amarillas_champions + amarillas_europa +amarillas_seleccion)
            player["rojas anuales"].append(rojas + rojas_carabao + rojas_champions + rojas_europa + rojas_seleccion)
            player["mvp de la fecha anuales"].append(mvp_de_la_fecha)
            player["partidos jugados"].append(partidos)
            player["equipo anual"].append(player["equipo"])
            player["vitrina"].append(vitrina)
            player["logros anuales"].append(logros_anuales)
            player["dinero"] += ((goles*5000)+(goles_carabao*2500)+(goles_champions*7500)+(goles_europa*6500)+(goles_seleccion*6500))
            player["dinero"] += ((asistencias*2000)+(asistencias_carabao*1000)+(asistencias_champions*2500)+(asistencias_europa*1500)+(asistencias_seleccion*3000))
            player["dinero"] -= ((amarillas*1000)+(amarillas_carabao*1000)+(amarillas_champions*1000)+(amarillas_europa*1000)+(amarillas_seleccion*1500))
            player["dinero"] -= ((rojas*2000)+(rojas_carabao*2000)+(rojas_champions*2500)+(rojas_europa*2000)+(rojas_seleccion*3000))
            player["dinero"] += (mvp_de_la_fecha*10000)
            
def mostrar_datos_anuales():
    goles_anuales = player["goles anuales"]
    asistencias_anuales = player["asistencias anuales"]
    amarillas_anuales = player["amarillas anuales"]
    rojas_anuales = player["rojas anuales"]
    mvp_de_la_fecha = player["mvp de la fecha anuales"]
    mvp_anuales = player["mvp del año anuales"]
    partidos_anuales = player["partidos jugados"]     
    equipo_anual = player["equipo anual"]  
    vitrina = player["vitrina"]
    logros = player["logros anuales"]
    dinero = player["dinero"]
    contador = 2023
    print("")
    input("")
    total = 0
    print("goles anuales")
    for i in goles_anuales:
        print(f"{contador}. {i}")
        contador += 1
        total += i
    print(f"los goles totales en la carrera {total}")
    contador = 2023
    print("")
    input("")
    total = 0
    print("asistencias anuales")
    for i in asistencias_anuales:
        print(f"{contador}. {i}")
        contador += 1
        total += i
    print(f"los asistencias totales en la carrera {total}")
    contador = 2023
    print("")
    input("")
    total = 0
    print("amarillas anuales")
    for i in amarillas_anuales:
        print(f"{contador}. {i}")
        contador += 1
        total += i
    print(f"los amarillas totales en la carrera {total}")
    contador = 2023
    print("")
    input("")
    total = 0
    print("rojas anuales")
    for i in rojas_anuales:
        print(f"{contador}. {i}")
        contador += 1
        total += i
    print(f"los rojas totales en la carrera {total}")
    contador = 2023
    print("")
    input("")
    total = 0
    print("mvp de la fecha anuales")
    for i in mvp_de_la_fecha:
        print(f"{contador}. {i}")
        contador += 1
        total += i
    print(f"los mvp de la fecha totales en la carrera {total}")
    contador = 2023
    print("")
    input("")
    print("mvp anuales")
    for i in mvp_anuales:
        if i == 1: j = "si"
        else: j = "no"
        print(f"{contador}. {j}")
        contador += 1
    contador = 2023
    print("")
    input("")
    total = 0
    print("partidos anuales")
    for i in partidos_anuales:
        print(f"{contador}. {i}")
        contador += 1
        total += i
    print(f"los partidos totales en la carrera {total}")
    contador = 2023
    print("")
    input("")
    print("equipo anual")
    for i in equipo_anual:
        print(f"{contador}. {i}")
        contador += 1
    contador = 2023
    print("")
    input("")
    print("logros")
    for i in logros:
        if len(i) != 0:
            for j in i:    
                print(f"{contador}. {j}")
        else: print(f"{contador}. sin logros")
        contador += 1
    contador = 2023
    print("")
    input("")
    print("vitrina")
    for i in vitrina:
        if len(i) != 0:
            for j in i:    
                print(f"{contador}. {j}")
        else: print(f"{contador}. vitrina vacia")
        contador += 1
    contador = 2023
    print("")
    input("")
    print("traspasos")
    for i in traspasos:   
        print(f"{contador}. {i}")
        contador += 1    
    print("")
    input("")
    print("dinero")
    print(f"dinero: {dinero}")
def cambiar_equipo():
    reputacion5 = [
    Arsenal["equipo"],Chelsea["equipo"],Manchester_City["equipo"],Manchester_United["equipo"],Tottenham["equipo"],Liverpool["equipo"],
    Napoli["equipo"],Inter["equipo"],Milan["equipo"],Juventus["equipo"],Roma["equipo"]
    ]
    reputacion4 = [
        Brigthon["equipo"],Newcastle["equipo"],
        Lazio["equipo"],Fiorentina["equipo"],Atalanta["equipo"]
        ]
    reputacion3 = [
Aston_Villa["equipo"],Brentford["equipo"],Crystal_Palace["equipo"],Fulham["equipo"],Swansea["equipo"],Norwich["equipo"],Watford["equipo"],Stoke_City["equipo"],Bologna["equipo"],Torino["equipo"],Udinese["equipo"],Sassuolo["equipo"],Sampdoria["equipo"],Genoa["equipo"],Parma["equipo"],Cagliari["equipo"]]
    reputacion2 = [
        Cardiff_City["equipo"],Queens_Park_Rangers["equipo"],Huddersfield_Town["equipo"],Birmingham["equipo"],Hull_City["equipo"],Sunderland["equipo"],Middlesbrough["equipo"],Sheffield_United["equipo"],Burnley["equipo"],Wolverhampton["equipo"],West_ham["equipo"],Southampton["equipo"],Nottingham_Forest["equipo"],Leicester_City["equipo"],Leeds_United["equipo"],Everton["equipo"],Monza["equipo"],Empoli["equipo"],Salernitana["equipo"],Lecce["equipo"],Hellas_Verona["equipo"],Spezia["equipo"],Frosinone["equipo"],Bari["equipo"],Palermo["equipo"],Brescia["equipo"],Cittadella["equipo"],Spal["equipo"],Benevento["equipo"]
        ]
    reputacion1 = [
Bournemouth["equipo"],Luton_Town["equipo"],Coventry_City["equipo"],Blackburn_Rovers["equipo"],Millwall["equipo"],West_Bromwich_Albion["equipo"],Preston_North_End["equipo"],Bristol_City["equipo"],Cremonese["equipo"],Sudtirol["equipo"],Reggina["equipo"],Venezia["equipo"],Modena["equipo"],Pisa["equipo"],Ascoli["equipo"],Como["equipo"],Ternana["equipo"],Cosenza["equipo"],Perugia["equipo"]
        ]
    ofertas = []
    if player["valoracion"] > 80:
        num = random.randint(0, 10)
        plata = random.randint(100, 500)
        oferta = reputacion5[num]
        contrato = random.randint(1, 3)
        ofertaa = [oferta,plata,contrato]
        ofertas.append(ofertaa)
    if player["valoracion"] > 60:
        num = random.randint(0, 4)
        plata = random.randint(50, 100)
        contrato = random.randint(1, 3)
        oferta = reputacion4[num]
        ofertaa = [oferta,plata,contrato]
        ofertas.append(ofertaa)
    if player["valoracion"] > 40:
        num = random.randint(0, 15)
        oferta = reputacion3[num]
        plata = random.randint(25, 50)
        contrato = random.randint(1, 3)
        ofertaa = [oferta,plata,contrato]
        ofertas.append(ofertaa)
    if player["valoracion"] > 20:
        num = random.randint(0, 28)
        oferta = reputacion2[num]
        plata = random.randint(5, 25)
        contrato = random.randint(1, 3)
        ofertaa = [oferta,plata,contrato]
        ofertas.append(ofertaa)
    num = random.randint(0, 18)
    oferta = reputacion1[num]
    plata = random.randint(1, 5)
    contrato = random.randint(1, 3)
    ofertaa = [oferta,plata,contrato]
    ofertas.append(ofertaa)
    contador = 1
    arrray = []
    for i in ofertas:
        input("")
        print(f"oferta {contador}")
        print(f'''
equipo: {i[0]}
precio: ${i[1]}M
años: {i[2]}
''')
        arrray.append(contador)
        contador += 1
    arrrray =[]
    for i in arrray:
        arrrray.append(str(i))
    conttt = 1
    while conttt == 1: 
        eleccion = input("que oferta deseas tomar")
        if eleccion in arrrray: 
            conttt = 0
            if eleccion == "1":
                print(f"HAS FICHADO POR EL {ofertas[0][0]} POR ${ofertas[0][1]}M CON UNA DURACION DE {ofertas[0][2]} AÑOS")
                ofertas[0]
                equipo_anteriror = equipo_player
                equipo_playerr = ofertas[0][0] 
                player["equipo"] = ofertas[0][0]
                player["contrato"] = ofertas[0][2]
                if equipo_anteriror == equipo_playerr: 
                    traspaso = f'Renovacion con el {equipo_playerr} por ${ofertas[0][1]}M'
                else: 
                    traspaso = f'Desde el {equipo_anteriror} al {equipo_playerr} por ${ofertas[0][1]}M' 
                traspasos.append(traspaso)
            elif eleccion == "2":
                print(f"HAS FICHADO POR EL {ofertas[1][0]} POR ${ofertas[1][1]}M CON UNA DURACION DE {ofertas[1][2]} AÑOS")
                ofertas[1]
                equipo_anteriror = equipo_player
                equipo_playerr =ofertas[1][0] 
                player["equipo"] = ofertas[1][0]
                player["contrato"] = ofertas[1][2]
                if equipo_anteriror == equipo_playerr: traspaso = f'Renovacion con el {equipo_playerr} por ${ofertas[1][1]}M' 
                else: traspaso = f'Desde el {equipo_anteriror} al {equipo_playerr} por ${ofertas[1][1]}M' 
                traspasos.append(traspaso)
            elif eleccion == "3": 
                print(f"HAS FICHADO POR EL {ofertas[2][0]} POR ${ofertas[2][1]}M CON UNA DURACION DE {ofertas[2][2]} AÑOS")
                ofertas[2]      
                equipo_anteriror = equipo_player
                equipo_playerr =ofertas[2][0] 
                player["equipo"] = ofertas[2][0] 
                player["contrato"] = ofertas[2][2]
                if equipo_anteriror == equipo_playerr:traspaso = f'Renovacion con el {equipo_playerr} por ${ofertas[2][1]}M'
                else:traspaso = f'Desde el {equipo_anteriror} al {equipo_playerr} por ${ofertas[2][1]}M' 
                traspasos.append(traspaso)
            elif eleccion == "4":
                print(f"HAS FICHADO POR EL {ofertas[3][0]} POR ${ofertas[3][1]}M CON UNA DURACION DE {ofertas[3][2]} AÑOS")
                ofertas[3]
                equipo_anteriror = equipo_player
                equipo_playerr =ofertas[3][0] 
                player["equipo"] = ofertas[3][0]
                player["contrato"] = ofertas[3][2]
                if equipo_anteriror == equipo_playerr:traspaso = f'Renovacion con el {equipo_playerr} por ${ofertas[3][1]}M' 
                else: traspaso = f'Desde el {equipo_anteriror} al {equipo_playerr} por ${ofertas[3][1]}M' 
                traspasos.append(traspaso)
            elif eleccion == "5":
                print(f"HAS FICHADO POR EL {ofertas[4][0]} POR ${ofertas[4][1]}M CON UNA DURACION DE {ofertas[4][2]} AÑOS")
                ofertas[4]
                equipo_anteriror = equipo_player
                equipo_playerr = ofertas[4][0] 
                player["equipo"] = ofertas[4][0]
                player["contrato"] = ofertas[4][2]
                if equipo_anteriror == equipo_playerr: traspaso = f'Renovacion con el {equipo_playerr} por ${ofertas[4][1]}M'
                else: traspaso = f'Desde el {equipo_anteriror} al {equipo_playerr} por ${ofertas[4][1]}M' 
                traspasos.append(traspaso)
        
    return equipo_playerr

def generar_grupos(equipos):
    n = len(equipos)
    fixture_ida = []
    fixture_vuelta = []
    for i in range(n - 1):
        ronda = []
        for j in range(n // 2):
            # Si es la primera ronda, el equipo i es local, sino es visitante
            if i == 0:
                partido = (equipos[j], equipos[n - 1 - j])
            else:
                partido = (equipos[n - 1 - j], equipos[j])
            ronda.append(partido)
        fixture_ida.append(ronda)

        # Rotación de equipos
        equipos.insert(1, equipos.pop())
    
    for ronda_ida in fixture_ida:
        ronda_vuelta = []
        for partido in ronda_ida:
            ronda_vuelta.append((partido[1], partido[0]))
        fixture_vuelta.append(ronda_vuelta)    
    
    return fixture_ida,fixture_vuelta          
def mostrar_grupos(grupo):
        for i in grupo:
            print(i)
def mostrar_grupos_champions():
    print("GRUPOS")
    input("")
    print("Grupo 1")
    print("")
    mostrar_grupos(grupo1_champions)
    input("")
    print("Grupo 2")
    print("")
    mostrar_grupos(grupo2_champions)
    input("")
    print("Grupo 3")
    print("")
    mostrar_grupos(grupo3_champions)
    input("")
    print("Grupo 4")
    print("")
    mostrar_grupos(grupo4_champions)
    input("")

def mostrar_grupos_europa_league():
    print("GRUPOS")
    input("")
    print("Grupo 1")
    print("")
    mostrar_grupos(grupo1_europa)
    input("")
    print("Grupo 2")
    print("")
    mostrar_grupos(grupo2_europa)
    input("")
    print("Grupo 3")
    print("")
    mostrar_grupos(grupo3_europa)
    input("")
    print("Grupo 4")
    print("")
    mostrar_grupos(grupo4_europa)
    input("")

def mezclar_lista(lista_original):
    lista = lista_original[:]
    longitud_lista = len(lista)
    for i in range(longitud_lista):
        indice_aleatorio = random.randint(0, longitud_lista - 1)
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[indice_aleatorio] = temporal
    return lista

def sancionados_champions(club):
    jugadores_sancionados = []
    for jugador in jugadores:
        if jugador["equipo"] == club:
            if jugador["sancionado_champions"] == True:
                sancionado = jugador["nombre"]
                jugadores_sancionados.append(sancionado)
            if jugador["nombre"] == nombre_del_jugador:
                if jugador["sancionado_champions"] == False:
                    jugador["partidos"] +=1               
    return jugadores_sancionados 
def desancionar_champions(club):
    for jugador in jugadores:
        if jugador["equipo"] == club:
            jugador["sancionado_champions"] = False

def sumar_gol_champions(nombre_jugador):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador["goles_champions"] += 1
            jugador["MVP"] += 2
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.5
            break
def sumar_asistencia_champions(nombre_jugador):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador["asistencias_champions"] += 1
            jugador["MVP"] += 1
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.25
            break        

def actualizar_rustico_champions(nombre_jugador,ama,roja):
    if ama == 1:
        for jugador in jugadores:
            if jugador["nombre"] == nombre_jugador:
                jugador["amarillas_champions"] += 1
                jugador["sancion_champions"] += 1
                jugador["MVP"] -= 1
                if jugador["sancion_champions"] >= 3:
                    jugador["sancionado_champions"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.25
    if roja == 1:  
        for jugador in jugadores:
            if jugador["nombre"] == nombre_jugador:
                jugador["rojas_champions"] += 1    
                jugador["sancion_champions"] = 3
                jugador["MVP"] -= 3
                jugador["sancionado_champions"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.5

def partidos_champions(club1,club2,tabla):
    print("")
    input("")
    jugadores_sancionados_locales = sancionados_champions(club1)
    jugadores_sancionados_visitantes = sancionados_champions(club2)
    desancionar_champions(club1)
    desancionar_champions(club2)
    jugadores_lesionados_locales = lesionados(club1)
    jugadores_lesionados_visitantes = lesionados(club2)
    deslesionar(club1)
    deslesionar(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totales:
            sumar_gol_champions(i)
        asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_champions(i)
    amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    rojas_locales = taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_locales) != 0:
        for i in lesionados_locales:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_champions(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_champions(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totalesv:
            sumar_gol_champions(i)
        asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_champions(i)
    amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_visitantes) != 0:
        for i in lesionados_visitantes:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_champions(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_champions(i,0,1) 
    if goallocal > goalsvisitor:
        fct.actualizar_tabla(tabla,club1,3,goallocal,goalsvisitor,1,0,0)
        fct.actualizar_tabla(tabla,club2,0,goalsvisitor,goallocal,0,0,1)
        sumar_ranking_club(club1,3)
        sumar_ranking_club(club2,0)
    elif goallocal < goalsvisitor:
        fct.actualizar_tabla(tabla,club1,0,goallocal,goalsvisitor,0,0,1)
        fct.actualizar_tabla(tabla,club2,3,goalsvisitor,goallocal,1,0,0)
        sumar_ranking_club(club1,0)
        sumar_ranking_club(club2,3)
    else:
        fct.actualizar_tabla(tabla,club1,1,goallocal,goalsvisitor,0,1,0)
        fct.actualizar_tabla(tabla,club2,1,goalsvisitor,goallocal,0,1,0)
        sumar_ranking_club(club1,1)
        sumar_ranking_club(club2,1)

def goleadores_totales_champions():
    input("mostrar tabla de goleadores de la champions")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles_champions"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f"\033[32m\U000026BD {j['goles_champions']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f"\U000026BD {j['goles_champions']} {j['nombre']} - {j['equipo']}")
    print("")    
def asistentes_totales_champions():
    input("mostrar tabla de asistentes de la champions")  
    print("")
    asistentes_ordenados = sorted(jugadores, key=lambda j: j["asistencias_champions"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(asistentes_ordenados[:10]):
        if i == 0:
            print(f"\033[32m{j['asistencias_champions']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f"{j['asistencias_champions']} {j['nombre']} - {j['equipo']}")
    print("")      
def mostrar_ama_champions():
    input("mostrar tabla de amarillas de la champions")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["amarillas_champions"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['amarillas_champions']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['amarillas_champions']} {j['nombre']} - {j['equipo']}")
    print("")     
def mostrar_rojas_champions():
    input("mostrar tabla de rojas de la champions")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["rojas_champions"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['rojas_champions']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['rojas_champions']} {j['nombre']} - {j['equipo']}")
    print("")
    input("")

def fecha_1(fixture,n,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[0][0][0]} vs {fixture[0][0][1]}')
    print(f'{fixture[0][1][0]} vs {fixture[0][1][1]}')
    print("")
    partidos_champions(fixture[0][0][0],fixture[0][0][1],tabla)
    partidos_champions(fixture[0][1][0],fixture[0][1][1],tabla)
    print("")
      
def fecha_2(fixture,n,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[1][0][0]} vs {fixture[1][0][1]}')
    print(f'{fixture[1][1][0]} vs {fixture[1][1][1]}')
    equipo1 = fixture[1][0][0]
    equipo2 = fixture[1][0][1]
    equipo3 = fixture[1][1][0]
    equipo4 = fixture[1][1][1]
    print("")
    partidos_champions(equipo1,equipo2,tabla)
    partidos_champions(equipo3,equipo4,tabla)
    print("")
    
def fecha_3(fixture,n,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[2][0][0]} vs {fixture[2][0][1]}')
    print(f'{fixture[2][1][0]} vs {fixture[2][1][1]}')
    equipo1 = fixture[2][0][0]
    equipo2 = fixture[2][0][1]
    equipo3 = fixture[2][1][0]
    equipo4 = fixture[2][1][1]
    print("")
    partidos_champions(equipo1,equipo2,tabla)
    partidos_champions(equipo3,equipo4,tabla)
    print("")

def partidos_europa(club1,club2,tabla):
    print("")
    input("")
    jugadores_sancionados_locales = sancionados_europa(club1)
    jugadores_sancionados_visitantes = sancionados_europa(club2)
    desancionar_europa(club1)
    desancionar_europa(club2)
    jugadores_lesionados_locales = lesionados(club1)
    jugadores_lesionados_visitantes = lesionados(club2)
    deslesionar(club1)
    deslesionar(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totales:
            sumar_gol_europa(i)
        asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_europa(i)
    amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    rojas_locales = taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_locales) != 0:
        for i in lesionados_locales:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_europa(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_europa(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totalesv:
            sumar_gol_europa(i)
        asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_europa(i)
    amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_visitantes) != 0:
        for i in lesionados_visitantes:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_europa(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_europa(i,0,1) 
    if goallocal > goalsvisitor:
        fct.actualizar_tabla(tabla,club1,3,goallocal,goalsvisitor,1,0,0)
        fct.actualizar_tabla(tabla,club2,0,goalsvisitor,goallocal,0,0,1)
        sumar_ranking_club(club1,3)
        sumar_ranking_club(club2,0)
    elif goallocal < goalsvisitor:
        fct.actualizar_tabla(tabla,club1,0,goallocal,goalsvisitor,0,0,1)
        fct.actualizar_tabla(tabla,club2,3,goalsvisitor,goallocal,1,0,0)
        sumar_ranking_club(club1,0)
        sumar_ranking_club(club2,3)
    else:
        fct.actualizar_tabla(tabla,club1,1,goallocal,goalsvisitor,0,1,0)
        fct.actualizar_tabla(tabla,club2,1,goalsvisitor,goallocal,0,1,0)
        sumar_ranking_club(club1,1)
        sumar_ranking_club(club2,1)

def sancionados_europa(club):
    jugadores_sancionados = []
    for jugador in jugadores:
        if jugador["equipo"] == club:
            if jugador["sancionado_europa"] == True:
                sancionado = jugador["nombre"]
                jugadores_sancionados.append(sancionado)
            if jugador["nombre"] == nombre_del_jugador:
                if jugador["sancionado_europa"] == False:
                    jugador["partidos"] +=1               
    return jugadores_sancionados 
def desancionar_europa(club):
    for jugador in jugadores:
        if jugador["equipo"] == club:
            jugador["sancionado_europa"] = False

def sumar_gol_europa(nombre_jugador):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador["goles_europa"] += 1
            jugador["MVP"] += 2
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.5
            break
def sumar_asistencia_europa(nombre_jugador):
    for jugador in jugadores:
        if jugador["nombre"] == nombre_jugador:
            jugador["asistencias_europa"] += 1
            jugador["MVP"] += 1
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.25
            break        

def actualizar_rustico_europa(nombre_jugador,ama,roja):
    if ama == 1:
        for jugador in jugadores:
            if jugador["nombre"] == nombre_jugador:
                jugador["amarillas_europa"] += 1
                jugador["sancion_europa"] += 1
                jugador["MVP"] -= 1
                if jugador["sancion_europa"] >= 3:
                    jugador["sancionado_europa"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.25
    if roja == 1:  
        for jugador in jugadores:
            if jugador["nombre"] == nombre_jugador:
                jugador["rojas_europa"] += 1    
                jugador["sancion_europa"] = 3
                jugador["MVP"] -= 3
                jugador["sancionado_europa"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.5

def partidos_europa_ida(club1,club2):
    print("")
    input("")
    jugadores_sancionados_locales = sancionados_europa(club1)
    jugadores_sancionados_visitantes = sancionados_europa(club2)
    desancionar_europa(club1)
    desancionar_europa(club2)
    jugadores_lesionados_locales = lesionados(club1)
    jugadores_lesionados_visitantes = lesionados(club2)
    deslesionar(club1)
    deslesionar(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totales:
            sumar_gol_europa(i)
        asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_europa(i)
    amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    rojas_locales = taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_locales) != 0:
        for i in lesionados_locales:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_europa(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_europa(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totalesv:
            sumar_gol_europa(i)
        asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_europa(i)
    amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_visitantes) != 0:
        for i in lesionados_visitantes:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_europa(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_europa(i,0,1) 
    if goallocal > goalsvisitor:
        sumar_ranking_club(club1,3)
        sumar_ranking_club(club2,0)
    elif goallocal < goalsvisitor:
        sumar_ranking_club(club1,0)
        sumar_ranking_club(club2,3)
    else:
        sumar_ranking_club(club1,1)
        sumar_ranking_club(club2,1)
    return goallocal,goalsvisitor

def fecha_1_e(fixture,n,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[0][0][0]} vs {fixture[0][0][1]}')
    print(f'{fixture[0][1][0]} vs {fixture[0][1][1]}')
    print("")
    partidos_europa(fixture[0][0][0],fixture[0][0][1],tabla)
    partidos_europa(fixture[0][1][0],fixture[0][1][1],tabla)
    print("")
def fecha_2_e(fixture,n,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[1][0][0]} vs {fixture[1][0][1]}')
    print(f'{fixture[1][1][0]} vs {fixture[1][1][1]}')
    equipo1 = fixture[1][0][0]
    equipo2 = fixture[1][0][1]
    equipo3 = fixture[1][1][0]
    equipo4 = fixture[1][1][1]
    print("")
    partidos_europa(equipo1,equipo2,tabla)
    partidos_europa(equipo3,equipo4,tabla)
    print("")
def fecha_3_e(fixture,n,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[2][0][0]} vs {fixture[2][0][1]}')
    print(f'{fixture[2][1][0]} vs {fixture[2][1][1]}')
    equipo1 = fixture[2][0][0]
    equipo2 = fixture[2][0][1]
    equipo3 = fixture[2][1][0]
    equipo4 = fixture[2][1][1]
    print("")
    partidos_europa(equipo1,equipo2,tabla)
    partidos_europa(equipo3,equipo4,tabla)
    print("")

def fecha_1_s(fixture,n,apto,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[0][0][0]} vs {fixture[0][0][1]}')
    print(f'{fixture[0][1][0]} vs {fixture[0][1][1]}')
    print("")
    partido_eurocopa_c(fixture[0][0][0],fixture[0][0][1],apto,tabla)
    partido_eurocopa_c(fixture[0][1][0],fixture[0][1][1],apto,tabla)
    print("")
def fecha_2_s(fixture,n,apto,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[1][0][0]} vs {fixture[1][0][1]}')
    print(f'{fixture[1][1][0]} vs {fixture[1][1][1]}')
    equipo1 = fixture[1][0][0]
    equipo2 = fixture[1][0][1]
    equipo3 = fixture[1][1][0]
    equipo4 = fixture[1][1][1]
    print("")
    partido_eurocopa_c(equipo1,equipo2,apto,tabla)
    partido_eurocopa_c(equipo3,equipo4,apto,tabla)
    print("")
def fecha_3_s(fixture,n,apto,tabla):
    print("")
    input(f'grupo {n}')
    print("")
    print(f'{fixture[2][0][0]} vs {fixture[2][0][1]}')
    print(f'{fixture[2][1][0]} vs {fixture[2][1][1]}')
    equipo1 = fixture[2][0][0]
    equipo2 = fixture[2][0][1]
    equipo3 = fixture[2][1][0]
    equipo4 = fixture[2][1][1]
    print("")
    partido_eurocopa_c(equipo1,equipo2,apto,tabla)
    partido_eurocopa_c(equipo3,equipo4,apto,tabla)
    print("")

def goleadores_totales_europa():
    input("mostrar tabla de goleadores de la europa league")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["goles_europa"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f"\033[32m\U000026BD {j['goles_europa']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f"\U000026BD {j['goles_europa']} {j['nombre']} - {j['equipo']}")
    print("")    
def asistentes_totales_europa():
    input("mostrar tabla de asistentes de la europa league")  
    print("")
    asistentes_ordenados = sorted(jugadores, key=lambda j: j["asistencias_europa"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(asistentes_ordenados[:10]):
        if i == 0:
            print(f"\033[32m{j['asistencias_europa']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f"{j['asistencias_europa']} {j['nombre']} - {j['equipo']}")
    print("")      
def mostrar_ama_europa():
    input("mostrar tabla de amarillas de la europa league")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["amarillas_europa"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['amarillas_europa']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['amarillas_europa']} {j['nombre']} - {j['equipo']}")
    print("")     
def mostrar_rojas_europa():
    input("mostrar tabla de rojas de la europa league")  
    print("")
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["rojas_europa"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['rojas_europa']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['rojas_europa']} {j['nombre']} - {j['equipo']}")
    print("")
    input("")

def partidos_champions_ida(club1,club2):
    print("")
    input("")
    jugadores_sancionados_locales = sancionados_champions(club1)
    jugadores_sancionados_visitantes = sancionados_champions(club2)
    desancionar_champions(club1)
    desancionar_champions(club2)
    jugadores_lesionados_locales = lesionados(club1)
    jugadores_lesionados_visitantes = lesionados(club2)
    deslesionar(club1)
    deslesionar(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totales:
            sumar_gol_champions(i)
        asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_champions(i)
    amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    rojas_locales = taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_locales) != 0:
        for i in lesionados_locales:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_champions(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_champions(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totalesv:
            sumar_gol_champions(i)
        asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_champions(i)
    amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_visitantes) != 0:
        for i in lesionados_visitantes:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_champions(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_champions(i,0,1) 
    if goallocal > goalsvisitor:
        sumar_ranking_club(club1,3)
        sumar_ranking_club(club2,0)
    elif goallocal < goalsvisitor:
        sumar_ranking_club(club1,0)
        sumar_ranking_club(club2,3)
    else:
        sumar_ranking_club(club1,1)
        sumar_ranking_club(club2,1)
    return goallocal,goalsvisitor

def partidos_champions_vuelta(club1,club2,goles_locales,goles_visitnates):
    print("partido de ida")
    print(f"{club2} {goles_locales}-{goles_visitnates} {club1}")
    input("")
    jugadores_sancionados_locales = sancionados_champions(club1)
    jugadores_sancionados_visitantes = sancionados_champions(club2)
    desancionar_champions(club1)
    desancionar_champions(club2)
    jugadores_lesionados_locales = lesionados(club1)
    jugadores_lesionados_visitantes = lesionados(club2)
    deslesionar(club1)
    deslesionar(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totales:
            sumar_gol_champions(i)
        asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_champions(i)
    amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    rojas_locales =taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_locales) != 0:
        for i in lesionados_locales:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_champions(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_champions(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totalesv:
            sumar_gol_champions(i)
        asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_champions(i)
    amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_visitantes) != 0:
        for i in lesionados_visitantes:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_champions(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_champions(i,0,1) 
    print("Global")
    print(f'{club1} {goallocal+goles_visitnates}-{goalsvisitor+goles_locales} {club2}')
    goles_loca = goallocal + goles_visitnates
    goles_visi = goalsvisitor + goles_locales
    if goallocal > goalsvisitor:
        sumar_ranking_club(club1,3)
        sumar_ranking_club(club2,0)
    elif goallocal < goalsvisitor:
        sumar_ranking_club(club1,0)
        sumar_ranking_club(club2,3)
    else:
        sumar_ranking_club(club1,1)
        sumar_ranking_club(club2,1)
    if goles_loca > goles_visi:
        print(F"PASA {club1}")
        ganador = club1
    elif goles_visi > goles_loca:    
        print(f"PASA {club2}")
        ganador = club2
    else:
        penalty_local = fct.numero_random() 
        penalty_visitor = fct.numero_random()
        if penalty_local == penalty_visitor:
            aux = penalty_visitor - 1
            penalty_visitor = aux    
        print("PENALES")
        input("")
        print(f'{club1} {penalty_local} - {penalty_visitor} {club2}') 
        if penalty_local > penalty_visitor:
            ganador = club1
        else:
            ganador = club2    
    return ganador

def partidos_europa_vuelta(club1,club2,goles_locales,goles_visitnates):
    print("partido de ida")
    print(f"{club2} {goles_locales}-{goles_visitnates} {club1}")
    input("")
    jugadores_sancionados_locales = sancionados_europa(club1)
    jugadores_sancionados_visitantes = sancionados_europa(club2)
    desancionar_europa(club1)
    desancionar_europa(club2)
    jugadores_lesionados_locales = lesionados(club1)
    jugadores_lesionados_visitantes = lesionados(club2)
    deslesionar(club1)
    deslesionar(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totales:
            sumar_gol_europa(i)
        asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_europa(i)
    amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    rojas_locales =taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_locales) != 0:
        for i in lesionados_locales:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_europa(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_europa(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        for i in goles_totalesv:
            sumar_gol_europa(i)
        asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_europa(i)
    amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
    if len(lesionados_visitantes) != 0:
        for i in lesionados_visitantes:
            actualizar_lesionados(i[0],i[1])
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_europa(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_europa(i,0,1) 
    print("Global")
    print(f'{club1} {goallocal+goles_visitnates}-{goalsvisitor+goles_locales} {club2}')
    goles_loca = goallocal + goles_visitnates
    goles_visi = goalsvisitor + goles_locales
    if goallocal > goalsvisitor:
        sumar_ranking_club(club1,3)
        sumar_ranking_club(club2,0)
    elif goallocal < goalsvisitor:
        sumar_ranking_club(club1,0)
        sumar_ranking_club(club2,3)
    else:
        sumar_ranking_club(club1,1)
        sumar_ranking_club(club2,1)
    if goles_loca > goles_visi:
        print(F"PASA {club1}")
        ganador = club1
    elif goles_visi > goles_loca:    
        print(f"PASA {club2}")
        ganador = club2
    else:
        penalty_local = fct.numero_random() 
        penalty_visitor = fct.numero_random()
        if penalty_local == penalty_visitor:
            aux = penalty_visitor - 1
            penalty_visitor = aux    
        print("PENALES")
        input("")
        print(f'{club1} {penalty_local} - {penalty_visitor} {club2}') 
        if penalty_local > penalty_visitor:
            ganador = club1
        else:
            ganador = club2    
    return ganador

def sancionados_eurocopa(club,apto):
    jugadores_sancionados = []
    for jugador in jugadores_selecciones:
        if jugador["equipo"] == club:
            if jugador["sancionado"] == True:
                sancionado = jugador["nombre"]
                jugadores_sancionados.append(sancionado)
            if apto == 1:
                if jugador["nombre"] == nombre_del_jugador:
                    if jugador["sancionado"] == False:
                        for jug in jugadores:
                            if jug["nombre"] == nombre_del_jugador:
                                jug["partidos"] +=1
    return jugadores_sancionados 
def desancionar_eurocopa(club):
    for jugador in jugadores_selecciones:
        if jugador["equipo"] == club:
            jugador["sancionado"] = False
def sumar_gol_eurocopa(nombre_jugador):
    for jugador in jugadores_selecciones:
        if jugador["nombre"] == nombre_jugador:
            jugador["goles"] += 1
            for jug in jugadores:
                if jug["nombre"] == nombre_jugador:
                    jug["MVP"] += 2
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.5
            break
def sumar_asistencia_eurocopa(nombre_jugador):
    for jugador in jugadores_selecciones:
        if jugador["nombre"] == nombre_jugador:
            jugador["asistencias"] += 1
            for jug in jugadores:
                if jug["nombre"] == nombre_jugador:
                    jug["MVP"] += 1
            if jugador["nombre"] == nombre_del_jugador:
                player["valoracion"] += 0.25
            break        
def actualizar_rustico_eurocopa(nombre_jugador,ama,roja):
    if ama == 1:
        for jugador in jugadores_selecciones:
            if jugador["nombre"] == nombre_jugador:
                jugador["amarillas"] += 1
                jugador["sancion"] += 1
                for jug in jugadores:
                    if jug["nombre"] == nombre_jugador:
                        jug["MVP"] -= 1
                if jugador["sancion"] >= 3:
                    jugador["sancionado"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.25
    if roja == 1:  
        for jugador in jugadores_selecciones:
            if jugador["nombre"] == nombre_jugador:
                jugador["rojas"] += 1    
                jugador["sancion"] = 3
                for jug in jugadores:
                    if jug["nombre"] == nombre_jugador:
                        jug["MVP"] -= 3
                jugador["sancionado"] = True
                if jugador["nombre"] == nombre_del_jugador:
                    player["valoracion"] -= 0.5

def goleadores_selecciones(division):
    if division == "e":
        division = "europa"
    elif division == "a":
        division = "america"  
    elif division == "f":
        division = "africa"
    elif division == "s":
        division = "asia"  
    input("mostrar tabla de goleadores")  
    print("")
    jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
    contador = 0
    import colorama
    colorama.init()
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
def asistentes_selecciones(division):
    if division == "e":
        division = "europa"
    elif division == "a":
        division = "america"   
    elif division == "f":
        division = "africa"
    elif division == "s":
        division = "asia"   
    input("mostrar tabla de asistentes")  
    print("")
    contador = 0
    asistentes_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
    import colorama
    colorama.init()
    for i, j in enumerate(asistentes_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("")        

def rojas_selecciones(division):
    if division == "e":
        division = "europa"
    elif division == "a":
        division = "america"  
    elif division == "f":
        division = "africa"
    elif division == "s":
        division = "asia"  
    input("mostrar tabla de rojas")  
    print("")
    jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["rojas"], reverse=True)
    import colorama
    colorama.init()
    contador = 0
    for i, j in enumerate(jugadores_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['rojas']} {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['rojas']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("") 
def amarillas_selecciones(division):
    if division == "e":
        division = "europa"
    elif division == "a":
        division = "america"
    elif division == "f":
        division = "africa"
    elif division == "s":
        division = "asia"    
    input("mostrar tabla de amarillas")  
    print("")
    asistentes_ordenados = sorted(jugadores_selecciones, key=lambda j: j["amarillas"], reverse=True)
    import colorama
    colorama.init()
    contador = 0
    for i, j in enumerate(asistentes_ordenados):
        if j["division"] == division:
            if contador == 10:
                break
            if contador == 0:
                print(f"\033[32m{j['amarillas']} {j['nombre']} - {j['equipo']}\033[0m")
            else:
                print(f"{j['amarillas']} {j['nombre']} - {j['equipo']}")
            contador += 1
    print("")

def mostrar_datos_mundiales():   
    input("mostrar la tabla de los goleadores del munidal")
    print("")
    print("Tabla de goleadores del munidal")
    print("")
    jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['goles']} {j['nombre']} - {j['equipo']}")
    input("mostrar tabla de asistentes del munidal")
    print("")
    print("Tabla de asistentes del munidal")
    print("")
    jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['asistencias']} {j['nombre']} - {j['equipo']}")
    input("mostrar tabla de amarillas del munidal")  
    print("")
    jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["amarillas"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['amarillas']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['amarillas']} {j['nombre']} - {j['equipo']}")
    print("")
    input("mostrar tabla de rojas del munidal")  
    print("")
    jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["rojas"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f" {j['rojas']} {j['nombre']} - {j['equipo']}\033[0m")
        else:
            print(f" {j['rojas']} {j['nombre']} - {j['equipo']}")

def definir_datos_fin(division,catogoria):
    if division == "e":
        if catogoria == 1:
            print("datos de la eurocopa")
            input("goleador")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "europa":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'goleador de la eurocopa'
                            logros_anuales.append(logro)
                            player["dinero"] += 500000
                            player["valoracion"] += 2
                    else:
                        print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
                    contador += 1
            print("")
            input("asistente")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "europa":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'asistente de la eurocopa'
                            logros_anuales.append(logro)
                            player["dinero"] += 250000
                            player["valoracion"] += 2
                    else:
                        print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
                    contador += 1
            print("") 
        elif catogoria == 2:
            print("datos de la clasificacion al mundial europea")
            input("goleador")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "europa":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'goleador de la clasificacion al mundial europea'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                            player["dinero"] += 500000
                    else:
                        print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
                    contador += 1
                    
            print("")
            input("asistente")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "europa":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'asistente de la clasificacion al mundial europea'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                    else:
                        print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
                    contador += 1
                    
            print("") 
    if division == "a":
        if catogoria == 1:
            print("datos de la copa america")
            input("goleador")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "america":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'goleador de la copa america'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                            player["dinero"] += 500000
                    else:
                        print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
                    contador += 1
            print("")
            input("asistente")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "america":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'asistente de la copa america'
                            logros_anuales.append(logro)
                            player["dinero"] += 250000
                            player["valoracion"] += 2
                    else:
                        print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
                    contador += 1
            print("") 
        elif catogoria == 2:
            print("datos de la clasificacion al mundial americana")
            input("goleador")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "america":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'goleador de la clasificacion al mundial americana'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                    else:
                        print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
                    contador += 1
                    
            print("")
            input("asistente")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "america":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'asistente de la clasificacion al mundial americana'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                    else:
                        print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
                    contador += 1
                    
            print("") 
    if division == "f":
        if catogoria == 1:
            print("datos de la copa africana")
            input("goleador")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "africa":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'goleador de la copa africana'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                            player["dinero"] += 500000
                    else:
                        print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
                    contador += 1
            print("")
            input("asistente")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "africa":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'asistente de la copa africana'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                            player["dinero"] += 250000
                    else:
                        print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
                    contador += 1
            print("") 
        elif catogoria == 2:
            print("datos de la clasificacion al mundial africana")
            input("goleador")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "africa":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'goleador de la clasificacion al mundial africana'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                    else:
                        print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
                    contador += 1
                    
            print("")
            input("asistente")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "africa":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'asistente de la clasificacion al mundial africana'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                    else:
                        print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
                    contador += 1
                    
            print("") 
    if division == "s":
        if catogoria == 1:
            print("datos de la copa asiatica")
            input("goleador")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "asia":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'goleador de la copa asiatica'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                            player["dinero"] += 500000
                    else:
                        print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
                    contador += 1
            print("")
            input("asistente")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "asia":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'asistente de la copa asiatica'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                            player["dinero"] += 250000
                    else:
                        print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
                    contador += 1
            print("") 
        elif catogoria == 2:
            print("datos de la clasificacion al mundial asiatica")
            input("goleador")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "asia":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'goleador de la clasificacion al mundial asiatica'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                    else:
                        print(f"{j['goles']} {j['nombre']} - {j['equipo']}")
                    contador += 1
                    
            print("")
            input("asistente")  
            print("")
            jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
            contador = 0
            import colorama
            colorama.init()
            for i, j in enumerate(jugadores_ordenados):
                if j["division"] == "asia":
                    if contador == 1:
                        break
                    if contador == 0:
                        print(f"\033[32m{j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
                        if j['nombre'] == player["nombre"]:
                            logro = f'asistente de la clasificacion al mundial asiatica'
                            logros_anuales.append(logro)
                            player["valoracion"] += 2
                    else:
                        print(f"{j['asistencias']} {j['nombre']} - {j['equipo']}")
                    contador += 1
                    
            print("") 

def mostrar_datos_selecciones(division):
    if division == 1:
        goleadores_selecciones("e")
        asistentes_selecciones("e")
        amarillas_selecciones("e")
        rojas_selecciones("e")
    if division == 2:
        goleadores_selecciones("a")
        asistentes_selecciones("a")
        amarillas_selecciones("a")
        rojas_selecciones("a")
    if division == 3:
        goleadores_selecciones("f")
        asistentes_selecciones("f")
        amarillas_selecciones("f")
        rojas_selecciones("f")
    if division == 4:
        goleadores_selecciones("s")
        asistentes_selecciones("s")
        amarillas_selecciones("s")
        rojas_selecciones("s")
        
def partido_eurocopa(club1,club2,apto):
    print("")
    input("")
    jugadores_sancionados_locales = sancionados_eurocopa(club1,apto)
    jugadores_sancionados_visitantes = sancionados_eurocopa(club2,apto)
    desancionar_eurocopa(club1)
    desancionar_eurocopa(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado_selecciones(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores_selecciones(club1,goallocal,jugadores_sancionados_locales,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
        for i in goles_totales:
            sumar_gol_eurocopa(i)
        asistencias_local = taq.asistentes_selecciones(club1,goallocal,jugadores_sancionados_locales,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_eurocopa(i)
    amarillas_locales = taq.amarillas_selecciones(club1,jugadores_sancionados_locales,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
    rojas_locales = taq.rojas_selecciones(club1,jugadores_sancionados_locales,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_eurocopa(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_eurocopa(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores_selecciones(club2,goalsvisitor,jugadores_sancionados_visitantes,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
        for i in goles_totalesv:
            sumar_gol_eurocopa(i)
        asistenciasvisitor = taq.asistentes_selecciones(club2,goalsvisitor,jugadores_sancionados_visitantes,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_eurocopa(i)
    amarillas_visitor = taq.amarillas_selecciones(club2,jugadores_sancionados_visitantes,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
    rojas_visitor = taq.rojas_selecciones(club2,jugadores_sancionados_visitantes,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_eurocopa(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_eurocopa(i,0,1) 
    if goallocal > goalsvisitor:
        ganador = club1
    elif goallocal < goalsvisitor:
        ganador = club2
    else:
        print("PENALES")
        input("")
        penaleslocal = fct.numero_random()
        penales_visitor = fct.numero_random()
        if penaleslocal == penales_visitor:
            penales_visitor -= 1
        print(f'{club1} {penaleslocal}-{penales_visitor} {club2}')
        if penaleslocal > penales_visitor:
            ganador = club1
        else: ganador = club2
    if goallocal > goalsvisitor:
        sumar_ranking_selecion(club1,3)
        sumar_ranking_selecion(club2,0)
    elif goallocal < goalsvisitor:
        sumar_ranking_selecion(club1,0)
        sumar_ranking_selecion(club2,3)
    else:
        sumar_ranking_selecion(club1,1)
        sumar_ranking_selecion(club2,1)    
    return ganador

def partido_eurocopa_c(club1,club2,apto,tabla):
    print("")
    input("")
    jugadores_sancionados_locales = sancionados_eurocopa(club1,apto)
    jugadores_sancionados_visitantes = sancionados_eurocopa(club2,apto)
    desancionar_eurocopa(club1)
    desancionar_eurocopa(club2)
    result,club1,goallocal,goalsvisitor,club2 = fct.resultado_selecciones(club1,club2)
    if goallocal != 0:
        goles_totales = taq.goleadores_selecciones(club1,goallocal,jugadores_sancionados_locales,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
        for i in goles_totales:
            sumar_gol_eurocopa(i)
        asistencias_local = taq.asistentes_selecciones(club1,goallocal,jugadores_sancionados_locales,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
        if len(asistencias_local) != 0:
            for i in asistencias_local:
                sumar_asistencia_eurocopa(i)
    amarillas_locales = taq.amarillas_selecciones(club1,jugadores_sancionados_locales,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
    rojas_locales = taq.rojas_selecciones(club1,jugadores_sancionados_locales,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
    if len(amarillas_locales) != 0:
        for i in amarillas_locales:
            actualizar_rustico_eurocopa(i,1,0)     
    if len(rojas_locales) != 0:
        for i in rojas_locales:
            actualizar_rustico_eurocopa(i,0,1) 
    if goalsvisitor != 0:
        goles_totalesv = taq.goleadores_selecciones(club2,goalsvisitor,jugadores_sancionados_visitantes,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
        for i in goles_totalesv:
            sumar_gol_eurocopa(i)
        asistenciasvisitor = taq.asistentes_selecciones(club2,goalsvisitor,jugadores_sancionados_visitantes,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
        if len(asistenciasvisitor) != 0:
            for i in asistenciasvisitor:
                sumar_asistencia_eurocopa(i)
    amarillas_visitor = taq.amarillas_selecciones(club2,jugadores_sancionados_visitantes,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
    rojas_visitor = taq.rojas_selecciones(club2,jugadores_sancionados_visitantes,player["nacionalidad"],player["valoracion"],player["nombre"],apto)
    if len(amarillas_visitor) != 0:
        for i in amarillas_visitor:
            actualizar_rustico_eurocopa(i,1,0)
    if len(rojas_visitor) != 0:
        for i in rojas_visitor:
            actualizar_rustico_eurocopa(i,0,1) 
    if goallocal > goalsvisitor:
        fct.actualizar_tabla(tabla,club1,3,goallocal,goalsvisitor,1,0,0)
        fct.actualizar_tabla(tabla,club2,0,goalsvisitor,goallocal,0,0,1)
    elif goallocal < goalsvisitor:
        fct.actualizar_tabla(tabla,club1,0,goallocal,goalsvisitor,0,0,1)
        fct.actualizar_tabla(tabla,club2,3,goalsvisitor,goallocal,1,0,0)
    else:
        fct.actualizar_tabla(tabla,club1,1,goallocal,goalsvisitor,0,1,0)
        fct.actualizar_tabla(tabla,club2,1,goalsvisitor,goallocal,0,1,0)
    if goallocal > goalsvisitor:
        sumar_ranking_selecion(club1,3)
        sumar_ranking_selecion(club2,0)
    elif goallocal < goalsvisitor:
        sumar_ranking_selecion(club1,0)
        sumar_ranking_selecion(club2,3)
    else:
        sumar_ranking_selecion(club1,1)
        sumar_ranking_selecion(club2,1)  

def jugar_eurocopa():
    apto = 0
    if nacionalidad == "España": 
        if player["valoracion"] > 60: 
            apto = 1
            print("Tu seleccionado te a convocado para la eurocopa")
    elif nacionalidad == "Francia":
        if player["valoracion"] > 60:
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Holanda":
        if player["valoracion"] > 50:
            apto = 1
            print("Tu seleccionado te a convocado para la eurocopa")
    elif nacionalidad == "Inglaterra":
        if player["valoracion"] > 60: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Italia":
        if player["valoracion"] > 60:
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Croacia":
        if player["valoracion"] > 50: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Belgica":
        if player["valoracion"] > 40:
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Portugal":
        if player["valoracion"] > 50: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Suiza":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Dinamarca":
        if player["valoracion"] > 40: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Polonia":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Noruega":
        if player["valoracion"] > 30:
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Alemania":
        if player["valoracion"] > 60: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Gales":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Serbia":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    elif nacionalidad == "Suecia":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la eurocopa")
            apto = 1
    else: apto = 0
    print("")
    print("EUROCOPA")
    equipos_eurocopa_ = ["España","Francia","Holanda","Inglaterra","Italia","Croacia","Belgica","Portugal","Suiza","Dinamarca","Polonia","Noruega","Alemania","Gales","Serbia","Suecia"] 
    equipos_eurocopa = mezclar_lista(equipos_eurocopa_)
    cuartos_eurocopa = []
    semis_eurocopa = []
    final_eurocopa = []
    input("")
    print("OCTAVOS DE FINAL")
    print("")
    print(f"{equipos_eurocopa[0]} vs {equipos_eurocopa[15]}")
    print(f"{equipos_eurocopa[1]} vs {equipos_eurocopa[14]}")
    print(f"{equipos_eurocopa[2]} vs {equipos_eurocopa[13]}")
    print(f"{equipos_eurocopa[3]} vs {equipos_eurocopa[12]}")
    print(f"{equipos_eurocopa[4]} vs {equipos_eurocopa[11]}")
    print(f"{equipos_eurocopa[5]} vs {equipos_eurocopa[10]}")
    print(f"{equipos_eurocopa[6]} vs {equipos_eurocopa[9]}")
    print(f"{equipos_eurocopa[7]} vs {equipos_eurocopa[8]}")
    ganador1 = partido_eurocopa(equipos_eurocopa[0],equipos_eurocopa[15],apto)
    cuartos_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_eurocopa[1],equipos_eurocopa[14],apto)
    cuartos_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_eurocopa[2],equipos_eurocopa[13],apto)
    cuartos_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_eurocopa[3],equipos_eurocopa[12],apto)
    cuartos_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_eurocopa[4],equipos_eurocopa[11],apto)
    cuartos_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_eurocopa[5],equipos_eurocopa[10],apto)
    cuartos_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_eurocopa[6],equipos_eurocopa[9],apto)
    cuartos_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_eurocopa[7],equipos_eurocopa[8],apto)
    cuartos_eurocopa.append(ganador1)
    mostrar_datos_selecciones(1)
    input("")
    print("CUARTOS DE FINAL")
    print("")
    print(f"{cuartos_eurocopa[0]} vs {cuartos_eurocopa[7]}")
    print(f"{cuartos_eurocopa[1]} vs {cuartos_eurocopa[6]}")
    print(f"{cuartos_eurocopa[2]} vs {cuartos_eurocopa[5]}")
    print(f"{cuartos_eurocopa[3]} vs {cuartos_eurocopa[4]}")
    ganador1 = partido_eurocopa(cuartos_eurocopa[0],cuartos_eurocopa[7],apto)
    semis_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(cuartos_eurocopa[1],cuartos_eurocopa[6],apto)
    semis_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(cuartos_eurocopa[2],cuartos_eurocopa[5],apto)
    semis_eurocopa.append(ganador1)
    ganador1 = partido_eurocopa(cuartos_eurocopa[3],cuartos_eurocopa[4],apto)
    semis_eurocopa.append(ganador1)
    mostrar_datos_selecciones(1)
    input("")
    print("SEMIFINALES")
    print("")
    print(f"{semis_eurocopa[0]} vs {semis_eurocopa[3]}")
    print(f"{semis_eurocopa[1]} vs {semis_eurocopa[2]}")
    ganador1 = partido_eurocopa(semis_eurocopa[0],semis_eurocopa[3],apto)
    final_eurocopa.append(ganador1)
    if apto == 1:
        if ganador1 == semis_eurocopa[0]:
            perdedor = semis_eurocopa[3]
        else :
            perdedor = semis_eurocopa[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinales de la eurocopa con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    ganador1 = partido_eurocopa(semis_eurocopa[1],semis_eurocopa[2],apto)
    final_eurocopa.append(ganador1)
    if apto == 1:
        if ganador1 == semis_eurocopa[1]:
            perdedor = semis_eurocopa[2]
        else :
            perdedor = semis_eurocopa[1]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinales de la eurocopa con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_selecciones(1)
    input("")
    print("FINAL")
    print("")
    print(f"{final_eurocopa[0]} vs {final_eurocopa[1]}")
    campeon_de_la_eurocopa = partido_eurocopa(final_eurocopa[0],final_eurocopa[1],apto)
    print("")
    print(f'{campeon_de_la_eurocopa} CAMPEON DE LA EUROCOPA')
    print("")
    if apto == 1:
        if campeon_de_la_eurocopa == final_eurocopa[0]:
            perdedor = final_eurocopa[1]
        else :
            perdedor = final_eurocopa[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'finalista de la eurocopa con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_selecciones(1)
    return campeon_de_la_eurocopa    
    
def jugar_copa_america():
    apto = 0
    if nacionalidad == "Argentina": 
        if player["valoracion"] > 60: 
            apto = 1
            print("Tu seleccionado te a convocado para la copa america")
    elif nacionalidad == "Uruguay":
        if player["valoracion"] > 60:
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Paraguay":
        if player["valoracion"] > 30:
            apto = 1
            print("Tu seleccionado te a convocado para la copa america")
    elif nacionalidad == "Chile":
        if player["valoracion"] > 50: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Bolivia":
        if player["valoracion"] > 30:
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Brasil":
        if player["valoracion"] > 60: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Peru":
        if player["valoracion"] > 40:
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Colombia":
        if player["valoracion"] > 50: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Ecuador":
        if player["valoracion"] > 40: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Venezuela":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Mexico":
        if player["valoracion"] > 40: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Estados Unidos":
        if player["valoracion"] > 40:
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Canada":
        if player["valoracion"] > 40: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Costa Rica":
        if player["valoracion"] > 20: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Cuba":
        if player["valoracion"] > 20: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    elif nacionalidad == "Honduras":
        if player["valoracion"] > 20: 
            print("Tu seleccionado te a convocado para la copa america")
            apto = 1
    else: apto = 0
    input("")
    print("COPA AMERICA")
    
    equipos_copa_america_ = ["Argentina","Uruguay","Paraguay","Chile","Bolivia","Brasil","Peru","Colombia","Ecuador","Venezuela","Mexico","Estados Unidos","Canada","Costa Rica","Cuba","Honduras"] 
    equipos_copa_america = mezclar_lista(equipos_copa_america_)
    cuartos_copa_america = []
    semis_copa_america = []
    final_copa_america = []
    print("")
    print("OCTAVOS DE FINAL")
    print("")
    print(f"{equipos_copa_america[0]} vs {equipos_copa_america[15]}")
    print(f"{equipos_copa_america[1]} vs {equipos_copa_america[14]}")
    print(f"{equipos_copa_america[2]} vs {equipos_copa_america[13]}")
    print(f"{equipos_copa_america[3]} vs {equipos_copa_america[12]}")
    print(f"{equipos_copa_america[4]} vs {equipos_copa_america[11]}")
    print(f"{equipos_copa_america[5]} vs {equipos_copa_america[10]}")
    print(f"{equipos_copa_america[6]} vs {equipos_copa_america[9]}")
    print(f"{equipos_copa_america[7]} vs {equipos_copa_america[8]}")
    ganador1 = partido_eurocopa(equipos_copa_america[0],equipos_copa_america[15],apto)
    cuartos_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_america[1],equipos_copa_america[14],apto)
    cuartos_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_america[2],equipos_copa_america[13],apto)
    cuartos_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_america[3],equipos_copa_america[12],apto)
    cuartos_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_america[4],equipos_copa_america[11],apto)
    cuartos_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_america[5],equipos_copa_america[10],apto)
    cuartos_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_america[6],equipos_copa_america[9],apto)
    cuartos_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_america[7],equipos_copa_america[8],apto)
    cuartos_copa_america.append(ganador1)
    mostrar_datos_selecciones(2)
    input("")
    print("CUARTOS DE FINAL")
    print("")
    print(f"{cuartos_copa_america[0]} vs {cuartos_copa_america[7]}")
    print(f"{cuartos_copa_america[1]} vs {cuartos_copa_america[6]}")
    print(f"{cuartos_copa_america[2]} vs {cuartos_copa_america[5]}")
    print(f"{cuartos_copa_america[3]} vs {cuartos_copa_america[4]}")
    ganador1 = partido_eurocopa(cuartos_copa_america[0],cuartos_copa_america[7],apto)
    semis_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(cuartos_copa_america[1],cuartos_copa_america[6],apto)
    semis_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(cuartos_copa_america[2],cuartos_copa_america[5],apto)
    semis_copa_america.append(ganador1)
    ganador1 = partido_eurocopa(cuartos_copa_america[3],cuartos_copa_america[4],apto)
    semis_copa_america.append(ganador1)
    mostrar_datos_selecciones(2)
    input("")
    print("SEMIFINALES")
    print("")
    print(f"{semis_copa_america[0]} vs {semis_copa_america[3]}")
    print(f"{semis_copa_america[1]} vs {semis_copa_america[2]}")
    ganador1 = partido_eurocopa(semis_copa_america[0],semis_copa_america[3],apto)
    final_copa_america.append(ganador1)
    if apto == 1:
        if ganador1 == semis_copa_america[0]:
            perdedor = semis_copa_america[3]
        else :
            perdedor = semis_copa_america[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinalista de la copa america con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    ganador1 = partido_eurocopa(semis_copa_america[1],semis_copa_america[2],apto)
    final_copa_america.append(ganador1)
    if apto == 1:
        if ganador1 == semis_copa_america[1]:
            perdedor = semis_copa_america[2]
        else :
            perdedor = semis_copa_america[1]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinalista de la copa america con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_selecciones(2)
    input("")
    print("FINAL")
    print("")
    print(f"{final_copa_america[0]} vs {final_copa_america[1]}")
    campeon_de_la_copa_america = partido_eurocopa(final_copa_america[0],final_copa_america[1],apto)
    print("")
    print(f'{campeon_de_la_copa_america} CAMPEON DE LA COPA AMERICA')
    print("")
    
    if apto == 1:
        if campeon_de_la_copa_america == final_copa_america[0]:
            perdedor = final_copa_america[1]
        else :
            perdedor = final_copa_america[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'finalista de la copa america con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_selecciones(2)
    return campeon_de_la_copa_america
  
def jugar_copa_africa():
    
    apto = 0
    if nacionalidad == "Egipto": 
        if player["valoracion"] > 40: 
            apto = 1
            print("Tu seleccionado te a convocado para la copa africa")
    elif nacionalidad == "Senegal":
        if player["valoracion"] > 40:
            print("Tu seleccionado te a convocado para la copa africa")
            apto = 1
    elif nacionalidad == "Tunez":
        if player["valoracion"] > 30:
            apto = 1
            print("Tu seleccionado te a convocado para la copa africa")
    elif nacionalidad == "Camerun":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la copa africa")
            apto = 1
    elif nacionalidad == "Marruecos":
        if player["valoracion"] > 40:
            print("Tu seleccionado te a convocado para la copa africa")
            apto = 1
    elif nacionalidad == "Nigeria":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la copa africa")
            apto = 1
    elif nacionalidad == "Ghana":
        if player["valoracion"] > 30:
            print("Tu seleccionado te a convocado para la copa africa")
            apto = 1
    elif nacionalidad == "Argelia":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la copa africa")
            apto = 1
    else: apto = 0
    input("")
    print("COPA AFRICA")
    equipos_copa_africa_ = ["Egipto","Senegal","Tunez","Camerun","Marruecos","Nigeria","Ghana","Argelia"] 
    equipos_copa_africa = mezclar_lista(equipos_copa_africa_)
    semis_copa_africa = []
    final_copa_africa = []
    input("")
    print("CUARTOS DE FINAL")
    print("")
    print(f"{equipos_copa_africa[0]} vs {equipos_copa_africa[7]}")
    print(f"{equipos_copa_africa[1]} vs {equipos_copa_africa[6]}")
    print(f"{equipos_copa_africa[2]} vs {equipos_copa_africa[5]}")
    print(f"{equipos_copa_africa[3]} vs {equipos_copa_africa[4]}")
    ganador1 = partido_eurocopa(equipos_copa_africa[0],equipos_copa_africa[7],apto)
    semis_copa_africa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_africa[1],equipos_copa_africa[6],apto)
    semis_copa_africa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_africa[2],equipos_copa_africa[5],apto)
    semis_copa_africa.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_africa[3],equipos_copa_africa[4],apto)
    semis_copa_africa.append(ganador1)
    mostrar_datos_selecciones(3)
    input("")
    print("SEMIFINALES")
    print("")
    print(f"{semis_copa_africa[0]} vs {semis_copa_africa[3]}")
    print(f"{semis_copa_africa[1]} vs {semis_copa_africa[2]}")
    ganador1 = partido_eurocopa(semis_copa_africa[0],semis_copa_africa[3],apto)
    final_copa_africa.append(ganador1)
    if apto == 1:
        if ganador1 == semis_copa_africa[0]:
            perdedor = semis_copa_africa[3]
        else :
            perdedor = semis_copa_africa[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinalista de la copa africana con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    ganador1 = partido_eurocopa(semis_copa_africa[1],semis_copa_africa[2],apto)
    final_copa_africa.append(ganador1)
    if apto == 1:
        if ganador1 == semis_copa_africa[1]:
            perdedor = semis_copa_africa[2]
        else :
            perdedor = semis_copa_africa[1]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinalista de la copa africana con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_selecciones(3)
    input("")
    print("FINAL")
    print("")
    print(f"{final_copa_africa[0]} vs {final_copa_africa[1]}")
    campeon_de_la_copa_africa = partido_eurocopa(final_copa_africa[0],final_copa_africa[1],apto)
    print("")
    print(f'{campeon_de_la_copa_africa} CAMPEON DE LA COPA AFRICANA')
    print("")
    if apto == 1:
        if campeon_de_la_copa_africa == final_copa_africa[0]:
            perdedor = final_copa_africa[1]
        else :
            perdedor = final_copa_africa[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'finalista de la copa africana con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_selecciones(3)
    return campeon_de_la_copa_africa
  
def jugar_copa_asia():
    apto = 0
    if nacionalidad == "Iran": 
        if player["valoracion"] > 30: 
            apto = 1
            print("Tu seleccionado te a convocado para la copa asia")
    elif nacionalidad == "Corea del Sur":
        if player["valoracion"] > 30:
            print("Tu seleccionado te a convocado para la copa asia")
            apto = 1
    elif nacionalidad == "Japon":
        if player["valoracion"] > 40:
            apto = 1
            print("Tu seleccionado te a convocado para la copa asia")
    elif nacionalidad == "China":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la copa asia")
            apto = 1
    elif nacionalidad == "Arabia Saudita":
        if player["valoracion"] > 30:
            print("Tu seleccionado te a convocado para la copa asia")
            apto = 1
    elif nacionalidad == "Israel":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la copa asia")
            apto = 1
    elif nacionalidad == "Australia":
        if player["valoracion"] > 40:
            print("Tu seleccionado te a convocado para la copa asia")
            apto = 1
    elif nacionalidad == "Qatar":
        if player["valoracion"] > 30: 
            print("Tu seleccionado te a convocado para la copa asia")
            apto = 1
    else: apto = 0
    input("")
    print("COPA ASIA")
    equipos_copa_asia_ = ["Iran","Corea del Sur","Japon","China","Arabia Saudita","Israel","Australia","Qatar"] 
    equipos_copa_asia = mezclar_lista(equipos_copa_asia_)
    semis_copa_asia = []
    final_copa_asia = []
    input("")
    print("CUARTOS DE FINAL")
    print("")
    print(f"{equipos_copa_asia[0]} vs {equipos_copa_asia[7]}")
    print(f"{equipos_copa_asia[1]} vs {equipos_copa_asia[6]}")
    print(f"{equipos_copa_asia[2]} vs {equipos_copa_asia[5]}")
    print(f"{equipos_copa_asia[3]} vs {equipos_copa_asia[4]}")
    ganador1 = partido_eurocopa(equipos_copa_asia[0],equipos_copa_asia[7],apto)
    semis_copa_asia.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_asia[1],equipos_copa_asia[6],apto)
    semis_copa_asia.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_asia[2],equipos_copa_asia[5],apto)
    semis_copa_asia.append(ganador1)
    ganador1 = partido_eurocopa(equipos_copa_asia[3],equipos_copa_asia[4],apto)
    semis_copa_asia.append(ganador1)
    mostrar_datos_selecciones(4)
    input("")
    print("SEMIFINALES")
    print("")
    print(f"{semis_copa_asia[0]} vs {semis_copa_asia[3]}")
    print(f"{semis_copa_asia[1]} vs {semis_copa_asia[2]}")
    ganador1 = partido_eurocopa(semis_copa_asia[0],semis_copa_asia[3],apto)
    final_copa_asia.append(ganador1)
    if apto == 1:
        if ganador1 == semis_copa_asia[0]:
            perdedor = semis_copa_asia[3]
        else :
            perdedor = semis_copa_asia[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinalista de la copa asiatica con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    ganador1 = partido_eurocopa(semis_copa_asia[1],semis_copa_asia[2],apto)
    final_copa_asia.append(ganador1)
    if apto == 1:
        if ganador1 == semis_copa_asia[1]:
            perdedor = semis_copa_asia[2]
        else :
            perdedor = semis_copa_asia[1]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinalista de la copa asiatica con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_selecciones(4)
    input("")
    print("FINAL")
    print("")
    print(f"{final_copa_asia[0]} vs {final_copa_asia[1]}")
    campeon_de_la_copa_asia = partido_eurocopa(final_copa_asia[0],final_copa_asia[1],apto)
    print("")
    print(f'{campeon_de_la_copa_asia} CAMPEON DE LA COPA ASIATICA')
    print("")
    if apto == 1:
        if campeon_de_la_copa_asia == final_copa_asia[0]:
            perdedor = final_copa_asia[1]
        else :
            perdedor = final_copa_asia[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'finalista de la copa asiatica con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_selecciones(4)
    return campeon_de_la_copa_asia   
  
def definir_equipos(equipo):
    if equipo == "España":  equipos = España
    elif equipo == "Francia": equipos = Francia
    elif equipo == "Holanda": equipos = Holanda
    elif equipo == "Inglaterra": equipos = Inglaterra
    elif equipo == "Italia": equipos = Italia
    elif equipo == "Croacia": equipos = Croacia
    elif equipo == "Belgica": equipos = Belgica
    elif equipo == "Portugal": equipos = Portugal
    elif equipo == "Suiza": equipos = Suiza
    elif equipo == "Dinamarca": equipos = Dinamarca
    elif equipo == "Polonia": equipos = Polonia
    elif equipo == "Noruega": equipos = Noruega
    elif equipo == "Alemania": equipos = Alemania
    elif equipo == "Gales": equipos = Gales
    elif equipo == "Serbia": equipos = Serbia
    elif equipo == "Suecia": equipos = Suecia
    elif equipo == "Argentina": equipos = Argentina
    elif equipo == "Uruguay": equipos = Uruguay
    elif equipo == "Paraguay": equipos = Paraguay
    elif equipo == "Chile": equipos = Chile
    elif equipo == "Bolivia": equipos = Bolivia
    elif equipo == "Brasil": equipos = Brasil
    elif equipo == "Peru": equipos = Peru
    elif equipo == "Colombia": equipos = Colombia
    elif equipo == "Ecuador": equipos = Ecuador
    elif equipo == "Venezuela": equipos = Venezuela
    elif equipo == "Mexico": equipos = Mexico
    elif equipo == "Estados Unidos": equipos = Estados_Unidos
    elif equipo == "Canada": equipos = Canada
    elif equipo == "Costa Rica": equipos = Costa_Rica
    elif equipo == "Cuba": equipos = Cuba
    elif equipo == "Honduras": equipos = Honduras
    elif equipo == "Iran": equipos = Iran
    elif equipo == "Corea del Sur":equipos = Corea_del_Sur
    elif equipo == "Japon":equipos = Japon
    elif equipo == "China":equipos = China
    elif equipo == "Arabia Saudita":equipos = Arabia_Saudita
    elif equipo == "Israel":equipos = Israel
    elif equipo == "Australia": equipos = Australia
    elif equipo == "Qatar":  equipos = Qatar
    elif equipo == "Egipto": equipos = Egipto
    elif equipo == "Senegal":equipos = Senegal
    elif equipo == "Tunez":equipos = Tunez
    elif equipo == "Camerun": equipos = Camerun
    elif equipo == "Marruecos":equipos = Marruecos
    elif equipo == "Nigeria":equipos = Nigeria
    elif equipo == "Ghana":equipos = Ghana
    elif equipo == "Argelia": equipos = Argelia
    return equipos
def jugar_mundial(apto):
    print("MUNDIAL")
    clas_europa[0] = definir_equipos(clas_europa[0])
    clas_europa[1] = definir_equipos(clas_europa[1])
    clas_europa[2] = definir_equipos(clas_europa[2])
    clas_europa[3] = definir_equipos(clas_europa[3])
    clas_america[0] = definir_equipos(clas_america[0])
    clas_america[1] = definir_equipos(clas_america[1])
    clas_america[2] = definir_equipos(clas_america[2])
    clas_america[3] = definir_equipos(clas_america[3])
    clas_africa[0] = definir_equipos(clas_africa[0])
    clas_africa[1] = definir_equipos(clas_africa[1])
    clas_africa[2] = definir_equipos(clas_africa[2])
    clas_africa[3] = definir_equipos(clas_africa[3])
    clas_asia[0] = definir_equipos(clas_asia[0])
    clas_asia[1] = definir_equipos(clas_asia[1])
    clas_asia[2] = definir_equipos(clas_asia[2])
    clas_asia[3] = definir_equipos(clas_asia[3])
    input("")
    bo1 = [clas_europa[0],clas_europa[1],clas_europa[2],clas_europa[3]]
    bo2 = [clas_america[0],clas_america[1],clas_america[2],clas_america[3]]
    bo3 = [clas_africa[0],clas_africa[1],clas_africa[2],clas_africa[3]]
    bo4 = [clas_asia[0],clas_asia[1],clas_asia[2],clas_asia[3]]
    b1 = mezclar_lista(bo1)
    b2 = mezclar_lista(bo2)
    b3 = mezclar_lista(bo3)
    b4 = mezclar_lista(bo4)
    grupo_mundial_1 = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
    tabla_mundial_1 = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
    fixure_mundial_1,xxxx = generar_grupos(grupo_mundial_1)
        
    grupo_mundial_2 = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
    tabla_mundial_2 = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
    fixure_mundial_2,xxxx = generar_grupos(grupo_mundial_2)
        
    grupo_mundial_3 = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
    tabla_mundial_3 = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
    fixure_mundial_3,xxxx = generar_grupos(grupo_mundial_3)
        
    grupo_mundial_4 = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
    tabla_mundial_4 = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
    fixure_mundial_4,xxxx = generar_grupos(grupo_mundial_4)
    print("GRUPOS")
    input("")
    print("Grupo 1")
    print("")
    mostrar_grupos(grupo_mundial_1)
    input("")
    print("Grupo 2")
    print("")
    mostrar_grupos(grupo_mundial_2)
    input("")
    print("Grupo 3")
    print("")
    mostrar_grupos(grupo_mundial_3)
    input("")
    print("Grupo 4")
    print("")
    mostrar_grupos(grupo_mundial_4)
    input("")
    print("FECHA 1 DEL MUNDIAL")
    input("")
    fecha_1_s(fixure_mundial_1,1,apto,tabla_mundial_1)
    fecha_1_s(fixure_mundial_2,2,apto,tabla_mundial_2)
    fecha_1_s(fixure_mundial_3,3,apto,tabla_mundial_3)
    fecha_1_s(fixure_mundial_4,4,apto,tabla_mundial_4)
    fct.mostrar_tablas_fecha_fin(tabla_mundial_1,tabla_mundial_2,tabla_mundial_3,tabla_mundial_4)   
    mostrar_datos_mundiales()
    input("")
    print("FECHA 2 DEL MUNDIAL")
    input("")
    fecha_2_s(fixure_mundial_1,1,apto,tabla_mundial_1)
    fecha_2_s(fixure_mundial_2,2,apto,tabla_mundial_2)
    fecha_2_s(fixure_mundial_3,3,apto,tabla_mundial_3)
    fecha_2_s(fixure_mundial_4,4,apto,tabla_mundial_4)
    fct.mostrar_tablas_fecha_fin(tabla_mundial_1,tabla_mundial_2,tabla_mundial_3,tabla_mundial_4) 
    mostrar_datos_mundiales()
    input("")
    print("FECHA 3 DEL MUNDIAL")
    input("")
    fecha_3_s(fixure_mundial_1,1,apto,tabla_mundial_1)
    fecha_3_s(fixure_mundial_2,2,apto,tabla_mundial_2)
    fecha_3_s(fixure_mundial_3,3,apto,tabla_mundial_3)
    fecha_3_s(fixure_mundial_4,4,apto,tabla_mundial_4)
    fct.mostrar_tablas_fecha_fin(tabla_mundial_1,tabla_mundial_2,tabla_mundial_3,tabla_mundial_4) 
    mostrar_datos_mundiales()
    primero_mun_1,segundo_mun_1 = fct.obtener_primer_y_segundo_equipo(tabla_mundial_1)
    primero_mun_2,segundo_mun_2 = fct.obtener_primer_y_segundo_equipo(tabla_mundial_2)
    primero_mun_3,segundo_mun_3 = fct.obtener_primer_y_segundo_equipo(tabla_mundial_3)
    primero_mun_4,segundo_mun_4 = fct.obtener_primer_y_segundo_equipo(tabla_mundial_4)
    primeros = [primero_mun_1,primero_mun_2,primero_mun_3,primero_mun_4]
    segundos = [segundo_mun_1,segundo_mun_2,segundo_mun_3,segundo_mun_4]
    primeros_ = primeros.copy()
    random.shuffle(primeros_)
    segundos_  = segundos.copy()
    random.shuffle(segundos_)
    input("")
    print("CUARTOS DE FINAL")
    print("")
    print(primeros_[0],"vs",segundos_[0])
    print(primeros_[1],"vs",segundos_[1])
    print(primeros_[2],"vs",segundos_[2])
    print(primeros_[3],"vs",segundos_[3])
    semis_mundial = []
    ganador1 = partido_eurocopa(primeros_[0],segundos_[0],apto)
    semis_mundial.append(ganador1)
    ganador1 = partido_eurocopa(primeros_[1],segundos_[1],apto)
    semis_mundial.append(ganador1)
    ganador1 = partido_eurocopa(primeros_[2],segundos_[2],apto)
    semis_mundial.append(ganador1)
    ganador1 = partido_eurocopa(primeros_[3],segundos_[3],apto)
    semis_mundial.append(ganador1)
    mostrar_datos_mundiales()
    input("")
    print("SEMIFINALES")
    print("")
    print(semis_mundial[0],"vs",semis_mundial[3])
    print(semis_mundial[1],"vs",semis_mundial[2])
    final_mundial = []
    ganador1 = partido_eurocopa(semis_mundial[0],semis_mundial[3],apto)
    final_mundial.append(ganador1)
    if apto == 1:
        if ganador1 == semis_mundial[0]:
            perdedor = semis_mundial[3]
        else :
            perdedor = semis_mundial[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinalista del mundial  con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    ganador1 = partido_eurocopa(semis_mundial[1],semis_mundial[2],apto)
    final_mundial.append(ganador1)
    if apto == 1:
        if ganador1 == semis_mundial[1]:
            perdedor = semis_mundial[2]
        else :
            perdedor = semis_mundial[1]
        if perdedor == player["nacionalidad"]: 
            logro = f'semifinalista del mundial  con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_mundiales()
    input("")
    print("FINAL")
    print("")
    print(final_mundial[0],"vs",final_mundial[1])
    campeonmunidal = partido_eurocopa(final_mundial[0],final_mundial[1],apto)
    print("")
    print(f'CAMPEON DEL MUNDIAL {campeonmunidal}')
    if apto == 1:
        if campeonmunidal == final_mundial[0]:
            perdedor = final_mundial[1]
        else :
            perdedor = final_mundial[0]
        if perdedor == player["nacionalidad"]: 
            logro = f'finalista del mundial  con {perdedor}'
            logros_anuales.append(logro)
            player["valoracion"] += 1
    mostrar_datos_mundiales()
    return campeonmunidal

def mostrar_datos_mundiales_fin():
    print("datos del mundial")
    print("goleador")
    print("")
    jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["goles"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['goles']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = f'goleador del mundial'
                logros_anuales.append(logro)
                player["valoracion"] += 2
                player["dinero"] += 1000000
        else:
            print(f" {j['goles']} {j['nombre']} - {j['equipo']}")
    input("")
    print("asistente")
    print("")
    jugadores_ordenados = sorted(jugadores_selecciones, key=lambda j: j["asistencias"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:1]):
        if i == 0:
            print(f" {j['asistencias']} {j['nombre']} - {j['equipo']}\033[0m")
            if j['nombre'] == player["nombre"]:
                logro = f'asistente del mundial'
                logros_anuales.append(logro)
                player["valoracion"] += 2
                player["dinero"] += 500000
        else:
            print(f" {j['asistencias']} {j['nombre']} - {j['equipo']}")
   
def actualizar_ranking_mostrar():
    for i in equipo_rankinkg:
        partidos = i["partidos"]
        puntos = i["puntos"]
        i["promedio"] = round(puntos / partidos,3)
    input("mostrar tabla de mejores equipos")  
    print("")
    jugadores_ordenados = sorted(equipo_rankinkg, key=lambda j: j["promedio"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f"{j['promedio']} {j['nombre']}")
        else:
            print(f"{j['promedio']} {j['nombre']}")
    print("")   
    for i in selecciones_ranking:
        partidos = i["partidos"]
        puntos = i["puntos"]
        i["promedio"] = round(puntos / partidos,3)
    input("mostrar tabla de mejores selecciones")  
    print("")
    jugadores_ordenados = sorted(selecciones_ranking, key=lambda j: j["promedio"], reverse=True)
    for i, j in enumerate(jugadores_ordenados[:10]):
        if i == 0:
            print(f"{j['promedio']} {j['nombre']}")
        else:
            print(f"{j['promedio']} {j['nombre']}")
    print("")    
    
nacionalidadd = ""
equipo_player = "libre"
cont = 1
contt = 1
while cont == 1:
    nacion = input('''
que continente desear representar 
1. Europa
2. America         
3. Asia
4. Africa    
.''')
    if nacion == "2":
        division_seleccion = "america"
        while contt == 1:
            nacionn = input('''
que seleccion elijes
1. Argentina
2. Uruguay
3. Paraguay
4. Chile
5. Bolivia
6. Brasil
7. Peru
8. Colombia
9. Ecuador
10. Venezuela
11. Mexico
12. Estados Unidos
13. Canada 
14. Costa Rica
15. Cuba
16. Honduras
.''')
            if nacionn == "1": nacionalidad = "Argentina"
            elif nacionn == "2":nacionalidad = "Uruguay"
            elif nacionn == "3":nacionalidad = "Paraguay"
            elif nacionn == "4":nacionalidad = "Chile"
            elif nacionn == "5":nacionalidad = "Bolivia"
            elif nacionn == "6":nacionalidad = "Brasil"
            elif nacionn == "7":nacionalidad = "Peru"
            elif nacionn == "8":nacionalidad = "Colombia"
            elif nacionn == "9":nacionalidad = "Ecuador"
            elif nacionn == "10":nacionalidad = "Venezuela"
            elif nacionn == "11":nacionalidad = "Mexico"
            elif nacionn == "12":nacionalidad = "Estados Unidos"
            elif nacionn == "13":nacionalidad = "Canada"
            elif nacionn == "14":nacionalidad = "Costa Rica"
            elif nacionn == "15":nacionalidad = "Cuba"
            elif nacionn == "16":nacionalidad = "Honduras"
            if nacionn in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'] : contt = 0
    elif nacion == "1":
        division_seleccion = "europa"
        while contt == 1:
            nacionn = input('''
que seleccion elijes
1. España
2. Francia
3. Holanda
4. Inglaterra
5. Italia
6. Croacia
7. Belgica
8. Portugal
9. Suiza
10. Dinamarca
11. Polonia
12. Noruega
13. Alemania 
14. Gales
15. Serbia
16. Suecia
.''')
            if nacionn == "1": nacionalidad = "España"
            elif nacionn == "2":nacionalidad = "Francia"
            elif nacionn == "3":nacionalidad = "Holanda"
            elif nacionn == "4":nacionalidad = "Inglaterra"
            elif nacionn == "5":nacionalidad = "Italia"
            elif nacionn == "6":nacionalidad = "Croacia"
            elif nacionn == "7":nacionalidad = "Belgica"
            elif nacionn == "8":nacionalidad = "Portugal"
            elif nacionn == "9":nacionalidad = "Suiza"
            elif nacionn == "10":nacionalidad = "Dinamarca"
            elif nacionn == "11":nacionalidad = "Polonia"
            elif nacionn == "12":nacionalidad = "Noruega"
            elif nacionn == "13":nacionalidad = "Alemania"
            elif nacionn == "14":nacionalidad = "Gales"
            elif nacionn == "15":nacionalidad = "Serbia"
            elif nacionn == "16":nacionalidad = "Suecia"
            if nacionn in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'] : contt = 0
    elif nacion == "3":
        division_seleccion = "asia"
        while contt == 1:
            nacionn = input('''
que seleccion elijes
1. Iran
2. Corea del Sur
3. Japon
4. China
5. Arabia Saudita
6. Israel
7. Australia
8. Qatar
.''')
            if nacionn == "1": nacionalidad = "Iran"
            elif nacionn == "2":nacionalidad = "Corea del Sur"
            elif nacionn == "3":nacionalidad = "Japon"
            elif nacionn == "4":nacionalidad = "China"
            elif nacionn == "5":nacionalidad = "Arabia Saudita"
            elif nacionn == "6":nacionalidad = "Israel"
            elif nacionn == "7":nacionalidad = "Australia"
            elif nacionn == "8":nacionalidad = "Qatar"
            if nacionn in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'] : contt = 0
    elif nacion == "4":
        division_seleccion = "africa"
        while contt == 1:
            nacionn = input('''
que seleccion elijes
1. Egipto
2. Senegal
3. Tunez
4. Camerun
5. Marruecos
6. Nigeria
7. Ghana
8. Argelia
.''')
            if nacionn == "1": nacionalidad = "Egipto"
            elif nacionn == "2":nacionalidad = "Senegal"
            elif nacionn == "3":nacionalidad = "Tunez"
            elif nacionn == "4":nacionalidad = "Camerun"
            elif nacionn == "5":nacionalidad = "Marruecos"
            elif nacionn == "6":nacionalidad = "Nigeria"
            elif nacionn == "7":nacionalidad = "Ghana"
            elif nacionn == "8":nacionalidad = "Argelia"
            if nacionn in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'] : contt = 0
    if nacion in ['1', '2', '3', '4']: cont = 0
 
dinero = 0
nacionalidadd = nacionalidad
edad = 16
traspasos = []
nombre_del_jugador = input("nombre del jugador: ")
player = {
    "nombre": nombre_del_jugador,
    "edad": edad,
    "nacionalidad": nacionalidadd,
    "valoracion": 0,
    "equipo":"",
    "vitrina":[],
    "goles anuales":[],
    "asistencias anuales":[],
    "amarillas anuales":[],
    "rojas anuales":[],
    "mvp de la fecha anuales":[],
    "mvp del año anuales":[],
    "partidos jugados":[],
    "equipo anual":[],
    "logros anuales": [],
    "traspasos": traspasos,
    "contrato": 0,
    "dinero":dinero,
}
Arsenal = {
"equipo":"Arsenal",
"reputacion" : 5,
"tabla" : {'Arsenal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Arsenal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Arsenal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores": ["Martinelli", "Gabriel Jesus", "Havertz", "Saka", "Odegaard"]
}
Aston_Villa = {
"equipo":"Aston Villa",
"reputacion" : 5,
"tabla" : {'Aston Villa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Aston Villa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Aston Villa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores": ["Coutinho", "Watkins", "Ramsey", "Buendía"]
}
Bournemouth = {
"equipo":"Bournemouth",
"reputacion" : 5,
"tabla" : {'Bournemouth':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Bournemouth':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Bournemouth':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores": ["Semenyo", "Solanke", "Adams", "Christie"]
}
Brentford = {
"equipo":"Brentford",
"reputacion" : 5,
"tabla" : {'Brentford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Brentford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Brentford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores": ["Toney", "Mbeumo", "Schade", "Ghoddos"]
}
Brigthon = {
"equipo":"Brigthon",
"reputacion" : 5,
"tabla" : {'Brigthon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Brigthon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Brigthon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Fati", "Welbeck", "Mitoma", "Enciso", "Ferguson"]
}
Chelsea = {
"equipo":"Chelsea",
"reputacion" : 5,
"tabla" : {'Chelsea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Chelsea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Chelsea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Sterling", "Fernandez", "Nkunku", "Mudryk", "Palmer"]
}
Crystal_Palace = {
"equipo":"Crystal Palace",
"reputacion" : 5,
"tabla" : {'Crystal Palace':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Crystal Palace':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Crystal Palace':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Ayew(cp)", "Mateta", "Doucoure", "Edouard"]
}
Everton = {
"equipo":"Everton",
"reputacion" : 5,
"tabla" : {'Everton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Everton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Everton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Beto", "McNeil", "Calvert-Lewin", "Danjuma"]
}
Fulham = {
"equipo":"Fulham",
"reputacion" : 5,
"tabla" : {'Fulham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Fulham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Fulham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Traore", "Jimenez", "Iwobi", "Willian"]
}
Leeds_United = {
"equipo":"Leeds United",
"reputacion" : 5,
"tabla" : {'Leeds United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Leeds United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Leeds United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Rutter","Summerville","Gnoto","Gray"]
}
Leicester_City = {
"equipo":"Leicester City",
"reputacion" : 5,
"tabla" : {'Leicester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Leicester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Leicester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Vardy","Iheanacho","Akgün","Mavididi"]
}
Liverpool = {
"equipo":"Liverpool",
"reputacion" : 5,
"tabla" : {'Liverpool':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Liverpool':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Liverpool':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Salah", "MacAllister", "Núñez", "Luis Díaz", "Diogo Jota", "Gakpo"]
}
Manchester_City = {
"equipo":"Manchester City",
"reputacion" : 5,
"tabla" : {'Manchester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Manchester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Manchester City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Haaland", "Foden", "Grealish", "Álvarez", "De Bruyne"]
}
Manchester_United = {
"equipo":"Manchester United",
"reputacion" : 5,
"tabla" : {'Manchester United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Manchester United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Manchester United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Rashford", "Mount", "Bruno Fernandes", "Martial", "Sancho", "Antony"]
}
Newcastle = {
"equipo":"Newcastle",
"reputacion" : 5,
"tabla" : {'Newcastle':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Newcastle':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Newcastle':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Isak", "Guimarães", "Joelinton", "Tonali", "Murphy"]
}
Nottingham_Forest = {
"equipo":"Nottingham Forest",
"reputacion" : 5,
"tabla" : {'Nottingham Forest':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Nottingham Forest':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Nottingham Forest':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Awoniyi", "Gibbs-White", "Origi", "Danilo"]
}
Southampton = {
"equipo":"Southampton",
"reputacion" : 5,
"tabla" : {'Southampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Southampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Southampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Adams","Alcaraz","Armstrong","Edozie"]
}
Tottenham = {
"equipo":"Tottenham",
"reputacion" : 5,
"tabla" : {'Tottenham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Tottenham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Tottenham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Richarlison", "Son", "Sarr", "Kulusevski", "Perisic"]
}
West_ham = {
"equipo":"West ham",
"reputacion" : 5,
"tabla" : {'West ham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'West ham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'West ham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Antonio", "Paquetá", "Benrahma", "Ings"]
}
Wolverhampton = {
"equipo":"Wolverhampton",
"reputacion" : 5,
"tabla" : {'Wolverhampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Wolverhampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Wolverhampton':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Diego Costa","Cunha","Adama Traoré","Sarabia"]
}

Burnley = {
"equipo":"Burnley",
"reputacion" : 5,
"tabla" : {'Burnley':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Burnley':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Burnley':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Tella","Hedilazio","Rodríguez","Barnes"]
}
Sheffield_United = {
"equipo":"Sheffield United",
"reputacion" : 5,
"tabla" : {'Sheffield United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Sheffield United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Sheffield United':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Osula", "Jebbison", "Archer", "Brewster"]
}
Luton_Town = {
"equipo":"Luton Town",
"reputacion" : 5,
"tabla" : {'Luton Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Luton Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Luton Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Adebayo", "Lokonga", "Morris", "Ogbene"]
}
Middlesbrough = {
"equipo":"Middlesbrough",
"reputacion" : 5,
"tabla" : {'Middlesbrough':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Middlesbrough':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Middlesbrough':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Greenwood","Silvera","Jones","Forss"]
}
Coventry_City = {
"equipo":"Coventry City",
"reputacion" : 5,
"tabla" : {'Coventry City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Coventry City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Coventry City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Godden","Simms","Tavares","Wright"]
}
Sunderland = {
"equipo":"Sunderland",
"reputacion" : 5,
"tabla" : {'Sunderland':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Sunderland':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Sunderland':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Clarke","Bennette","Semedo","Rigg"]
}
Blackburn_Rovers = {
"equipo":"Blackburn Rovers",
"reputacion" : 5,
"tabla" : {'Blackburn Rovers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Blackburn Rovers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Blackburn Rovers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Leonard","Gallagher","Ennis","Hedges"]
}
Millwall= {
"equipo":"Millwall",
"reputacion" : 5,
"tabla" : {'Millwall':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Millwall':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Millwall':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Bradshaw","Nisbet","Watmore","Emakhu"]}
West_Bromwich_Albion = {
"equipo":"West Bromwich Albion",
"reputacion" : 5,
"tabla" : {'West Bromwich Albion':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'West Bromwich Albion':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'West Bromwich Albion':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Dike","Wallace","Diangana","Phillips"]
}
Swansea = {
"equipo":"Swansea",
"reputacion" : 5,
"tabla" : {'Swansea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Swansea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Swansea':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Lowe","Ginnelly","Cooper","Cullen"]
}
Watford = {
"equipo":"Watford",
"reputacion" : 5,
"tabla" : {'Watford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Watford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Watford':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Bayo","Martins","Healeyr","Ince"]
}
Preston_North_End = {
"equipo":"Preston North End",
"reputacion" : 5,
"tabla" : {'Preston North End':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Preston North End':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Preston North End':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Keane","Holmes","Riis","McCann"]
}
Norwich = {
"equipo":"Norwich",
"reputacion" : 5,
"tabla" : {'Norwich':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Norwich':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Norwich':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Barnes","Sargent","Gibbs","Idah"]
}
Bristol_City = {
"equipo":"Bristol City",
"reputacion" : 5,
"tabla" : {'Bristol City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Bristol City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Bristol City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Wells","Cornick","Bell","Conway"]}
Hull_City = {
"equipo":"Hull City",
"reputacion" : 5,
"tabla" : {'Hull City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Hull City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Hull City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Delap","Lokilo","Sinik","Connolly"]
}
Stoke_City = {
"equipo":"Stoke City",
"reputacion" : 5,
"tabla" : {'Stoke City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Stoke City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Stoke City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Gooch","Campbell","Mmaee","Gayle"]
}
Birmingham = {
"equipo":"Birmingham",
"reputacion" : 5,
"tabla" : {'Birmingham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Birmingham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Birmingham':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Hogan","Jutkiewicz","Roberts","Stansfield"]
}
Huddersfield_Town = {
"equipo":"Huddersfield Town",
"reputacion" : 5,
"tabla" : {'Huddersfield Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Huddersfield Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Huddersfield Town':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Koroma","Burgzorg","Ward","Hudlin"]}
Cardiff_City = {
"equipo":"Cardiff City",
"reputacion" : 5,
"tabla" : {'Cardiff City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Cardiff City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Cardiff City':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Ugbo","Robinson","Bowler","Grant"]
}
Queens_Park_Rangers = {
"equipo":"Queens Park Rangers",
"reputacion" : 5,
"tabla" : {'Queens Park Rangers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Queens Park Rangers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Queens Park Rangers':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Dykes","Adomah","Willock","Smyth"]
}

Napoli = {
"equipo":"Napoli",
"reputacion" : 5,
"tabla" : {'Napoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Napoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Napoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Osimhen","Raspadori","Simeone","Politano","Kvaratskhelia"]
}
Lazio = {
"equipo":"Lazio",
"reputacion" : 4,
"tabla" : {'Lazio':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Lazio':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Lazio':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Immobile","Anderson","Pedro(L)","Basic","Isaksen"]
}
Inter = {
"equipo":"Inter",
"reputacion" : 5,
"tabla" : {'Inter':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Inter':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Inter':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Martinez","Alexis Sánchez","Arnautovic","Calhanoglu","Mkhitaryan"]
}
Milan = {
"equipo":"Milan",
"reputacion" : 5,
"tabla" : {'Milan':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Milan':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Milan':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Giroud","Leão","Pulisic","Jović","Romero"]
}
Atalanta = {
"equipo":"Atalanta",
"reputacion" : 4,
"tabla" : {'Atalanta':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Atalanta':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Atalanta':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores": ["Muriel","Scamacca","Pasalic","Lookman","Adopo"]
}
Roma = {
"equipo":"Roma",
"reputacion" : 5,
"tabla" : {'Roma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Roma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Roma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Dybala","Belotti","El Shaarawy","Lukaku","Pellegrini"]
}
Juventus = {
"equipo":"Juventus",
"reputacion" : 5,
"tabla" : {'Juventus':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Juventus':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Juventus':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Vlahovic","Kean","Chiesa","Milik","Pogba"]
}
Fiorentina = {
"equipo":"Fiorentina",
"reputacion" : 4,
"tabla" : {'Fiorentina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Fiorentina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Fiorentina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["N.Gonzalez","Arthur","Beltrán","Sottil","Kouamé"]}
Bologna = {
"equipo":"Bologna",
"reputacion" : 3,
"tabla" : {'Bologna':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Bologna':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Bologna':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Karlsson","Ndoye","Orsolini","Hooijdonk"]
}
Torino = {
"equipo":"Torino",
"reputacion" : 5,
"tabla" : {'Torino':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Torino':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Torino':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Pellegri","Radonjic","Sanabria","Vlasic"]
}
Monza = {
"equipo":"Monza",
"reputacion" : 5,
"tabla" : {'Monza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Monza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Monza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Carvalho","Colombo","Maric","Ciurria"]}
Udinese = {
"equipo":"Udinese",
"reputacion" : 5,
"tabla" : {'Udinese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Udinese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Udinese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Deulofeu","Thauvin","Brenner"," Success"]
}
Sassuolo = {
"equipo":"Sassuolo",
"reputacion" : 5,
"tabla" : {'Sassuolo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Sassuolo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Sassuolo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Berardi","Lauriente","Mulattieri","Pinamonti"]
}
Empoli = {
"equipo":"Empoli",
"reputacion" : 5,
"tabla" : {'Empoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Empoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Empoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Caputo","Cambiaghi","Gyasi","Destro"]
}
Salernitana = {
"equipo":"Salernitana",
"reputacion" : 5,
"tabla" : {'Salernitana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Salernitana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Salernitana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Botheim","Candreva","Ikwuemesi","Maggiore"]
}
Lecce = {
"equipo":"Lecce",
"reputacion" : 5,
"tabla" : {'Lecce':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Lecce':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Lecce':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Piccoli","Krstovic","Banda","Burnete"]
}
Hellas_Verona = {
"equipo":"Hellas Verona",
"reputacion" : 5,
"tabla" : {'Hellas Verona':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Hellas Verona':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Hellas Verona':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Mboula","Djuric","Braaf","Ngonge"]
}
Spezia = {
"equipo":"Spezia",
"reputacion" : 5,
"tabla" : {'Spezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Spezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Spezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Moro","Krollis","Verde","Elia"]
}
Cremonese = {
"equipo":"Cremonese",
"reputacion" : 5,
"tabla" : {'Cremonese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Cremonese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Cremonese':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Ciofani","Buonaiuto","Coda","Zanimacchia"]
}
Sampdoria = {
"equipo":"Sampdoria",
"reputacion" : 5,
"tabla" : {'Sampdoria':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Sampdoria':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Sampdoria':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Estanis","Borini","Gumina","Monache"]
}
Frosinone = {
"equipo":"Frosinone",
"reputacion" : 5,
"tabla" : {'Frosinone':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Frosinone':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Frosinone':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Cheddira","Kvernadze","Soule","Cuni"]
}
Genoa = {
"equipo":"Genoa",
"reputacion" : 5,
"tabla" : {'Genoa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Genoa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Genoa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Retegui","Gudmundsson","Ekuban","Fini"]}
Bari = {
"equipo":"Bari",
"reputacion" : 5,
"tabla" : {'Bari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Bari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Bari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Diaw","Nasti","Maita","Sibilli"]}
Parma = {
"equipo":"Parma",
"reputacion" : 5,
"tabla" : {'Parma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Parma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Parma':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Colak","Benedyczak","Begic","Mihaila"]
}
Cagliari = {
"equipo":"Cagliari",
"reputacion" : 5,
"tabla" : {'Cagliari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Cagliari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Cagliari':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Lapadula","Pavoletti","Petagna","Zito"]
}
Sudtirol = {
"equipo":"Sudtirol",
"reputacion" : 5,
"tabla" : {'Sudtirol':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Sudtirol':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Sudtirol':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Rover","Odogwu","Pecorino","Cisco"]
}
Reggina = {
"equipo":"Reggina",
"reputacion" : 5,
"tabla" : {'Reggina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Reggina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Reggina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Gondo","Lanini","Pettinari","Vido"]
}
Venezia = {
"equipo":"Venezia",
"reputacion" : 5,
"tabla" : {'Venezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Venezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Venezia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Johsen","Pierini","Tessmann","Pohjanpalo"]
}
Palermo = {
"equipo":"Palermo",
"reputacion" : 5,
"tabla" : {'Palermo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Palermo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Palermo':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Mancuso","Brunori","Soleri","Segre"]
}
Modena = {
"equipo":"Modena",
"reputacion" : 5,
"tabla" : {'Modena':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Modena':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Modena':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Falcinelli","Manconi","Giovannini","Gerli"]
}
Pisa = {
"equipo":"Pisa",
"reputacion" : 5,
"tabla" : {'Pisa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Pisa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Pisa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Mlakar","Torregrossa","Tramoni","Nagy"]
}
Ascoli = {
"equipo":"Ascoli",
"reputacion" : 5,
"tabla" : {'Ascoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Ascoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Ascoli':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Pedro Mendes","Millico","Nestorovski","Caligara"]
}
Como = {
"equipo":"Como",
"reputacion" : 5,
"tabla" : {'Como':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Como':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Como':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Cutrone","Gabrielloni","Baselli","Cerri"]
}
Ternana = {
"equipo":"Ternana",
"reputacion" : 5,
"tabla" : {'Ternana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Ternana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Ternana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Favili","Dionisi","Raimondo","Proietti"]
}
Brescia = {
"equipo":"Brescia",
"reputacion" : 5,
"tabla" : {'Brescia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Brescia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Brescia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Moncini","Bianchi","Bisoli","Ferro"]
}
Cittadella = {
"equipo":"Cittadella",
"reputacion" : 5,
"tabla" : {'Cittadella':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Cittadella':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Cittadella':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Magrassi","Maistrello","Pittarello","Danzi"]
}
Cosenza = {
"equipo":"Cosenza",
"reputacion" : 5,
"tabla" : {'Cosenza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Cosenza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Cosenza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Forte","Tutino","Novello","Crespi"]
}
Perugia = {
"equipo":"Perugia",
"reputacion" : 5,
"tabla" : {'Perugia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Perugia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Perugia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Matos","Cudrig","Cudrig","Seghetti"]
}
Spal = {
"equipo":"Spal",
"reputacion" : 5,
"tabla" : {'Spal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Spal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Spal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Antenucci","Dalmonte","Siligardi","Rabbi"]
}
Benevento = {
"equipo":"Benevento",
"reputacion" : 5,
"tabla" : {'Benevento':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla premier" : {'Benevento':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"tabla europa" : {'Benevento':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Improta","Ciano","Marotta","Bolsius"]
}

psg = {
"equipo":"PSG",
"tabla premier" :{'PSG':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores": ["Mbappe","Asensio","O.Dembele","Muani","Barcola"]
}

Barcelona ={
"equipo":"Barcelona",
"tabla premier" : {'Barcelona':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Lewandowski","Gavi","Felix","Raphinha","Torres"]
}
Real_Madrid ={
"equipo": "Real Madrid",
"tabla premier" : {'Real Madrid':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Bellingham","Vinicius","Rodrygo","Modric","Tchouameni"]
}
B_Dortmund = {
"equipo":"B.Dortmund",
"tabla premier" : {'B.Dortmund':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Haller","Moukoko","Adeyemi","Reus","Reyna"]
}
Bayern_Munich = {
"equipo":"Bayern Munich",
"tabla premier" :{'Bayern Munich':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Kane","Gnabry","Müller","Musiala","Sané"]
}
Ajax ={
"equipo" : "Ajax",
"tabla premier" : {'Ajax':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Bergwijn","Akpom","Mikautadze","Godts","Tahirovic"]
}
Shakhtar = {
"equipo" : "Shakhtar",
"tabla premier" : {'Shakhtar':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Traore","Sikan","Petryak","Zubkov","Bondarenko"]
}
Brugge = {
"equipo":"Brugge",
"tabla europa" : {'Brugge':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Buchanan","Nusa","Jutglà","Vermant","Olsen"]}
Lyon ={
"equipo":"O.Lyon",
"tabla premier" : {'O.Lyon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Lacazette","Baldé","Jeffinho","Tolisso","Tagliafico"]
}

Atl_Madrid ={
"equipo": "Atl.Madrid",
"tabla premier" : {'Atl.Madrid':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Griezmann","Morata","de Paul","Koke","Lemar"]}
B_Leverkusen = {
"equipo":"B.Leverkusen",
"tabla europa" : {'B.Leverkusen':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Tella","Hložek","Hofmann","Adli","Boniface"]
}
Sporting_Lisboa = {
"equipo":"Sporting Lisboa",
"tabla europa" : {'Sporting Lisboa':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Paulinho","Trincao","Edwards","Santos","Goncalves"]
}
Frankfurt = {
"equipo":"Frankfurt",
"tabla europa" : {'Frankfurt':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Götze","Marmoush","Ngankam","Alario","Rode"]
}
Marsella = {
"equipo":"O.Marsella",
"tabla europa" : {'O.Marsella':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Aubameyang","Sarr(M)","Correa","Ndiaye","Gueye"]
}
Sevilla = {
"equipo":"Sevilla",
"tabla europa" : {'Sevilla':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Zakharyan","En-Nesyri","Suso","Ocampos","Rakitić"]
}
Benfica = {
"equipo" : "Benfica",
"tabla premier" : {'Benfica':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Neres","Rafa","Di María","Musa","Gouveia"]
}
Leipzig = {
"equipo":"Leipzig",
"tabla europa" : {'Leipzig':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Poulsen","Werner","Sesko","Olmo","Openda"]
}
Monaco = {
"equipo": "Monaco",
"tabla europa" : {'Monaco':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Ben Yedder","Martins(M)","Embolo","Seghir","Camara"]
}
psv = {
"equipo":"PSV",
"tabla europa":{'PSV':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["de Jong","Bakayoko","Til","Veerman","Lang"]
}
Real_Sociedad = {
"equipo":"Real Sociedad",
"tabla europa":{'Real Sociedad':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},
"jugadores":["Sadiq","Oyarzabal","Andre Silva","Kubo","Zakharyan"]
}

España = {"equipo":"España","tabla":{'España':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Francia = {"equipo":"Francia","tabla":{'Francia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Holanda = {"equipo":"Holanda","tabla":{'Holanda':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Inglaterra = {"equipo":"Inglaterra","tabla":{'Inglaterra':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Italia = {"equipo":"Italia","tabla":{'Italia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Croacia = {"equipo":"Croacia","tabla":{'Croacia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Belgica = {"equipo":"Belgica","tabla":{'Belgica':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Portugal = {"equipo":"Portugal","tabla":{'Portugal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Suiza = {"equipo":"Suiza","tabla":{'Suiza':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Dinamarca = {"equipo":"Dinamarca","tabla":{'Dinamarca':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Polonia = {"equipo":"Polonia","tabla":{'Polonia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Noruega = {"equipo":"Noruega","tabla":{'Noruega':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Alemania = {"equipo":"Alemania","tabla":{'Alemania':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Gales = {"equipo":"Gales","tabla":{'Gales':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Serbia = {"equipo":"Serbia","tabla":{'Serbia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Suecia = {"equipo":"Suecia","tabla":{'Suecia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Argentina = {"equipo":"Argentina","tabla":{'Argentina':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Uruguay = {"equipo":"Uruguay","tabla":{'Uruguay':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Paraguay = {"equipo":"Paraguay","tabla":{'Paraguay':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Chile = {"equipo":"Chile","tabla":{'Chile':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Bolivia = {"equipo":"Bolivia","tabla":{'Bolivia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Brasil = {"equipo":"Brasil","tabla":{'Brasil':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Peru = {"equipo":"Peru","tabla":{'Peru':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Colombia = {"equipo":"Colombia","tabla":{'Colombia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Ecuador = {"equipo":"Ecuador","tabla":{'Ecuador':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Venezuela = {"equipo":"Venezuela","tabla":{'Venezuela':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Mexico = {"equipo":"Mexico","tabla":{'Mexico':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Estados_Unidos = {"equipo":"Estados Unidos","tabla":{'Estados Unidos':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Canada = {"equipo":"Canada","tabla":{'Canada':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Costa_Rica = {"equipo":"Costa Rica","tabla":{'Costa Rica':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Cuba = {"equipo":"Cuba","tabla":{'Cuba':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Honduras = {"equipo":"Honduras","tabla":{'Honduras':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Iran = {"equipo":"Iran","tabla":{'Iran':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Corea_del_Sur = {"equipo":"Corea del Sur","tabla":{'Corea del Sur':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Japon = {"equipo":"Japon","tabla":{'Japon':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
China = {"equipo":"China","tabla":{'China':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Arabia_Saudita = {"equipo":"Arabia Saudita","tabla":{'Arabia Saudita':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Israel = {"equipo":"Israel","tabla":{'Israel':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Australia = {"equipo":"Australia","tabla":{'Australia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Qatar = {"equipo":"Qatar","tabla":{'Qatar':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Egipto = {"equipo":"Egipto","tabla":{'Egipto':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Senegal = {"equipo":"Senegal","tabla":{'Senegal':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Tunez = {"equipo":"Tunez","tabla":{'Tunez':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Camerun = {"equipo":"Camerun","tabla":{'Camerun':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Marruecos = {"equipo":"Marruecos","tabla":{'Marruecos':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Nigeria = {"equipo":"Nigeria","tabla":{'Nigeria':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Ghana = {"equipo":"Ghana","tabla":{'Ghana':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}
Argelia = {"equipo":"Argelia","tabla":{'Argelia':{'PTS':0,'GF': 0, 'GC': 0, 'GD': 0,'V':0,'E':0,'D':0},},}

equipo_player = cambiar_equipo()
jugadores_ = [
Arsenal["jugadores"],Aston_Villa["jugadores"],Bournemouth["jugadores"],Brentford["jugadores"],Brigthon["jugadores"],Chelsea["jugadores"],Crystal_Palace["jugadores"],Everton["jugadores"],Fulham["jugadores"],Leeds_United["jugadores"],Leicester_City["jugadores"],Liverpool["jugadores"],Manchester_City["jugadores"],Manchester_United["jugadores"],Newcastle["jugadores"],Nottingham_Forest["jugadores"],Southampton["jugadores"],Tottenham["jugadores"],West_ham["jugadores"],Wolverhampton["jugadores"],Burnley["jugadores"],Sheffield_United["jugadores"],Luton_Town["jugadores"],Middlesbrough["jugadores"],Coventry_City["jugadores"],Sunderland["jugadores"],Blackburn_Rovers["jugadores"],Millwall["jugadores"],West_Bromwich_Albion["jugadores"],Swansea["jugadores"],Watford["jugadores"],Preston_North_End["jugadores"],Norwich["jugadores"],Bristol_City["jugadores"],Hull_City["jugadores"],Stoke_City["jugadores"],Birmingham["jugadores"],Huddersfield_Town["jugadores"],Cardiff_City["jugadores"],Queens_Park_Rangers["jugadores"]]

serieA_equipos = [
    Napoli,Lazio,Inter,Milan,Atalanta,Roma,
  Juventus,Fiorentina,Bologna,Sassuolo,Torino,Monza,Udinese,Empoli,Salernitana,Lecce,Hellas_Verona,Spezia,Cremonese,Sampdoria]
serieB_equipos = [
    Frosinone,Genoa,Bari,Parma,Cagliari,Sudtirol,Reggina,Venezia,Palermo,Modena,Pisa,Ascoli,Como,Ternana,Cittadella,Brescia,Cosenza,Perugia,Spal,Benevento
]
premier_league_equipos =[   
                         Arsenal,Aston_Villa,Bournemouth,Brentford,Brigthon,Chelsea,Crystal_Palace,Everton,Fulham,Leeds_United,Leicester_City,Liverpool,Manchester_City,Manchester_United,Newcastle,Nottingham_Forest,Southampton,Tottenham,West_ham,Wolverhampton]

sky_by_championship_equipos =[
Burnley,Sheffield_United,Luton_Town,Middlesbrough,Coventry_City,Sunderland,Blackburn_Rovers,Millwall,West_Bromwich_Albion,Swansea,Watford,Preston_North_End,Norwich,Bristol_City,Hull_City,Stoke_City,Birmingham,Huddersfield_Town,Cardiff_City,Queens_Park_Rangers]

selecciones_ranking = [
    {"nombre":"España","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Francia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Holanda","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Inglaterra","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Italia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Croacia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Belgica","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Portugal","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Suiza","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Dinamarca","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Polonia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Noruega","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Alemania","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Gales","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Serbia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Argentina","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Suecia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Uruguay","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Paraguay","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Chile","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Bolivia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Brasil","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Peru","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Colombia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Ecuador","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Venezuela","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Mexico","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Estados Unidos","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Canada","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Costa Rica","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Cuba","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Honduras","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Egipto","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Senegal","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Tunez","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Camerun","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Marruecos","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Nigeria","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Ghana","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Argelia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Iran","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Corea del Sur","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Japon","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"China","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Arabia Saudita","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Israel","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Australia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Qatar","partidos":0,"puntos":0,"promedio":0},
    
]

equipo_rankinkg = [
    {"nombre":"Arsenal","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Aston Villa","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Bournemouth","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Brentford","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Brigthon","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Chelsea","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Crystal Palace","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Everton","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Fulham","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Leeds United","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Leicester City","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Liverpool","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Manchester City","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Manchester United","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Newcastle","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Nottingham Forest","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Southampton","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Tottenham","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"West ham","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Wolverhampton","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Burnley","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Sheffield United","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Luton Town","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Middlesbrough","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Coventry City","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Sunderland","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Blackburn Rovers","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Millwall","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"West Bromwich Albion","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Swansea","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Watford","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Preston North End","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Norwich","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Bristol City","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Hull City","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Stoke City","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Birmingham","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Huddersfield Town","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Cardiff City","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Queens Park Rangers","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"PSG","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"O.Lyon","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Inter","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Juventus","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Milan","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Napoli","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Roma","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Atl.Madrid","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Barcelona","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Real Madrid","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"B.Dortmund","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Bayern Munich","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"B.Leverkusen","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Sporting Lisboa","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Frankfurt","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"O.Marsella","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Sevilla","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Benfica","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Leipzig","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Ajax","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Monaco","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Shakhtar","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Brugge","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"PSV","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Real Sociedad","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Benevento","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Spal","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Perugia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Cosenza","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Cittadella","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Brescia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Ternana","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Como","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Cagliari","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Ascoli","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Pisa","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Modena","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Palermo","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Venezia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Cremonese","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Reggina","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Sudtirol","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Bari","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Parma","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Genoa","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Frosinone","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Sampdoria","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Spezia","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Hellas Verona","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Lecce","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Empoli","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Salernitana","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Sassuolo","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Udinese","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Bologna","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Fiorentina","partidos":0,"puntos":0,"promedio":0},
    {"nombre":"Lazio","partidos":0,"puntos":0,"promedio":0},
]

jugadores_selecciones = [
    {"nombre":player["nombre"],"goles":0,"equipo":player["nacionalidad"],
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":division_seleccion},
    
    {"nombre":"Morata","goles":0,"equipo":"España",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Olmo","goles":0,"equipo":"España",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Gavi","goles":0,"equipo":"España",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Aspas","goles":0,"equipo":"España",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Mbappe","goles":0,"equipo":"Francia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Giroud","goles":0,"equipo":"Francia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Griezmann","goles":0,"equipo":"Francia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Muani","goles":0,"equipo":"Francia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Depay","goles":0,"equipo":"Holanda",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Weghorst","goles":0,"equipo":"Holanda",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Simons","goles":0,"equipo":"Holanda",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Wijnaldum","goles":0,"equipo":"Holanda",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},  
    
    {"nombre":"Kane","goles":0,"equipo":"Inglaterra",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Saka","goles":0,"equipo":"Inglaterra",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Foden","goles":0,"equipo":"Inglaterra",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Rashford","goles":0,"equipo":"Inglaterra",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Scamacca","goles":0,"equipo":"Italia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Tonali","goles":0,"equipo":"Italia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Jorginho","goles":0,"equipo":"Italia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Retegui","goles":0,"equipo":"Italia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Perisic","goles":0,"equipo":"Croacia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Kramaric","goles":0,"equipo":"Croacia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Brozovic","goles":0,"equipo":"Croacia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Pasalic","goles":0,"equipo":"Croacia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Lukaku","goles":0,"equipo":"Belgica",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"De Bruyne","goles":0,"equipo":"Belgica",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Trossard","goles":0,"equipo":"Belgica",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Bakayoko","goles":0,"equipo":"Belgica",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"C.Ronaldo","goles":0,"equipo":"Portugal",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Félix","goles":0,"equipo":"Portugal",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Leão","goles":0,"equipo":"Portugal",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Bruno Fernandes","goles":0,"equipo":"Portugal",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Xhaka","goles":0,"equipo":"Suiza",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Okafor","goles":0,"equipo":"Suiza",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Steffen","goles":0,"equipo":"Suiza",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Fassnacht","goles":0,"equipo":"Suiza",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Eriksen","goles":0,"equipo":"Dinamarca",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Braithwaite","goles":0,"equipo":"Dinamarca",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Dolberg","goles":0,"equipo":"Dinamarca",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Cornelius","goles":0,"equipo":"Dinamarca",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Lewandowski","goles":0,"equipo":"Polonia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Zielinski","goles":0,"equipo":"Polonia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Skoras","goles":0,"equipo":"Polonia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Swiderski","goles":0,"equipo":"Polonia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Haaland","goles":0,"equipo":"Noruega",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Brynhildsen","goles":0,"equipo":"Noruega",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"odegaard","goles":0,"equipo":"Noruega",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Sorloth","goles":0,"equipo":"Noruega",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Havertz","goles":0,"equipo":"Alemania",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Gündogan","goles":0,"equipo":"Alemania",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Müller","goles":0,"equipo":"Alemania",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Gnabry","goles":0,"equipo":"Alemania",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Bale","goles":0,"equipo":"Gales",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Ramsey","goles":0,"equipo":"Gales",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Moore","goles":0,"equipo":"Gales",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Ampadu","goles":0,"equipo":"Gales",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Mitrovic","goles":0,"equipo":"Serbia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Jovic","goles":0,"equipo":"Serbia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Vlahovic","goles":0,"equipo":"Serbia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Tadic","goles":0,"equipo":"Serbia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    {"nombre":"Isak","goles":0,"equipo":"Suecia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Forsberg","goles":0,"equipo":"Suecia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Elanga","goles":0,"equipo":"Suecia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    {"nombre":"Gyokeres","goles":0,"equipo":"Suecia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"europa"},
    
    
    
    
    
    
    {"nombre":"Messi","goles":0,"equipo":"Argentina",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"MacAllister","goles":0,"equipo":"Argentina",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Álvarez","goles":0,"equipo":"Argentina",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Fernandez","goles":0,"equipo":"Argentina",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Núñez","goles":0,"equipo":"Uruguay",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Suárez","goles":0,"equipo":"Uruguay",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Cavani","goles":0,"equipo":"Uruguay",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Valverde","goles":0,"equipo":"Uruguay",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Samudio","goles":0,"equipo":"Paraguay",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Ávalos","goles":0,"equipo":"Paraguay",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Cardozo","goles":0,"equipo":"Paraguay",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Villasanti","goles":0,"equipo":"Paraguay",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Ben Brereton Díaz","goles":0,"equipo":"Chile",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Aránguiz","goles":0,"equipo":"Chile",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Vidal","goles":0,"equipo":"Chile",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Vargas","goles":0,"equipo":"Chile",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Vaca","goles":0,"equipo":"Bolivia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Chura","goles":0,"equipo":"Bolivia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Sagredo","goles":0,"equipo":"Bolivia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Sagredo","goles":0,"equipo":"Bolivia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Neymar","goles":0,"equipo":"Brasil",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Richarlison","goles":0,"equipo":"Brasil",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Firmino","goles":0,"equipo":"Brasil",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Paquetá","goles":0,"equipo":"Brasil",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Lapadula","goles":0,"equipo":"Peru",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Cueva","goles":0,"equipo":"Peru",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Carrillo","goles":0,"equipo":"Peru",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Ormeño","goles":0,"equipo":"Peru",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Luis Díaz","goles":0,"equipo":"Colombia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Borja","goles":0,"equipo":"Colombia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Borre","goles":0,"equipo":"Colombia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Zapata","goles":0,"equipo":"Colombia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Valencia","goles":0,"equipo":"Ecuador",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Mena","goles":0,"equipo":"Ecuador",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Plata","goles":0,"equipo":"Ecuador",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Palacios","goles":0,"equipo":"Ecuador",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Hurtado","goles":0,"equipo":"Venezuela",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Soteldo","goles":0,"equipo":"Venezuela",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Savarino","goles":0,"equipo":"Venezuela",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Córdova","goles":0,"equipo":"Venezuela",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Lozano","goles":0,"equipo":"Mexico",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Guardado","goles":0,"equipo":"Mexico",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Herrera","goles":0,"equipo":"Mexico",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Antuna","goles":0,"equipo":"Mexico",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Pulisic","goles":0,"equipo":"Estados Unidos",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"McKennie","goles":0,"equipo":"Estados Unidos",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Reyna","goles":0,"equipo":"Estados Unidos",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Adams","goles":0,"equipo":"Estados Unidos",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"David","goles":0,"equipo":"Canada",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Larin","goles":0,"equipo":"Canada",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Wotherspoon","goles":0,"equipo":"Canada",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Davies","goles":0,"equipo":"Canada",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Campbell","goles":0,"equipo":"Costa Rica",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Alcocer","goles":0,"equipo":"Costa Rica",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Tejeda","goles":0,"equipo":"Costa Rica",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Calvo","goles":0,"equipo":"Costa Rica",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    {"nombre":"Paradela","goles":0,"equipo":"Cuba",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Cavafe","goles":0,"equipo":"Cuba",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Espino","goles":0,"equipo":"Cuba",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Pozo","goles":0,"equipo":"Cuba",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
 
    {"nombre":"Quioto","goles":0,"equipo":"Honduras",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Arrada","goles":0,"equipo":"Honduras",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Juanique","goles":0,"equipo":"Honduras",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    {"nombre":"Leveron","goles":0,"equipo":"Honduras",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"america"},
    
    
    
    
    
    {"nombre":"Salah","goles":0,"equipo":"Egipto",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Mohamed","goles":0,"equipo":"Egipto",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Zizo","goles":0,"equipo":"Egipto",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Hamdy","goles":0,"equipo":"Egipto",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    
    {"nombre":"Mane","goles":0,"equipo":"Senegal",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Sarr","goles":0,"equipo":"Senegal",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Gueye","goles":0,"equipo":"Senegal",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Sarr(O.L)","goles":0,"equipo":"Senegal",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    
    {"nombre":"Khazri","goles":0,"equipo":"Tunez",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Jaziri","goles":0,"equipo":"Tunez",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Msakni","goles":0,"equipo":"Tunez",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Rafia","goles":0,"equipo":"Tunez",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    
    {"nombre":"Aboubakar","goles":0,"equipo":"Camerun",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Siliki","goles":0,"equipo":"Camerun",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Malong","goles":0,"equipo":"Camerun",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Ngamaleu","goles":0,"equipo":"Camerun",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    
    {"nombre":"Hakimi","goles":0,"equipo":"Marruecos",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"En-Nesyri","goles":0,"equipo":"Marruecos",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Amrabat","goles":0,"equipo":"Marruecos",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Munir","goles":0,"equipo":"Marruecos",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    
    {"nombre":"Iheanacho","goles":0,"equipo":"Nigeria",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Iwobi","goles":0,"equipo":"Nigeria",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Awoniyi","goles":0,"equipo":"Nigeria",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Olayinka","goles":0,"equipo":"Nigeria",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    
    {"nombre":"Ayew","goles":0,"equipo":"Ghana",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Ayew(cp)","goles":0,"equipo":"Ghana",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Partey","goles":0,"equipo":"Ghana",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Paintsil","goles":0,"equipo":"Ghana",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    
    {"nombre":"Mahrez","goles":0,"equipo":"Argelia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Benrahma","goles":0,"equipo":"Argelia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Bounedjah","goles":0,"equipo":"Argelia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    {"nombre":"Boulaya","goles":0,"equipo":"Argelia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"africa"},
    
    {"nombre":"Taremi","goles":0,"equipo":"Iran",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Amiri","goles":0,"equipo":"Iran",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Shekari","goles":0,"equipo":"Iran",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Gholizadeh","goles":0,"equipo":"Iran",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    
    {"nombre":"Son","goles":0,"equipo":"Corea del Sur",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Min-kyu","goles":0,"equipo":"Corea del Sur",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Hee-chan","goles":0,"equipo":"Corea del Sur",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Jae-sung","goles":0,"equipo":"Corea del Sur",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    
    {"nombre":"Mitoma","goles":0,"equipo":"Japon",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Kubo","goles":0,"equipo":"Japon",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Nishimura","goles":0,"equipo":"Japon",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Asano","goles":0,"equipo":"Japon",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    
    {"nombre":"Lei","goles":0,"equipo":"China",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Elkerson","goles":0,"equipo":"China",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Yuning","goles":0,"equipo":"China",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Long","goles":0,"equipo":"China",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    
    {"nombre":"Al-Shehri","goles":0,"equipo":"Arabia Saudita",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Asiri","goles":0,"equipo":"Arabia Saudita",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Sharahili","goles":0,"equipo":"Arabia Saudita",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Kanno","goles":0,"equipo":"Arabia Saudita",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    
    {"nombre":"Solomon","goles":0,"equipo":"Israel",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Dasa","goles":0,"equipo":"Israel",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Lavi","goles":0,"equipo":"Israel",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Vitor","goles":0,"equipo":"Israel",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    
    {"nombre":"Duke","goles":0,"equipo":"Australia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Kuol","goles":0,"equipo":"Australia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Cummings","goles":0,"equipo":"Australia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"McGree","goles":0,"equipo":"Australia",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    
    {"nombre":"Alil","goles":0,"equipo":"Qatar",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Afif","goles":0,"equipo":"Qatar",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Muneer","goles":0,"equipo":"Qatar",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    {"nombre":"Madibo","goles":0,"equipo":"Qatar",
    "amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"asistencias":0,"division":"asia"},
    ]

jugadores = [
{"nombre": player["nombre"],"goles": 0,"equipo":equipo_player,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"partidos":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Martinelli","asistencias":0,"goles":0,"equipo":"Arsenal","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Gabriel Jesus","goles":0,"equipo":"Arsenal","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Havertz", "goles": 0,"equipo":"Arsenal","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Saka", "goles": 0,"equipo":"Arsenal","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Odegaard", "goles": 0,"equipo":"Arsenal","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Coutinho","goles": 0,"equipo":"Aston Villa","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Watkins","goles": 0,"equipo":"Aston Villa","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ramsey","goles": 0,"equipo":"Aston Villa","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Buendía","goles": 0,"equipo":"Aston Villa","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Semenyo","goles": 0,"equipo":"Bournemouth","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Solanke","goles": 0,"equipo":"Bournemouth","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Adams","goles": 0,"equipo":"Bournemouth","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Christie","goles": 0,"equipo":"Bournemouth","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre": "Toney","goles": 0,"equipo":"Brentford","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Mbeumo","goles": 0,"equipo":"Brentford","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Schade","goles": 0,"equipo":"Brentford","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Ghoddos","goles": 0,"equipo":"Brentford","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre": "Fati","goles": 0,"equipo":"Brigthon","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Welbeck","goles": 0,"equipo":"Brigthon","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Mitoma","goles": 0,"equipo":"Brigthon","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Enciso","goles": 0,"equipo":"Brigthon","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Ferguson","goles": 0,"equipo":"Brigthon","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre": "Palmer","goles": 0,"equipo":"Chelsea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Mudryk","goles": 0,"equipo":"Chelsea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Sterling","goles": 0,"equipo":"Chelsea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Fernandez","goles": 0,"equipo":"Chelsea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Nkunku","goles": 0,"equipo":"Chelsea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre": "Mateta","goles": 0,"equipo":"Crystal Palace","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Ayew(cp)","goles": 0,"equipo":"Crystal Palace","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Doucoure","goles": 0,"equipo":"Crystal Palace","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Edouard","goles": 0,"equipo":"Crystal Palace","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre": "Beto","goles": 0,"equipo":"Everton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "McNeil","goles":0,"equipo":"Everton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Calvert-Lewin","goles": 0,"equipo":"Everton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre": "Danjuma","goles": 0,"equipo":"Everton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre": "Traore","goles": 0,"equipo":"Fulham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Willian","goles": 0,"equipo":"Fulham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Jimenez","goles": 0,"equipo":"Fulham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Iwobi","goles": 0,"equipo":"Fulham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Rutter","goles": 0,"equipo":"Leeds United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Summerville","goles": 0,"equipo":"Leeds United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Gnoto","goles": 0,"equipo":"Leeds United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Gray","goles": 0,"equipo":"Leeds United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Vardy","goles": 0,"equipo":"Leicester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Akgün","goles": 0,"equipo":"Leicester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Mavididi","goles": 0,"equipo":"Leicester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Iheanacho","goles": 0,"equipo":"Leicester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Salah","goles": 0,"equipo":"Liverpool","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "MacAllister","goles": 0,"equipo":"Liverpool","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Núñez","goles": 0,"equipo":"Liverpool","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Luis Díaz","goles": 0,"equipo":"Liverpool","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Diogo Jota","goles": 0,"equipo":"Liverpool","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Haaland","goles": 0,"equipo":"Manchester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Foden","goles": 0,"equipo":"Manchester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "De Bruyne","goles": 0,"equipo":"Manchester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Álvarez","goles": 0,"equipo":"Manchester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Grealish","goles": 0,"equipo":"Manchester City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Rashford","goles": 0,"equipo":"Manchester United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Sancho","goles": 0,"equipo":"Manchester United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Bruno Fernandes","goles": 0,"equipo":"Manchester United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Martial","goles": 0,"equipo":"Manchester United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Mount","goles": 0,"equipo":"Manchester United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Isak","goles": 0,"equipo":"Newcastle","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Guimarães","goles": 0,"equipo":"Newcastle","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Joelinton","goles": 0,"equipo":"Newcastle","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Tonali","goles": 0,"equipo":"Newcastle","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Murphy","goles": 0,"equipo":"Newcastle","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Awoniyi","goles": 0,"equipo":"Nottingham Forest","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Gibbs-White","goles": 0,"equipo":"Nottingham Forest","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Origi","goles": 0,"equipo":"Nottingham Forest","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Danilo","goles": 0,"equipo":"Nottingham Forest","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Adams","goles": 0,"equipo":"Southampton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Alcaraz","goles": 0,"equipo":"Southampton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Armstrong","equipo":"Southampton","goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Edozie","goles": 0,"equipo":"Southampton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Sarr","goles": 0,"equipo":"Tottenham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Richarlison","goles": 0,"equipo":"Tottenham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Son","goles": 0,"equipo":"Tottenham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Kulusevski","goles": 0,"equipo":"Tottenham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Perisic","goles": 0,"equipo":"Tottenham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Antonio","goles": 0,"equipo":"West ham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Paquetá","goles": 0,"equipo":"West ham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Benrahma","goles": 0,"equipo":"West ham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Ings","goles": 0,"equipo":"West ham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Silva","goles": 0,"equipo":"Wolverhampton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Cunha","goles": 0,"equipo":"Wolverhampton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Kalajdzic","goles": 0,"equipo":"Wolverhampton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Sarabia","goles": 0,"equipo":"Wolverhampton","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"premier","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Foster","goles": 0,"equipo":"Burnley","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Redmond","goles": 0,"equipo":"Burnley","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Amdouni","goles": 0,"equipo":"Burnley","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Brownhill","goles": 0,"equipo":"Burnley","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Osula","goles": 0,"equipo":"Sheffield United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Jebbison","goles": 0,"equipo":"Sheffield United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Archer","goles": 0,"equipo":"Sheffield United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Brewster","goles": 0,"equipo":"Sheffield United","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Morris","goles": 0,"equipo":"Luton Town","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Adebayo","goles": 0,"equipo":"Luton Town","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Lokonga","goles": 0,"equipo":"Luton Town","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Ogbene","goles": 0,"equipo":"Luton Town","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Greenwood","goles": 0,"equipo":"Middlesbrough","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Silvera","goles": 0,"equipo":"Middlesbrough","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Jones","goles": 0,"equipo":"Middlesbrough","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Forss","goles": 0,"equipo":"Middlesbrough","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Godden","goles": 0,"equipo":"Coventry City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Simms","goles": 0,"equipo":"Coventry City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Tavares","goles": 0,"equipo":"Coventry City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Wright","goles": 0,"equipo":"Coventry City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Clarke","goles": 0,"equipo":"Sunderland","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Bennette","goles": 0,"equipo":"Sunderland","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Semedo","goles": 0,"equipo":"Sunderland","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Rigg","goles": 0,"equipo":"Sunderland","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Leonard","goles": 0,"equipo":"Blackburn Rovers","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Gallagher","goles": 0,"equipo":"Blackburn Rovers","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Ennis","goles": 0,"equipo":"Blackburn Rovers","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Hedges","goles": 0,"equipo":"Blackburn Rovers","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Bradshaw","goles": 0,"equipo":"Millwall","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Nisbet","goles": 0,"equipo":"Millwall","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Watmore","goles": 0,"equipo":"Millwall","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Emakhu","goles": 0,"equipo":"Millwall","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Dike","goles": 0,"equipo":"West Bromwich Albion","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Wallace","goles": 0,"equipo":"West Bromwich Albion","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Diangana","goles": 0,"equipo":"West Bromwich Albion","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Phillips","goles": 0,"equipo":"West Bromwich Albion","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Lowe","goles": 0,"equipo":"Swansea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Ginnelly","goles": 0,"equipo":"Swansea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Cooper","goles": 0,"equipo":"Swansea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Cullen","goles": 0,"equipo":"Swansea","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Bayo","goles": 0,"equipo":"Watford","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Martins","goles": 0,"equipo":"Watford","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Healeyr","goles": 0,"equipo":"Watford","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Ince","goles": 0,"equipo":"Watford","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Keane","goles": 0,"equipo":"Preston North End","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Holmes","goles": 0,"equipo":"Preston North End","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Riis","goles": 0,"equipo":"Preston North End","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "McCann","goles": 0,"equipo":"Preston North End","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Barnes","goles": 0,"equipo":"Norwich","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Sargent","goles": 0,"equipo":"Norwich","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Gibbs","goles": 0,"equipo":"Norwich","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Idah","goles": 0,"equipo":"Norwich","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Wells","goles": 0,"equipo":"Bristol City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Cornick","goles": 0,"equipo":"Bristol City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Bell","goles": 0,"equipo":"Bristol City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Conway","goles": 0,"equipo":"Bristol City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Delap","goles": 0,"equipo":"Hull City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Lokilo","goles": 0,"equipo":"Hull City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Sinik","goles": 0,"equipo":"Hull City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Connolly","goles": 0,"equipo":"Hull City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Gooch","goles": 0,"equipo":"Stoke City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Campbell","goles": 0,"equipo":"Stoke City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Mmaee","goles": 0,"equipo":"Stoke City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Gayle","goles": 0,"equipo":"Stoke City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Hogan","goles": 0,"equipo":"Birmingham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Jutkiewicz","goles": 0,"equipo":"Birmingham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Roberts","goles": 0,"equipo":"Birmingham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Stansfield","goles": 0,"equipo":"Birmingham","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Koroma","goles": 0,"equipo":"Huddersfield Town","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Burgzorg","goles": 0,"equipo":"Huddersfield Town","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Ward","goles": 0,"equipo":"Huddersfield Town","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Hudlin","goles": 0,"equipo":"Huddersfield Town","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Ugbo","goles": 0,"equipo":"Cardiff City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Robinson","goles": 0,"equipo":"Cardiff City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Bowler","goles": 0,"equipo":"Cardiff City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Grant","goles": 0,"equipo":"Cardiff City","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    {"nombre": "Dykes","goles": 0,"equipo":"Queens Park Rangers","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Adomah","goles": 0,"equipo":"Queens Park Rangers","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Willock","goles": 0,"equipo":"Queens Park Rangers","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    {"nombre": "Smyth","goles": 0,"equipo":"Queens Park Rangers","MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"championship","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
    
    
 {"nombre":"Asensio","goles":0,"equipo":"PSG","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Mbappe","goles":0,"equipo":"PSG","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"O.Dembele","goles":0,"equipo":"PSG","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Muani","goles":0,"equipo":"PSG","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Barcola","goles":0,"equipo":"PSG","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Lacazette","goles":0,"equipo":"Lyon","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Baldé","goles":0,"equipo":"Lyon","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Jeffinho","goles":0,"equipo":"Lyon","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Tolisso","goles":0,"equipo":"Lyon","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Tagliafico","goles":0,"equipo":"Lyon","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Griezmann","goles":0,"equipo":"Atl.Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Morata","goles":0,"equipo":"Atl.Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"de Paul","goles":0,"equipo":"Atl.Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Koke","goles":0,"equipo":"Atl.Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Lemar","goles":0,"equipo":"Atl.Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Lewandowski","goles":0,"equipo":"Barcelona","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Gavi","goles":0,"equipo":"Barcelona","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Felix","goles":0,"equipo":"Barcelona","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Raphinha","goles":0,"equipo":"Barcelona","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Torres","goles":0,"equipo":"Barcelona","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Bellingham","goles":0,"equipo":"Real Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Vinicius","goles":0,"equipo":"Real Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Rodrygo","goles":0,"equipo":"Real Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Modric","goles":0,"equipo":"Real Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Tchouameni","goles":0,"equipo":"Real Madrid","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Haller","goles":0,"equipo":"B.Dortmund","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Moukoko","goles":0,"equipo":"B.Dortmund","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Adeyemi","goles":0,"equipo":"B.Dortmund","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Reus","goles":0,"equipo":"B.Dortmund","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Reyna","goles":0,"equipo":"B.Dortmund","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Gnabry","goles":0,"equipo":"Bayern Munich","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Kane","goles":0,"equipo":"Bayern Munich","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Müller","goles":0,"equipo":"Bayern Munich","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Musiala","goles":0,"equipo":"Bayern Munich","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Sané","goles":0,"equipo":"Bayern Munich","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Tella","goles":0,"equipo":"B.Leverkusen","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Hložek","goles":0,"equipo":"B.Leverkusen","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Hofmann","goles":0,"equipo":"B.Leverkusen","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Adli","goles":0,"equipo":"B.Leverkusen","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Boniface","goles":0,"equipo":"B.Leverkusen","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Paulinho","goles":0,"equipo":"Sporting Lisboa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Trincao","goles":0,"equipo":"Sporting Lisboa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Edwards","goles":0,"equipo":"Sporting Lisboa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Santos","goles":0,"equipo":"Sporting Lisboa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Goncalves","goles":0,"equipo":"Sporting Lisboa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Götze","goles":0,"equipo":"Frankfurt","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Marmoush","goles":0,"equipo":"Frankfurt","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ngankam","goles":0,"equipo":"Frankfurt","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Alario","goles":0,"equipo":"Frankfurt","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Rode","goles":0,"equipo":"Frankfurt","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Aubameyang","goles":0,"equipo":"Marsella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Correa","goles":0,"equipo":"Marsella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Sarr(M)","goles":0,"equipo":"Marsella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ndiaye","goles":0,"equipo":"Marsella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},{"nombre":"Gueye","goles":0,"equipo":"Marsella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Zakharyan","goles":0,"equipo":"Sevilla","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"En-Nesyri","goles":0,"equipo":"Sevilla","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Suso","goles":0,"equipo":"Sevilla","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ocampos","goles":0,"equipo":"Sevilla","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Rakitić","goles":0,"equipo":"Sevilla","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Neres","goles":0,"equipo":"Benfica","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Rafa","goles":0,"equipo":"Benfica","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Di María","goles":0,"equipo":"Benfica","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Musa","goles":0,"equipo":"Benfica","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Gouveia","goles":0,"equipo":"Benfica","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Poulsen","goles":0,"equipo":"Leipzig","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Werner","goles":0,"equipo":"Leipzig","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Sesko","goles":0,"equipo":"Leipzig","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Olmo","goles":0,"equipo":"Leipzig","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Openda","goles":0,"equipo":"Leipzig","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Bergwijn","goles":0,"equipo":"Ajax","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Akpom","goles":0,"equipo":"Ajax","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Mikautadze","goles":0,"equipo":"Ajax","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Godts","goles":0,"equipo":"Ajax","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Tahirovic","goles":0,"equipo":"Ajax","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Ben Yedder","goles":0,"equipo":"Monaco","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Martins(M)","goles":0,"equipo":"Monaco","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Embolo","goles":0,"equipo":"Monaco","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Seghir","goles":0,"equipo":"Monaco","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Camara","goles":0,"equipo":"Monaco","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Traore","goles":0,"equipo":"Shakhtar","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Sikan","goles":0,"equipo":"Shakhtar","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Petryak","goles":0,"equipo":"Shakhtar","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Zubkov","goles":0,"equipo":"Shakhtar","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Bondarenko","goles":0,"equipo":"Shakhtar","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Buchanan","goles":0,"equipo":"Brugge","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Nusa","goles":0,"equipo":"Brugge","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Jutglà","goles":0,"equipo":"Brugge","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Vermant","goles":0,"equipo":"Brugge","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Olsen","goles":0,"equipo":"Brugge","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"de Jong","goles":0,"equipo":"PSV","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Bakayoko","goles":0,"equipo":"PSV","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Til","goles":0,"equipo":"PSV","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Veerman","goles":0,"equipo":"PSV","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Lang","goles":0,"equipo":"PSV","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Sadiq","goles":0,"equipo":"Real Sociedad","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Oyarzabal","goles":0,"equipo":"Real Sociedad","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Andre Silva","goles":0,"equipo":"Real Sociedad","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Kubo","goles":0,"equipo":"Real Sociedad","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Zakharyan","goles":0,"equipo":"Real Sociedad","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"champions","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},





{"nombre":"Martinez","goles":0,"equipo":"Inter","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Alexis Sánchez","goles":0,"equipo":"Inter","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Mkhitaryan","goles":0,"equipo":"Inter","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Calhanoglu","goles":0,"equipo":"Inter","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Arnautovic","goles":0,"equipo":"Inter","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Kean","goles":0,"equipo":"Juventus","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pogba","goles":0,"equipo":"Juventus","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Chiesa","goles":0,"equipo":"Juventus","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Milik","goles":0,"equipo":"Juventus","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Vlahovic","goles":0,"equipo":"Juventus","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Giroud","goles":0,"equipo":"Milan","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Leão","goles":0,"equipo":"Milan","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pulisic","goles":0,"equipo":"Milan","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Jović","goles":0,"equipo":"Milan","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Romero","goles":0,"equipo":"Milan","sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"goles": 0,"MVP":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},



{"nombre":"Osimhen","goles":0,"equipo":"Napoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Raspadori","goles":0,"equipo":"Napoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Simeone","goles":0,"equipo":"Napoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Politano","goles":0,"equipo":"Napoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Kvaratskhelia","goles":0,"equipo":"Napoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

 {"nombre":"Dybala","goles":0,"equipo":"Roma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
 {"nombre":"Belotti","goles":0,"equipo":"Roma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
 {"nombre":"El Shaarawy","goles":0,"equipo":"Roma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
 {"nombre":"Pellegrini","goles":0,"equipo":"Roma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
 {"nombre":"Lukaku","goles":0,"equipo":"Roma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},




{"nombre":"Immobile","goles":0,"equipo":"Lazio","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Anderson","goles":0,"equipo":"Lazio","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pedro(L)","goles":0,"equipo":"Lazio","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Basic","goles":0,"equipo":"Lazio","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Isaksen","goles":0,"equipo":"Lazio","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Muriel","goles":0,"equipo":"Atalanta","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Scamacca","goles":0,"equipo":"Atalanta","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pasalic","goles":0,"equipo":"Atalanta","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Lookman","goles":0,"equipo":"Atalanta","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Adopo","goles":0,"equipo":"Atalanta","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"N.Gonzalez","goles":0,"equipo":"Fiorentina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Arthur","goles":0,"equipo":"Fiorentina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Beltrán","goles":0,"equipo":"Fiorentina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Sottil","goles":0,"equipo":"Fiorentina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Kouamé","goles":0,"equipo":"Fiorentina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Karlsson","goles":0,"equipo":"Bologna","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ndoye","goles":0,"equipo":"Bologna","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Orsolini","goles":0,"equipo":"Bologna","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Hooijdonk","goles":0,"equipo":"Bologna","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Pellegri","goles":0,"equipo":"Torino","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Radonjic","goles":0,"equipo":"Torino","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Sanabria","goles":0,"equipo":"Torino","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Vlasic","goles":0,"equipo":"Torino","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Carvalho","goles":0,"equipo":"Monza","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ciurria","goles":0,"equipo":"Monza","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Maric","goles":0,"equipo":"Monza","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Colombo","goles":0,"equipo":"Monza","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Deulofeu","goles":0,"equipo":"Udinese","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Thauvin","goles":0,"equipo":"Udinese","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Brenner","goles":0,"equipo":"Udinese","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Success","goles":0,"equipo":"Udinese","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Berardi","goles":0,"equipo":"Sassuolo","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Lauriente","goles":0,"equipo":"Sassuolo","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pinamonti","goles":0,"equipo":"Sassuolo","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ceide","goles":0,"equipo":"Sassuolo","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Mulattieri","goles":0,"equipo":"Empoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Cambiaghi","goles":0,"equipo":"Empoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Caputo","goles":0,"equipo":"Empoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Destro","goles":0,"equipo":"Empoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Gyasi","goles":0,"equipo":"Salernitana","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Botheim","goles":0,"equipo":"Salernitana","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Candreva","goles":0,"equipo":"Salernitana","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ikwuemesi","goles":0,"equipo":"Salernitana","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Burnete","goles":0,"equipo":"Lecce","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Piccoli","goles":0,"equipo":"Lecce","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Krstovic","goles":0,"equipo":"Lecce","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Banda","goles":0,"equipo":"Lecce","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Mboula","goles":0,"equipo":"Hellas Verona","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Djuric","goles":0,"equipo":"Hellas Verona","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Braaf","goles":0,"equipo":"Hellas Verona","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ngonge","goles":0,"equipo":"Hellas Verona","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Moro","goles":0,"equipo":"Spezia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Krollis","goles":0,"equipo":"Spezia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Verde","goles":0,"equipo":"Spezia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Elia","goles":0,"equipo":"Spezia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Ciofani","goles":0,"equipo":"Cremonese","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Buonaiuto","goles":0,"equipo":"Cremonese","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Coda","goles":0,"equipo":"Cremonese","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Zanimacchia","goles":0,"equipo":"Cremonese","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Estanis","goles":0,"equipo":"Sampdoria","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Borini","goles":0,"equipo":"Sampdoria","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Gumina","goles":0,"equipo":"Sampdoria","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Monache","goles":0,"equipo":"Sampdoria","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie A","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Cheddira","goles":0,"equipo":"Frosinone","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Kvernadze","goles":0,"equipo":"Frosinone","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Soule","goles":0,"equipo":"Frosinone","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Cuni","goles":0,"equipo":"Frosinone","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Retegui","goles":0,"equipo":"Genoa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Gudmundsson","goles":0,"equipo":"Genoa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ekuban","goles":0,"equipo":"Genoa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Fini","goles":0,"equipo":"Genoa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Diaw","goles":0,"equipo":"Bari","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Nasti","goles":0,"equipo":"Bari","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Maita","goles":0,"equipo":"Bari","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Sibilli","goles":0,"equipo":"Bari","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Colak","goles":0,"equipo":"Parma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Benedyczak","goles":0,"equipo":"Parma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Begic","goles":0,"equipo":"Parma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Mihaila","goles":0,"equipo":"Parma","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Lapadula","goles":0,"equipo":"Cagliari","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pavoletti","goles":0,"equipo":"Cagliari","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Petagna","goles":0,"equipo":"Cagliari","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Zito","goles":0,"equipo":"Cagliari","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Rover","goles":0,"equipo":"Sudtirol","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Odogwu","goles":0,"equipo":"Sudtirol","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pecorino","goles":0,"equipo":"Sudtirol","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Cisco","goles":0,"equipo":"Sudtirol","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Gondo","goles":0,"equipo":"Reggina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Lanini","goles":0,"equipo":"Reggina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pettinari","goles":0,"equipo":"Reggina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Vido","goles":0,"equipo":"Reggina","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Johsen","goles":0,"equipo":"Venezia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pierini","goles":0,"equipo":"Venezia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Tessmann","goles":0,"equipo":"Venezia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pohjanpalo","goles":0,"equipo":"Venezia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Mancuso","goles":0,"equipo":"Palermo","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Brunori","goles":0,"equipo":"Palermo","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Soleri","goles":0,"equipo":"Palermo","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Segre","goles":0,"equipo":"Palermo","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"Modena":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Falcinelli","goles":0,"equipo":"Modena","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Manconi","goles":0,"equipo":"Modena","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Giovannini","goles":0,"equipo":"Modena","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Gerli","goles":0,"equipo":"Modena","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Mlakar","goles":0,"equipo":"Pisa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Torregrossa","goles":0,"equipo":"Pisa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Tramoni","goles":0,"equipo":"Pisa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Nagy","goles":0,"equipo":"Pisa","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Pedro Mendes","goles":0,"equipo":"Ascoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Millico","goles":0,"equipo":"Ascoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Nestorovski","goles":0,"equipo":"Ascoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Caligara","goles":0,"equipo":"Ascoli","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Cutrone","goles":0,"equipo":"Como","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Gabrielloni","goles":0,"equipo":"Como","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Baselli","goles":0,"equipo":"Como","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Cerri","goles":0,"equipo":"Como","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Favili","goles":0,"equipo":"Ternana","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Dionisi","goles":0,"equipo":"Ternana","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Raimondo","goles":0,"equipo":"Ternana","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Proietti","goles":0,"equipo":"Ternana","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Moncini","goles":0,"equipo":"Brescia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Bianchi","goles":0,"equipo":"Brescia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Bisoli","goles":0,"equipo":"Brescia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Ferro","goles":0,"equipo":"Brescia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Magrassi","goles":0,"equipo":"Cittadella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Maistrello","goles":0,"equipo":"Cittadella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Pittarello","goles":0,"equipo":"Cittadella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Danzi","goles":0,"equipo":"Cittadella","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Forte","goles":0,"equipo":"Cosenza","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Tutino","goles":0,"equipo":"Cosenza","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Novello","goles":0,"equipo":"Cosenza","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Crespi","goles":0,"equipo":"Cosenza","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Matos","goles":0,"equipo":"Perugia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Cudrig","goles":0,"equipo":"Perugia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Julitanmo","goles":0,"equipo":"Perugia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Seghetti","goles":0,"equipo":"Perugia","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Antenucci","goles":0,"equipo":"Spal","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Dalmonte","goles":0,"equipo":"Spal","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Siligardi","goles":0,"equipo":"Spal","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Rabbi","goles":0,"equipo":"Spal","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

{"nombre":"Ciano","goles":0,"equipo":"Benevento","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Improta","goles":0,"equipo":"Benevento","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Marotta","goles":0,"equipo":"Benevento","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},
{"nombre":"Bolsius","goles":0,"equipo":"Benevento","asistencias":0,"amarillas":0,"rojas":0,"sancion":0,"sancionado":False,"MVP":0,"MVP de la fecha":0,"mvpcontrol":0,"goles_carabao":0,"amarillas_carabao":0,"asistencias_carabao":0,"rojas_carabao":0,"sancion_carabao":0,"sancionado_carabao":False,"division":"serie B","asistencias":0,"sancionado_champions":False,"goles_champions":0,"asistencias_champions":0,"sancion_champions":0,"rojas_champions":0,"amarillas_champions":0,"sancionado_europa":False,"goles_europa":0,"asistencias_europa":0,"sancion_europa":0,"rojas_europa":0,"amarillas_europa":0,"lesion":0,"lesionado":False},

]

campeones_premier = []
campeones_championship = []
campeones_carabao = []
campeones_comunity = []
campeones_champions = []
campeones_europa = []
campeones_recopa = []
campeones_serieA = []
campeones_serieB = []
campeones_copa_italia = []
campeones_recopa_italia = []
contador = 1
campeon_eurocopa1= ""
campeon_eurocopa2= ""
campeon_eurocopa3= ""
campeon_eurocopa4= ""
campeon_eurocopa5= ""
campeon_eurocopa6= ""
campeon_eurocopa7= ""
campeon_eurocopa8= ""
campeon_eurocopa9= ""
campeon_eurocopa10= ""
campeon_copa_america1= ""
campeon_copa_america2= ""
campeon_copa_america3= ""
campeon_copa_america4= ""
campeon_copa_america5= ""
campeon_copa_america6= ""
campeon_copa_america7= ""
campeon_copa_america8= ""
campeon_copa_america9= ""
campeon_copa_america10= ""
campeon_finalisima1= ""
campeon_finalisima2= ""
campeon_finalisima3= ""
campeon_finalisima4= ""
campeon_finalisima5= ""
campeon_finalisima6= ""
campeon_finalisima7= ""
campeon_finalisima8= ""
campeon_finalisima9= ""
campeon_finalisima10= ""
campeon_copa_africa1= ""
campeon_copa_africa2= ""
campeon_copa_africa3= ""
campeon_copa_africa4= ""
campeon_copa_africa5= ""
campeon_copa_africa6= ""
campeon_copa_africa7= ""
campeon_copa_africa8= ""
campeon_copa_africa9= ""
campeon_copa_africa10= ""
campeon_copa_asia1= ""
campeon_copa_asia2= ""
campeon_copa_asia3= ""
campeon_copa_asia4= ""
campeon_copa_asia5= ""
campeon_copa_asia6= ""
campeon_copa_asia7= ""
campeon_copa_asia8= ""
campeon_copa_asia9= ""
campeon_copa_asia10= ""
campeon_mundial1= ""
campeon_mundial2= ""
campeon_mundial3= ""
campeon_mundial4= ""
campeon_mundial5= ""
clas_europa = []
clas_america = []
clas_africa = []
clas_asia = []
while (contador < 21):
    vitrina = []
    logros_anuales = []
    player["contrato"] -= 1
    
    tabla_serieA = [
    serieA_equipos[0]["tabla"],serieA_equipos[1]["tabla"],serieA_equipos[2]["tabla"],serieA_equipos[3]["tabla"],serieA_equipos[4]["tabla"],serieA_equipos[5]["tabla"],serieA_equipos[6]["tabla"],serieA_equipos[7]["tabla"],serieA_equipos[8]["tabla"],serieA_equipos[9]["tabla"],serieA_equipos[10]["tabla"],serieA_equipos[11]["tabla"],serieA_equipos[12]["tabla"],serieA_equipos[13]["tabla"],serieA_equipos[14]["tabla"],serieA_equipos[15]["tabla"],serieA_equipos[16]["tabla"],serieA_equipos[17]["tabla"],serieA_equipos[18]["tabla"],serieA_equipos[19]["tabla"]
    ]
    tabla_serieB = [
    serieB_equipos[0]["tabla"],serieB_equipos[1]["tabla"],serieB_equipos[2]["tabla"],serieB_equipos[3]["tabla"],serieB_equipos[4]["tabla"],serieB_equipos[5]["tabla"],serieB_equipos[6]["tabla"],serieB_equipos[7]["tabla"],serieB_equipos[8]["tabla"],serieB_equipos[9]["tabla"],serieB_equipos[10]["tabla"],serieB_equipos[11]["tabla"],serieB_equipos[12]["tabla"],serieB_equipos[13]["tabla"],serieB_equipos[14]["tabla"],serieB_equipos[15]["tabla"],serieB_equipos[16]["tabla"],serieB_equipos[17]["tabla"],serieB_equipos[18]["tabla"],serieB_equipos[19]["tabla"]
    ]
    
    tabla_premier = [
    premier_league_equipos[0]["tabla"],premier_league_equipos[1]["tabla"],premier_league_equipos[2]["tabla"],premier_league_equipos[3]["tabla"],premier_league_equipos[4]["tabla"],premier_league_equipos[5]["tabla"],premier_league_equipos[6]["tabla"],premier_league_equipos[7]["tabla"],premier_league_equipos[8]["tabla"],premier_league_equipos[9]["tabla"],premier_league_equipos[10]["tabla"],premier_league_equipos[11]["tabla"],premier_league_equipos[12]["tabla"],premier_league_equipos[13]["tabla"],premier_league_equipos[14]["tabla"],premier_league_equipos[15]["tabla"],premier_league_equipos[16]["tabla"],premier_league_equipos[17]["tabla"],premier_league_equipos[18]["tabla"],premier_league_equipos[19]["tabla"]
    ]

    tabla_championship = [
    sky_by_championship_equipos[0]["tabla"],sky_by_championship_equipos[1]["tabla"],sky_by_championship_equipos[2]["tabla"],sky_by_championship_equipos[3]["tabla"],sky_by_championship_equipos[4]["tabla"],sky_by_championship_equipos[5]["tabla"],sky_by_championship_equipos[6]["tabla"],sky_by_championship_equipos[7]["tabla"],sky_by_championship_equipos[8]["tabla"],sky_by_championship_equipos[9]["tabla"],sky_by_championship_equipos[10]["tabla"],sky_by_championship_equipos[11]["tabla"],sky_by_championship_equipos[12]["tabla"],sky_by_championship_equipos[13]["tabla"],sky_by_championship_equipos[14]["tabla"],sky_by_championship_equipos[15]["tabla"],sky_by_championship_equipos[16]["tabla"],sky_by_championship_equipos[17]["tabla"],sky_by_championship_equipos[18]["tabla"],sky_by_championship_equipos[19]["tabla"]
    ]

    serieA = [
        serieA_equipos[0]["equipo"],serieA_equipos[1]["equipo"],serieA_equipos[2]["equipo"],serieA_equipos[3]["equipo"],serieA_equipos[4]["equipo"],serieA_equipos[5]["equipo"],serieA_equipos[6]["equipo"],serieA_equipos[7]["equipo"],serieA_equipos[8]["equipo"],serieA_equipos[9]["equipo"],serieA_equipos[10]["equipo"],serieA_equipos[11]["equipo"],serieA_equipos[12]["equipo"],serieA_equipos[13]["equipo"],serieA_equipos[14]["equipo"],serieA_equipos[15]["equipo"],serieA_equipos[16]["equipo"],serieA_equipos[17]["equipo"],serieA_equipos[18]["equipo"],serieA_equipos[19]["equipo"]
    ]
    
    serieB = [
        serieB_equipos[0]["equipo"],serieB_equipos[1]["equipo"],serieB_equipos[2]["equipo"],serieB_equipos[3]["equipo"],serieB_equipos[4]["equipo"],serieB_equipos[5]["equipo"],serieB_equipos[6]["equipo"],serieB_equipos[7]["equipo"],serieB_equipos[8]["equipo"],serieB_equipos[9]["equipo"],serieB_equipos[10]["equipo"],serieB_equipos[11]["equipo"],serieB_equipos[12]["equipo"],serieB_equipos[13]["equipo"],serieB_equipos[14]["equipo"],serieB_equipos[15]["equipo"],serieB_equipos[16]["equipo"],serieB_equipos[17]["equipo"],serieB_equipos[18]["equipo"],serieB_equipos[19]["equipo"]
    ]
    
    premier_league = [
           premier_league_equipos[0]["equipo"],premier_league_equipos[1]["equipo"],premier_league_equipos[2]["equipo"],premier_league_equipos[3]["equipo"],premier_league_equipos[4]["equipo"],premier_league_equipos[5]["equipo"],premier_league_equipos[6]["equipo"],premier_league_equipos[7]["equipo"],premier_league_equipos[8]["equipo"],premier_league_equipos[9]["equipo"],premier_league_equipos[10]["equipo"],premier_league_equipos[11]["equipo"],premier_league_equipos[12]["equipo"],premier_league_equipos[13]["equipo"],premier_league_equipos[14]["equipo"],premier_league_equipos[15]["equipo"],premier_league_equipos[16]["equipo"],premier_league_equipos[17]["equipo"],premier_league_equipos[18]["equipo"],premier_league_equipos[19]["equipo"]] 

    sky_by_championship = [
           sky_by_championship_equipos[0]["equipo"],sky_by_championship_equipos[1]["equipo"],sky_by_championship_equipos[2]["equipo"],sky_by_championship_equipos[3]["equipo"],sky_by_championship_equipos[4]["equipo"],sky_by_championship_equipos[5]["equipo"],sky_by_championship_equipos[6]["equipo"],sky_by_championship_equipos[7]["equipo"],sky_by_championship_equipos[8]["equipo"],sky_by_championship_equipos[9]["equipo"],sky_by_championship_equipos[10]["equipo"],sky_by_championship_equipos[11]["equipo"],sky_by_championship_equipos[12]["equipo"],sky_by_championship_equipos[13]["equipo"],sky_by_championship_equipos[14]["equipo"],sky_by_championship_equipos[15]["equipo"],sky_by_championship_equipos[16]["equipo"],sky_by_championship_equipos[17]["equipo"],sky_by_championship_equipos[18]["equipo"],sky_by_championship_equipos[19]["equipo"]]
    
    for i in jugadores:
        if i["nombre"] == player["nombre"]:
            for j in sky_by_championship:
                if j == i["equipo"]:
                    i["division"] = "championship"
            for j in premier_league:
                if j == i["equipo"]:
                    i["division"] = "premier"
            for j in serieA:
                if j == i["equipo"]:
                    i["division"] = "serie A"
            for j in serieB:
                if j == i["equipo"]:
                    i["division"] = "serie B"
    
    n = len(premier_league)
    partidos_por_equipo = 38
    fixture_ida_premier = []
    fixture_vuelta_premier = []

    for i in range(n - 1):
        ronda = []
        for j in range(n // 2):
            if i == 0:
                partido = (premier_league[j], premier_league[n - 1 - j])
            else:
                partido = (premier_league[n - 1 - j], premier_league[j])
            ronda.append(partido)
        fixture_ida_premier.append(ronda)
        premier_league.insert(1, premier_league.pop())
    for ronda_ida in fixture_ida_premier:
        ronda_vuelta = []
        for partido in ronda_ida:
            ronda_vuelta.append((partido[1], partido[0]))
        fixture_vuelta_premier.append(ronda_vuelta)
    n = len(sky_by_championship)
    partidos_por_equipo = 38
    fixture_ida_championship = []
    fixture_vuelta_championship = []
    for i in range(n - 1):
        ronda = []
        for j in range(n // 2):
            if i == 0:
                partido = (sky_by_championship[j], sky_by_championship[n - 1 - j])
            else:
                partido = (sky_by_championship[n - 1 - j], sky_by_championship[j])
            ronda.append(partido)
        fixture_ida_championship.append(ronda)
        sky_by_championship.insert(1, sky_by_championship.pop())
    for ronda_ida in fixture_ida_championship:
        ronda_vuelta = []
        for partido in ronda_ida:
            ronda_vuelta.append((partido[1], partido[0]))
        fixture_vuelta_championship.append(ronda_vuelta)

    n = len(serieA)
    partidos_por_equipo = 38
    fixture_ida_serieA = []
    fixture_vuelta_serieA = []
    for i in range(n - 1):
        ronda = []
        for j in range(n // 2):
            if i == 0:
                partido = (serieA[j], serieA[n - 1 - j])
            else:
                partido = (serieA[n - 1 - j], serieA[j])
            ronda.append(partido)
        fixture_ida_serieA.append(ronda)
        serieA.insert(1, serieA.pop())
    for ronda_ida in fixture_ida_serieA:
        ronda_vuelta = []
        for partido in ronda_ida:
            ronda_vuelta.append((partido[1], partido[0]))
        fixture_vuelta_serieA.append(ronda_vuelta)
    
    n = len(serieB)
    partidos_por_equipo = 38
    fixture_ida_serieB = []
    fixture_vuelta_serieB = []
    for i in range(n - 1):
        ronda = []
        for j in range(n // 2):
            if i == 0:
                partido = (serieB[j], serieB[n - 1 - j])
            else:
                partido = (serieB[n - 1 - j], serieB[j])
            ronda.append(partido)
        fixture_ida_serieB.append(ronda)
        serieB.insert(1, serieB.pop())
    for ronda_ida in fixture_ida_serieB:
        ronda_vuelta = []
        for partido in ronda_ida:
            ronda_vuelta.append((partido[1], partido[0]))
        fixture_vuelta_serieB.append(ronda_vuelta)

    ronda_ida_num = 1
    input("")
    for ronda_premier, ronda_championship, ronda_serieA, ronda_serieB in zip(fixture_ida_premier, fixture_ida_championship,fixture_ida_serieA,fixture_ida_serieB):
        print(f"jornada {ronda_ida_num} Premier League:")
        for partido in ronda_premier:
            print(partido[0], "vs", partido[1])
        input("")
        for partido in ronda_premier:
            generar_partido(partido[0],partido[1],tabla_premier)
            input("")
        input("")
        fct.mostrar_tabla(tabla_premier)
        input("")
        goleadores_totales("p")
        input("")
        asistentes_totales("p")
        input("")
        amarillas_totales("p")
        input("")
        rojas_totales("p")
        input("")
        lesionados_totales("p")
        input("")
        ver_mvp_fecha_premier()
 
        print(f"jornada {ronda_ida_num} Championship:")
        for partido in ronda_championship:
            print(partido[0], "vs", partido[1])
        input("")
        for partido in ronda_championship:
            generar_partido(partido[0],partido[1],tabla_championship)
            input("")
        fct.mostrar_tabla(tabla_championship)
        input("")
        goleadores_totales("c")
        input("")
        asistentes_totales("c")
        input("")
        amarillas_totales("c")
        input("")
        rojas_totales("c")
        input("")
        lesionados_totales("c")
        input("")
        ver_mvp_fecha_championship()
        
        print(f"jornada {ronda_ida_num} Serie A:")
        for partido in ronda_serieA:
            print(partido[0], "vs", partido[1])
        input("")
        for partido in ronda_serieA:
            generar_partido(partido[0],partido[1],tabla_serieA)
            input("")
        input("")
        fct.mostrar_tabla(tabla_serieA)
        input("")
        goleadores_totales("sa")
        input("")
        asistentes_totales("sa")
        input("")
        amarillas_totales("sa")
        input("")
        rojas_totales("sa")
        input("")
        lesionados_totales("sa")
        input("")
        ver_mvp_fecha_seriea()
        
        print(f"jornada {ronda_ida_num} Serie B:")
        for partido in ronda_serieB:
            print(partido[0], "vs", partido[1])
        input("")
        for partido in ronda_serieB:
            generar_partido(partido[0],partido[1],tabla_serieB)
            input("")
        input("")
        fct.mostrar_tabla(tabla_serieB)
        input("")
        goleadores_totales("sb")
        input("")
        asistentes_totales("sb")
        input("")
        amarillas_totales("sb")
        input("")
        rojas_totales("sb")
        input("")
        lesionados_totales("sb")
        input("")
        ver_mvp_fecha_serieb()
        ver_datos_player()
        ronda_ida_num += 1
        recetearmvp()
    
    input("VUELTA")
    playoff_carabao_cup = []
    avos16_carabao = []
    avos16_copa_italia = []
    playoff_copa_italia= []
    equipo_champions = []
    equipo_champions_i_ = []
    equipo_europa = []
    equipo_europa_i_ = []
    equipos_ordenados = sorted(tabla_premier, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        if i < 4:
            equipo_champions.append(nombre_equipo)
        if i == 4: equipo_europa.append(nombre_equipo)
        if i == 5: equipo_europa.append(nombre_equipo)
        if i == 6: equipo_europa.append(nombre_equipo)
        avos16_carabao.append(nombre_equipo)
    equipos_ordenados = sorted(tabla_championship, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        if i < 7:
            avos16_carabao.append(nombre_equipo)
        else:
            playoff_carabao_cup.append(nombre_equipo)
    
    equipos_ordenados = sorted(tabla_serieA, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        if i < 4:
            equipo_champions_i_.append(nombre_equipo)
        if i == 4: equipo_europa_i_.append(nombre_equipo)
        if i == 5: equipo_europa_i_.append(nombre_equipo)
        if i == 6: equipo_europa_i_.append(nombre_equipo)
        avos16_copa_italia.append(nombre_equipo)
    equipos_ordenados = sorted(tabla_serieB, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        if i < 7:
            avos16_copa_italia.append(nombre_equipo)
        else:
            playoff_copa_italia.append(nombre_equipo)
    print("CARABAO CUP")
    input("")
    print("PLAYOFFS DE CLASIFICACION")
    cruce_1_carabao = f"{playoff_carabao_cup[0]} vs {playoff_carabao_cup[11]}"    
    cruce_2_carabao = f"{playoff_carabao_cup[1]} vs {playoff_carabao_cup[10]}"    
    cruce_3_carabao = f"{playoff_carabao_cup[2]} vs {playoff_carabao_cup[9]}"    
    cruce_4_carabao = f"{playoff_carabao_cup[3]} vs {playoff_carabao_cup[8]}"  
    cruce_5_carabao = f"{playoff_carabao_cup[4]} vs {playoff_carabao_cup[7]}"  
    cruce_6_carabao = f"{playoff_carabao_cup[5]} vs {playoff_carabao_cup[6]}"  

    print(cruce_1_carabao)
    print(cruce_2_carabao)
    print(cruce_3_carabao)
    print(cruce_4_carabao)
    print(cruce_5_carabao)
    print(cruce_6_carabao)

    ganador1 = playoff_carabao(playoff_carabao_cup[0],playoff_carabao_cup[11])
    avos16_carabao.append(ganador1)
    ganador2 = playoff_carabao(playoff_carabao_cup[1],playoff_carabao_cup[10])
    avos16_carabao.append(ganador2)
    ganador3 = playoff_carabao(playoff_carabao_cup[2],playoff_carabao_cup[9])
    avos16_carabao.append(ganador3)
    ganador4 = playoff_carabao(playoff_carabao_cup[3],playoff_carabao_cup[8])
    avos16_carabao.append(ganador4)
    ganador5 = playoff_carabao(playoff_carabao_cup[4],playoff_carabao_cup[7])
    avos16_carabao.append(ganador5)
    ganador6 = playoff_carabao(playoff_carabao_cup[5],playoff_carabao_cup[6])
    avos16_carabao.append(ganador6)
    mostrar_datos_carabao()
    print("")
    print("COPA ITALIA")
    input("")
    print("PLAYOFFS DE CLASIFICACION")
    cruce_1_copa_italia = f"{playoff_copa_italia[0]} vs {playoff_copa_italia[11]}"    
    cruce_2_copa_italia = f"{playoff_copa_italia[1]} vs {playoff_copa_italia[10]}"    
    cruce_3_copa_italia = f"{playoff_copa_italia[2]} vs {playoff_copa_italia[9]}"    
    cruce_4_copa_italia = f"{playoff_copa_italia[3]} vs {playoff_copa_italia[8]}"  
    cruce_5_copa_italia = f"{playoff_copa_italia[4]} vs {playoff_copa_italia[7]}"  
    cruce_6_copa_italia = f"{playoff_copa_italia[5]} vs {playoff_copa_italia[6]}"  

    print(cruce_1_copa_italia)
    print(cruce_2_copa_italia)
    print(cruce_3_copa_italia)
    print(cruce_4_copa_italia)
    print(cruce_5_copa_italia)
    print(cruce_6_copa_italia)

    ganador1 = playoff_carabao(playoff_copa_italia[0],playoff_copa_italia[11])
    avos16_copa_italia.append(ganador1)
    ganador2 = playoff_carabao(playoff_copa_italia[1],playoff_copa_italia[10])
    avos16_copa_italia.append(ganador2)
    ganador3 = playoff_carabao(playoff_copa_italia[2],playoff_copa_italia[9])
    avos16_copa_italia.append(ganador3)
    ganador4 = playoff_carabao(playoff_copa_italia[3],playoff_copa_italia[8])
    avos16_copa_italia.append(ganador4)
    ganador5 = playoff_carabao(playoff_copa_italia[4],playoff_copa_italia[7])
    avos16_copa_italia.append(ganador5)
    ganador6 = playoff_carabao(playoff_copa_italia[5],playoff_copa_italia[6])
    avos16_copa_italia.append(ganador6)
    mostrar_datos_copa_italia()
    print("")
    print("")
    input("EUROPA LEAGUE")
    print("")
    equipo_europa_ = []
    equipo_europa_i = []
    for club in equipo_europa:
            if club == "Arsenal":
                equipo_europa_.append(Arsenal)
            elif club == "Aston Villa":
                equipo_europa_.append(Aston_Villa)
            elif club == "Bournemouth":
                equipo_europa_.append(Bournemouth)
            elif club == "Brentford":
                equipo_europa_.append(Brentford)
            elif club == "Brigthon":
                equipo_europa_.append(Brigthon)
            elif club == "Chelsea":
                equipo_europa_.append(Chelsea)
            elif club == "Crystal Palace":
                equipo_europa_.append(Crystal_Palace)
            elif club == "Everton":
                equipo_europa_.append(Everton)
            elif club == "Fulham":
                equipo_europa_.append(Fulham)
            elif club == "Leeds United":
                equipo_europa_.append(Leeds_United)
            elif club == "Leicester City":
                equipo_europa_.append(Leicester_City)
            elif club == "Liverpool":
                equipo_europa_.append(Liverpool)
            elif club == "Manchester City":
                equipo_europa_.append(Manchester_City)
            elif club == "Manchester United":
                equipo_europa_.append(Manchester_United)
            elif club == "Newcastle":
                equipo_europa_.append(Newcastle)
            elif club == "Nottingham Forest":
                equipo_europa_.append(Nottingham_Forest)
            elif club == "Southampton":
                equipo_europa_.append(Southampton)
            elif club == "Tottenham":
                equipo_europa_.append(Tottenham)
            elif club == "West ham":
                equipo_europa_.append(West_ham)
            elif club == "Wolverhampton":
                equipo_europa_.append(Wolverhampton)
            elif club == "Burnley":
                equipo_europa_.append(Burnley)
            elif club == "Sheffield United":
                equipo_europa_.append(Sheffield_United)
            elif club == "Luton Town":
                equipo_europa_.append(Luton_Town)
            elif club == "Middlesbrough":
                equipo_europa_.append(Middlesbrough)
            elif club == "Coventry City":
                equipo_europa_.append(Coventry_City)
            elif club == "Sunderland":
                equipo_europa_.append(Sunderland)
            elif club == "Blackburn Rovers":
                equipo_europa_.append(Blackburn_Rovers)     
            elif club == "Millwall":
                equipo_europa_.append(Millwall)
            elif club == "West Bromwich Albion":
                equipo_europa_.append(West_Bromwich_Albion)   
            elif club == "Swansea":
                equipo_europa_.append(Swansea)
            elif club == "Watford":
                equipo_europa_.append(Watford)  
            elif club == "Preston North End":
                equipo_europa_.append(Preston_North_End)      
            elif club == "Norwich":
                equipo_europa_.append(Norwich)              
            elif club == "Bristol City":
                equipo_europa_.append(Bristol_City)
            elif club == "Hull City":
                equipo_europa_.append(Hull_City)   
            elif club == "Stoke City":
                equipo_europa_.append(Stoke_City)      
            elif club == "Birmingham":
                equipo_europa_.append(Birmingham)   
            elif club == "Huddersfield Town":
                equipo_europa_.append(Huddersfield_Town)
            elif club == "Cardiff City":
                equipo_europa_.append(Cardiff_City)  
            elif club == "Queens Park Rangers":
                equipo_europa_.append(Queens_Park_Rangers)
    for club in equipo_europa_i_:
            if club == "Napoli":
                equipo_europa_i.append(Napoli)
            elif club == "Lazio":
                equipo_europa_i.append(Lazio)
            elif club == "Inter":
                equipo_europa_i.append(Inter)
            elif club == "Milan":
                equipo_europa_i.append(Milan)
            elif club == "Atalanta":
                equipo_europa_i.append(Atalanta)
            elif club == "Roma":
                equipo_europa_i.append(Roma)
            elif club == "Juventus":
                equipo_europa_i.append(Juventus)
            elif club == "Fiorentina":
                equipo_europa_i.append(Fiorentina)
            elif club == "Bologna":
                equipo_europa_i.append(Bologna)
            elif club == "Torino":
                equipo_europa_i.append(Torino)
            elif club == "Monza":
                equipo_europa_i.append(Monza)
            elif club == "Udinese":
                equipo_europa_i.append(Monza)
            elif club == "Sassuolo":
                equipo_europa_i.append(Sassuolo)
            elif club == "Empoli":
                equipo_europa_i.append(Empoli)
            elif club == "Salernitana":
                equipo_europa_i.append(Salernitana)
            elif club == "Lecce":
                equipo_europa_i.append(Lecce)
            elif club == "Hellas Verona":
                equipo_europa_i.append(Hellas_Verona)
            elif club == "Spezia":
                equipo_europa_i.append(Spezia)
            elif club == "Cremonese":
                equipo_europa_i.append(Cremonese)
            elif club == "Sampdoria":
                equipo_europa_i.append(Sampdoria)
            elif club == "Frosinone":
                equipo_europa_i.append(Frosinone)
            elif club == "Genoa":
                equipo_europa_i.append(Genoa)
            elif club == "Bari":
                equipo_europa_i.append(Bari)
            elif club == "Parma":
                equipo_europa_i.append(Parma)
            elif club == "Cagliari":
                equipo_europa_i.append(Cagliari)
            elif club == "Sudtirol":
                equipo_europa_i.append(Sudtirol)
            elif club == "Reggina":
                equipo_europa_i.append(Reggina)     
            elif club == "Venezia":
                equipo_europa_i.append(Venezia)
            elif club == "Palermo":
                equipo_europa_i.append(Palermo)   
            elif club == "Modena":
                equipo_europa_i.append(Modena)
            elif club == "Pisa":
                equipo_europa_i.append(Pisa)  
            elif club == "Ascoli":
                equipo_europa_i.append(Ascoli)      
            elif club == "Como":
                equipo_europa_i.append(Como)              
            elif club == "Ternana":
                equipo_europa_i.append(Ternana)
            elif club == "Brescia":
                equipo_europa_i.append(Brescia)   
            elif club == "Cittadella":
                equipo_europa_i.append(Cittadella)      
            elif club == "Cosenza":
                equipo_europa_i.append(Cosenza)   
            elif club == "Perugia":
                equipo_europa_i.append(Perugia)
            elif club == "Spal":
                equipo_europa_i.append(Spal)  
            elif club == "Benevento":
                equipo_europa_i.append(Benevento)
    
    bombo1 = [equipo_europa_[0],equipo_europa_[1],equipo_europa_[2],psv]
    bombo2 = [equipo_europa_i[0],equipo_europa_i[1],Sporting_Lisboa,equipo_europa_i[2]]
    bombo3 = [Monaco,Real_Sociedad,Marsella,Sevilla]
    bombo4 = [Brugge,Leipzig,Frankfurt,B_Leverkusen]
    bombo_1_mezclado = mezclar_lista(bombo1)
    bombo_2_mezclado = mezclar_lista(bombo2)
    bombo_3_mezclado = mezclar_lista(bombo3)
    bombo_4_mezclado = mezclar_lista(bombo4)
    grupo1_europa = [bombo_1_mezclado[0]["equipo"],bombo_2_mezclado[0]["equipo"],bombo_3_mezclado[0]["equipo"],bombo_4_mezclado[0]["equipo"]]
    tabla1_europa = [bombo_1_mezclado[0]["tabla europa"],bombo_2_mezclado[0]["tabla europa"],bombo_3_mezclado[0]["tabla europa"],bombo_4_mezclado[0]["tabla europa"]]
    fixure_ida_1_europa,fixure_vuelta_1_europa = generar_grupos(grupo1_europa)
    grupo2_europa = [bombo_1_mezclado[1]["equipo"],bombo_2_mezclado[1]["equipo"],bombo_3_mezclado[1]["equipo"],bombo_4_mezclado[1]["equipo"]]
    tabla2_europa = [bombo_1_mezclado[1]["tabla europa"],bombo_2_mezclado[1]["tabla europa"],bombo_3_mezclado[1]["tabla europa"],bombo_4_mezclado[1]["tabla europa"]]
    fixure_ida_2_europa,fixure_vuelta_2_europa = generar_grupos(grupo2_europa)
    grupo3_europa = [bombo_1_mezclado[2]["equipo"],bombo_2_mezclado[2]["equipo"],bombo_3_mezclado[2]["equipo"],bombo_4_mezclado[2]["equipo"]]
    tabla3_europa = [bombo_1_mezclado[2]["tabla europa"],bombo_2_mezclado[2]["tabla europa"],bombo_3_mezclado[2]["tabla europa"],bombo_4_mezclado[2]["tabla europa"]]
    fixure_ida_3_europa,fixure_vuelta_3_europa = generar_grupos(grupo3_europa)
    grupo4_europa = [bombo_1_mezclado[3]["equipo"],bombo_2_mezclado[3]["equipo"],bombo_3_mezclado[3]["equipo"],bombo_4_mezclado[3]["equipo"]]
    tabla4_europa = [bombo_1_mezclado[3]["tabla europa"],bombo_2_mezclado[3]["tabla europa"],bombo_3_mezclado[3]["tabla europa"],bombo_4_mezclado[3]["tabla europa"]]
    fixure_ida_4_europa,fixure_vuelta_4_europa = generar_grupos(grupo4_europa)
    mostrar_grupos_europa_league()
    print("FECHA 1 DE LA EUROPA LEAGUE")
    input("")
    fecha_1_e(fixure_ida_1_europa,1,tabla1_europa)
    fecha_1_e(fixure_ida_2_europa,2,tabla2_europa)
    fecha_1_e(fixure_ida_3_europa,3,tabla3_europa)
    fecha_1_e(fixure_ida_4_europa,4,tabla4_europa)
    fct.mostrar_tablas_fecha_fin(tabla1_europa,tabla2_europa,tabla3_europa,tabla4_europa)
    goleadores_totales_europa()
    asistentes_totales_europa()
    mostrar_ama_europa()
    mostrar_rojas_europa()
    input("CHAMPIONS LEAGUE")
    print("")
    equipos_champions_ = []
    equipo_champions_i = []
    for club in equipo_champions:
            if club == "Arsenal":
                equipos_champions_.append(Arsenal)
            elif club == "Aston Villa":
                equipos_champions_.append(Aston_Villa)
            elif club == "Bournemouth":
                equipos_champions_.append(Bournemouth)
            elif club == "Brentford":
                equipos_champions_.append(Brentford)
            elif club == "Brigthon":
                equipos_champions_.append(Brigthon)
            elif club == "Chelsea":
                equipos_champions_.append(Chelsea)
            elif club == "Crystal Palace":
                equipos_champions_.append(Crystal_Palace)
            elif club == "Everton":
                equipos_champions_.append(Everton)
            elif club == "Fulham":
                equipos_champions_.append(Fulham)
            elif club == "Leeds United":
                equipos_champions_.append(Leeds_United)
            elif club == "Leicester City":
                equipos_champions_.append(Leicester_City)
            elif club == "Liverpool":
                equipos_champions_.append(Liverpool)
            elif club == "Manchester City":
                equipos_champions_.append(Manchester_City)
            elif club == "Manchester United":
                equipos_champions_.append(Manchester_United)
            elif club == "Newcastle":
                equipos_champions_.append(Newcastle)
            elif club == "Nottingham Forest":
                equipos_champions_.append(Nottingham_Forest)
            elif club == "Southampton":
                equipos_champions_.append(Southampton)
            elif club == "Tottenham":
                equipos_champions_.append(Tottenham)
            elif club == "West ham":
                equipos_champions_.append(West_ham)
            elif club == "Wolverhampton":
                equipos_champions_.append(Wolverhampton)
            elif club == "Burnley":
                equipos_champions_.append(Burnley)
            elif club == "Sheffield United":
                equipos_champions_.append(Sheffield_United)
            elif club == "Luton Town":
                equipos_champions_.append(Luton_Town)
            elif club == "Middlesbrough":
                equipos_champions_.append(Middlesbrough)
            elif club == "Coventry City":
                equipos_champions_.append(Coventry_City)
            elif club == "Sunderland":
                equipos_champions_.append(Sunderland)
            elif club == "Blackburn Rovers":
                equipos_champions_.append(Blackburn_Rovers)     
            elif club == "Millwall":
                equipos_champions_.append(Millwall)
            elif club == "West Bromwich Albion":
                equipos_champions_.append(West_Bromwich_Albion)   
            elif club == "Swansea":
                equipos_champions_.append(Swansea)
            elif club == "Watford":
                equipos_champions_.append(Watford)  
            elif club == "Preston North End":
                equipos_champions_.append(Preston_North_End)      
            elif club == "Norwich":
                equipos_champions_.append(Norwich)              
            elif club == "Bristol City":
                equipos_champions_.append(Bristol_City)
            elif club == "Hull City":
                equipos_champions_.append(Hull_City)   
            elif club == "Stoke City":
                equipos_champions_.append(Stoke_City)      
            elif club == "Birmingham":
                equipos_champions_.append(Birmingham)   
            elif club == "Huddersfield Town":
                equipos_champions_.append(Huddersfield_Town)
            elif club == "Cardiff City":
                equipos_champions_.append(Cardiff_City)  
            elif club == "Queens Park Rangers":
                equipos_champions_.append(Queens_Park_Rangers)
    for club in equipo_champions_i_:
            if club == "Napoli":
                equipo_champions_i.append(Napoli)
            elif club == "Lazio":
                equipo_champions_i.append(Lazio)
            elif club == "Inter":
                equipo_champions_i.append(Inter)
            elif club == "Milan":
                equipo_champions_i.append(Milan)
            elif club == "Atalanta":
                equipo_champions_i.append(Atalanta)
            elif club == "Roma":
                equipo_champions_i.append(Roma)
            elif club == "Juventus":
                equipo_champions_i.append(Juventus)
            elif club == "Fiorentina":
                equipo_champions_i.append(Fiorentina)
            elif club == "Bologna":
                equipo_champions_i.append(Bologna)
            elif club == "Torino":
                equipo_champions_i.append(Torino)
            elif club == "Monza":
                equipo_champions_i.append(Monza)
            elif club == "Udinese":
                equipo_champions_i.append(Monza)
            elif club == "Sassuolo":
                equipo_champions_i.append(Sassuolo)
            elif club == "Empoli":
                equipo_champions_i.append(Empoli)
            elif club == "Salernitana":
                equipo_champions_i.append(Salernitana)
            elif club == "Lecce":
                equipo_champions_i.append(Lecce)
            elif club == "Hellas Verona":
                equipo_champions_i.append(Hellas_Verona)
            elif club == "Spezia":
                equipo_champions_i.append(Spezia)
            elif club == "Cremonese":
                equipo_champions_i.append(Cremonese)
            elif club == "Sampdoria":
                equipo_champions_i.append(Sampdoria)
            elif club == "Frosinone":
                equipo_champions_i.append(Frosinone)
            elif club == "Genoa":
                equipo_champions_i.append(Genoa)
            elif club == "Bari":
                equipo_champions_i.append(Bari)
            elif club == "Parma":
                equipo_champions_i.append(Parma)
            elif club == "Cagliari":
                equipo_champions_i.append(Cagliari)
            elif club == "Sudtirol":
                equipo_champions_i.append(Sudtirol)
            elif club == "Reggina":
                equipo_champions_i.append(Reggina)     
            elif club == "Venezia":
                equipo_champions_i.append(Venezia)
            elif club == "Palermo":
                equipo_champions_i.append(Palermo)   
            elif club == "Modena":
                equipo_champions_i.append(Modena)
            elif club == "Pisa":
                equipo_champions_i.append(Pisa)  
            elif club == "Ascoli":
                equipo_champions_i.append(Ascoli)      
            elif club == "Como":
                equipo_champions_i.append(Como)              
            elif club == "Ternana":
                equipo_champions_i.append(Ternana)
            elif club == "Brescia":
                equipo_champions_i.append(Brescia)   
            elif club == "Cittadella":
                equipo_champions_i.append(Cittadella)      
            elif club == "Cosenza":
                equipo_champions_i.append(Cosenza)   
            elif club == "Perugia":
                equipo_champions_i.append(Perugia)
            elif club == "Spal":
                equipo_champions_i.append(Spal)  
            elif club == "Benevento":
                equipo_champions_i.append(Benevento)
        
    
    bombo1 = [equipos_champions_[0],equipos_champions_[1],equipos_champions_[2],Ajax]
    bombo2 = [Real_Madrid,Barcelona,Atl_Madrid,Shakhtar]
    bombo3 = [equipo_champions_i[0],equipo_champions_i[1],equipo_champions_i[2],Benfica]
    bombo4 = [Lyon,psg,Bayern_Munich,B_Dortmund]
    bombo_1_mezclado = mezclar_lista(bombo1)
    bombo_2_mezclado = mezclar_lista(bombo2)
    bombo_3_mezclado = mezclar_lista(bombo3)
    bombo_4_mezclado = mezclar_lista(bombo4)
    grupo1_champions = [bombo_1_mezclado[0]["equipo"],bombo_2_mezclado[0]["equipo"],bombo_3_mezclado[0]["equipo"],bombo_4_mezclado[0]["equipo"]]
    tabla1_champions = [bombo_1_mezclado[0]["tabla premier"],bombo_2_mezclado[0]["tabla premier"],bombo_3_mezclado[0]["tabla premier"],bombo_4_mezclado[0]["tabla premier"]]
    fixure_ida_1,fixure_vuelta_1 = generar_grupos(grupo1_champions)
    grupo2_champions = [bombo_1_mezclado[1]["equipo"],bombo_2_mezclado[1]["equipo"],bombo_3_mezclado[1]["equipo"],bombo_4_mezclado[1]["equipo"]]
    tabla2_champions = [bombo_1_mezclado[1]["tabla premier"],bombo_2_mezclado[1]["tabla premier"],bombo_3_mezclado[1]["tabla premier"],bombo_4_mezclado[1]["tabla premier"]]
    fixure_ida_2,fixure_vuelta_2 = generar_grupos(grupo2_champions)
    grupo3_champions = [bombo_1_mezclado[2]["equipo"],bombo_2_mezclado[2]["equipo"],bombo_3_mezclado[2]["equipo"],bombo_4_mezclado[2]["equipo"]]
    tabla3_champions = [bombo_1_mezclado[2]["tabla premier"],bombo_2_mezclado[2]["tabla premier"],bombo_3_mezclado[2]["tabla premier"],bombo_4_mezclado[2]["tabla premier"]]
    fixure_ida_3,fixure_vuelta_3 = generar_grupos(grupo3_champions)
    grupo4_champions = [bombo_1_mezclado[3]["equipo"],bombo_2_mezclado[3]["equipo"],bombo_3_mezclado[3]["equipo"],bombo_4_mezclado[3]["equipo"]]
    tabla4_champions = [bombo_1_mezclado[3]["tabla premier"],bombo_2_mezclado[3]["tabla premier"],bombo_3_mezclado[3]["tabla premier"],bombo_4_mezclado[3]["tabla premier"]]
    fixure_ida_4,fixure_vuelta_4 = generar_grupos(grupo4_champions)        
    mostrar_grupos_champions()
    
    print("FECHA 1 DE LA CHAMPIONS LEAGUES")
    input("")
    fecha_1(fixure_ida_1,1,tabla1_champions)
    fecha_1(fixure_ida_2,2,tabla2_champions)
    fecha_1(fixure_ida_3,3,tabla3_champions)
    fecha_1(fixure_ida_4,4,tabla4_champions)
    fct.mostrar_tablas_fecha_fin(tabla1_champions,tabla2_champions,tabla3_champions,tabla4_champions)
    goleadores_totales_champions()
    asistentes_totales_champions()
    mostrar_ama_champions()
    mostrar_rojas_champions()
    input("")
    cuartos_champions_primeros = []
    cuartos_champions_segundos = []
    cuartos_europa_primeros = []
    cuartos_europa_segundos = []
    
    apto = 0
    if nacionalidad == "España": 
        if player["valoracion"] > 60: 
            apto = 1
    elif nacionalidad == "Francia":
        if player["valoracion"] > 60:
            apto = 1
    elif nacionalidad == "Holanda":
        if player["valoracion"] > 50:
            apto = 1
    elif nacionalidad == "Inglaterra":
        if player["valoracion"] > 60: 
            apto = 1
    elif nacionalidad == "Italia":
        if player["valoracion"] > 60:
            apto = 1
    elif nacionalidad == "Croacia":
        if player["valoracion"] > 50: 
            apto = 1
    elif nacionalidad == "Belgica":
        if player["valoracion"] > 40:
            apto = 1
    elif nacionalidad == "Portugal":
        if player["valoracion"] > 50: 
            apto = 1
    elif nacionalidad == "Suiza":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Dinamarca":
        if player["valoracion"] > 40: 
            apto = 1
    elif nacionalidad == "Polonia":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Noruega":
        if player["valoracion"] > 30:
            apto = 1
    elif nacionalidad == "Alemania":
        if player["valoracion"] > 60: 
            apto = 1
    elif nacionalidad == "Gales":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Serbia":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Suecia":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Argentina": 
        if player["valoracion"] > 60: 
            apto = 1
    elif nacionalidad == "Uruguay":
        if player["valoracion"] > 60:
            apto = 1
    elif nacionalidad == "Paraguay":
        if player["valoracion"] > 30:
            apto = 1
    elif nacionalidad == "Chile":
        if player["valoracion"] > 50: 
            apto = 1
    elif nacionalidad == "Bolivia":
        if player["valoracion"] > 30:
            apto = 1
    elif nacionalidad == "Brasil":
        if player["valoracion"] > 60: 
            apto = 1
    elif nacionalidad == "Peru":
        if player["valoracion"] > 40:
            apto = 1
    elif nacionalidad == "Colombia":
        if player["valoracion"] > 50: 
            apto = 1
    elif nacionalidad == "Ecuador":
        if player["valoracion"] > 40: 
            apto = 1
    elif nacionalidad == "Venezuela":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Mexico":
        if player["valoracion"] > 40: 
            apto = 1
    elif nacionalidad == "Estados Unidos":
        if player["valoracion"] > 40:
            apto = 1
    elif nacionalidad == "Canada":
        if player["valoracion"] > 40: 
            apto = 1
    elif nacionalidad == "Costa Rica":
        if player["valoracion"] > 20: 
            apto = 1
    elif nacionalidad == "Cuba":
        if player["valoracion"] > 20: 
            apto = 1
    elif nacionalidad == "Honduras":
        if player["valoracion"] > 20: 
            apto = 1
    elif nacionalidad == "Iran": 
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Corea del Sur":
        if player["valoracion"] > 30:
            apto = 1
    elif nacionalidad == "Japon":
        if player["valoracion"] > 40:
            apto = 1
    elif nacionalidad == "China":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Arabia Saudita":
        if player["valoracion"] > 30:
            apto = 1
    elif nacionalidad == "Israel":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Australia":
        if player["valoracion"] > 40:
            apto = 1
    elif nacionalidad == "Qatar":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Egipto": 
        if player["valoracion"] > 40: 
            apto = 1
    elif nacionalidad == "Senegal":
        if player["valoracion"] > 40:
            apto = 1
    elif nacionalidad == "Tunez":
        if player["valoracion"] > 30:
            apto = 1
    elif nacionalidad == "Camerun":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Marruecos":
        if player["valoracion"] > 40:
            apto = 1
    elif nacionalidad == "Nigeria":
        if player["valoracion"] > 30: 
            apto = 1
    elif nacionalidad == "Ghana":
        if player["valoracion"] > 30:
            apto = 1
    elif nacionalidad == "Argelia":
        if player["valoracion"] > 30: 
            apto = 1
    
    if contador == 1:
        campeon_eurocopa1 = jugar_eurocopa()
        campeon_copa_america1 = jugar_copa_america()
        campeon_copa_asia1 = jugar_copa_asia()
        campeon_copa_africa1 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa1} vs {campeon_copa_africa1}")
        print(f"{campeon_copa_america1} vs {campeon_copa_asia1}")
        ganador1 = partido_eurocopa(campeon_eurocopa1,campeon_copa_africa1,apto)
        ganador2 = partido_eurocopa(campeon_copa_america1,campeon_copa_asia1,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima1 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima1}')
        print("")
        input("")
        if apto == 1:
            if campeon_eurocopa1 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa1})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_america1 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america1})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia1 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia1})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa1 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa1})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima1 == player["nacionalidad"]:
                player["valoracion"] += 3 
                trofeo = f"Finalissima ({campeon_finalisima1})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 3:    
        campeon_eurocopa2 = jugar_eurocopa()
        campeon_copa_america2 = jugar_copa_america()
        campeon_copa_asia2 = jugar_copa_asia()
        campeon_copa_africa2 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa2} vs {campeon_copa_asia2}")
        print(f"{campeon_copa_america2} vs {campeon_copa_africa2}")
        ganador1 = partido_eurocopa(campeon_eurocopa2,campeon_copa_asia2,apto)
        ganador2 = partido_eurocopa(campeon_copa_america2,campeon_copa_africa2,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima2 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima2}')
        print("")
        input("")
        input("")
        if apto == 1:
            if campeon_eurocopa2 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa2})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_america2 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america2})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia2 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia2})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa2 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa2})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima2 == player["nacionalidad"]:
                player["valoracion"] += 3  
                trofeo = f"Finalissima ({campeon_finalisima2})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 5:    
        campeon_eurocopa3 = jugar_eurocopa()
        campeon_copa_america3 = jugar_copa_america()
        campeon_copa_asia3 = jugar_copa_asia()
        campeon_copa_africa3 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa3} vs {campeon_copa_africa3}")
        print(f"{campeon_copa_america3} vs {campeon_copa_asia3}")
        ganador1 = partido_eurocopa(campeon_eurocopa3,campeon_copa_africa3,apto)
        ganador2 = partido_eurocopa(campeon_copa_america3,campeon_copa_asia3,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima3 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima3}')
        print("")
        input("")
        if apto == 1:
            if campeon_copa_america3 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america3})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_eurocopa3 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa3})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia3 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia3})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa3 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa3})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima3 == player["nacionalidad"]:
                player["valoracion"] += 3 
                trofeo = f"Finalissima ({campeon_finalisima3})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 7:    
        campeon_eurocopa4 = jugar_eurocopa()
        campeon_copa_america4 = jugar_copa_america()
        campeon_copa_asia4 = jugar_copa_asia()
        campeon_copa_africa4 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa4} vs {campeon_copa_asia4}")
        print(f"{campeon_copa_america4} vs {campeon_copa_africa4}")
        ganador1 = partido_eurocopa(campeon_eurocopa4,campeon_copa_asia4,apto)
        ganador2 = partido_eurocopa(campeon_copa_america4,campeon_copa_africa4,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima4 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima4}')
        print("")
        input("")
        input("")
        if apto == 1:
            if campeon_copa_america4 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america4})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_eurocopa4 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa4})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia4 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia4})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa4 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa4})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima4 == player["nacionalidad"]:
                player["valoracion"] += 3  
                trofeo = f"Finalissima ({campeon_finalisima4})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 9:    
        campeon_eurocopa5 = jugar_eurocopa()
        campeon_copa_america5 = jugar_copa_america()
        campeon_copa_asia5 = jugar_copa_asia()
        campeon_copa_africa5 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa5} vs {campeon_copa_africa5}")
        print(f"{campeon_copa_america5} vs {campeon_copa_asia5}")
        ganador1 = partido_eurocopa(campeon_eurocopa5,campeon_copa_africa5,apto)
        ganador2 = partido_eurocopa(campeon_copa_america5,campeon_copa_asia5,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima5 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima5}')
        print("")
        input("")
        if apto == 1:
            if campeon_copa_america5 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america5})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_eurocopa5 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa5})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia5 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia5})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa5 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa5})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima5 == player["nacionalidad"]:
                player["valoracion"] += 3
                trofeo = f"Finalissima ({campeon_finalisima5})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 11:
        campeon_eurocopa6 = jugar_eurocopa()
        campeon_copa_america6 = jugar_copa_america()
        campeon_copa_asia6 = jugar_copa_asia()
        campeon_copa_africa6 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa6} vs {campeon_copa_africa6}")
        print(f"{campeon_copa_america6} vs {campeon_copa_asia6}")
        ganador1 = partido_eurocopa(campeon_eurocopa6,campeon_copa_africa6,apto)
        ganador2 = partido_eurocopa(campeon_copa_america6,campeon_copa_asia6,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima6 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima6}')
        print("")
        input("")
        if apto == 1:
            if campeon_eurocopa6 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa6})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_america6 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america6})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia6 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia6})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa6 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa6})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima6 == player["nacionalidad"]:
                player["valoracion"] += 3 
                trofeo = f"Finalissima ({campeon_finalisima6})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 13:    
        campeon_eurocopa7 = jugar_eurocopa()
        campeon_copa_america7 = jugar_copa_america()
        campeon_copa_asia7 = jugar_copa_asia()
        campeon_copa_africa7 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa7} vs {campeon_copa_asia7}")
        print(f"{campeon_copa_america7} vs {campeon_copa_africa7}")
        ganador1 = partido_eurocopa(campeon_eurocopa7,campeon_copa_asia7,apto)
        ganador2 = partido_eurocopa(campeon_copa_america7,campeon_copa_africa7,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima7 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima7}')
        print("")
        input("")
        input("")
        if apto == 1:
            if campeon_eurocopa7 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa7})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_america7== player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america7})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia7 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia7})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa7 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa7})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima7 == player["nacionalidad"]:
                player["valoracion"] += 3  
                trofeo = f"Finalissima ({campeon_finalisima7})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 15:    
        campeon_eurocopa8 = jugar_eurocopa()
        campeon_copa_america8 = jugar_copa_america()
        campeon_copa_asia8 = jugar_copa_asia()
        campeon_copa_africa8 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa8} vs {campeon_copa_africa8}")
        print(f"{campeon_copa_america8} vs {campeon_copa_asia8}")
        ganador1 = partido_eurocopa(campeon_eurocopa8,campeon_copa_africa8,apto)
        ganador2 = partido_eurocopa(campeon_copa_america8,campeon_copa_asia8,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima8 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima8}')
        print("")
        input("")
        if apto == 1:
            if campeon_copa_america8 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america8})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_eurocopa8 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa8})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia8 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia8})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa8 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa8})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima8 == player["nacionalidad"]:
                player["valoracion"] += 3 
                trofeo = f"Finalissima ({campeon_finalisima8})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 17:    
        campeon_eurocopa9 = jugar_eurocopa()
        campeon_copa_america9 = jugar_copa_america()
        campeon_copa_asia9 = jugar_copa_asia()
        campeon_copa_africa9 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa9} vs {campeon_copa_asia9}")
        print(f"{campeon_copa_america9} vs {campeon_copa_africa9}")
        ganador1 = partido_eurocopa(campeon_eurocopa9,campeon_copa_asia9,apto)
        ganador2 = partido_eurocopa(campeon_copa_america9,campeon_copa_africa9,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima9 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima9}')
        print("")
        input("")
        input("")
        if apto == 1:
            if campeon_copa_america9 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america9})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_eurocopa9 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa9})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia9 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia9})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa9 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa9})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima9 == player["nacionalidad"]:
                player["valoracion"] += 3  
                trofeo = f"Finalissima ({campeon_finalisima9})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    if contador == 19:    
        campeon_eurocopa10 = jugar_eurocopa()
        campeon_copa_america10 = jugar_copa_america()
        campeon_copa_asia10 = jugar_copa_asia()
        campeon_copa_africa10 = jugar_copa_africa()
        print("")
        input("")
        print("FINALISSIMA")
        print("SEMIFINALES")
        input("")
        print(f"{campeon_eurocopa10} vs {campeon_copa_africa10}")
        print(f"{campeon_copa_america10} vs {campeon_copa_asia10}")
        ganador1 = partido_eurocopa(campeon_eurocopa10,campeon_copa_africa10,apto)
        ganador2 = partido_eurocopa(campeon_copa_america10,campeon_copa_asia10,apto)
        input("")
        print("FINAL")
        print(f"{ganador1} vs {ganador2}")
        input("")
        campeon_finalisima10 = partido_eurocopa(ganador1,ganador2,apto)
        print(f'CAMPEON DE LA FINALISSIMA {campeon_finalisima10}')
        print("")
        input("")
        if apto == 1:
            if campeon_copa_america10 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa America ({campeon_copa_america10})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_eurocopa10 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Eurocopa ({campeon_eurocopa10})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_asia10 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Asia ({campeon_copa_asia10})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_copa_africa10 == player["nacionalidad"]:
                player["valoracion"] += 5   
                trofeo = f"Copa Africa ({campeon_copa_africa10})"
                vitrina.append(trofeo)
                player["dinero"] += 2000000
            if campeon_finalisima10 == player["nacionalidad"]:
                player["valoracion"] += 3
                trofeo = f"Finalissima ({campeon_finalisima10})"
                vitrina.append(trofeo)
                player["dinero"] += 1000000
    
    if contador == 2:
        print("CLASIFICATORIO AL MUNDIAL")
        input("")
        print("EUROPA")
        bo1 = [Alemania,Inglaterra,Italia,España]
        bo2 = [Francia,Holanda,Croacia,Portugal]
        bo3 = [Belgica,Dinamarca,Suiza,Polonia]
        bo4 = [Noruega,Gales,Serbia,Suecia]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_e = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_e = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_e,fixure_vuelta_1_e = generar_grupos(grupo_clasi_1_e)
        
        grupo_clasi_2_e = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_e = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_e,fixure_vuelta_2_e = generar_grupos(grupo_clasi_2_e)
        
        grupo_clasi_3_e = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_e = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_e,fixure_vuelta_3_e = generar_grupos(grupo_clasi_3_e)
        
        grupo_clasi_4_e = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_e = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_e,fixure_vuelta_4_e = generar_grupos(grupo_clasi_4_e)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_e)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_e)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_e)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_e)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
        input("")
        fecha_1_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
        fecha_1_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
        fecha_1_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
        fecha_1_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
        mostrar_datos_selecciones(1)
        input("")
        input("")
        print("AMERICA")
        bo1 = [Argentina,Brasil,Uruguay,Colombia]
        bo2 = [Chile,Peru,Ecuador,Mexico]
        bo3 = [Estados_Unidos,Canada,Venezuela,Bolivia]
        bo4 = [Costa_Rica,Cuba,Honduras,Paraguay]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_a = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_a = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_a,fixure_vuelta_1_a = generar_grupos(grupo_clasi_1_a)
        
        grupo_clasi_2_a = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_a = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_a,fixure_vuelta_2_a = generar_grupos(grupo_clasi_2_a)
        
        grupo_clasi_3_a = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_a = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_a,fixure_vuelta_3_a = generar_grupos(grupo_clasi_3_a)
        
        grupo_clasi_4_a = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_a = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_a,fixure_vuelta_4_a = generar_grupos(grupo_clasi_4_a)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_a)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_a)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_a)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_a)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
        input("")
        fecha_1_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
        fecha_1_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
        fecha_1_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
        fecha_1_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
        mostrar_datos_selecciones(2)
        input("")
        print("AFRICA")
        bo1 = [Egipto,Senegal]
        bo2 = [Marruecos,Nigeria]
        bo3 = [Ghana,Argelia]
        bo4 = [Tunez,Camerun]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_f = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_f = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_f,fixure_vuelta_1_f = generar_grupos(grupo_clasi_1_f)
        grupo_clasi_2_f = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_f = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_f,fixure_vuelta_2_f = generar_grupos(grupo_clasi_2_f)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_f)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_f)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
        input("")
        fecha_1_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
        fecha_1_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
        mostrar_datos_selecciones(3)
        input("")
        print("ASIA")
        bo1 = [Japon,Australia]
        bo2 = [China,Corea_del_Sur]
        bo3 = [Iran,Israel]
        bo4 = [Arabia_Saudita,Qatar]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_s = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_s = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_s,fixure_vuelta_1_s = generar_grupos(grupo_clasi_1_s)
        grupo_clasi_2_s = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_s = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_s,fixure_vuelta_2_s = generar_grupos(grupo_clasi_2_s)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_s)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_s)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL ASIA")
        input("")
        fecha_1_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
        fecha_1_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
        mostrar_datos_selecciones(4)
        input("")
    
    if contador == 6:
        print("CLASIFICATORIO AL MUNDIAL")
        input("")
        print("EUROPA")
        bo1 = [Alemania,Inglaterra,Italia,España]
        bo2 = [Francia,Holanda,Croacia,Portugal]
        bo3 = [Belgica,Dinamarca,Suiza,Polonia]
        bo4 = [Noruega,Gales,Serbia,Suecia]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_e = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_e = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_e,fixure_vuelta_1_e = generar_grupos(grupo_clasi_1_e)
        
        grupo_clasi_2_e = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_e = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_e,fixure_vuelta_2_e = generar_grupos(grupo_clasi_2_e)
        
        grupo_clasi_3_e = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_e = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_e,fixure_vuelta_3_e = generar_grupos(grupo_clasi_3_e)
        
        grupo_clasi_4_e = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_e = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_e,fixure_vuelta_4_e = generar_grupos(grupo_clasi_4_e)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_e)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_e)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_e)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_e)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
        input("")
        fecha_1_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
        fecha_1_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
        fecha_1_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
        fecha_1_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
        mostrar_datos_selecciones(1)
        input("")
        input("")
        print("AMERICA")
        bo1 = [Argentina,Brasil,Uruguay,Colombia]
        bo2 = [Chile,Peru,Ecuador,Mexico]
        bo3 = [Estados_Unidos,Canada,Venezuela,Bolivia]
        bo4 = [Costa_Rica,Cuba,Honduras,Paraguay]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_a = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_a = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_a,fixure_vuelta_1_a = generar_grupos(grupo_clasi_1_a)
        
        grupo_clasi_2_a = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_a = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_a,fixure_vuelta_2_a = generar_grupos(grupo_clasi_2_a)
        
        grupo_clasi_3_a = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_a = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_a,fixure_vuelta_3_a = generar_grupos(grupo_clasi_3_a)
        
        grupo_clasi_4_a = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_a = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_a,fixure_vuelta_4_a = generar_grupos(grupo_clasi_4_a)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_a)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_a)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_a)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_a)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
        input("")
        fecha_1_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
        fecha_1_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
        fecha_1_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
        fecha_1_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
        mostrar_datos_selecciones(2)
        input("")
        print("AFRICA")
        bo1 = [Egipto,Senegal]
        bo2 = [Marruecos,Nigeria]
        bo3 = [Ghana,Argelia]
        bo4 = [Tunez,Camerun]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_f = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_f = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_f,fixure_vuelta_1_f = generar_grupos(grupo_clasi_1_f)
        grupo_clasi_2_f = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_f = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_f,fixure_vuelta_2_f = generar_grupos(grupo_clasi_2_f)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_f)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_f)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
        input("")
        fecha_1_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
        fecha_1_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
        mostrar_datos_selecciones(3)
        input("")
        print("ASIA")
        bo1 = [Japon,Australia]
        bo2 = [China,Corea_del_Sur]
        bo3 = [Iran,Israel]
        bo4 = [Arabia_Saudita,Qatar]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_s = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_s = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_s,fixure_vuelta_1_s = generar_grupos(grupo_clasi_1_s)
        grupo_clasi_2_s = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_s = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_s,fixure_vuelta_2_s = generar_grupos(grupo_clasi_2_s)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_s)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_s)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL ASIA")
        input("")
        fecha_1_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
        fecha_1_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
        mostrar_datos_selecciones(4)
        input("")
     
    if contador == 10:
        print("CLASIFICATORIO AL MUNDIAL")
        input("")
        print("EUROPA")
        bo1 = [Alemania,Inglaterra,Italia,España]
        bo2 = [Francia,Holanda,Croacia,Portugal]
        bo3 = [Belgica,Dinamarca,Suiza,Polonia]
        bo4 = [Noruega,Gales,Serbia,Suecia]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_e = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_e = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_e,fixure_vuelta_1_e = generar_grupos(grupo_clasi_1_e)
        
        grupo_clasi_2_e = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_e = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_e,fixure_vuelta_2_e = generar_grupos(grupo_clasi_2_e)
        
        grupo_clasi_3_e = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_e = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_e,fixure_vuelta_3_e = generar_grupos(grupo_clasi_3_e)
        
        grupo_clasi_4_e = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_e = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_e,fixure_vuelta_4_e = generar_grupos(grupo_clasi_4_e)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_e)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_e)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_e)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_e)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
        input("")
        fecha_1_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
        fecha_1_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
        fecha_1_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
        fecha_1_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e, tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
        mostrar_datos_selecciones(1)
        input("")
        input("")
        print("AMERICA")
        bo1 = [Argentina,Brasil,Uruguay,Colombia]
        bo2 = [Chile,Peru,Ecuador,Mexico]
        bo3 = [Estados_Unidos,Canada,Venezuela,Bolivia]
        bo4 = [Costa_Rica,Cuba,Honduras,Paraguay]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_a = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_a = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_a,fixure_vuelta_1_a = generar_grupos(grupo_clasi_1_a)
        
        grupo_clasi_2_a = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_a = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_a,fixure_vuelta_2_a = generar_grupos(grupo_clasi_2_a)
        
        grupo_clasi_3_a = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_a = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_a,fixure_vuelta_3_a = generar_grupos(grupo_clasi_3_a)
        
        grupo_clasi_4_a = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_a = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_a,fixure_vuelta_4_a = generar_grupos(grupo_clasi_4_a)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_a)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_a)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_a)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_a)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
        input("")
        fecha_1_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
        fecha_1_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
        fecha_1_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
        fecha_1_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a, tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
        mostrar_datos_selecciones(2)
        input("")
        print("AFRICA")
        bo1 = [Egipto,Senegal]
        bo2 = [Marruecos,Nigeria]
        bo3 = [Ghana,Argelia]
        bo4 = [Tunez,Camerun]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_f = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_f = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_f,fixure_vuelta_1_f = generar_grupos(grupo_clasi_1_f)
        grupo_clasi_2_f = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_f = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_f,fixure_vuelta_2_f = generar_grupos(grupo_clasi_2_f)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_f)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_f)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
        input("")
        fecha_1_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
        fecha_1_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
        mostrar_datos_selecciones(3)
        input("")
        print("ASIA")
        bo1 = [Japon,Australia]
        bo2 = [China,Corea_del_Sur]
        bo3 = [Iran,Israel]
        bo4 = [Arabia_Saudita,Qatar]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_s = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_s = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_s,fixure_vuelta_1_s = generar_grupos(grupo_clasi_1_s)
        grupo_clasi_2_s = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_s = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_s,fixure_vuelta_2_s = generar_grupos(grupo_clasi_2_s)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_s)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_s)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL ASIA")
        input("")
        fecha_1_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
        fecha_1_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
        mostrar_datos_selecciones(4)
        input("")
     
    if contador == 14:
        print("CLASIFICATORIO AL MUNDIAL")
        input("")
        print("EUROPA")
        bo1 = [Alemania,Inglaterra,Italia,España]
        bo2 = [Francia,Holanda,Croacia,Portugal]
        bo3 = [Belgica,Dinamarca,Suiza,Polonia]
        bo4 = [Noruega,Gales,Serbia,Suecia]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_e = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_e = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_e,fixure_vuelta_1_e = generar_grupos(grupo_clasi_1_e)
        
        grupo_clasi_2_e = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_e = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_e,fixure_vuelta_2_e = generar_grupos(grupo_clasi_2_e)
        
        grupo_clasi_3_e = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_e = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_e,fixure_vuelta_3_e = generar_grupos(grupo_clasi_3_e)
        
        grupo_clasi_4_e = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_e = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_e,fixure_vuelta_4_e = generar_grupos(grupo_clasi_4_e)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_e)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_e)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_e)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_e)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
        input("")
        fecha_1_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
        fecha_1_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
        fecha_1_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
        fecha_1_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,
                                     tabla_clasi_3_e,tabla_clasi_4_e)  
        mostrar_datos_selecciones(1)
        input("")
        input("")
        print("AMERICA")
        bo1 = [Argentina,Brasil,Uruguay,Colombia]
        bo2 = [Chile,Peru,Ecuador,Mexico]
        bo3 = [Estados_Unidos,Canada,Venezuela,Bolivia]
        bo4 = [Costa_Rica,Cuba,Honduras,Paraguay]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_a = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_a = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_a,fixure_vuelta_1_a = generar_grupos(grupo_clasi_1_a)
        
        grupo_clasi_2_a = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_a = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_a,fixure_vuelta_2_a = generar_grupos(grupo_clasi_2_a)
        
        grupo_clasi_3_a = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_a = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_a,fixure_vuelta_3_a = generar_grupos(grupo_clasi_3_a)
        
        grupo_clasi_4_a = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_a = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_a,fixure_vuelta_4_a = generar_grupos(grupo_clasi_4_a)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_a)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_a)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_a)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_a)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
        input("")
        fecha_1_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
        fecha_1_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
        fecha_1_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
        fecha_1_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
        mostrar_datos_selecciones(2)
        input("")
        print("AFRICA")
        bo1 = [Egipto,Senegal]
        bo2 = [Marruecos,Nigeria]
        bo3 = [Ghana,Argelia]
        bo4 = [Tunez,Camerun]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_f = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_f = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_f,fixure_vuelta_1_f = generar_grupos(grupo_clasi_1_f)
        grupo_clasi_2_f = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_f = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_f,fixure_vuelta_2_f = generar_grupos(grupo_clasi_2_f)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_f)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_f)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
        input("")
        fecha_1_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
        fecha_1_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
        mostrar_datos_selecciones(3)
        input("")
        print("ASIA")
        bo1 = [Japon,Australia]
        bo2 = [China,Corea_del_Sur]
        bo3 = [Iran,Israel]
        bo4 = [Arabia_Saudita,Qatar]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_s = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_s = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_s,fixure_vuelta_1_s = generar_grupos(grupo_clasi_1_s)
        grupo_clasi_2_s = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_s = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_s,fixure_vuelta_2_s = generar_grupos(grupo_clasi_2_s)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_s)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_s)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL ASIA")
        input("")
        fecha_1_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
        fecha_1_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
        mostrar_datos_selecciones(4)
        input("")
    
    if contador == 18:
        print("CLASIFICATORIO AL MUNDIAL")
        input("")
        print("EUROPA")
        bo1 = [Alemania,Inglaterra,Italia,España]
        bo2 = [Francia,Holanda,Croacia,Portugal]
        bo3 = [Belgica,Dinamarca,Suiza,Polonia]
        bo4 = [Noruega,Gales,Serbia,Suecia]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_e = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_e = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_e,fixure_vuelta_1_e = generar_grupos(grupo_clasi_1_e)
        
        grupo_clasi_2_e = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_e = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_e,fixure_vuelta_2_e = generar_grupos(grupo_clasi_2_e)
        
        grupo_clasi_3_e = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_e = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_e,fixure_vuelta_3_e = generar_grupos(grupo_clasi_3_e)
        
        grupo_clasi_4_e = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_e = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_e,fixure_vuelta_4_e = generar_grupos(grupo_clasi_4_e)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_e)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_e)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_e)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_e)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
        input("")
        fecha_1_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
        fecha_1_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
        fecha_1_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
        fecha_1_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
        mostrar_datos_selecciones(1)
        input("")
        input("")
        print("AMERICA")
        bo1 = [Argentina,Brasil,Uruguay,Colombia]
        bo2 = [Chile,Peru,Ecuador,Mexico]
        bo3 = [Estados_Unidos,Canada,Venezuela,Bolivia]
        bo4 = [Costa_Rica,Cuba,Honduras,Paraguay]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_a = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_a = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_a,fixure_vuelta_1_a = generar_grupos(grupo_clasi_1_a)
        
        grupo_clasi_2_a = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_a = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_a,fixure_vuelta_2_a = generar_grupos(grupo_clasi_2_a)
        
        grupo_clasi_3_a = [b1[2]["equipo"],b2[2]["equipo"],b3[2]["equipo"],b4[2]["equipo"]]
        tabla_clasi_3_a = [b1[2]["tabla"],b2[2]["tabla"],b3[2]["tabla"],b4[2]["tabla"]]
        fixure_ida_3_a,fixure_vuelta_3_a = generar_grupos(grupo_clasi_3_a)
        
        grupo_clasi_4_a = [b1[3]["equipo"],b2[3]["equipo"],b3[3]["equipo"],b4[3]["equipo"]]
        tabla_clasi_4_a = [b1[3]["tabla"],b2[3]["tabla"],b3[3]["tabla"],b4[3]["tabla"]]
        fixure_ida_4_a,fixure_vuelta_4_a = generar_grupos(grupo_clasi_4_a)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_a)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_a)
        input("")
        print("Grupo 3")
        print("")
        mostrar_grupos(grupo_clasi_3_a)
        input("")
        print("Grupo 4")
        print("")
        mostrar_grupos(grupo_clasi_4_a)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
        input("")
        fecha_1_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
        fecha_1_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
        fecha_1_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
        fecha_1_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
        fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
        mostrar_datos_selecciones(2)
        input("")
        print("AFRICA")
        bo1 = [Egipto,Senegal]
        bo2 = [Marruecos,Nigeria]
        bo3 = [Ghana,Argelia]
        bo4 = [Tunez,Camerun]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_f = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_f = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_f,fixure_vuelta_1_f = generar_grupos(grupo_clasi_1_f)
        grupo_clasi_2_f = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_f = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_f,fixure_vuelta_2_f = generar_grupos(grupo_clasi_2_f)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_f)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_f)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
        input("")
        fecha_1_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
        fecha_1_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
        mostrar_datos_selecciones(3)
        input("")
        print("ASIA")
        bo1 = [Japon,Australia]
        bo2 = [China,Corea_del_Sur]
        bo3 = [Iran,Israel]
        bo4 = [Arabia_Saudita,Qatar]
        b1 = mezclar_lista(bo1)
        b2 = mezclar_lista(bo2)
        b3 = mezclar_lista(bo3)
        b4 = mezclar_lista(bo4)
        grupo_clasi_1_s = [b1[0]["equipo"],b2[0]["equipo"],b3[0]["equipo"],b4[0]["equipo"]]
        tabla_clasi_1_s = [b1[0]["tabla"],b2[0]["tabla"],b3[0]["tabla"],b4[0]["tabla"]]
        fixure_ida_1_s,fixure_vuelta_1_s = generar_grupos(grupo_clasi_1_s)
        grupo_clasi_2_s = [b1[1]["equipo"],b2[1]["equipo"],b3[1]["equipo"],b4[1]["equipo"]]
        tabla_clasi_2_s = [b1[1]["tabla"],b2[1]["tabla"],b3[1]["tabla"],b4[1]["tabla"]]
        fixure_ida_2_s,fixure_vuelta_2_s = generar_grupos(grupo_clasi_2_s)
        print("GRUPOS")
        input("")
        print("Grupo 1")
        print("")
        mostrar_grupos(grupo_clasi_1_s)
        input("")
        print("Grupo 2")
        print("")
        mostrar_grupos(grupo_clasi_2_s)
        input("")
        print("FECHA 1 DEL CLASIFICATORIO AL MUNDIAL ASIA")
        input("")
        fecha_1_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
        fecha_1_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
        fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
        mostrar_datos_selecciones(4)
        input("")
     
    if contador == 4:
        campeon_mundial1 = jugar_mundial(apto) 
        if apto == 1:
            if campeon_mundial1 == player["nacionalidad"]:
                player["valoracion"] += 5
                trofeo = f"Mundial ({campeon_mundial1})"
                vitrina.append(trofeo)
                player["dinero"] += 5000000
    if contador == 8:
        campeon_mundial2 = jugar_mundial(apto) 
        if apto == 1:
            if campeon_mundial2 == player["nacionalidad"]:
                player["valoracion"] += 5
                trofeo = f"Mundial ({campeon_mundial2})"
                vitrina.append(trofeo)
                player["dinero"] += 5000000
    if contador == 12:
        campeon_mundial3 = jugar_mundial(apto) 
        if apto == 1:
            if campeon_mundial3 == player["nacionalidad"]:
                player["valoracion"] += 5
                trofeo = f"Mundial ({campeon_mundial3})"
                vitrina.append(trofeo)
                player["dinero"] += 5000000
    if contador == 16:
        campeon_mundial4 = jugar_mundial(apto) 
        if apto == 1:
            if campeon_mundial4 == player["nacionalidad"]:
                player["valoracion"] += 5
                trofeo = f"Mundial ({campeon_mundial4})"
                vitrina.append(trofeo)
                player["dinero"] += 5000000
    if contador == 20:
        campeon_mundial5 = jugar_mundial(apto) 
        if apto == 1:
            if campeon_mundial5 == player["nacionalidad"]:
                player["valoracion"] += 5
                trofeo = f"Mundial ({campeon_mundial5})"
                vitrina.append(trofeo)
                player["dinero"] += 5000000
    
    for ronda_premier, ronda_championship,ronda_serieA,ronda_serieB in zip(fixture_vuelta_premier, fixture_vuelta_championship,fixture_vuelta_serieA,fixture_vuelta_serieB):
        print(f"jornada {ronda_ida_num} Premier League:")
        for partido in ronda_premier:
            print(partido[0], "vs", partido[1])
        input("")
        for partido in ronda_premier:
            generar_partido(partido[0],partido[1],tabla_premier)
            input("")
        fct.mostrar_tabla(tabla_premier)
        input("")
        goleadores_totales("p")
        input("")
        asistentes_totales("p")
        input("")
        amarillas_totales("p")
        input("")
        rojas_totales("p")
        input("")
        lesionados_totales("p")
        input("")
        ver_mvp_fecha_premier()

        print(f"jornada {ronda_ida_num} Championship:")
        for partido in ronda_championship:
            print(partido[0], "vs", partido[1])
        input("")
        for partido in ronda_championship:
            generar_partido(partido[0],partido[1],tabla_championship)
            input("")
        fct.mostrar_tabla(tabla_championship)
        input("")
        goleadores_totales("c")
        input("")
        asistentes_totales("c")
        input("")
        amarillas_totales("c")
        input("")
        rojas_totales("c")
        input("")
        lesionados_totales("c")
        input("")
        ver_mvp_fecha_championship()
        print(f"jornada {ronda_ida_num} Serie A:")
        for partido in ronda_serieA:
            print(partido[0], "vs", partido[1])
        input("")
        for partido in ronda_serieA:
            generar_partido(partido[0],partido[1],tabla_serieA)
            input("")
        fct.mostrar_tabla(tabla_serieA)
        input("")
        goleadores_totales("sa")
        input("")
        asistentes_totales("sa")
        input("")
        amarillas_totales("sa")
        input("")
        rojas_totales("sa")
        input("")
        lesionados_totales("sa")
        input("")
        ver_mvp_fecha_seriea()
        print(f"jornada {ronda_ida_num} Serie B:")
        for partido in ronda_serieB:
            print(partido[0], "vs", partido[1])
        input("")
        for partido in ronda_serieB:
            generar_partido(partido[0],partido[1],tabla_serieB)
            input("")
        fct.mostrar_tabla(tabla_serieB)
        input("")
        goleadores_totales("sb")
        input("")
        asistentes_totales("sb")
        input("")
        amarillas_totales("sb")
        input("")
        rojas_totales("sb")
        input("")
        lesionados_totales("sb")
        input("")
        ver_mvp_fecha_serieb()
        ver_datos_player()
        recetearmvp()
        ronda_ida_num += 1
        if contador == 2:
            if ronda_ida_num == 22:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 24:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
                
            if ronda_ida_num == 28:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_1_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_1_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_1_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_1_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_1_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_1_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_1_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_1_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_1_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_1_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_1_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_1_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 30:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 35:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                clas_e_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_e) 
                clas_e_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_e)
                clas_e_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_e)
                clas_e_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_e)  
                clas_europa = [clas_e_1,clas_e_2,clas_e_3,clas_e_4]
                input("")
                print("LOS EUROPEOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_e_1}    
2. {clas_e_2}
3. {clas_e_3}
4. {clas_e_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)
                mostrar_datos_selecciones(2)
                input("")
                clas_a_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_a) 
                clas_a_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_a)
                clas_a_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_a)
                clas_a_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_a)  
                clas_america = [clas_a_1,clas_a_2,clas_a_3,clas_a_4]
                input("")
                print("LOS AMERICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_a_1}    
2. {clas_a_2}
3. {clas_a_3}
4. {clas_a_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)
                mostrar_datos_selecciones(3)
                input("")
                clas_f_1,clas_f_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_f) 
                clas_f_2,clas_f_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_f)
                clas_africa = [clas_f_1,clas_f_2,clas_f_3,clas_f_4]
                input("")
                print("LOS AFRICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_f_1}    
2. {clas_f_2}
3. {clas_f_3}
4. {clas_f_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)
                mostrar_datos_selecciones(4)
                input("")
                clas_s_1,clas_s_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_s) 
                clas_s_2,clas_s_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_s)
                clas_asia = [clas_s_1,clas_s_2,clas_s_3,clas_s_4]
                input("")
                print("LOS ASIATICOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_s_1}    
2. {clas_s_2}
3. {clas_s_3}
4. {clas_s_4}
                ''')
                if apto == 1:
                    if player["nacionalidad"] in [clas_e_1,clas_e_2,clas_e_3,clas_e_4,clas_a_1,clas_a_2,clas_a_3,clas_a_4,clas_f_1,clas_f_2,clas_f_3,clas_f_4,clas_s_1,clas_s_2,clas_s_3,clas_s_4]:
                            logro = f"Clasificacion al mundial con {player['nacionalidad']}"
                            logros_anuales.append(logro)
                            player["valoracion"] += 3
                            player["dinero"] += 250000
        if contador == 6:
            if ronda_ida_num == 22:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 24:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
                
            if ronda_ida_num == 28:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_1_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_1_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_1_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_1_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_1_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_1_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_1_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_1_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_1_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_1_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_1_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_1_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 30:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 35:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                clas_e_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_e) 
                clas_e_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_e)
                clas_e_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_e)
                clas_e_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_e)  
                clas_europa = [clas_e_1,clas_e_2,clas_e_3,clas_e_4]
                input("")
                print("LOS EUROPEOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_e_1}    
2. {clas_e_2}
3. {clas_e_3}
4. {clas_e_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)
                mostrar_datos_selecciones(2)
                input("")
                clas_a_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_a) 
                clas_a_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_a)
                clas_a_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_a)
                clas_a_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_a)  
                clas_america = [clas_a_1,clas_a_2,clas_a_3,clas_a_4]
                input("")
                print("LOS AMERICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_a_1}    
2. {clas_a_2}
3. {clas_a_3}
4. {clas_a_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)
                mostrar_datos_selecciones(3)
                input("")
                clas_f_1,clas_f_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_f) 
                clas_f_2,clas_f_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_f)
                clas_africa = [clas_f_1,clas_f_2,clas_f_3,clas_f_4]
                input("")
                print("LOS AFRICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_f_1}    
2. {clas_f_2}
3. {clas_f_3}
4. {clas_f_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)
                mostrar_datos_selecciones(4)
                input("")
                clas_s_1,clas_s_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_s) 
                clas_s_2,clas_s_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_s)
                clas_asia = [clas_s_1,clas_s_2,clas_s_3,clas_s_4]
                input("")
                print("LOS ASIATICOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_s_1}    
2. {clas_s_2}
3. {clas_s_3}
4. {clas_s_4}
                ''')
                if apto == 1:
                    if player["nacionalidad"] in [clas_e_1,clas_e_2,clas_e_3,clas_e_4,clas_a_1,clas_a_2,clas_a_3,clas_a_4,clas_f_1,clas_f_2,clas_f_3,clas_f_4,clas_s_1,clas_s_2,clas_s_3,clas_s_4]:
                        logro = f"Clasificacion al mundial con {player['nacionalidad']}"
                        logros_anuales.append(logro)
                        player["valoracion"] += 3
                        player["dinero"] += 250000
        if contador == 10:
            if ronda_ida_num == 22:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 24:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
                
            if ronda_ida_num == 28:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_1_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_1_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_1_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_1_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_1_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_1_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_1_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_1_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_1_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_1_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_1_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_1_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 30:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 35:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                clas_e_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_e) 
                clas_e_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_e)
                clas_e_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_e)
                clas_e_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_e)  
                clas_europa = [clas_e_1,clas_e_2,clas_e_3,clas_e_4]
                input("")
                print("LOS EUROPEOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_e_1}    
2. {clas_e_2}
3. {clas_e_3}
4. {clas_e_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)
                mostrar_datos_selecciones(2)
                input("")
                clas_a_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_a) 
                clas_a_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_a)
                clas_a_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_a)
                clas_a_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_a)  
                clas_america = [clas_a_1,clas_a_2,clas_a_3,clas_a_4]
                input("")
                print("LOS AMERICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_a_1}    
2. {clas_a_2}
3. {clas_a_3}
4. {clas_a_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)
                mostrar_datos_selecciones(3)
                input("")
                clas_f_1,clas_f_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_f) 
                clas_f_2,clas_f_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_f)
                clas_africa = [clas_f_1,clas_f_2,clas_f_3,clas_f_4]
                input("")
                print("LOS AFRICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_f_1}    
2. {clas_f_2}
3. {clas_f_3}
4. {clas_f_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)
                mostrar_datos_selecciones(4)
                input("")
                clas_s_1,clas_s_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_s) 
                clas_s_2,clas_s_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_s)
                clas_asia = [clas_s_1,clas_s_2,clas_s_3,clas_s_4]
                input("")
                print("LOS ASIATICOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_s_1}    
2. {clas_s_2}
3. {clas_s_3}
4. {clas_s_4}
                ''')
                if apto == 1:
                    if player["nacionalidad"] in [clas_e_1,clas_e_2,clas_e_3,clas_e_4,clas_a_1,clas_a_2,clas_a_3,clas_a_4,clas_f_1,clas_f_2,clas_f_3,clas_f_4,clas_s_1,clas_s_2,clas_s_3,clas_s_4]:
                        logro = f"Clasificacion al mundial con {player['nacionalidad']}"
                        logros_anuales.append(logro)
                        player["valoracion"] += 3
                        player["dinero"] += 250000
        if contador == 14:
            if ronda_ida_num == 22:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 24:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
                
            if ronda_ida_num == 28:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_1_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_1_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_1_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_1_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_1_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_1_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_1_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_1_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_1_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_1_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_1_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_1_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 30:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 35:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                clas_e_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_e) 
                clas_e_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_e)
                clas_e_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_e)
                clas_e_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_e)  
                clas_europa = [clas_e_1,clas_e_2,clas_e_3,clas_e_4]
                input("")
                print("LOS EUROPEOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_e_1}    
2. {clas_e_2}
3. {clas_e_3}
4. {clas_e_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)
                mostrar_datos_selecciones(2)
                input("")
                clas_a_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_a) 
                clas_a_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_a)
                clas_a_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_a)
                clas_a_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_a)  
                clas_america = [clas_a_1,clas_a_2,clas_a_3,clas_a_4]
                input("")
                print("LOS AMERICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_a_1}    
2. {clas_a_2}
3. {clas_a_3}
4. {clas_a_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)
                mostrar_datos_selecciones(3)
                input("")
                clas_f_1,clas_f_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_f) 
                clas_f_2,clas_f_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_f)
                clas_africa = [clas_f_1,clas_f_2,clas_f_3,clas_f_4]
                input("")
                print("LOS AFRICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_f_1}    
2. {clas_f_2}
3. {clas_f_3}
4. {clas_f_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)
                mostrar_datos_selecciones(4)
                input("")
                clas_s_1,clas_s_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_s) 
                clas_s_2,clas_s_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_s)
                clas_asia = [clas_s_1,clas_s_2,clas_s_3,clas_s_4]
                input("")
                print("LOS ASIATICOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_s_1}    
2. {clas_s_2}
3. {clas_s_3}
4. {clas_s_4}
                ''')
                if apto == 1:
                    if player["nacionalidad"] in [clas_e_1,clas_e_2,clas_e_3,clas_e_4,clas_a_1,clas_a_2,clas_a_3,clas_a_4,clas_f_1,clas_f_2,clas_f_3,clas_f_4,clas_s_1,clas_s_2,clas_s_3,clas_s_4]:
                        logro = f"Clasificacion al mundial con {player['nacionalidad']}"
                        logros_anuales.append(logro)
                        player["valoracion"] += 3
                        player["dinero"] += 250000
        if contador == 18:
            if ronda_ida_num == 22:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 2 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 24:
                print("CLASIFICATORIO AL MUNDIAL")
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_ida_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_ida_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_ida_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_ida_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e) 
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_ida_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_ida_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_ida_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_ida_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a) 
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_ida_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_ida_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f) 
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 3 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_ida_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_ida_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s) 
                mostrar_datos_selecciones(4)
                input("")
                
            if ronda_ida_num == 28:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_1_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_1_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_1_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_1_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_1_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_1_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_1_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_1_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_1_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_1_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 4 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_1_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_1_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 30:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_2_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_2_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_2_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_2_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_2_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_2_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_2_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_2_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)  
                mostrar_datos_selecciones(2)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_2_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_2_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)  
                mostrar_datos_selecciones(3)
                input("")
                print("FECHA 5 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_2_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_2_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)  
                mostrar_datos_selecciones(4)
                input("")
            if ronda_ida_num == 35:
                print("CLASIFICATORIO AL MUNDIAL")
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL EUROPEO")
                input("")
                fecha_3_s(fixure_vuelta_1_e,1,apto,tabla_clasi_1_e)
                fecha_3_s(fixure_vuelta_2_e,2,apto,tabla_clasi_2_e)
                fecha_3_s(fixure_vuelta_3_e,3,apto,tabla_clasi_3_e)
                fecha_3_s(fixure_vuelta_4_e,4,apto,tabla_clasi_4_e)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_e,tabla_clasi_2_e,tabla_clasi_3_e,tabla_clasi_4_e)  
                mostrar_datos_selecciones(1)
                input("")
                clas_e_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_e) 
                clas_e_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_e)
                clas_e_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_e)
                clas_e_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_e)  
                clas_europa = [clas_e_1,clas_e_2,clas_e_3,clas_e_4]
                input("")
                print("LOS EUROPEOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_e_1}    
2. {clas_e_2}
3. {clas_e_3}
4. {clas_e_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AMERICA")
                input("")
                fecha_3_s(fixure_vuelta_1_a,1,apto,tabla_clasi_1_a)
                fecha_3_s(fixure_vuelta_2_a,2,apto,tabla_clasi_2_a)
                fecha_3_s(fixure_vuelta_3_a,3,apto,tabla_clasi_3_a)
                fecha_3_s(fixure_vuelta_4_a,4,apto,tabla_clasi_4_a)
                fct.mostrar_tablas_fecha_fin(tabla_clasi_1_a,tabla_clasi_2_a,tabla_clasi_3_a,tabla_clasi_4_a)
                mostrar_datos_selecciones(2)
                input("")
                clas_a_1,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_a) 
                clas_a_2,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_a)
                clas_a_3,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_3_a)
                clas_a_4,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla_clasi_4_a)  
                clas_america = [clas_a_1,clas_a_2,clas_a_3,clas_a_4]
                input("")
                print("LOS AMERICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_a_1}    
2. {clas_a_2}
3. {clas_a_3}
4. {clas_a_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL AFRICA")
                input("")
                fecha_3_s(fixure_vuelta_1_f,1,apto,tabla_clasi_1_f)
                fecha_3_s(fixure_vuelta_2_f,2,apto,tabla_clasi_2_f)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_f,tabla_clasi_2_f)
                mostrar_datos_selecciones(3)
                input("")
                clas_f_1,clas_f_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_f) 
                clas_f_2,clas_f_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_f)
                clas_africa = [clas_f_1,clas_f_2,clas_f_3,clas_f_4]
                input("")
                print("LOS AFRICANOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_f_1}    
2. {clas_f_2}
3. {clas_f_3}
4. {clas_f_4}
                ''')    
                print("FECHA 6 DEL CLASIFICATORIO AL MUNDIAL ASIA")
                input("")
                fecha_3_s(fixure_vuelta_1_s,1,apto,tabla_clasi_1_s)
                fecha_3_s(fixure_vuelta_2_s,2,apto,tabla_clasi_2_s)
                fct.mostrar_tablas_fecha_fin_(tabla_clasi_1_s,tabla_clasi_2_s)
                mostrar_datos_selecciones(4)
                input("")
                clas_s_1,clas_s_3 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_1_s) 
                clas_s_2,clas_s_4 = fct.obtener_primer_y_segundo_equipo(tabla_clasi_2_s)
                clas_asia = [clas_s_1,clas_s_2,clas_s_3,clas_s_4]
                input("")
                print("LOS ASIATICOS CLASIFICADOS AL MUNDIAL SON")
                print(f'''
1. {clas_s_1}    
2. {clas_s_2}
3. {clas_s_3}
4. {clas_s_4}
                ''')
                if apto == 1:
                    if player["nacionalidad"] in [clas_e_1,clas_e_2,clas_e_3,clas_e_4,clas_a_1,clas_a_2,clas_a_3,clas_a_4,clas_f_1,clas_f_2,clas_f_3,clas_f_4,clas_s_1,clas_s_2,clas_s_3,clas_s_4]:
                        logro = f"Clasificacion al mundial con {player['nacionalidad']}"
                        logros_anuales.append(logro)
                        player["valoracion"] += 3
                        player["dinero"] += 250000
        
        if ronda_ida_num == 21:
            input("")
            print("ERUOPA LEAGUE")
            print("FECHA 2 DE LA EUROPA LEAGUES")
            input("")
            fecha_2_e(fixure_ida_1_europa,1,tabla1_europa)
            fecha_2_e(fixure_ida_2_europa,2,tabla2_europa)
            fecha_2_e(fixure_ida_3_europa,3,tabla3_europa)
            fecha_2_e(fixure_ida_4_europa,4,tabla4_europa)
            fct.mostrar_tablas_fecha_fin(tabla1_europa,tabla2_europa,tabla3_europa,tabla4_europa)
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            
            input("")
            print("CHAMPIONS LEAGUE")
            print("FECHA 2 DE LA CHAMPIONS LEAGUES")
            input("")
            fecha_2(fixure_ida_1,1,tabla1_champions)
            fecha_2(fixure_ida_2,2,tabla2_champions)
            fecha_2(fixure_ida_3,3,tabla3_champions)
            fecha_2(fixure_ida_4,4,tabla4_champions)
            fct.mostrar_tablas_fecha_fin(tabla1_champions,tabla2_champions,tabla3_champions,tabla4_champions)
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()

        if ronda_ida_num == 23:
            print("CARABAO CUP")
            input("")
            print("16 AVOS DE FINAL")
            print(f"{avos16_carabao[0]} vs {avos16_carabao[31]}")
            print(f"{avos16_carabao[1]} vs {avos16_carabao[30]}")
            print(f"{avos16_carabao[2]} vs {avos16_carabao[29]}")
            print(f"{avos16_carabao[3]} vs {avos16_carabao[28]}")
            print(f"{avos16_carabao[4]} vs {avos16_carabao[27]}")
            print(f"{avos16_carabao[5]} vs {avos16_carabao[26]}")
            print(f"{avos16_carabao[6]} vs {avos16_carabao[25]}")
            print(f"{avos16_carabao[7]} vs {avos16_carabao[24]}")
            print(f"{avos16_carabao[8]} vs {avos16_carabao[23]}")
            print(f"{avos16_carabao[9]} vs {avos16_carabao[22]}")
            print(f"{avos16_carabao[10]} vs {avos16_carabao[21]}")
            print(f"{avos16_carabao[11]} vs {avos16_carabao[20]}")
            print(f"{avos16_carabao[12]} vs {avos16_carabao[19]}")
            print(f"{avos16_carabao[13]} vs {avos16_carabao[18]}")
            print(f"{avos16_carabao[14]} vs {avos16_carabao[17]}")
            print(f"{avos16_carabao[15]} vs {avos16_carabao[16]}")

            ganador1 = playoff_carabao(avos16_carabao[0],avos16_carabao[31])
            ganador2 = playoff_carabao(avos16_carabao[1],avos16_carabao[30])
            ganador3 =playoff_carabao(avos16_carabao[2],avos16_carabao[29])
            ganador4 =playoff_carabao(avos16_carabao[3],avos16_carabao[28])
            ganador5 =playoff_carabao(avos16_carabao[4],avos16_carabao[27])
            ganador6 =playoff_carabao(avos16_carabao[5],avos16_carabao[26])
            ganador7 =playoff_carabao(avos16_carabao[6],avos16_carabao[25])
            ganador8 =playoff_carabao(avos16_carabao[7],avos16_carabao[24])
            ganador9 =playoff_carabao(avos16_carabao[8],avos16_carabao[23])
            ganador10 =playoff_carabao(avos16_carabao[9],avos16_carabao[22])
            ganador11 =playoff_carabao(avos16_carabao[10],avos16_carabao[21])
            ganador12 =playoff_carabao(avos16_carabao[11],avos16_carabao[20])
            ganador13 =playoff_carabao(avos16_carabao[12],avos16_carabao[19])
            ganador14 =playoff_carabao(avos16_carabao[13],avos16_carabao[18])
            ganador15 =playoff_carabao(avos16_carabao[14],avos16_carabao[17])
            ganador16 =playoff_carabao(avos16_carabao[15],avos16_carabao[16])
            mostrar_datos_carabao()
            carabao_octavos = [ganador1,ganador2,ganador3,ganador4,ganador5,ganador6,ganador7,ganador8,ganador9,ganador10,ganador11,ganador12,ganador13,ganador14,ganador15,ganador16]

            print("COPA ITALIA")
            input("")
            print("16 AVOS DE FINAL")
            print(f"{avos16_copa_italia[0]} vs {avos16_copa_italia[31]}")
            print(f"{avos16_copa_italia[1]} vs {avos16_copa_italia[30]}")
            print(f"{avos16_copa_italia[2]} vs {avos16_copa_italia[29]}")
            print(f"{avos16_copa_italia[3]} vs {avos16_copa_italia[28]}")
            print(f"{avos16_copa_italia[4]} vs {avos16_copa_italia[27]}")
            print(f"{avos16_copa_italia[5]} vs {avos16_copa_italia[26]}")
            print(f"{avos16_copa_italia[6]} vs {avos16_copa_italia[25]}")
            print(f"{avos16_copa_italia[7]} vs {avos16_copa_italia[24]}")
            print(f"{avos16_copa_italia[8]} vs {avos16_copa_italia[23]}")
            print(f"{avos16_copa_italia[9]} vs {avos16_copa_italia[22]}")
            print(f"{avos16_copa_italia[10]} vs {avos16_copa_italia[21]}")
            print(f"{avos16_copa_italia[11]} vs {avos16_copa_italia[20]}")
            print(f"{avos16_copa_italia[12]} vs {avos16_copa_italia[19]}")
            print(f"{avos16_copa_italia[13]} vs {avos16_copa_italia[18]}")
            print(f"{avos16_copa_italia[14]} vs {avos16_copa_italia[17]}")
            print(f"{avos16_copa_italia[15]} vs {avos16_copa_italia[16]}")

            ganador1 = playoff_carabao(avos16_copa_italia[0],avos16_copa_italia[31])
            ganador2 = playoff_carabao(avos16_copa_italia[1],avos16_copa_italia[30])
            ganador3 =playoff_carabao(avos16_copa_italia[2],avos16_copa_italia[29])
            ganador4 =playoff_carabao(avos16_copa_italia[3],avos16_copa_italia[28])
            ganador5 =playoff_carabao(avos16_copa_italia[4],avos16_copa_italia[27])
            ganador6 =playoff_carabao(avos16_copa_italia[5],avos16_copa_italia[26])
            ganador7 =playoff_carabao(avos16_copa_italia[6],avos16_copa_italia[25])
            ganador8 =playoff_carabao(avos16_copa_italia[7],avos16_copa_italia[24])
            ganador9 =playoff_carabao(avos16_copa_italia[8],avos16_copa_italia[23])
            ganador10 =playoff_carabao(avos16_copa_italia[9],avos16_copa_italia[22])
            ganador11 =playoff_carabao(avos16_copa_italia[10],avos16_copa_italia[21])
            ganador12 =playoff_carabao(avos16_copa_italia[11],avos16_copa_italia[20])
            ganador13 =playoff_carabao(avos16_copa_italia[12],avos16_copa_italia[19])
            ganador14 =playoff_carabao(avos16_copa_italia[13],avos16_copa_italia[18])
            ganador15 =playoff_carabao(avos16_copa_italia[14],avos16_copa_italia[17])
            ganador16 =playoff_carabao(avos16_copa_italia[15],avos16_copa_italia[16])
            mostrar_datos_copa_italia()
            copa_italia_octavos = [ganador1,ganador2,ganador3,ganador4,ganador5,ganador6,ganador7,ganador8,ganador9,ganador10,ganador11,ganador12,ganador13,ganador14,ganador15,ganador16]
        if ronda_ida_num == 23:
            input("")
            print("ERUOPA LEAGUE")
            print("FECHA 3 DE LA EUROPA LEAGUES")
            input("")
            fecha_3_e(fixure_ida_1_europa,1,tabla1_europa)
            fecha_3_e(fixure_ida_2_europa,2,tabla2_europa)
            fecha_3_e(fixure_ida_3_europa,3,tabla3_europa)
            fecha_3_e(fixure_ida_4_europa,4,tabla4_europa)
            fct.mostrar_tablas_fecha_fin(tabla1_europa,tabla2_europa,tabla3_europa,tabla4_europa)
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            input("")
            print("CHAMPIONS LEAGUE")
            print("FECHA 3 DE LA CHAMPIONS LEAGUES")
            input("")
            fecha_3(fixure_ida_1,1,tabla1_champions)
            fecha_3(fixure_ida_2,2,tabla2_champions)
            fecha_3(fixure_ida_3,3,tabla3_champions)
            fecha_3(fixure_ida_4,4,tabla4_champions)
            fct.mostrar_tablas_fecha_fin(tabla1_champions,tabla2_champions,tabla3_champions,tabla4_champions)
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()

        if ronda_ida_num == 25:
            input("")
            print("ERUOPA LEAGUE")
            print("FECHA 4 DE LA EUROPA LEAGUE")
            input("")
            fecha_1_e(fixure_vuelta_1_europa,1,tabla1_europa)
            fecha_1_e(fixure_vuelta_2_europa,2,tabla2_europa)
            fecha_1_e(fixure_vuelta_3_europa,3,tabla3_europa)
            fecha_1_e(fixure_vuelta_4_europa,4,tabla4_europa)
            fct.mostrar_tablas_fecha_fin(tabla1_europa,tabla2_europa,tabla3_europa,tabla4_europa)
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            input("")
            print("CHAMPIONS LEAGUE")
            print("FECHA 4 DE LA CHAMPIONS LEAGUES")
            input("")
            fecha_1(fixure_vuelta_1,1,tabla1_champions)
            fecha_1(fixure_vuelta_2,2,tabla2_champions)
            fecha_1(fixure_vuelta_3,3,tabla3_champions)
            fecha_1(fixure_vuelta_4,4,tabla4_champions)
            fct.mostrar_tablas_fecha_fin(tabla1_champions,tabla2_champions,tabla3_champions,tabla4_champions)
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()
        
        if ronda_ida_num == 26:
            print("CARABAO CUP")
            input("")
            print("OCTAVOS DE FINAL")
            print(f"{carabao_octavos[0]} vs {carabao_octavos[15]}")
            print(f"{carabao_octavos[1]} vs {carabao_octavos[14]}")
            print(f"{carabao_octavos[2]} vs {carabao_octavos[13]}")
            print(f"{carabao_octavos[3]} vs {carabao_octavos[12]}")
            print(f"{carabao_octavos[4]} vs {carabao_octavos[11]}")
            print(f"{carabao_octavos[5]} vs {carabao_octavos[10]}")
            print(f"{carabao_octavos[6]} vs {carabao_octavos[9]}")
            print(f"{carabao_octavos[7]} vs {carabao_octavos[8]}")

            ganador1 = playoff_carabao(carabao_octavos[0],carabao_octavos[15])
            ganador2 = playoff_carabao(carabao_octavos[1],carabao_octavos[14])
            ganador3 =playoff_carabao(carabao_octavos[2],carabao_octavos[13])
            ganador4 =playoff_carabao(carabao_octavos[3],carabao_octavos[12])
            ganador5 =playoff_carabao(carabao_octavos[4],carabao_octavos[11])
            ganador6 =playoff_carabao(carabao_octavos[5],carabao_octavos[10])
            ganador7 =playoff_carabao(carabao_octavos[6],carabao_octavos[9])
            ganador8 =playoff_carabao(carabao_octavos[7],carabao_octavos[8])
            mostrar_datos_carabao()
            carabao_cuartos = [ganador1,ganador2,ganador3,ganador4,ganador5,ganador6,ganador7,ganador8]
            
            print("COPA ITALIA")
            input("")
            print("OCTAVOS DE FINAL")
            print(f"{copa_italia_octavos[0]} vs {copa_italia_octavos[15]}")
            print(f"{copa_italia_octavos[1]} vs {copa_italia_octavos[14]}")
            print(f"{copa_italia_octavos[2]} vs {copa_italia_octavos[13]}")
            print(f"{copa_italia_octavos[3]} vs {copa_italia_octavos[12]}")
            print(f"{copa_italia_octavos[4]} vs {copa_italia_octavos[11]}")
            print(f"{copa_italia_octavos[5]} vs {copa_italia_octavos[10]}")
            print(f"{copa_italia_octavos[6]} vs {copa_italia_octavos[9]}")
            print(f"{copa_italia_octavos[7]} vs {copa_italia_octavos[8]}")

            ganador1 = playoff_carabao(copa_italia_octavos[0],copa_italia_octavos[15])
            ganador2 = playoff_carabao(copa_italia_octavos[1],copa_italia_octavos[14])
            ganador3 =playoff_carabao(copa_italia_octavos[2],copa_italia_octavos[13])
            ganador4 =playoff_carabao(copa_italia_octavos[3],copa_italia_octavos[12])
            ganador5 =playoff_carabao(copa_italia_octavos[4],copa_italia_octavos[11])
            ganador6 =playoff_carabao(copa_italia_octavos[5],copa_italia_octavos[10])
            ganador7 =playoff_carabao(copa_italia_octavos[6],copa_italia_octavos[9])
            ganador8 =playoff_carabao(copa_italia_octavos[7],copa_italia_octavos[8])
            mostrar_datos_copa_italia()
            copa_italia_cuartos = [ganador1,ganador2,ganador3,ganador4,ganador5,ganador6,ganador7,ganador8]
            
        if ronda_ida_num == 27:
            input("")
            print("ERUOPA LEAGUE")
            print("FECHA 5 DE LA EUROPA LEAGUE")
            input("")
            fecha_2_e(fixure_vuelta_1_europa,1,tabla1_europa)
            fecha_2_e(fixure_vuelta_2_europa,2,tabla2_europa)
            fecha_2_e(fixure_vuelta_3_europa,3,tabla3_europa)
            fecha_2_e(fixure_vuelta_4_europa,4,tabla4_europa)
            fct.mostrar_tablas_fecha_fin(tabla1_europa,tabla2_europa,tabla3_europa,tabla4_europa)
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            input("")
            print("CHAMPIONS LEAGUE")
            print("FECHA 5 DE LA CHAMPIONS LEAGUES")
            input("")
            fecha_2(fixure_vuelta_1,1,tabla1_champions)
            fecha_2(fixure_vuelta_2,2,tabla2_champions)
            fecha_2(fixure_vuelta_3,3,tabla3_champions)
            fecha_2(fixure_vuelta_4,4,tabla4_champions)
            fct.mostrar_tablas_fecha_fin(tabla1_champions,tabla2_champions,tabla3_champions,tabla4_champions)
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()

        if ronda_ida_num == 29:
            print("CARABAO CUP")
            input("")
            print("CUARTOS DE FINAL")
            print(f"{carabao_cuartos[0]} vs {carabao_cuartos[7]}")
            print(f"{carabao_cuartos[1]} vs {carabao_cuartos[6]}")
            print(f"{carabao_cuartos[2]} vs {carabao_cuartos[5]}")
            print(f"{carabao_cuartos[3]} vs {carabao_cuartos[4]}")
            
            ganador1 = playoff_carabao(carabao_cuartos[0],carabao_cuartos[7])
            ganador2 = playoff_carabao(carabao_cuartos[1],carabao_cuartos[6])
            ganador3 =playoff_carabao(carabao_cuartos[2],carabao_cuartos[5])
            ganador4 =playoff_carabao(carabao_cuartos[3],carabao_cuartos[4])
            mostrar_datos_carabao()
            carabao_semis = [ganador1,ganador2,ganador3,ganador4]  
            
            print("COPA ITALIA")
            input("")
            print("CUARTOS DE FINAL")
            print(f"{copa_italia_cuartos[0]} vs {copa_italia_cuartos[7]}")
            print(f"{copa_italia_cuartos[1]} vs {copa_italia_cuartos[6]}")
            print(f"{copa_italia_cuartos[2]} vs {copa_italia_cuartos[5]}")
            print(f"{copa_italia_cuartos[3]} vs {copa_italia_cuartos[4]}")
            
            ganador1 = playoff_carabao(copa_italia_cuartos[0],copa_italia_cuartos[7])
            ganador2 = playoff_carabao(copa_italia_cuartos[1],copa_italia_cuartos[6])
            ganador3 =playoff_carabao(copa_italia_cuartos[2],copa_italia_cuartos[5])
            ganador4 =playoff_carabao(copa_italia_cuartos[3],copa_italia_cuartos[4])
            mostrar_datos_copa_italia()
            copa_italia_semis = [ganador1,ganador2,ganador3,ganador4]  

        if ronda_ida_num == 29:
            input("")
            print("ERUOPA LEAGUE")
            print("FECHA 6 DE LA EUROPA LEAGUE")
            input("")
            fecha_3_e(fixure_vuelta_1_europa,1,tabla1_europa)
            fecha_3_e(fixure_vuelta_2_europa,2,tabla2_europa)
            fecha_3_e(fixure_vuelta_3_europa,3,tabla3_europa)
            fecha_3_e(fixure_vuelta_4_europa,4,tabla4_europa)
            fct.mostrar_tablas_fecha_fin(tabla1_europa,tabla2_europa,tabla3_europa,tabla4_europa)
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            primero_1_e,segundo_1_e = fct.obtener_primer_y_segundo_equipo(tabla1_europa)
            primero_2_e,segundo_2_e = fct.obtener_primer_y_segundo_equipo(tabla2_europa)
            primero_3_e,segundo_3_e = fct.obtener_primer_y_segundo_equipo(tabla3_europa)
            primero_4_e,segundo_4_e = fct.obtener_primer_y_segundo_equipo(tabla4_europa)
            cuartos_europa_primeros = [primero_1_e,primero_2_e,primero_3_e,primero_4_e]
            cuartos_europa_segundos = [segundo_1_e,segundo_2_e,segundo_3_e,segundo_4_e]
            input("")
            print("CHAMPIONS LEAGUE")
            print("FECHA 6 DE LA CHAMPIONS LEAGUES")
            input("")
            fecha_3(fixure_vuelta_1,1,tabla1_champions)
            fecha_3(fixure_vuelta_2,2,tabla2_champions)
            fecha_3(fixure_vuelta_3,3,tabla3_champions)
            fecha_3(fixure_vuelta_4,4,tabla4_champions)
            fct.mostrar_tablas_fecha_fin(tabla1_champions,tabla2_champions,tabla3_champions,tabla4_champions)
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()
            primero_1_c,segundo_1_c = fct.obtener_primer_y_segundo_equipo(tabla1_champions)
            primero_2_c,segundo_2_c = fct.obtener_primer_y_segundo_equipo(tabla2_champions)
            primero_3_c,segundo_3_c = fct.obtener_primer_y_segundo_equipo(tabla3_champions)
            primero_4_c,segundo_4_c = fct.obtener_primer_y_segundo_equipo(tabla4_champions)
            cuartos_champions_primeros = [primero_1_c,primero_2_c,primero_3_c,primero_4_c]
            cuartos_champions_segundos = [segundo_1_c,segundo_2_c,segundo_3_c,segundo_4_c]
            
        if ronda_ida_num == 31:
            input("")
            print("ERUOPA LEAGUE")
            cuartos_europa_primeros_mezclados = cuartos_europa_primeros.copy()
            random.shuffle(cuartos_europa_primeros_mezclados)
            cuartos_europa_segundos_mezclados  = cuartos_europa_segundos.copy()
            random.shuffle(cuartos_europa_primeros_mezclados)
            input("")
            print("CUARTOS DE FINAL")
            input("")
            print(cuartos_europa_primeros_mezclados[0],"vs",cuartos_europa_segundos_mezclados[0])
            print(cuartos_europa_primeros_mezclados[1],"vs",cuartos_europa_segundos_mezclados[1])
            print(cuartos_europa_primeros_mezclados[2],"vs",cuartos_europa_segundos_mezclados[2])
            print(cuartos_europa_primeros_mezclados[3],"vs",cuartos_europa_segundos_mezclados[3])
            input("CUARTOS DE FINAL IDA")
            print("")
            input("")
            goles_local_cuartos_1_europa,goles_visitantes_cuartos_1_europa = partidos_europa_ida(cuartos_europa_primeros_mezclados[0],cuartos_europa_segundos_mezclados[0])
            print("")
            input("")
            goles_local_cuartos_2_europa,goles_visitantes_cuartos_2_europa = partidos_europa_ida(cuartos_europa_primeros_mezclados[1],cuartos_europa_segundos_mezclados[1])
            print("")
            input("")
            goles_local_cuartos_3_europa,goles_visitantes_cuartos_3_europa = partidos_europa_ida(cuartos_europa_primeros_mezclados[2],cuartos_europa_segundos_mezclados[2])
            print("")
            input("")
            goles_local_cuartos_4_europa,goles_visitantes_cuartos_4_europa = partidos_europa_ida(cuartos_europa_primeros_mezclados[3],cuartos_europa_segundos_mezclados[3])
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            
            input("")
            print("CHAMPIONS LEAGUE")
            cuartos_champions_primeros_mezclados = cuartos_champions_primeros.copy()
            random.shuffle(cuartos_champions_primeros_mezclados)
            cuartos_champions_segundos_mezclados  = cuartos_champions_segundos.copy()
            random.shuffle(cuartos_champions_segundos_mezclados)
            input("")
            print("CUARTOS DE FINAL")
            input("")
            print(cuartos_champions_primeros_mezclados[0],"vs",cuartos_champions_segundos_mezclados[0])
            print(cuartos_champions_primeros_mezclados[1],"vs",cuartos_champions_segundos_mezclados[1])
            print(cuartos_champions_primeros_mezclados[2],"vs",cuartos_champions_segundos_mezclados[2])
            print(cuartos_champions_primeros_mezclados[3],"vs",cuartos_champions_segundos_mezclados[3])
            input("CUARTOS DE FINAL IDA")
            print("")
            input("")
            goles_local_cuartos_1_champions,goles_visitantes_cuartos_1_champions = partidos_champions_ida(cuartos_champions_primeros_mezclados[0],cuartos_champions_segundos_mezclados[0])
            print("")
            input("")
            goles_local_cuartos_2_champions,goles_visitantes_cuartos_2_champions = partidos_champions_ida(cuartos_champions_primeros_mezclados[1],cuartos_champions_segundos_mezclados[1])
            print("")
            input("")
            goles_local_cuartos_3_champions,goles_visitantes_cuartos_3_champions = partidos_champions_ida(cuartos_champions_primeros_mezclados[2],cuartos_champions_segundos_mezclados[2])
            print("")
            input("")
            goles_local_cuartos_4_champions,goles_visitantes_cuartos_4_champions = partidos_champions_ida(cuartos_champions_primeros_mezclados[3],cuartos_champions_segundos_mezclados[3])
                        
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()
            
        if ronda_ida_num == 32:
            semis_champions = []
            semis_europa = []
            input("")
            print("EUROPA LEAGUE")
            input("CUARTOS DE FINAL VUELTA")
            print(f"{cuartos_europa_segundos_mezclados[0]} {goles_visitantes_cuartos_1_europa} - {goles_local_cuartos_1_europa} {cuartos_europa_primeros_mezclados[0]}")
            print(f"{cuartos_europa_segundos_mezclados[1]} {goles_visitantes_cuartos_2_europa} - {goles_local_cuartos_2_europa} {cuartos_europa_primeros_mezclados[1]}")
            print(f"{cuartos_europa_segundos_mezclados[2]} {goles_visitantes_cuartos_3_europa} - {goles_local_cuartos_3_europa} {cuartos_europa_primeros_mezclados[2]}")
            print(f"{cuartos_europa_segundos_mezclados[3]} {goles_visitantes_cuartos_4_europa} - {goles_local_cuartos_4_europa} {cuartos_europa_primeros_mezclados[3]}")
            input("")
            print("")
            print(cuartos_europa_segundos_mezclados[0],"vs",cuartos_europa_primeros_mezclados[0])
            input("")
            print("")
            ganador1 = partidos_europa_vuelta(cuartos_europa_segundos_mezclados[0],cuartos_europa_primeros_mezclados[0],goles_local_cuartos_1_europa,goles_visitantes_cuartos_1_europa)
            input("")
            print("")
            print(cuartos_europa_segundos_mezclados[1],"vs",cuartos_europa_primeros_mezclados[1])
            input("")
            print("")
            ganador2 = partidos_europa_vuelta(cuartos_europa_segundos_mezclados[1],cuartos_europa_primeros_mezclados[1],goles_local_cuartos_2_europa,goles_visitantes_cuartos_2_europa)
            input("")
            print("")
            print(cuartos_europa_segundos_mezclados[2],"vs",cuartos_europa_primeros_mezclados[2])
            input("")
            print("")
            ganador3 = partidos_europa_vuelta(cuartos_europa_segundos_mezclados[2],cuartos_europa_primeros_mezclados[2],goles_local_cuartos_3_europa,goles_visitantes_cuartos_3_europa)
            input("")
            print("")
            print(cuartos_europa_segundos_mezclados[3],"vs",cuartos_europa_primeros_mezclados[3])
            input("")
            print("")
            ganador4 = partidos_europa_vuelta(cuartos_europa_segundos_mezclados[3],cuartos_europa_primeros_mezclados[3],goles_local_cuartos_4_europa,goles_visitantes_cuartos_4_europa)
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            semis_europa = [ganador1,ganador2,ganador3,ganador4]
            input("")
            print("CHAMPIONS LEAGUE")
            input("CUARTOS DE FINAL VUELTA")
            print(f"{cuartos_champions_segundos_mezclados[0]} {goles_visitantes_cuartos_1_champions} - {goles_local_cuartos_1_champions} {cuartos_champions_primeros_mezclados[0]}")
            print(f"{cuartos_champions_segundos_mezclados[1]} {goles_visitantes_cuartos_2_champions} - {goles_local_cuartos_2_champions} {cuartos_champions_primeros_mezclados[1]}")
            print(f"{cuartos_champions_segundos_mezclados[2]} {goles_visitantes_cuartos_3_champions} - {goles_local_cuartos_3_champions} {cuartos_champions_primeros_mezclados[2]}")
            print(f"{cuartos_champions_segundos_mezclados[3]} {goles_visitantes_cuartos_4_champions} - {goles_local_cuartos_4_champions} {cuartos_champions_primeros_mezclados[3]}")
            input("")
            print("")
            print(cuartos_champions_segundos_mezclados[0],"vs",cuartos_champions_primeros_mezclados[0])
            input("")
            print("")
            ganador1 = partidos_champions_vuelta(cuartos_champions_segundos_mezclados[0],cuartos_champions_primeros_mezclados[0],goles_local_cuartos_1_champions,goles_visitantes_cuartos_1_champions)
            input("")
            print("")
            print(cuartos_champions_segundos_mezclados[1],"vs",cuartos_champions_primeros_mezclados[1])
            input("")
            print("")
            ganador2 = partidos_champions_vuelta(cuartos_champions_segundos_mezclados[1],cuartos_champions_primeros_mezclados[1],goles_local_cuartos_2_champions,goles_visitantes_cuartos_2_champions)
            input("")
            print("")
            print(cuartos_champions_segundos_mezclados[2],"vs",cuartos_champions_primeros_mezclados[2])
            input("")
            print("")
            ganador3 = partidos_champions_vuelta(cuartos_champions_segundos_mezclados[2],cuartos_champions_primeros_mezclados[2],goles_local_cuartos_3_champions,goles_visitantes_cuartos_3_champions)
            input("")
            print("")
            print(cuartos_champions_segundos_mezclados[3],"vs",cuartos_champions_primeros_mezclados[3])
            input("")
            print("")
            ganador4 = partidos_champions_vuelta(cuartos_champions_segundos_mezclados[3],cuartos_champions_primeros_mezclados[3],goles_local_cuartos_4_champions,goles_visitantes_cuartos_4_champions)
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()
            semis_champions = [ganador1,ganador2,ganador3,ganador4]
        if ronda_ida_num == 34:
            print("CARABAO CUP")
            input("")
            print("SEMIFINALES")
            print(f"{carabao_semis[0]} vs {carabao_semis[3]}")
            print(f"{carabao_semis[1]} vs {carabao_semis[2]}")

            ganador1 = playoff_carabao(carabao_semis[0],carabao_semis[3])
            ganador2 = playoff_carabao(carabao_semis[1],carabao_semis[2])
            if ganador1 == carabao_semis[0]: perdedor_Semi_cara1 = carabao_semis[3]
            else : perdedor_Semi_cara1 = carabao_semis[0]
            if ganador2 == carabao_semis[1]: perdedor_Semi_cara2 = carabao_semis[2]
            else : perdedor_Semi_cara2 = carabao_semis[1]
            mostrar_datos_carabao()
            carabao_final = [ganador1,ganador2]
            
            print("COPA ITALIA")
            input("")
            print("SEMIFINALES")
            print(f"{copa_italia_semis[0]} vs {copa_italia_semis[3]}")
            print(f"{copa_italia_semis[1]} vs {copa_italia_semis[2]}")

            ganador1 = playoff_carabao(copa_italia_semis[0],copa_italia_semis[3])
            ganador2 = playoff_carabao(copa_italia_semis[1],copa_italia_semis[2])
            if ganador1 == copa_italia_semis[0]: perdedor_Semi_copa_italia1 = copa_italia_semis[3]
            else : perdedor_Semi_copa_italia1 = copa_italia_semis[0]
            if ganador2 == copa_italia_semis[1]: perdedor_Semi_copa_italia2 = copa_italia_semis[2]
            else : perdedor_Semi_copa_italia2 = copa_italia_semis[1]
            mostrar_datos_copa_italia()
            copa_italia_final = [ganador1,ganador2]
        
        if ronda_ida_num == 36:
            print("SEMIFINALES")
            print("EUROPA LEAGUE")
            input("")
            print(semis_europa[0],"vs",semis_europa[1])
            print(semis_europa[2],"vs",semis_europa[3])
            input("SEMIFINALES IDA")
            print("")
            print(semis_europa[0],"vs",semis_europa[1])
            input("")
            print("")
            goles_local_semis_1_europa , goles_visitantes_semis_1_europa = partidos_europa_ida(semis_europa[0],semis_europa[1])
            print("")
            print(semis_europa[2],"vs",semis_europa[3])
            input("")
            print("")
            goles_local_semis_2_europa , goles_visitantes_semis_2_europa = partidos_europa_ida(semis_europa[2],semis_europa[3])
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            input("")
            print("SEMIFINALES")
            print("CHAMPIONS LEAGUE")
            input("")
            print(semis_champions[0],"vs",semis_champions[1])
            print(semis_champions[2],"vs",semis_champions[3])
            input("SEMIFINALES IDA")
            print("")
            print(semis_champions[0],"vs",semis_champions[1])
            input("")
            print("")
            goles_local_semis_1_champions , goles_visitantes_semis_1_champions = partidos_champions_ida(semis_champions[0],semis_champions[1])
            print("")
            print(semis_champions[2],"vs",semis_champions[3])
            input("")
            print("")
            goles_local_semis_2_champions , goles_visitantes_semis_2_champions = partidos_champions_ida(semis_champions[2],semis_champions[3])
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()
            
        if ronda_ida_num == 37:
            print("EUROPA LEAGUE")
            input("SEMIFINALES VUELTA")
            print(f"{semis_europa[1]} {goles_visitantes_semis_1_europa} - {goles_local_semis_1_europa} {semis_europa[0]}")
            print(f"{semis_europa[3]} {goles_visitantes_semis_2_europa} - {goles_local_semis_2_europa} {semis_europa[2]}")
            input("")
            print("")
            print(semis_europa[1],"vs",semis_europa[0])
            input("")
            print("")
            ganador1 = partidos_europa_vuelta(semis_europa[1],semis_europa[0],goles_local_semis_1_europa,goles_visitantes_semis_1_europa)
            input("")
            if ganador1 == semis_europa[1]: perdedor_Semi_europa1 = semis_europa[0]
            else : perdedor_Semi_europa1 = semis_europa[1]
            print("")
            print(semis_europa[3],"vs",semis_europa[2])
            input("")
            print("")
            ganador2 = partidos_europa_vuelta(semis_europa[3],semis_europa[2],goles_local_semis_2_europa,goles_visitantes_semis_2_europa)
            goleadores_totales_europa()
            if ganador2 == semis_europa[3]: perdedor_Semi_europa2 = semis_europa[2]
            else : perdedor_Semi_europa2 = semis_europa[3]
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            final_europa = [ganador1,ganador2]
            
            print("CHAMPIONS LEAGUE")
            input("SEMIFINALES VUELTA")
            print(f"{semis_champions[1]} {goles_visitantes_semis_1_champions} - {goles_local_semis_1_champions} {semis_champions[0]}")
            print(f"{semis_champions[3]} {goles_visitantes_semis_2_champions} - {goles_local_semis_2_champions} {semis_champions[2]}")
            input("")
            print("")
            print(semis_champions[1],"vs",semis_champions[0])
            input("")
            print("")
            ganador1 = partidos_champions_vuelta(semis_champions[1],semis_champions[0],goles_local_semis_1_champions,goles_visitantes_semis_1_champions)
            input("")
            print("")
            print(semis_champions[3],"vs",semis_champions[2])
            input("")
            print("")
            ganador2 = partidos_champions_vuelta(semis_champions[3],semis_champions[2],goles_local_semis_2_champions,goles_visitantes_semis_2_champions)
            
            if ganador1 == semis_champions[0]: perdedor_Semi_champions1 = semis_champions[1]
            else : perdedor_Semi_champions1 = semis_champions[0]
            
            if ganador2 == semis_champions[3]: perdedor_Semi_champions2 = semis_champions[2]
            else : perdedor_Semi_champions2 = semis_champions[3]
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()
            final_champions = [ganador1,ganador2]
        if ronda_ida_num == 38:
            print("CARABAO CUP")
            input("")
            print("FINAL")
            print(f"{carabao_final[0]} vs {carabao_final[1]}")

            ganador1 = playoff_carabao(carabao_final[0],carabao_final[1])
            campeon_carabao = ganador1
            if campeon_carabao == carabao_final[0]:
                perdedor_carabao = carabao_final[1]
            else: perdedor_carabao = carabao_final[0]
            print(f"CAMPEON DE LA CARABAO CUP {campeon_carabao}")   
            input("")
            mostrar_datos_carabao()
            print("COPA ITALIA")
            input("")
            print("FINAL")
            print(f"{copa_italia_final[0]} vs {copa_italia_final[1]}")

            ganador1 = playoff_carabao(copa_italia_final[0],copa_italia_final[1])
            campeon_copa_italia = ganador1
            if campeon_copa_italia == copa_italia_final[0]:
                perdedor_copa_italia = copa_italia_final[1]
            else: perdedor_copa_italia = copa_italia_final[0]
            print(f"CAMPEON DE LA COPA ITALIA {campeon_copa_italia}")   
            input("")
            mostrar_datos_copa_italia()

        if ronda_ida_num == 38:
            input("")
            print("EUROPA LEAGUE")
            print("FINAL")
            input("")
            print(f"{final_europa[0]} - {final_europa[1]}")
            jugadores_sancionados_locales = sancionados_europa(final_europa[0])
            jugadores_sancionados_visitantes = sancionados_europa(final_europa[1])
            desancionar_europa(final_europa[0])
            desancionar_europa(final_europa[1])
            jugadores_lesionados_locales = lesionados(final_europa[0])
            jugadores_lesionados_visitantes = lesionados(final_europa[1])
            deslesionar(final_europa[0])
            deslesionar(final_europa[1])
            input("")
            result,club1,goallocal,goalsvisitor,club2 = fct.resultado(final_europa[0],final_europa[1])
            if goallocal != 0:
                goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
                for i in goles_totales:
                    sumar_gol_europa(i)
                asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"]) 
                if len(asistencias_local) != 0:
                    for i in asistencias_local:
                        sumar_asistencia_europa(i)
            amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
            rojas_locales = taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
            lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
            if len(lesionados_locales) != 0:
                for i in lesionados_locales:
                    actualizar_lesionados(i[0],i[1])
            if len(amarillas_locales) != 0:
                for i in amarillas_locales:
                    actualizar_rustico_europa(i,1,0)     
            if len(rojas_locales) != 0:
                for i in rojas_locales:
                    actualizar_rustico_europa(i,0,1) 
            if goalsvisitor != 0:
                goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
                for i in goles_totalesv:
                    sumar_gol_europa(i)
                asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
                if len(asistenciasvisitor) != 0:
                    for i in asistenciasvisitor:
                        sumar_asistencia_europa(i)
            amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
            rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
            lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
            if len(lesionados_visitantes) != 0:
                for i in lesionados_visitantes:
                    actualizar_lesionados(i[0],i[1])
            if len(amarillas_visitor) != 0:
                for i in amarillas_visitor:
                    actualizar_rustico_europa(i,1,0)
            if len(rojas_visitor) != 0:
                for i in rojas_visitor:
                    actualizar_rustico_europa(i,0,1) 
            if goallocal > goalsvisitor:
                print(F"CAMPEON DE LA EUROPA LEAGUE {club1}")
                campeon_europa = club1
                perdedor_europa = club2
            elif goalsvisitor > goallocal:    
                print(f"CAMEPON DE LA EUROPA LEAGUE {club2}")
                campeon_europa = club2
                perdedor_europa = club1
            else:
                penalty_local = fct.numero_random() 
                penalty_visitor = fct.numero_random()
                if penalty_local == penalty_visitor:
                    aux = penalty_visitor - 1
                    penalty_visitor = aux    
                print("PENALES")
                input("")
                print(f'{club1} {penalty_local} - {penalty_visitor} {club2}') 
                if penalty_local > penalty_visitor:
                    print(f'CAMEPON DE LA EUROPA LEAGUE {club1}')
                    campeon_europa = club1
                    perdedor_europa = club2
                else:
                    print(f'CAMEPON DE LA EUROPA LEAGUE {club2}')    
                    campeon_europa = club2
                    perdedor_europa = club1
            goleadores_totales_europa()
            asistentes_totales_europa()
            mostrar_ama_europa()
            mostrar_rojas_europa()
            input("")
            input("")
            print("CHAMPIONS LEAGUE")
            print("FINAL")
            input("")
            print(f"{final_champions[0]} - {final_champions[1]}")
            jugadores_sancionados_locales = sancionados_champions(final_champions[0])
            jugadores_sancionados_visitantes = sancionados_champions(final_champions[1])
            desancionar_champions(final_champions[0])
            desancionar_champions(final_champions[1])
            jugadores_lesionados_locales = lesionados(final_champions[0])
            jugadores_lesionados_visitantes = lesionados(final_champions[1])
            deslesionar(final_champions[0])
            deslesionar(final_champions[1])
            input("")
            result,club1,goallocal,goalsvisitor,club2 = fct.resultado(final_champions[0],final_champions[1])
            if goallocal != 0:
                goles_totales = taq.goleadores(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
                for i in goles_totales:
                    sumar_gol_champions(i)
                asistencias_local = taq.asistentes(club1,goallocal,jugadores_sancionados_locales,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"]) 
                if len(asistencias_local) != 0:
                    for i in asistencias_local:
                        sumar_asistencia_champions(i)
            amarillas_locales = taq.amarillas(club1,jugadores_sancionados_locales,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
            rojas_locales = taq.rojas(club1,jugadores_sancionados_locales,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
            lesionados_locales = taq.lesiones(club1,jugadores_sancionados_locales,jugadores_lesionados_locales,player["equipo"],player["valoracion"],player["nombre"])
            if len(lesionados_locales) != 0:
                for i in lesionados_locales:
                    actualizar_lesionados(i[0],i[1])
            if len(amarillas_locales) != 0:
                for i in amarillas_locales:
                    actualizar_rustico_champions(i,1,0)     
            if len(rojas_locales) != 0:
                for i in rojas_locales:
                    actualizar_rustico_champions(i,0,1) 
            if goalsvisitor != 0:
                goles_totalesv = taq.goleadores(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
                for i in goles_totalesv:
                    sumar_gol_champions(i)
                asistenciasvisitor = taq.asistentes(club2,goalsvisitor,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
                if len(asistenciasvisitor) != 0:
                    for i in asistenciasvisitor:
                        sumar_asistencia_champions(i)
            amarillas_visitor = taq.amarillas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
            rojas_visitor = taq.rojas(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
            lesionados_visitantes = taq.lesiones(club2,jugadores_sancionados_visitantes,jugadores_lesionados_visitantes,player["equipo"],player["valoracion"],player["nombre"])
            if len(lesionados_visitantes) != 0:
                for i in lesionados_visitantes:
                    actualizar_lesionados(i[0],i[1])
            if len(amarillas_visitor) != 0:
                for i in amarillas_visitor:
                    actualizar_rustico_champions(i,1,0)
            if len(rojas_visitor) != 0:
                for i in rojas_visitor:
                    actualizar_rustico_champions(i,0,1) 
            if goallocal > goalsvisitor:
                print(F"CAMPEON DE LA CHAMPIONS LEAGUE {club1}")
                campeon_champions = club1
                perdedor_champions = club2
            elif goalsvisitor > goallocal:    
                print(f"CAMEPON DE LA CHAMPIONS LEAGUE {club2}")
                campeon_champions = club2
                perdedor_champions = club1
            else:
                penalty_local = fct.numero_random() 
                penalty_visitor = fct.numero_random()
                if penalty_local == penalty_visitor:
                    aux = penalty_visitor - 1
                    penalty_visitor = aux    
                print("PENALES")
                input("")
                print(f'{club1} {penalty_local} - {penalty_visitor} {club2}') 
                if penalty_local > penalty_visitor:
                    print(f'CAMEPON DE LA CHAMPIONS LEAGUE {club1}')
                    campeon_champions = club1
                    perdedor_champions = club2
                else:
                    print(f'CAMEPON DE LA CHAMPIONS LEAGUE {club2}')    
                    campeon_champions = club2
                    perdedor_champions = club1
            goleadores_totales_champions()
            asistentes_totales_champions()
            mostrar_ama_champions()
            mostrar_rojas_champions()
            input("")
    campeon_carabaoo = campeon_carabao
    campeon_copa_italiaa = campeon_copa_italia
    equipos_ordenados = sorted(tabla_premier, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        if i == 1:
            campeon_premier = nombre_equipo
        if i == 20:
            if nombre_equipo == player["equipo"]:
                player["valoracion"] -= 5
                player["dinero"] -= 250000
        if i == 19:
            if nombre_equipo == player["equipo"]:
                player["valoracion"] -= 5
                player["dinero"] -= 250000
        if i == 18:
            if nombre_equipo == player["equipo"]:
                player["valoracion"] -= 5
                player["dinero"] -= 250000
        if nombre_equipo == player["equipo"]:
            if i == 2:
                logro = f"segundo puesto en la Premier League con {nombre_equipo}"
                logros_anuales.append(logro)
                player["dinero"] += 750000
            elif i == 3:
                logro = f"tercer puesto en la Premier League con {nombre_equipo}"
                logros_anuales.append(logro)
                player["dinero"] += 500000
    
    equipos_ordenados = sorted(tabla_championship, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        if i == 1:
            campeon_championship = nombre_equipo
        if nombre_equipo == player["equipo"]:
            if i == 1:
                logro = f"ascenso en la Champioship con {nombre_equipo}"
                logros_anuales.append(logro)
                if nombre_equipo == player["equipo"]:
                    player["valoracion"] += 4
                    player["dinero"] += 250000
            if i == 2:
                logro = f"ascenso en la Champioship con {nombre_equipo}"
                logros_anuales.append(logro)
                if nombre_equipo == player["equipo"]:
                    player["valoracion"] += 4
                    player["dinero"] += 250000
            elif i == 3:
                logro = f"ascenso en la Champioship con {nombre_equipo}"
                logros_anuales.append(logro)
                if nombre_equipo == player["equipo"]:
                    player["valoracion"] += 4
                    player["dinero"] += 250000
    
    equipos_ordenados = sorted(tabla_serieA, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        if i == 1:
            campeon_serieA = nombre_equipo
        if i == 20:
            if nombre_equipo == player["equipo"]:
                player["valoracion"] -= 5
                player["dinero"] -= 250000
        if i == 19:
            if nombre_equipo == player["equipo"]:
                player["valoracion"] -= 5
                player["dinero"] -= 250000
        if i == 18:
            if nombre_equipo == player["equipo"]:
                player["valoracion"] -= 5
                player["dinero"] -= 250000
        if nombre_equipo == player["equipo"]:
            if i == 2:
                logro = f"segundo puesto en la Serie A con {nombre_equipo}"
                logros_anuales.append(logro)
                player["dinero"] += 750000
            elif i == 3:
                logro = f"tercer puesto en la Serie A con {nombre_equipo}"
                logros_anuales.append(logro)
                player["dinero"] += 500000
    
    equipos_ordenados = sorted(tabla_serieB, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        if i == 1:
            campeon_serieB = nombre_equipo
        if nombre_equipo == player["equipo"]:
            if i == 1:
                logro = f"ascenso en la Serie B con {nombre_equipo}"
                logros_anuales.append(logro)
                if nombre_equipo == player["equipo"]:
                    player["valoracion"] += 4
                    player["dinero"] += 250000
            if i == 2:
                logro = f"ascenso en la Serie B con {nombre_equipo}"
                logros_anuales.append(logro)
                if nombre_equipo == player["equipo"]:
                    player["valoracion"] += 4
                    player["dinero"] += 250000
            elif i == 3:
                logro = f"ascenso en la Serie B con {nombre_equipo}"
                logros_anuales.append(logro)
                if nombre_equipo == player["equipo"]:
                    player["valoracion"] += 4
                    player["dinero"] += 250000
    
    if perdedor_copa_italia == player["equipo"]: 
        logro = f'segundo puesto en la Copa Italia con {perdedor_copa_italia}'
        player["dinero"] += 200000
        logros_anuales.append(logro)
        player["valoracion"] += 2
    if perdedor_carabao == player["equipo"]: 
        logro = f'segundo puesto en la Carabao Cup con {perdedor_carabao}'
        player["dinero"] += 200000
        logros_anuales.append(logro)
        player["valoracion"] += 2
    if perdedor_champions == player["equipo"]: 
        logro = f'segundo puesto en la Champions League con {perdedor_champions}'
        player["dinero"] += 500000
        logros_anuales.append(logro)
        player["valoracion"] += 3
    if perdedor_europa == player["equipo"]: 
        logro = f'segundo puesto en la Europa League con {perdedor_europa}'
        player["dinero"] += 500000
        logros_anuales.append(logro)  
        player["valoracion"] += 2
    if perdedor_Semi_europa1 ==  player["equipo"]:
        logro = f'Semifinalista de la Europa League con {perdedor_Semi_europa1}'
        player["dinero"] += 200000
        logros_anuales.append(logro) 
        player["valoracion"] += 1 
    if perdedor_Semi_europa2 ==  player["equipo"]:
        logro = f'Semifinalista de la Europa League con {perdedor_Semi_europa2}'
        player["dinero"] += 200000
        logros_anuales.append(logro)  
        player["valoracion"] += 1
    if perdedor_Semi_champions1 ==  player["equipo"]:
        logro = f'Semifinalista de la Champions League con {perdedor_Semi_champions1}'
        player["dinero"] += 250000
        logros_anuales.append(logro)  
        player["valoracion"] += 1
    if perdedor_Semi_champions2 ==  player["equipo"]:
        logro = f'Semifinalista de la Champions League con {perdedor_Semi_champions2}'
        player["dinero"] += 250000
        logros_anuales.append(logro)
        player["valoracion"] += 1
    if perdedor_Semi_cara1 ==  player["equipo"]:
        logro = f'Semifinalista de la Carabao cup con {perdedor_Semi_cara1}'
        player["dinero"] += 100000
        logros_anuales.append(logro)  
        player["valoracion"] += 1
    if perdedor_Semi_cara2 ==  player["equipo"]:
        logro = f'Semifinalista de la Carabao cup con {perdedor_Semi_cara2}'
        player["dinero"] += 100000
        logros_anuales.append(logro)
        player["valoracion"] += 1
    if perdedor_Semi_copa_italia1 ==  player["equipo"]:
        logro = f'Semifinalista de la Copa Italia con {perdedor_Semi_copa_italia1}'
        player["dinero"] += 100000
        logros_anuales.append(logro)  
        player["valoracion"] += 1
    if perdedor_Semi_copa_italia2 ==  player["equipo"]:
        logro = f'Semifinalista de la Copa Italia con {perdedor_Semi_copa_italia2}'
        player["dinero"] += 100000
        logros_anuales.append(logro)
        player["valoracion"] += 1
    
    input("")
    print("")
    print(f"Campeon de la premier league: {campeon_premier}")
    input("")
    print(f"Campeon de la championship: {campeon_championship}")
    input("")
    print("COMMUNITY SHIELD")
    if campeon_carabao == campeon_premier:
        campeon_carabao = perdedor_carabao
    elif campeon_carabao == campeon_championship:
        campeon_carabao = perdedor_carabao
        input("")
    print("SEMIFINALES DE LA COMMUNITY SHIELD")
    print(campeon_carabao, "vs", campeon_championship)
    ganadorsemicomu = playoff_carabao(campeon_carabao,campeon_championship)
    input("")
    print("FINAL COMMUNITY SHIELD")
    print(campeon_premier,"vs",ganadorsemicomu)
    campeon_comunity = playoff_carabao(campeon_premier,ganadorsemicomu)
    print("")
    print(f'CAMPEON DE LA COMUNNITY SHIELD {campeon_comunity}')
    print("")
    print(f"Campeon de la Serie A: {campeon_serieA}")
    input("")
    print(f"Campeon de la Serie B: {campeon_serieB}")
    input("")
    print("RECOPA ITALIANA")
    input("")
    if campeon_copa_italia == campeon_serieA:
        campeon_copa_italia = perdedor_copa_italia
    elif campeon_copa_italia == campeon_serieB:
        campeon_copa_italia = perdedor_copa_italia
    input("")
    print("SEMIFINALES DE LA RECOPA ITALIANA")
    print(campeon_copa_italia, "vs", campeon_serieB)
    ganadorsemicomuu = playoff_carabao(campeon_copa_italia,campeon_serieB)
    input("")
    print("FINAL RECOPA ITALIANA")
    print(campeon_serieA,"vs",ganadorsemicomuu)
    campeon_recopa_italia = playoff_carabao(campeon_serieA,ganadorsemicomuu)
    print("")
    print(f'CAMPEON DE LA RECOPA ITALIANA {campeon_recopa_italia}')
    input("")
    print("FINAL DE LA RECOPA EUROPEA")
    print("")
    print(f'{campeon_champions} vs {campeon_europa}')
    ganador_recopa = playoff_carabao(campeon_champions,campeon_europa)
    print("")
    print(f'CAMPEON DE LA RECOPA DE EUROPA {ganador_recopa}')
    input("")
    print(F'''
LOS CAMPEONES DE ESTE AÑO SON:
1. {campeon_premier} (Premier League)
2. {campeon_championship} (Sky By Championship)
3. {campeon_carabaoo} (Carabao Cup)
4. {campeon_comunity} (Community Shield)
5. {campeon_serieA} (Serie A)
6. {campeon_serieB} (Serie B)
7. {campeon_copa_italiaa} (Copa italia)
8. {campeon_recopa_italia} (Recopa Italiana)
9. {campeon_champions} (Champions League)
10. {campeon_europa} (Europa League)
11. {ganador_recopa} (Recopa De Europa)
''')
    
    if ganador_recopa == player["equipo"]:
        player["valoracion"] += 2
        trofeo = f"Recopa De Europa ({ganador_recopa})"
        player["dinero"] += 250000
        vitrina.append(trofeo)
    if campeon_europa == player["equipo"]:
        player["valoracion"] += 8
        trofeo = f"Europa League ({campeon_europa})"
        player["dinero"] += 1000000
        vitrina.append(trofeo)
    if campeon_champions == player["equipo"]:
        player["valoracion"] += 10
        trofeo = f"Champions League ({campeon_champions})"
        player["dinero"] += 2000000
        vitrina.append(trofeo)
    if campeon_premier == player["equipo"]:
        player["valoracion"] += 11
        trofeo = f"Premier League ({campeon_premier})"
        player["dinero"] += 1500000
        vitrina.append(trofeo)
    if campeon_championship == player["equipo"]:
        player["valoracion"] += 3  
        trofeo = f"Sky By Championship ({campeon_championship})"
        player["dinero"] += 1000000
        vitrina.append(trofeo)
    if campeon_carabaoo == player["equipo"]:
        player["valoracion"] += 4
        trofeo = f"Carabao Cup ({campeon_carabaoo})"
        player["dinero"] += 500000
        vitrina.append(trofeo)
    if campeon_comunity == player["equipo"]:
        player["valoracion"] += 2   
        trofeo = f"Community Shield ({campeon_comunity})"
        player["dinero"] += 250000
        vitrina.append(trofeo)
    if campeon_serieA == player["equipo"]:
        player["valoracion"] += 11
        trofeo = f"Serie A ({campeon_serieA})"
        player["dinero"] += 1500000
        vitrina.append(trofeo)
    if campeon_serieB == player["equipo"]:
        player["valoracion"] += 3  
        trofeo = f"Serie B ({campeon_serieB})"
        player["dinero"] += 1000000
        vitrina.append(trofeo)
    if campeon_copa_italiaa == player["equipo"]:
        player["valoracion"] += 4
        trofeo = f"Copa Italia ({campeon_copa_italiaa})"
        player["dinero"] += 500000
        vitrina.append(trofeo)
    if campeon_recopa_italia == player["equipo"]:
        player["valoracion"] += 2   
        trofeo = f"Recopa Italiana ({campeon_recopa_italia})"
        player["dinero"] += 250000
        vitrina.append(trofeo)
    logros = mostrar_goleadores_asistentes()
    if contador in [1,3,5,7,9,11,13,15,17,19]:
        definir_datos_fin("e",1)
        definir_datos_fin("a",1)
        definir_datos_fin("f",1)
        definir_datos_fin("s",1)
    if contador in [2,6,10,14,18]:
        definir_datos_fin("e",2)
        definir_datos_fin("a",2)
        definir_datos_fin("f",2)
        definir_datos_fin("s",2)
    if contador in [4,8,12,16,20]:
        mostrar_datos_mundiales_fin()
    if len(logros) != 0:
        for i in logros:
            logros_anuales.append(i)
    print("")
    mvp_del_añooo = mvp_del_año()
    if len(mvp_del_añooo) != 0:
        for i in mvp_del_añooo:
            logros_anuales.append(i)
    campeones_premier.append(campeon_premier)
    campeones_championship.append(campeon_championship)
    campeones_carabao.append(campeon_carabaoo)
    campeones_comunity.append(campeon_comunity)
    campeones_champions.append(campeon_champions)
    campeones_europa.append(campeon_europa)
    campeones_recopa.append(ganador_recopa)
    campeones_serieA.append(campeon_serieA)
    campeones_serieB.append(campeon_serieB)
    campeones_copa_italia.append(campeon_copa_italiaa)
    campeones_recopa_italia.append(campeon_recopa_italia)
    mostrar_campeones_totales()
    actualizar_ranking_mostrar()
    guardar_datos_anuales(vitrina,logros_anuales)
    mostrar_datos_anuales()
    if player["valoracion"] > 100:
        player["valoracion"] = 100
    if player["contrato"] != 0:
        cancelacion_contrato = input("deseas cancelar el contrato con tu club (1 = si)")
        if cancelacion_contrato == "1":
            player["contrato"] = 0
            player["valoracion"] -= 10
    equipo_playerr = equipo_player
    if player["contrato"] == 0:
        equipo_playerr = cambiar_equipo()
        equipo_player = equipo_playerr
    else: 
        print(f"te quedan {player['contrato']} años de contrato")
        traspaso = ""
        traspasos.append(traspaso)
    for jugador in jugadores:
        if jugador["nombre"] == nombre_del_jugador:
            jugador["partidos"] = 0
            jugador["equipo"] = equipo_player
    sky_by_championship_equipos,premier_league_equipos = divisionacomodar(tabla_premier,tabla_championship)
    serieA_equipos,serieB_equipos = divisionacomodar_i(tabla_serieA,tabla_serieB)
    resetear_tabla() 
    edad += 1
    contador += 1
    if edad < 25: player["valoracion"] += 3
    elif edad > 30:player["valoracion"] -= 3
    print(f'tu valoracion es: {player["valoracion"]}')
ruta_archivo = r'C:\Users\Uusario\Documents\portal\primer sitio web\proyectos\python_proyrctos\partidos\modo_carrera\datos_player.txt'
fct.agregar_dato(ruta_archivo,player)