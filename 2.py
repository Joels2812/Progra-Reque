# Ingeniería de Requerimientos
# Tarea Programada
# Profesor: Néstor Morales Rodríguez
# Integrantes:
# Galvez Bogantes Kenneth Mauricio
# Hernandez Hernandez Dayana Alexandra
# Hernandez Venegas Luis Sebastian
# Ledezma Mora Joel Stuard
# Porras Soto Jose Ignacio
# Rios Nuñez Luis Fabian
# Soto Aguilar Pedro Antonio
# II Semestre 2021



#Librerías necesarias para el funcionamiento del programa
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tabulate import tabulate
import re

#Codificación para el funcionamiento del menú principal
def verMenu():
    while(True):
        menuPrincipal()
        opcionUsuario = seleccionarOpcionPrincipal()
        if(opcionUsuario == 1):
            opcionesBolsa()
            indice = seleccionarOpcionIndice()
            if(indice == 9):
                menuPrincipal()
            else:
                infoIndice(nombreURL(indice))
        elif(opcionUsuario == 2):
            opcionesBolsa()
            indice = seleccionarOpcionIndice()
            if(indice == 9):
                menuPrincipal()
            else:
                empresasIndice(nombreURL(indice))
        elif(opcionUsuario == 3):
            optionsHistoricos()
            opcion = seleccionarOpcionPrincipal()
            if(opcion == 1):
                opcionesBolsa()
                indice = seleccionarOpcionIndice()
                month = validateMonth()
                day = validateDay(month)
                historicoIndice(nombreURL(indice), month, day)
            elif(opcion == 2):
                opcionesBolsa()
                indice = seleccionarOpcionIndice()
                optionsEmpresas(nombreURL(indice))
                indiceEmpresa = validateEmpresa()
                print("es.investing.com" + obtainEmpresasURL(nombreURL(indice), indiceEmpresa))
                month = validateMonth()
            elif(opcion == 3):
                opcionesBolsa()
                indice = seleccionarOpcionIndice()
                optionsEmpresas(nombreURL(indice))
                indiceEmpresa = validateEmpresa()
                URLN = ("es.investing.com" + obtainEmpresasURL(nombreURL(indice), indiceEmpresa))
                noticiasEmpresa(URLN)
            else:
                menuPrincipal()
        else:
            print("Muchas gracias por usar el SEIS")
            break

#Interfaz del menú principal
def menuPrincipal():
    print("\nStock Exchange Information System (SEIS)")
    print("1. Consultar información de un índice bursátil")
    print("2. Consultar empresas que pertenecen a un índice bursátil")
    print("3. Consultar históricos/noticias de índices/empresas")
    print("4. Salir\n")
    print("Indique la opción que desea ejecutar: ")

#Valida las restricciones del menú principal
def seleccionarOpcionPrincipal():
    while(True):
        opcion = input()
        if(esEntero(opcion)==False):
            print("Ingrese un número entero")
        else:
            opcion = int(opcion)
            if(opcion < 1 or opcion > 4):
                print("Ingrese un dato válido")
            else:
                return opcion

#Valida si el dato ingresado en un numero entero
def esEntero(num):
    try:
        int(num)
        return True
    except:
        return False

#Muestra las opciones de bolsa disponibles
def opcionesBolsa():
    print("\nLista de índices")
    print("1. DOW 30 (USA)")
    print("2. Nasdaq100(USA)")
    print("3. Bovespa (Brazil)")
    print("4. DAX (Alemania)")
    print("5. EuroStoxx 50 (Alemania)")
    print("6. FTSE 100 (Reino Unido)")
    print("7. IBEX 35 (España)")
    print("8. Nikkei 225 (Japón)")
    print("9. Volver\n")
    print("Indique el índice que desea consultar: ")

#Valida las restricciones del índice de bolsas
def seleccionarOpcionIndice():
    while(True):
        opcion = input()
        if(esEntero(opcion)==False):
            print("Ingrese un número entero")
        else:
            opcion = int(opcion)
            if(opcion < 1 or opcion > 9):
                print("Ingrese un dato válido")
            else:
                return opcion

#Para seleccionar la bolsa en el índice
def nombreURL(numIndice):
    if(numIndice == 1):
        return "Dow Jones"
    elif(numIndice == 2):
        return "Nasdaq"
    elif(numIndice == 3):
        return "Bovespa"
    elif(numIndice == 4):
        return "DAX"
    elif(numIndice == 5):
        return "Euro Stoxx 50"
    elif(numIndice == 6):
        return "FTSE 100"
    elif(numIndice == 7):
        return "IBEX 35"
    else:
        return "Nikkei 225"

