import random
from tabulate import tabulate
import arch as taq
import json


def agregar_dato(ruta_archivo,contenido):
    with open(ruta_archivo, "w") as archivo:
        json.dump(contenido, archivo)

def obtener_primer_y_segundo_equipo(equipos):
    equipos_ordenados = sorted(equipos, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    
    if len(equipos_ordenados) >= 2:
        primer_equipo = list(equipos_ordenados[0].keys())[0]
        segundo_equipo = list(equipos_ordenados[1].keys())[0]
        return primer_equipo, segundo_equipo
    
    return None, None

def actualizar_tablaaa_copas(equiposs):
    equipos_ordenados = sorted(equiposs, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    return equipos_ordenados
def mostrar_tabla_copas(equipos_ordenados):
    tabla = []
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        puntos = equipo[nombre_equipo]['PTS']
        goles = equipo[nombre_equipo]['GF']
        vic = equipo[nombre_equipo]['V']
        emp = equipo[nombre_equipo]['E']
        der = equipo[nombre_equipo]['D']
        diferencia_goles = equipo[nombre_equipo]['GD']
        golesencontra = equipo[nombre_equipo]['GC']
        tabla.append([i, nombre_equipo, puntos,vic,emp,der, goles,golesencontra, diferencia_goles])

    headers = ["POS", "EQUIPO", "PTS","V","E","D" ,"GF","GC", "GD"]
    print(tabulate(tabla, headers=headers, tablefmt="pretty"))

def mostrar_tablas_fecha_fin(tabla1,tabla2,tabla3,tabla4):
    print("")
    input("mostrar tablas")
    print("")
    print("tabla grupo 1")
    equipos_ordenados = actualizar_tablaaa_copas(tabla1)
    mostrar_tabla_copas(equipos_ordenados)
    input("")
    print("tabla grupo 2")
    equipos_ordenados = actualizar_tablaaa_copas(tabla2)
    mostrar_tabla_copas(equipos_ordenados)
    input("")
    print("tabla grupo 3")
    equipos_ordenados = actualizar_tablaaa_copas(tabla3)
    mostrar_tabla_copas(equipos_ordenados)
    input("")
    print("tabla grupo 4")
    equipos_ordenados = actualizar_tablaaa_copas(tabla4)
    mostrar_tabla_copas(equipos_ordenados)
    input("")

def mostrar_tablas_fecha_fin_(tabla1,tabla2):
    print("")
    input("mostrar tablas")
    print("")
    print("tabla grupo 1")
    equipos_ordenados = actualizar_tablaaa_copas(tabla1)
    mostrar_tabla_copas(equipos_ordenados)
    input("")
    print("tabla grupo 2")
    equipos_ordenados = actualizar_tablaaa_copas(tabla2)
    mostrar_tabla_copas(equipos_ordenados)
    input("")

def resultado(club1,club2):
    e1 = "Arsenal"
    reputatione1 = 5
    e2 = "Aston Villa"
    reputatione2 = 3
    e3 = "Bournemouth"
    reputatione3 = 1
    e4 = "Brentford"
    reputatione4 = 3
    e5 = "Brigthon"
    reputatione5 = 4
    e6 = "Chelsea"
    reputatione6 = 5
    e7 = "Crystal Palace"
    reputatione7 = 3
    e8 = "Everton"
    reputatione8 = 2
    e9 = "Fulham"
    reputatione9 = 3
    e10 = "Leeds United"
    reputatione10 = 2
    e11 = "Leicester City"
    reputatione11 = 2
    e12 = "Liverpool"
    reputatione12 = 5
    e13 = "Manchester City"
    reputatione13 = 5
    e14 = "Manchester United"
    reputatione14 = 5
    e15 = "Newcastle"
    reputatione15 = 4
    e16 = "Nottingham Forest"
    reputatione16 = 2
    e17 = "Southampton"
    reputatione17 = 2
    e18 = "Tottenham"
    reputatione18 = 5
    e19 = "West ham"
    reputatione19 = 2
    e20 = "Wolverhampton"
    reputatione20 = 2
    e21 = "Burnley"
    reputatione21 = 2
    e22 = "Sheffield United"
    reputatione22 = 2
    e23 = "Luton Town"
    reputatione23 = 1
    e24 = "Middlesbrough"
    reputatione24 = 2
    e25 = "Coventry City"
    reputatione25 = 1
    e26 = "Sunderland"
    reputatione26 = 2
    e27 = "Blackburn Rovers"
    reputatione27 = 1
    e28 = "Millwall"
    reputatione28 = 1
    e29 = "West Bromwich Albion"
    reputatione29 = 1
    e30 = "Swansea"
    reputatione30 = 3
    e31 = "Watford"
    reputatione31 = 3
    e32 = "Preston North End"
    reputatione32 = 1
    e33 = "Norwich"
    reputatione33 = 3
    e34 = "Bristol City"
    reputatione34 = 1
    e35 = "Hull City"
    reputatione35 = 2
    e36 = "Stoke City"
    reputatione36 = 3
    e37 = "Birmingham"
    reputatione37 = 2
    e38 = "Huddersfield Town"
    reputatione38 = 2
    e39 = "Cardiff City"
    reputatione39 = 2
    e40 = "Queens Park Rangers"
    reputatione40 = 2
    e41 = "PSG"
    reputatione41 = 5
    e42 = "O.Lyon"
    reputatione42 = 3
    e43 = "Inter"
    reputatione43 = 5
    e44 = "Juventus"
    reputatione44 = 5
    e45 = "Milan"
    reputatione45 = 5
    e46 = "Napoli"
    reputatione46 = 5
    e47 = "Roma"
    reputatione47 = 5
    e48 = "Atl.Madrid"
    reputatione48 = 4
    e49 = "Barcelona"
    reputatione49 = 5
    e50 = "Real Madrid"
    reputatione50 = 5
    e51 = "B.Dortmund"
    reputatione51 = 5
    e52 = "Bayern Munich"
    reputatione52 = 5
    e53 = "B.Leverkusen"
    reputatione53 = 3
    e54 = "Porto"
    reputatione54 = 3
    e55 = "Sporting Lisboa"
    reputatione55 = 3
    e56 = "Frankfurt"
    reputatione56 = 3
    e57 = "O.Marsella"
    reputatione57 = 3
    e58 = "Sevilla"
    reputatione58 = 3
    e59 = "Benfica"
    reputatione59 = 3
    e60 = "Leipzig"
    reputatione60 = 3
    e61 = "Ajax"
    reputatione61 = 3
    e62 = "Monaco"
    reputatione62 = 3
    e63 = "Shakhtar"
    reputatione63 = 2
    e64 = "Brugge"
    reputatione64 = 2
    e65 = "PSV"
    reputatione65 = 2
    e66 = "Real Sociedad"
    reputatione66 = 2
    
    e67 = "Lazio"
    reputatione67 = 4
    e68 = "Atalanta"
    reputatione68 = 4
    e69 = "Fiorentina"
    reputatione69 = 4
    e70 = "Bologna"
    reputatione70 = 3
    e71 = "Torino"
    reputatione71 = 3
    e72 = "Monza"
    reputatione72 = 2
    e73 = "Udinese"
    reputatione73 = 3
    e74 = "Sassuolo"
    reputatione74 = 3
    e75 = "Empoli"
    reputatione75 = 2
    e76 = "Salernitana"
    reputatione76 = 2
    e77 = "Lecce"
    reputatione77 = 2
    e78 = "Hellas Verona"
    reputatione78 = 2
    e79 = "Spezia"
    reputatione79 = 2
    e80 = "Cremonese"
    reputatione80 = 1
    e81 = "Sampdoria"
    reputatione81 = 3
    e82 = "Frosinone"
    reputatione82 = 2
    e83 = "Genoa"
    reputatione83 = 3
    e84 = "Bari"
    reputatione84 = 2
    e85 = "Parma"
    reputatione85 = 3
    e86 = "Cagliari"
    reputatione86 = 3
    e87 = "Sudtirol"
    reputatione87 = 1
    e88 = "Reggina"
    reputatione88 = 1
    e89 = "Venezia"
    reputatione89 = 1
    e90 = "Palermo"
    reputatione90 = 2
    e91 = "Modena"
    reputatione91 = 1
    e92 = "Pisa"
    reputatione92 = 1
    e93 = "Ascoli"
    reputatione93 = 1
    e94 = "Como"
    reputatione94 = 1
    e95 = "Ternana"
    reputatione95 = 1
    e96 = "Brescia"
    reputatione96 = 2
    e97 = "Cittadella"
    reputatione97 = 2
    e98 = "Cosenza"
    reputatione98 = 1
    e99 = "Perugia"
    reputatione99 = 1
    e100 = "Spal"
    reputatione100 = 2
    e101 = "Benevento"
    reputatione101 = 2
    if club1 == "Arsenal":
        clublocal = e1
        reputationlocal = reputatione1
    elif club1 == "Aston Villa":
        clublocal = e2
        reputationlocal = reputatione2
    elif club1 == "Bournemouth":
        clublocal = e3
        reputationlocal = reputatione3
    elif club1 == "Brentford":
        clublocal = e4
        reputationlocal = reputatione4
    elif club1 == "Brigthon":
        clublocal = e5
        reputationlocal = reputatione5
    elif club1 == "Chelsea":
        clublocal = e6
        reputationlocal = reputatione6
    elif club1 == "Crystal Palace":
        clublocal = e7        
        reputationlocal = reputatione7
    elif club1 == "Everton":
        clublocal = e8
        reputationlocal = reputatione8
    elif club1 == "Fulham":
        clublocal = e9
        reputationlocal = reputatione9
    elif club1 == "Leeds United":
        clublocal = e10
        reputationlocal = reputatione10
    elif club1 == "Leicester City":
        clublocal = e11
        reputationlocal = reputatione11
    elif club1 == "Liverpool":
        clublocal = e12
        reputationlocal = reputatione12
    elif club1 == "Manchester City":
        clublocal = e13
        reputationlocal = reputatione13
    elif club1 == "Manchester United":
        clublocal = e14
        reputationlocal = reputatione14
    elif club1 == "Newcastle":
        clublocal = e15
        reputationlocal = reputatione15
    elif club1 == "Nottingham Forest":
        clublocal = e16
        reputationlocal = reputatione16
    elif club1 == "Southampton":
        clublocal = e17
        reputationlocal = reputatione17
    elif club1 == "Tottenham":
        clublocal = e18
        reputationlocal = reputatione18
    elif club1 == "West ham":
        clublocal = e19
        reputationlocal = reputatione19
    elif club1 == "Wolverhampton":
        clublocal = e20
        reputationlocal = reputatione20
    elif club1 == "Burnley":
        clublocal = e21
        reputationlocal = reputatione21    
    elif club1 == "Sheffield United":
        clublocal = e22
        reputationlocal = reputatione22
    elif club1 == "Luton Town":
        clublocal = e23
        reputationlocal = reputatione23
    elif club1 == "Middlesbrough":
        clublocal = e24
        reputationlocal = reputatione24            
    elif club1 == "Coventry City":
        clublocal = e25
        reputationlocal = reputatione25    
    elif club1 == "Sunderland":
        clublocal = e26
        reputationlocal = reputatione26
    elif club1 == "Blackburn Rovers":
        clublocal = e27
        reputationlocal = reputatione27
    elif club1 == "Millwall":
        clublocal = e28
        reputationlocal = reputatione28    
    elif club1 == "West Bromwich Albion":
        clublocal = e29
        reputationlocal = reputatione29
    elif club1 == "Swansea":
        clublocal = e30
        reputationlocal = reputatione30
    elif club1 == "Watford":
        clublocal = e31
        reputationlocal = reputatione31            
    elif club1 == "Preston North End":
        clublocal = e32
        reputationlocal = reputatione32    
    elif club1 == "Norwich":
        clublocal = e33
        reputationlocal = reputatione33
    elif club1 == "Bristol City":
        clublocal = e34
        reputationlocal = reputatione34
    elif club1 == "Hull City":
        clublocal = e35
        reputationlocal = reputatione35    
    elif club1 == "Stoke City":
        clublocal = e36
        reputationlocal = reputatione36
    elif club1 == "Birmingham":
        clublocal = e37
        reputationlocal = reputatione37
    elif club1 == "Huddersfield Town":
        clublocal = e38
        reputationlocal = reputatione38            
    elif club1 == "Cardiff City":
        clublocal = e39
        reputationlocal = reputatione39    
    elif club1 == "Queens Park Rangers":
        clublocal = e40
        reputationlocal = reputatione40    
    elif club1 == "PSG":
        clublocal = e41
        reputationlocal = reputatione41
    elif club1 == "O.Lyon":
        clublocal = e42
        reputationlocal = reputatione42
    elif club1 == "Inter":
        clublocal = e43
        reputationlocal = reputatione43
    elif club1 == "Juventus":
        clublocal = e44
        reputationlocal = reputatione44
    elif club1 == "Milan":
        clublocal = e45
        reputationlocal = reputatione45
    elif club1 == "Napoli":
        clublocal = e46
        reputationlocal = reputatione46
    elif club1 == "Roma":
        clublocal = e47
        reputationlocal = reputatione47
    elif club1 == "Atl.Madrid":
        clublocal = e48
        reputationlocal = reputatione48
    elif club1 == "Barcelona":
        clublocal = e49
        reputationlocal = reputatione49
    elif club1 == "Real Madrid":
        clublocal = e50
        reputationlocal = reputatione50
    elif club1 == "B.Dortmund":
        clublocal = e51
        reputationlocal = reputatione51
    elif club1 == "Bayern Munich":
        clublocal = e52
        reputationlocal = reputatione52
    elif club1 == "B.Leverkusen":
        clublocal = e53
        reputationlocal = reputatione53
    elif club1 == "Porto":
        clublocal = e54
        reputationlocal = reputatione54
    elif club1 == "Sporting Lisboa":
        clublocal = e55
        reputationlocal = reputatione55
    elif club1 == "Frankfurt":
        clublocal = e56
        reputationlocal = reputatione56        
    elif club1 == "O.Marsella":
        clublocal = e57
        reputationlocal = reputatione57
    elif club1 == "Sevilla":
        clublocal = e58
        reputationlocal = reputatione58    
    elif club1 == "Benfica":
        clublocal = e59
        reputationlocal = reputatione59
    elif club1 == "Leipzig":
        clublocal = e60
        reputationlocal = reputatione60
    elif club1 == "Ajax":
        clublocal = e61
        reputationlocal = reputatione61        
    elif club1 == "Monaco":
        clublocal = e62
        reputationlocal = reputatione62
    elif club1 == "Shakhtar":
        clublocal = e63
        reputationlocal = reputatione63  
    elif club1 == "Brugge":
        clublocal = e64
        reputationlocal = reputatione64
    elif club1 == "PSV":
        clublocal = e65
        reputationlocal = reputatione65        
    elif club1 == "Real Sociedad":
        clublocal = e66
        reputationlocal = reputatione66
    elif club1 == "Lazio":
        clublocal = e67
        reputationlocal = reputatione67        
    elif club1 == "Atalanta":
        clublocal = e68
        reputationlocal = reputatione68
    elif club1 == "Fiorentina":
        clublocal = e69
        reputationlocal = reputatione69    
    elif club1 == "Bologna":
        clublocal = e70
        reputationlocal = reputatione70
    elif club1 == "Torino":
        clublocal = e71
        reputationlocal = reputatione71
    elif club1 == "Monza":
        clublocal = e72
        reputationlocal = reputatione72        
    elif club1 == "Udinese":
        clublocal = e73
        reputationlocal = reputatione73
    elif club1 == "Sassuolo":
        clublocal = e74
        reputationlocal = reputatione74  
    elif club1 == "Empoli":
        clublocal = e75
        reputationlocal = reputatione75
    elif club1 == "Salernitana":
        clublocal = e76
        reputationlocal = reputatione76    
    elif club1 == "Lecce":
        clublocal = e77
        reputationlocal = reputatione77        
    elif club1 == "Hellas Verona":
        clublocal = e78
        reputationlocal = reputatione78
    elif club1 == "Spezia":
        clublocal = e79
        reputationlocal = reputatione79    
    elif club1 == "Cremonese":
        clublocal = e80
        reputationlocal = reputatione80
    elif club1 == "Sampdoria":
        clublocal = e81
        reputationlocal = reputatione81
    elif club1 == "Frosinone":
        clublocal = e82
        reputationlocal = reputatione82        
    elif club1 == "Genoa":
        clublocal = e83
        reputationlocal = reputatione83
    elif club1 == "Bari":
        clublocal = e84
        reputationlocal = reputatione84  
    elif club1 == "Parma":
        clublocal = e85
        reputationlocal = reputatione85
    elif club1 == "Cagliari":
        clublocal = e86
        reputationlocal = reputatione86 
    elif club1 == "Sudtirol":
        clublocal = e87
        reputationlocal = reputatione87        
    elif club1 == "Reggina":
        clublocal = e88
        reputationlocal = reputatione88
    elif club1 == "Venezia":
        clublocal = e89
        reputationlocal = reputatione89    
    elif club1 == "Palermo":
        clublocal = e90
        reputationlocal = reputatione90
    elif club1 == "Modena":
        clublocal = e91
        reputationlocal = reputatione91
    elif club1 == "Pisa":
        clublocal = e92
        reputationlocal = reputatione92        
    elif club1 == "Ascoli":
        clublocal = e93
        reputationlocal = reputatione93
    elif club1 == "Como":
        clublocal = e94
        reputationlocal = reputatione94  
    elif club1 == "Ternana":
        clublocal = e95
        reputationlocal = reputatione95
    elif club1 == "Brescia":
        clublocal = e96
        reputationlocal = reputatione96 
    elif club1 == "Cittadella":
        clublocal = e97
        reputationlocal = reputatione97
    elif club1 == "Cosenza":
        clublocal = e98
        reputationlocal = reputatione98  
    elif club1 == "Perugia":
        clublocal = e99
        reputationlocal = reputatione99
    elif club1 == "Spal":
        clublocal = e100
        reputationlocal = reputatione100
    elif club1 == "Benevento":
        clublocal = e101
        reputationlocal = reputatione101
    else:
        print("sos medio dislexico papito no?")
        
    if club2 == "Arsenal":
        clubvisitor = e1
        reputationvisitor = reputatione1
    elif club2 == "Aston Villa":
        clubvisitor = e2
        reputationvisitor = reputatione2
    elif club2 == "Bournemouth":
        clubvisitor = e3
        reputationvisitor = reputatione3
    elif club2 == "Brentford":
        clubvisitor = e4
        reputationvisitor = reputatione4
    elif club2 == "Brigthon":
        clubvisitor = e5
        reputationvisitor = reputatione5
    elif club2 == "Chelsea":
        clubvisitor = e6
        reputationvisitor = reputatione6
    elif club2 == "Crystal Palace":
        clubvisitor = e7        
        reputationvisitor = reputatione7
    elif club2 == "Everton":
        clubvisitor = e8
        reputationvisitor = reputatione8
    elif club2 == "Fulham":
        clubvisitor = e9
        reputationvisitor = reputatione9
    elif club2 == "Leeds United":
        clubvisitor = e10
        reputationvisitor = reputatione10
    elif club2 == "Leicester City":
        clubvisitor = e11
        reputationvisitor = reputatione11
    elif club2 == "Liverpool":
        clubvisitor = e12
        reputationvisitor = reputatione12
    elif club2 == "Manchester City":
        clubvisitor = e13
        reputationvisitor = reputatione13
    elif club2 == "Manchester United":
        clubvisitor = e14
        reputationvisitor = reputatione14
    elif club2 == "Newcastle":
        clubvisitor = e15
        reputationvisitor = reputatione15
    elif club2 == "Nottingham Forest":
        clubvisitor = e16
        reputationvisitor = reputatione16
    elif club2 == "Southampton":
        clubvisitor = e17
        reputationvisitor = reputatione17
    elif club2 == "Tottenham":
        clubvisitor = e18
        reputationvisitor = reputatione18
    elif club2 == "West ham":
        clubvisitor = e19
        reputationvisitor = reputatione19
    elif club2 == "Wolverhampton":
        clubvisitor = e20
        reputationvisitor = reputatione20
    elif club2 == "Burnley":
        clubvisitor = e21
        reputationvisitor = reputatione21    
    elif club2 == "Sheffield United":
        clubvisitor = e22
        reputationvisitor = reputatione22
    elif club2 == "Luton Town":
        clubvisitor = e23
        reputationvisitor = reputatione23
    elif club2 == "Middlesbrough":
        clubvisitor = e24
        reputationvisitor = reputatione24            
    elif club2 == "Coventry City":
        clubvisitor = e25
        reputationvisitor = reputatione25    
    elif club2 == "Sunderland":
        clubvisitor = e26
        reputationvisitor = reputatione26
    elif club2 == "Blackburn Rovers":
        clubvisitor = e27
        reputationvisitor = reputatione27
    elif club2 == "Millwall":
        clubvisitor = e28
        reputationvisitor = reputatione28    
    elif club2 == "West Bromwich Albion":
        clubvisitor = e29
        reputationvisitor = reputatione29
    elif club2 == "Swansea":
        clubvisitor = e30
        reputationvisitor = reputatione30
    elif club2 == "Watford":
        clubvisitor = e31
        reputationvisitor = reputatione31            
    elif club2 == "Preston North End":
        clubvisitor = e32
        reputationvisitor = reputatione32    
    elif club2 == "Norwich":
        clubvisitor = e33
        reputationvisitor = reputatione33
    elif club2 == "Bristol City":
        clubvisitor = e34
        reputationvisitor = reputatione34
    elif club2 == "Hull City":
        clubvisitor = e35
        reputationvisitor = reputatione35    
    elif club2 == "Stoke City":
        clubvisitor = e36
        reputationvisitor = reputatione36
    elif club2 == "Birmingham":
        clubvisitor = e37
        reputationvisitor = reputatione37
    elif club2 == "Huddersfield Town":
        clubvisitor = e38
        reputationvisitor = reputatione38            
    elif club2 == "Cardiff City":
        clubvisitor = e39
        reputationvisitor = reputatione39    
    elif club2 == "Queens Park Rangers":
        clubvisitor = e40
        reputationvisitor = reputatione40    
    elif club2 == "PSG":
        clubvisitor = e41        
        reputationvisitor = reputatione41
    elif club2 == "O.Lyon":
        clubvisitor = e42
        reputationvisitor = reputatione42
    elif club2 == "Inter":
        clubvisitor = e43
        reputationvisitor = reputatione43
    elif club2 == "Juventus":
        clubvisitor = e44
        reputationvisitor = reputatione44
    elif club2 == "Milan":
        clubvisitor = e45
        reputationvisitor = reputatione45
    elif club2 == "Napoli":
        clubvisitor = e46
        reputationvisitor = reputatione46
    elif club2 == "Roma":
        clubvisitor = e47
        reputationvisitor = reputatione47
    elif club2 == "Atl.Madrid":
        clubvisitor = e48
        reputationvisitor = reputatione48
    elif club2 == "Barcelona":
        clubvisitor = e49
        reputationvisitor = reputatione49
    elif club2 == "Real Madrid":
        clubvisitor = e50
        reputationvisitor = reputatione50
    elif club2 == "B.Dortmund":
        clubvisitor = e51
        reputationvisitor = reputatione51
    elif club2 == "Bayern Munich":
        clubvisitor = e52
        reputationvisitor = reputatione52
    elif club2 == "B.Leverkusen":
        clubvisitor = e53
        reputationvisitor = reputatione53
    elif club2 == "Porto":
        clubvisitor = e54
        reputationvisitor = reputatione54
    elif club2 == "Sporting Lisboa":
        clubvisitor = e55
        reputationvisitor = reputatione55
    elif club2 == "Frankfurt":
        clubvisitor = e56
        reputationvisitor = reputatione56        
    elif club2 == "O.Marsella":
        clubvisitor = e57
        reputationvisitor = reputatione57
    elif club2 == "Sevilla":
        clubvisitor = e58
        reputationvisitor = reputatione58    
    elif club2 == "Benfica":
        clubvisitor = e59
        reputationvisitor = reputatione59
    elif club2 == "Leipzig":
        clubvisitor = e60
        reputationvisitor = reputatione60
    elif club2 == "Ajax":
        clubvisitor = e61
        reputationvisitor = reputatione61        
    elif club2 == "Monaco":
        clubvisitor = e62
        reputationvisitor = reputatione62
    elif club2 == "Shakhtar":
        clubvisitor = e63
        reputationvisitor = reputatione63  
    elif club2 == "Brugge":
        clubvisitor = e64
        reputationvisitor = reputatione64
    elif club2 == "PSV":
        clubvisitor = e65
        reputationvisitor = reputatione65        
    elif club2 == "Real Sociedad":
        clubvisitor = e66
        reputationvisitor = reputatione66  
        
    elif club2 == "Lazio":
        clubvisitor = e67
        reputationvisitor = reputatione67  
    elif club2 == "Atalanta":
        clubvisitor = e68
        reputationvisitor = reputatione68  
    elif club2 == "Fiorentina":
        clubvisitor = e69
        reputationvisitor = reputatione69 
    elif club2 == "Bologna":
        clubvisitor = e70
        reputationvisitor = reputatione70  
    elif club2 == "Torino":
        clubvisitor = e71
        reputationvisitor = reputatione71
    elif club2 == "Monza":
        clubvisitor = e72
        reputationvisitor = reputatione72  
    elif club2 == "Udinese":
        clubvisitor = e73
        reputationvisitor = reputatione73
    elif club2 == "Sassuolo":
        clubvisitor = e74
        reputationvisitor = reputatione74  
    elif club2 == "Empoli":
        clubvisitor = e75
        reputationvisitor = reputatione75
    elif club2 == "Salernitana":
        clubvisitor = e76
        reputationvisitor = reputatione76  
    elif club2 == "Lecce":
        clubvisitor = e77
        reputationvisitor = reputatione77
    elif club2 == "Hellas Verona":
        clubvisitor = e78
        reputationvisitor = reputatione78  
    elif club2 == "Spezia":
        clubvisitor = e79
        reputationvisitor = reputatione79
    elif club2 == "Cremonese":
        clubvisitor = e80
        reputationvisitor = reputatione80  
    elif club2 == "Sampdoria":
        clubvisitor = e81
        reputationvisitor = reputatione81
    elif club2 == "Frosinone":
        clubvisitor = e82
        reputationvisitor = reputatione82  
    elif club2 == "Genoa":
        clubvisitor = e83
        reputationvisitor = reputatione83
    elif club2 == "Bari":
        clubvisitor = e84
        reputationvisitor = reputatione84  
    elif club2 == "Parma":
        clubvisitor = e85
        reputationvisitor = reputatione85
    elif club2 == "Cagliari":
        clubvisitor = e86
        reputationvisitor = reputatione86  
    elif club2 == "Sudtirol":
        clubvisitor = e87
        reputationvisitor = reputatione87
    elif club2 == "Reggina":
        clubvisitor = e88
        reputationvisitor = reputatione88  
    elif club2 == "Venezia":
        clubvisitor = e89
        reputationvisitor = reputatione89
    elif club2 == "Palermo":
        clubvisitor = e90
        reputationvisitor = reputatione90
    elif club2 == "Modena":
        clubvisitor = e91
        reputationvisitor = reputatione91
    elif club2 == "Pisa":
        clubvisitor = e92
        reputationvisitor = reputatione92
    elif club2 == "Ascoli":
        clubvisitor = e93
        reputationvisitor = reputatione93
    elif club2 == "Como":
        clubvisitor = e94
        reputationvisitor = reputatione94
    elif club2 == "Ternana":
        clubvisitor = e95
        reputationvisitor = reputatione95
    elif club2 == "Brescia":
        clubvisitor = e96
        reputationvisitor = reputatione96
    elif club2 == "Cittadella":
        clubvisitor = e97
        reputationvisitor = reputatione97
    elif club2 == "Cosenza":
        clubvisitor = e98
        reputationvisitor = reputatione98
    elif club2 == "Perugia":
        clubvisitor = e99
        reputationvisitor = reputatione99
    elif club2 == "Spal":
        clubvisitor = e100
        reputationvisitor = reputatione100
    elif club2 == "Benevento":
        clubvisitor = e101
        reputationvisitor = reputatione101
    else:
        print("sos medio dislexico papito no?")
        
    reputation = (reputationlocal - reputationvisitor)    
    if reputation == 0:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.39, 0.30, 0.19, 0.1, 0.02, 0, 0]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.39, 0.30, 0.19, 0.1, 0.02, 0, 0]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == 1:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.30, 0.32, 0.18, 0.1, 0.05, 0.03, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.36, 0.34, 0.15, 0.1, 0.03, 0.02, 0]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == 2:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.25, 0.32, 0.21, 0.12, 0.05, 0.03, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.41, 0.35, 0.12, 0.1, 0.02, 0, 0]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == 3:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.20, 0.25, 0.25, 0.15, 0.08, 0.05, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.45, 0.40, 0.1, 0.05, 0, 0, 0]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == 4:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.1, 0.20, 0.30, 0.20, 0.12, 0.06, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.6, 0.30, 0.11, 0, 0, 0, 0]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == -1:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.36, 0.34, 0.15, 0.1, 0.03, 0.02, 0]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.30, 0.32, 0.18, 0.1, 0.05, 0.03, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0] 
    elif reputation == -2:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.41, 0.35, 0.12, 0.1, 0.02, 0, 0]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.25, 0.32, 0.21, 0.12, 0.05, 0.03, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0] 
    elif reputation == -3 :    
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.20, 0.25, 0.25, 0.15, 0.08, 0.05, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.45, 0.40, 0.1, 0.05, 0, 0, 0]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == -4:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.1, 0.20, 0.30, 0.20, 0.12, 0.06, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.6, 0.30, 0.11, 0, 0, 0, 0]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        
    result = print(f'{club1} {goallocal}-{goalsvisitor} {club2}') 
    return result,club1,goallocal,goalsvisitor,club2