#Para tomar el URL de la bolsa correspondiente, se utiliza para las 3 funciones
def returnIndiceURL(nombreIndice):
    if(nombreIndice == "Dow Jones"):
        return "https://es.investing.com/indices/us-30"
    elif(nombreIndice == "Nasdaq"):
        return "https://es.investing.com/indices/nasdaq-composite"
    elif(nombreIndice == "Bovespa"):
        return "https://es.investing.com/indices/bovespa"
    elif(nombreIndice == "DAX"):
        return "https://es.investing.com/indices/germany-30"
    elif(nombreIndice == "Euro Stoxx 50"):
        return "https://es.investing.com/indices/eu-stoxx50"
    elif(nombreIndice == "FTSE 100"):
        return "https://es.investing.com/indices/uk-100"
    elif(nombreIndice == "IBEX 35"):
        return "https://es.investing.com/indices/spain-35"
    else:
        return "https://es.investing.com/indices/japan-ni225"

#Toma un URL secundario, se utiliza para la primera función
def returnIndiceURLB(nombreIndice):
    if(nombreIndice == "Dow Jones"):
        return "https://es.finance.yahoo.com/quote/%5EDJI?p=%5EDJI"
    elif(nombreIndice == "Nasdaq"):
        return "https://es.finance.yahoo.com/quote/%5EIXIC?p=%5EIXIC"
    elif(nombreIndice == "Bovespa"):
        return "https://es.finance.yahoo.com/quote/%5EBVSP?p=%5EBVSP"
    elif(nombreIndice == "DAX"):
        return "https://es.finance.yahoo.com/quote/%5EGDAXI?p=%5EGDAXI"
    elif(nombreIndice == "Euro Stoxx 50"):
        return "https://es.finance.yahoo.com/quote/%5ESTOXX50E?p=%5ESTOXX50E"
    elif(nombreIndice == "FTSE 100"):
        return "https://es.finance.yahoo.com/quote/%5EFTSE?p=%5EFTSE"
    elif(nombreIndice == "IBEX 35"):
        return "https://es.finance.yahoo.com/quote/%5EIBEX?p=%5EIBEX"
    else:
        return "https://es.finance.yahoo.com/quote/%5EN225?p=%5EN225"

#Interfaz para ver las opciones de la función 3
def optionsHistoricos():
    print("\nLista de opciones")
    print("1. Consultar históricos de un mes de un índice")
    print("2. Consultar históricos de un mes para una empresa")
    print("3. Consultar noticias de una empresa")
    print("4. Volver\n")
    print("Indique la opción que desea ejecutar")

#Valida el mes, se utiliza en la función 3
def validateMonth():
    print("Indique el # del mes que desea consultar: ")
    while(True):
        month = input()
        if(esEntero(month)==False):
            print("Ingrese un dato válido")
        else:
            month = int(month)
            if(month < 1 or month > 12):
                print("Ingrese un dato válido")
            else:
                return month

#Valida el día, se utiliza en la función 3
def validateDay(month):
    print("Indique el # de día que desea consultar: ")
    while(True):
        day = input()
        if(esEntero(day)==False):
            print("Ingrese un dato válido")
        else:
            day = int(day)
            if(month == 2):
                if(day < 1 or day > 28):
                    print("Ingrese un dato válido")
                else:
                    return day
            elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                if(day < 1 or day > 31):
                    print("Ingrese un dato válido")
                else:
                    return day
            else:
                if(day < 1 or day > 30):
                    print("Ingrese un dato válido")
                else:
                    return day

#Muestra los nombres de las empresas, se utiliza en la función 2 y 3
def optionsEmpresas(nombreIndice):
    URL = obtainBolsaURL(nombreIndice) + "-components"
    print("Información obtenida de la página: " + URL)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    pagina = requests.get(URL, headers=headers)
    soup = BeautifulSoup(pagina.content,"html.parser")

    nb = soup.find_all("span",class_="alertBellGrayPlus js-plus-icon genToolTip oneliner")

    names = list()
    contador = 0
    for i in nb:
        if contador < 20:
            names.append(i["data-name"])
        else:
            break
        contador += 1

    df = pd.DataFrame({"Nombre de la empresa":names})

    print (df.to_markdown())