def resultado_selecciones(club1,club2):
    e1 = "España"
    reputatione1 = 5
    e2 = "Francia"
    reputatione2 = 5
    e3 = "Holanda"
    reputatione3 = 4
    e4 = "Inglaterra"
    reputatione4 = 5
    e5 = "Italia"
    reputatione5 = 5
    e6 = "Croacia"
    reputatione6 = 4
    e7 = "Belgica"
    reputatione7 = 3
    e8 = "Portugal"
    reputatione8 = 4
    e9 = "Suiza"
    reputatione9 = 2
    e10 = "Dinamarca"
    reputatione10 = 3
    e11 = "Polonia"
    reputatione11 = 2
    e12 = "Noruega"
    reputatione12 = 2
    e13 = "Alemania" 
    reputatione13 = 5
    e14 = "Gales"
    reputatione14 = 1
    e15 = "Serbia"
    reputatione15 = 1
    e16 = "Suecia"
    reputatione16 = 1
     
    e17 = "Argentina"
    reputatione17 = 5
    e18 = "Uruguay"
    reputatione18 = 4
    e19 = "Paraguay"
    reputatione19 = 2
    e20 = "Chile"
    reputatione20 = 3
    e21 = "Bolivia"
    reputatione21 = 1
    e22 = "Brasil"
    reputatione22 = 5
    e23 = "Peru"
    reputatione23 = 3
    e24 = "Colombia"
    reputatione24 = 4
    e25 = "Ecuador"
    reputatione25 = 3
    e26 = "Venezuela"
    reputatione26 = 2
    e27 = "Mexico"
    reputatione27 = 3
    e28 = "Estados Unidos"
    reputatione28 = 3
    e29 = "Canada"
    reputatione29 = 2
    e30 = "Costa Rica"
    reputatione30 = 1
    e31 = "Cuba"
    reputatione31 = 1
    e32 = "Honduras"
    reputatione32 = 1
    
    e33 = "Egipto"
    reputatione33 = 3
    e34 = "Senegal"
    reputatione34 = 3
    e35 = "Tunez"
    reputatione35 = 2
    e36 = "Camerun"
    reputatione36 = 2
    e37 = "Marruecos"
    reputatione37 = 3
    e38 = "Nigeria"
    reputatione38 = 2
    e39 = "Ghana"
    reputatione39 = 1
    e40 = "Argelia"
    reputatione40 = 1
    
    e41 = "Iran"
    reputatione41 = 2
    e42 = "Corea del Sur"
    reputatione42 = 3
    e43 = "Japon"
    reputatione43 = 3
    e44 = "China"
    reputatione44 = 1
    e45 = "Arabia Saudita"
    reputatione45 = 2
    e46 = "Israel"
    reputatione46 = 1
    e47 = "Australia"
    reputatione47 = 3
    e48 = "Qatar"
    reputatione48 = 2
    if club1 == "España":
        clublocal = e1
        reputationlocal = reputatione1
    elif club1 == "Francia":
        clublocal = e2
        reputationlocal = reputatione2
    elif club1 == "Holanda":
        clublocal = e3
        reputationlocal = reputatione3
    elif club1 == "Inglaterra":
        clublocal = e4
        reputationlocal = reputatione4
    elif club1 == "Italia":
        clublocal = e5
        reputationlocal = reputatione5
    elif club1 == "Croacia":
        clublocal = e6
        reputationlocal = reputatione6
    elif club1 == "Belgica":
        clublocal = e7        
        reputationlocal = reputatione7
    elif club1 == "Portugal":
        clublocal = e8
        reputationlocal = reputatione8
    elif club1 == "Suiza":
        clublocal = e9
        reputationlocal = reputatione9
    elif club1 == "Dinamarca":
        clublocal = e10
        reputationlocal = reputatione10
    elif club1 == "Polonia":
        clublocal = e11
        reputationlocal = reputatione11
    elif club1 == "Noruega":
        clublocal = e12
        reputationlocal = reputatione12
    elif club1 == "Alemania":
        clublocal = e13
        reputationlocal = reputatione13
    elif club1 == "Gales":
        clublocal = e14
        reputationlocal = reputatione14
    elif club1 == "Serbia":
        clublocal = e15
        reputationlocal = reputatione15
    elif club1 == "Suecia":
        clublocal = e16
        reputationlocal = reputatione16        
    elif club1 == "Argentina":
        clublocal = e17
        reputationlocal = reputatione17
    elif club1 == "Uruguay":
        clublocal = e18
        reputationlocal = reputatione18
    elif club1 == "Paraguay":
        clublocal = e19
        reputationlocal = reputatione19
    elif club1 == "Chile":
        clublocal = e20
        reputationlocal = reputatione20
    elif club1 == "Bolivia":
        clublocal = e21
        reputationlocal = reputatione21    
    elif club1 == "Brasil":
        clublocal = e22
        reputationlocal = reputatione22
    elif club1 == "Peru":
        clublocal = e23
        reputationlocal = reputatione23
    elif club1 == "Colombia":
        clublocal = e24
        reputationlocal = reputatione24            
    elif club1 == "Ecuador":
        clublocal = e25
        reputationlocal = reputatione25    
    elif club1 == "Venezuela":
        clublocal = e26
        reputationlocal = reputatione26
    elif club1 == "Mexico":
        clublocal = e27
        reputationlocal = reputatione27
    elif club1 == "Estados Unidos":
        clublocal = e28
        reputationlocal = reputatione28    
    elif club1 == "Canada":
        clublocal = e29
        reputationlocal = reputatione29
    elif club1 == "Costa Rica":
        clublocal = e30
        reputationlocal = reputatione30
    elif club1 == "Cuba":
        clublocal = e31
        reputationlocal = reputatione31 
    elif club1 == "Honduras":
        clublocal = e32
        reputationlocal = reputatione32          
    elif club1 == "Egipto":
        clublocal = e33
        reputationlocal = reputatione33
    elif club1 == "Senegal":
        clublocal = e34
        reputationlocal = reputatione34
    elif club1 == "Tunez":
        clublocal = e35
        reputationlocal = reputatione35    
    elif club1 == "Camerun":
        clublocal = e36
        reputationlocal = reputatione36
    elif club1 == "Marruecos":
        clublocal = e37
        reputationlocal = reputatione37
    elif club1 == "Nigeria":
        clublocal = e38
        reputationlocal = reputatione38            
    elif club1 == "Ghana":
        clublocal = e39
        reputationlocal = reputatione39    
    elif club1 == "Argelia":
        clublocal = e40
        reputationlocal = reputatione40    
    elif club1 == "Iran":
        clublocal = e41
        reputationlocal = reputatione41
    elif club1 == "Corea del Sur":
        clublocal = e42
        reputationlocal = reputatione42
    elif club1 == "Japon":
        clublocal = e43
        reputationlocal = reputatione43
    elif club1 == "China":
        clublocal = e44
        reputationlocal = reputatione44
    elif club1 == "Arabia Saudita":
        clublocal = e45
        reputationlocal = reputatione45
    elif club1 == "Israel":
        clublocal = e46
        reputationlocal = reputatione46
    elif club1 == "Australia":
        clublocal = e47
        reputationlocal = reputatione47     
    elif club1 == "Qatar":
        clublocal = e48
        reputationlocal = reputatione48   
    else:
        print("sos medio dislexico papito no?")
    if club2 == "España":
        clubvisitor = e1
        reputationvisitor = reputatione1
    elif club2 == "Francia":
        clubvisitor = e2
        reputationvisitor = reputatione2
    elif club2 == "Holanda":
        clubvisitor = e3
        reputationvisitor = reputatione3
    elif club2 == "Inglaterra":
        clubvisitor = e4
        reputationvisitor = reputatione4
    elif club2 == "Italia":
        clubvisitor = e5
        reputationvisitor = reputatione5
    elif club2 == "Croacia":
        clubvisitor = e6
        reputationvisitor = reputatione6
    elif club2 == "Belgica":
        clubvisitor = e7        
        reputationvisitor = reputatione7
    elif club2 == "Portugal":
        clubvisitor = e8
        reputationvisitor = reputatione8
    elif club2 == "Suiza":
        clubvisitor = e9
        reputationvisitor = reputatione9
    elif club2 == "Dinamarca":
        clubvisitor = e10
        reputationvisitor = reputatione10
    elif club2 == "Polonia":
        clubvisitor = e11
        reputationvisitor = reputatione11
    elif club2 == "Noruega":
        clubvisitor = e12
        reputationvisitor = reputatione12
    elif club2 == "Alemania":
        clubvisitor = e13
        reputationvisitor = reputatione13
    elif club2 == "Gales":
        clubvisitor = e14
        reputationvisitor = reputatione14
    elif club2 == "Serbia":
        clubvisitor = e15
        reputationvisitor = reputatione15
    elif club2 == "Suecia":
        clubvisitor = e16
        reputationvisitor = reputatione16
    elif club2 == "Argentina":
        clubvisitor = e17
        reputationvisitor = reputatione17
    elif club2 == "Uruguay":
        clubvisitor = e18
        reputationvisitor = reputatione18
    elif club2 == "Paraguay":
        clubvisitor = e19
        reputationvisitor = reputatione19
    elif club2 == "Chile":
        clubvisitor = e20
        reputationvisitor = reputatione20
    elif club2 == "Bolivia":
        clubvisitor = e21
        reputationvisitor = reputatione21    
    elif club2 == "Brasil":
        clubvisitor = e22
        reputationvisitor = reputatione22
    elif club2 == "Peru":
        clubvisitor = e23
        reputationvisitor = reputatione23
    elif club2 == "Colombia":
        clubvisitor = e24
        reputationvisitor = reputatione24            
    elif club2 == "Ecuador":
        clubvisitor = e25
        reputationvisitor = reputatione25    
    elif club2 == "Venezuela":
        clubvisitor = e26
        reputationvisitor = reputatione26
    elif club2 == "Mexico":
        clubvisitor = e27
        reputationvisitor = reputatione27
    elif club2 == "Estados Unidos":
        clubvisitor = e28
        reputationvisitor = reputatione28    
    elif club2 == "Canada":
        clubvisitor = e29
        reputationvisitor = reputatione29
    elif club2 == "Costa Rica":
        clubvisitor = e30
        reputationvisitor = reputatione30
    elif club2 == "Cuba":
        clubvisitor = e31
        reputationvisitor = reputatione31 
    elif club2 == "Honduras":
        clubvisitor = e32
        reputationvisitor = reputatione32  
    elif club2 == "Egipto":
        clubvisitor = e33
        reputationvisitor = reputatione33
    elif club2 == "Senegal":
        clubvisitor = e34
        reputationvisitor = reputatione34
    elif club2 == "Tunez":
        clubvisitor = e35
        reputationvisitor = reputatione35    
    elif club2 == "Camerun":
        clubvisitor = e36
        reputationvisitor = reputatione36
    elif club2 == "Marruecos":
        clubvisitor = e37
        reputationvisitor = reputatione37
    elif club2 == "Nigeria":
        clubvisitor = e38
        reputationvisitor = reputatione38            
    elif club2 == "Ghana":
        clubvisitor = e39
        reputationvisitor = reputatione39    
    elif club2 == "Argelia":
        clubvisitor = e40
        reputationvisitor = reputatione40    
    elif club2 == "Iran":
        clubvisitor = e41        
        reputationvisitor = reputatione41
    elif club2 == "Corea del Sur":
        clubvisitor = e42
        reputationvisitor = reputatione42
    elif club2 == "Japon":
        clubvisitor = e43
        reputationvisitor = reputatione43
    elif club2 == "China":
        clubvisitor = e44
        reputationvisitor = reputatione44
    elif club2 == "Arabia Saudita":
        clubvisitor = e45
        reputationvisitor = reputatione45
    elif club2 == "Israel":
        clubvisitor = e46
        reputationvisitor = reputatione46
    elif club2 == "Australia":
        clubvisitor = e47
        reputationvisitor = reputatione47
    elif club2 == "Qatar":
        clubvisitor = e48
        reputationvisitor = reputatione48
    else:
        print("sos medio dislexico papito no?")
        
    reputation = (reputationlocal - reputationvisitor)    
    if reputation == 0:
        numeros = [0, 1, 2, 3, 4]
        probabilidades = [0.39, 0.30, 0.19, 0.1, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3,4]
        probabilidades = [0.39, 0.30, 0.19, 0.1, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == 1:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.30, 0.32, 0.18, 0.1, 0.05, 0.03, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5]
        probabilidades = [0.36, 0.34, 0.15, 0.1, 0.03, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == 2:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.25, 0.32, 0.21, 0.12, 0.05, 0.03, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4]
        probabilidades = [0.41, 0.35, 0.12, 0.1, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == 3:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.20, 0.25, 0.25, 0.15, 0.08, 0.05, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3]
        probabilidades = [0.45, 0.40, 0.1, 0.05]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == 4:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.1, 0.20, 0.30, 0.20, 0.12, 0.06, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2]
        probabilidades = [0.6, 0.30, 0.11]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == -1:
        numeros = [0, 1, 2, 3, 4, 5]
        probabilidades = [0.36, 0.34, 0.15, 0.1, 0.03, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.30, 0.32, 0.18, 0.1, 0.05, 0.03, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0] 
    elif reputation == -2:
        numeros = [0, 1, 2, 3, 4]
        probabilidades = [0.41, 0.35, 0.12, 0.1, 0.02]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.25, 0.32, 0.21, 0.12, 0.05, 0.03, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0] 
    elif reputation == -3 :    
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.20, 0.25, 0.25, 0.15, 0.08, 0.05, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2, 3]
        probabilidades = [0.45, 0.40, 0.1, 0.05]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
    elif reputation == -4:
        numeros = [0, 1, 2, 3, 4, 5, 6]
        probabilidades = [0.1, 0.20, 0.30, 0.20, 0.12, 0.06, 0.02]
        goalsvisitor = random.choices(numeros, weights=probabilidades)[0]
        numeros = [0, 1, 2]
        probabilidades = [0.6, 0.30, 0.11]
        goallocal = random.choices(numeros, weights=probabilidades)[0]
        
    result = print(f'{club1} {goallocal}-{goalsvisitor} {club2}') 
    return result,club1,goallocal,goalsvisitor,club2