#Valida el dato ingresado para buscar la empresa
def validateEmpresa():
    while(True):
        print("Indique el # de la empresa que desea consultar: ")
        option = input()
        if(esEntero(option)==False):
            print("Ingrese un dato válido")
        else:
            option = int(option)
            if(option < 0 or option > 19):
                print("Ingrese un dato válido")
            else:
                return option

#Se usa para obtener el URL de la empresa correspondiente
def obtainEmpresasURL(nombreIndice, pIndice):
    URL = obtainBolsaURL(nombreIndice) + "-components"
    print("Informacion obtenida de la página: " + URL)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    pagina = requests.get(URL, headers=headers)
    soup = BeautifulSoup(pagina.content,"html.parser")

    ex = soup.find_all("a", href=re.compile("/equities/"))

    extencions = list()
    contador = 0
    for i in ex:
        if contador < 30:
            contador += 1
        elif contador >= 30 and contador < 50:
            extencions.append(i["href"])
            contador += 1
        else:
            break

    return extencions[pIndice]


#Funcionalidad a
def infoIndice(nombreIndice):
    URL = returnIndiceURL(nombreIndice)
    URLB = returnIndiceURLB(nombreIndice)
    pagina = requests.get(URL)
    soup = BeautifulSoup(pagina.content,"html.parser")

    #Nombre del índice
    iN = soup.find_all("h1",class_="text-2xl font-semibold instrument-header_title__GTWDv mobile:mb-2")

    names = list()
    contador = 0
    for i in iN:
        if contador < 1:
            names.append(i.text)
        else:
            break
        contador += 1


    #Valor actual del índice
    aV = soup.find_all("span",class_="instrument-price_last__KQzyA")
    actualValue = list()

    contador = 0
    for i in aV:
        if contador < 1:
            actualValue.append(i.text)
        else:
            break
        contador += 1


    #Diferencia en puntos enteros
    ptD = soup.find_all("span",class_="instrument-price_change-value__jkuml instrument-price_up__2-OcT")
    pointsDif = list()


    contador = 0
    for i in ptD:
        if contador < 1:
            pointsDif.append(i.text)
        else:
            break
        contador += 1

    if(len(pointsDif)==0):
        dP = soup.find_all("span",class_="instrument-price_change-value__jkuml instrument-price_down__3dhtw")

        contador = 0
        for i in dP:
            if contador < 1:
                pointsDif.append(i.text)
            else:
                break
            contador += 1


    #Diferencia en porcentaje
    pgD = soup.find_all("span",class_="instrument-price_change-percent__19cas instrument-price_down__3dhtw")
    porcentageDif = list()

    contador = 0
    for i in pgD:
        if contador < 1:
            porcentageDif.append(i.text)
        else:
            break
        contador += 1

    if(len(porcentageDif)==0):
        dPj = soup.find_all("span",class_="instrument-price_change-percent__19cas instrument-price_up__2-OcT")

        contador = 0
        for i in dPj:
            if contador < 1:
                porcentageDif.append(i.text)
            else:
                break
            contador += 1

    #Valor de cierre
    cV = soup.find_all("span",class_="key-info_dd-numeric__2cYjc")
    closingValue = list()
    contador = 0
    for i in cV:
        if contador < 1:
            closingValue.append(i.text)
        else:
            break
        contador += 1

    #Apertura
    pagina = requests.get(URLB)
    soup = BeautifulSoup(pagina.content,"html.parser")
    oP = soup.find_all("span",class_="Trsdu(0.3s)")

    opening = list()

    contador = 0
    for i in oP:
        if contador < 1:
            opening.append(i.text)
        else:
            break
        contador += 1

    #Rango Diario
    pagina = requests.get(URLB)
    soup = BeautifulSoup(pagina.content,"html.parser")
    dR = soup.find_all("td",class_="Ta(end) Fw(600) Lh(14px)")

    dailyRange = list()

    contador = 0
    for i in dR:
        if contador < 1:
            dailyRange.append(i.text)
        else:
            break
        contador += 1

    pd.set_option ('display.max_rows', 1)
    pd.set_option ('display.max_columns', 7)
    df = pd.DataFrame({"Nombre completo del índice":names,"Valor actual":actualValue,"Diferencia en puntos enteros":pointsDif,"Diferencia en porcentaje":porcentageDif,"Valor de cierre":closingValue,"Apertura":opening,"Rango diario":dailyRange})#,index = list(range(1,2)))

    print (df.to_markdown())