def mostrar_tabla(equiposs):
    equipos_ordenados = sorted(equiposs, key=lambda x: (x[list(x.keys())[0]]['PTS'], x[list(x.keys())[0]]['GD']), reverse=True)
    tabla = []
    for i, equipo in enumerate(equipos_ordenados, start=1):
        nombre_equipo = list(equipo.keys())[0]
        puntos = equipo[nombre_equipo]['PTS']
        goles = equipo[nombre_equipo]['GF']
        vic = equipo[nombre_equipo]['V']
        emp = equipo[nombre_equipo]['E']
        der = equipo[nombre_equipo]['D']
        diferencia_goles = equipo[nombre_equipo]['GD']
        golesencontra = equipo[nombre_equipo]['GC']
        tabla.append([i, nombre_equipo, puntos,vic,emp,der, goles,golesencontra, diferencia_goles])

    headers = ["POS", "EQUIPO", "PTS","V","E","D" ,"GF","GC", "GD"]
    print(tabulate(tabla, headers=headers, tablefmt="pretty"))

def numero_random():
    return random.randint(1, 5)

def actualizar_tabla(tabla,nombre_equipo,pts,goles_local,goles_visitante,victorias,empates,derrotas):
    for equipo in tabla:
        if nombre_equipo in equipo:
            equipo[nombre_equipo]['PTS'] += pts
            equipo[nombre_equipo]['GF'] += goles_local
            equipo[nombre_equipo]['GC'] += goles_visitante
            diferencia_goles = goles_local - goles_visitante
            equipo[nombre_equipo]['GD'] += diferencia_goles
            equipo[nombre_equipo]['V'] += victorias
            equipo[nombre_equipo]['E'] += empates
            equipo[nombre_equipo]['D'] += derrotas
            break