#Funcionalidad b
def empresasIndice(nombreIndice):
    URL = obtainBolsaURL(nombreIndice) + "-components"
    print("Información obtenida de: " + URL)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    pagina = requests.get(URL, headers=headers)
    soup = BeautifulSoup(pagina.content,"html.parser")

    #Nombres de las empresas
    eN = soup.find_all("span",class_="alertBellGrayPlus js-plus-icon genToolTip oneliner")

    names = list()
    contador = 0
    for i in eN:
        if contador < 20:
            names.append(i["data-name"])
        else:
            break
        contador += 1

    #Último valor
    lV = soup.find_all("td",class_=re.compile("-last"))

    lastValue = list()
    contador = 0
    for i in lV:
        if contador < 20:
            lastValue.append(i.text)
        else:
            break
        contador += 1

    #Valor máximo
    mV = soup.find_all("td",class_=re.compile("-high"))

    maxValue = list()
    contador = 0
    for i in mV:
        if contador < 20:
            maxValue.append(i.text)
        else:
            break
        contador += 1

    #Valor mínimo
    mV = soup.find_all("td",class_=re.compile("-low"))

    minValue = list()
    contador = 0
    for i in mV:
        if contador < 20:
            minValue.append(i.text)
        else:
            break
        contador += 1

    #Variación en números enteros
    iV = soup.find_all("td",class_=re.compile("-pc"))

    integersVar = list()
    contador = 0
    for i in iV:
        if contador < 20:
            integersVar.append(i.text)
        else:
            break
        contador += 1

    #Variación en porcentaje
    pV = soup.find_all("td",class_=re.compile("-pcp"))

    porcentageVar = list()
    contador = 0
    for i in pV:
        if contador < 20:
            porcentageVar.append(i.text)
        else:
            break
        contador += 1

    #Volumen
    vL = soup.find_all("td",class_=re.compile("-turnover"))

    volume = list()
    contador = 0
    for i in vL:
        if contador < 20:
            volume.append(i.text)
        else:
            break
        contador += 1

    df = pd.DataFrame({"Nombre de la empresa":names,"Último valor":lastValue,"Valor máximo":maxValue,"Valor mínimo":minValue,"Variación en puntos enteros":integersVar,"Variación en porcentaje":porcentageVar,"Volumen":volume})#,index = list(range(1,2)))

    print(df.to_markdown())
    #print(df.to_markdown(tablefmt="grid")) #OTRO POSIBLE FORMATO PARA LAS TABLAS AUNQUE AUN CON ALGUNOS PROBLEMAS DE VISUALIZACION.

def obtainBolsaURL(nombreIndice):
    URL = "https://es.investing.com/indices/major-indices"
    BuscarURL = "https://es.investing.com"
    pagina = requests.get(URL)
    soup = BeautifulSoup(pagina.content,"html.parser")

    nb = soup.find_all("a",class_="inv-link bold datatable_cell--name__link__1XAxP")

    names = list()
    contador = 0
    for i in nb:
        if contador < 44:
            names.append(i.text)
        else:
            break
        contador += 1

    ex = soup.find_all("a",class_="inv-link bold datatable_cell--name__link__1XAxP")

    extencions = list()
    contador = 0
    for i in ex:
        if contador < 44:
            extencions.append(i["href"])
        else:
            break
        contador += 1

    return BuscarURL + extencions[contadorIndice(names, nombreIndice)]

def contadorIndice(bolsasList, nombreIndice):
    contador = 0
    for i in bolsasList:
        if(i == nombreIndice):
            return contador
        contador += 1

#Funcionalidad c
def noticiasEmpresa(nombreIndice):
    URL = nombreIndice
    print("Información obtenida de: " + URL)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    pagina = requests.get(URL, headers=headers)
    soup = BeautifulSoup(pagina.content,"html.parser")

    #Nombre de las empresa
    eN = soup.find_all("span",class_="float_lang_base_1 relativeAttr")

    name = list()
    contador = 0
    for i in eN:
        if contador < 20:
            name.append(i["data-name"])
        else:
            break
        contador += 1

    #Noticias
    nT = soup.find_all("td",class_="articleDetails")

    notices = list()
    contador = 0
    for i in nT:
        if contador < 20:
            notices.append(i.text)
        else:
            break
        contador += 1

    df = pd.DataFrame({"Nombre de la empresa":name,"Noticias":notices})#,index = list(range(1,2)))

    print(df.to_markdown())


verMenu()