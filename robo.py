import os
import cv2
import pytesseract
import pydirectinput as bot 
import pyautogui as bot2
import time
import re
import string
import csv
import sys

time.sleep(15)
#x, y = bot.position()
#bot.click(317, 1429)
#print ("Posicao atual do mouse:")
#print ("x = "+str(x)+" y = "+str(y))
#
contador = 1
x = range(15000)
for n in x:
    print("Posição:", contador)
    bot.click(1030, 1314 , 1 )
    #bot.rightClick()
    time.sleep(1)
    bot.click(540, 1378, 1)
    imagem = bot2.screenshot(region=(27, 220, 1180, 842))
    imagem.save('analise.png')
    img = cv2.imread("analise.png")
    pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract\Tesseract.exe"
    custom_oem_psm_config = r'--oem 3 --psm 6'
    resultado = pytesseract.image_to_string(
    img,  config=custom_oem_psm_config, lang='eng')
    # marca
    for line in resultado.split('\n'):
        if 'Marca' in line:
            marca = re.sub("Marca ", "", line)

    # modelo
    for line in resultado.split('\n'):
        if 'Modelo' in line:
            modelo = re.sub("Modelo ", "", line)

    # ano
    for line in resultado.split('\n'):
        if 'Ano' in line:
            ano = re.sub("Ano ", "", line)

    #aro
    for line in resultado.split('\n'):
        if 'Diam. aro ' in line:
            aro = re.sub("Diam. aro ", "", line)

    # divergenciaemcurvas min e max
    for line in resultado.split('\n'):
        if 'Conv. diant. total' in line:
            try:
                conv = re.sub("Conv. diant. total ", "", line)
                VAL_DIVERG_CURVAS_MIN = conv.split()[0]
                VAL_DIVERG_CURVAS_MAX = conv.split()[2]
            except:
                print('Erro')
            finally:
                pass

    # VAL_E1_CONVER_MIN e MAX
    for line in resultado.split('\n'):        
        if 'Conv. diant.' in line:
            try:
                conv = re.sub("Conv. diant. ", "", line)
                VAL_E1_CONVER_MIN = conv.split()[0]
                VAL_E1_CONVER_MAX = conv.split()[2]
            except:
                print('Erro')
            finally:
                pass

    for line in resultado.split('\n'):
        if 'Conv. diant. ' in line:
            if not '--' in line:
                try:
                    conv = re.sub("Conv. diant. ", "", line)
                    VAL_E1_CONVER_ESQUER_MIN = conv.split()[0]
                    VAL_E1_CONVER_ESQUER_MIN = VAL_E1_CONVER_ESQUER_MIN.split("°")[0]
                    VAL_E1_CONVER_ESQUER_MAX = conv.split()[2]
                    VAL_E1_CONVER_ESQUER_MAX = VAL_E1_CONVER_ESQUER_MAX.split("(")[0]
                    VAL_E1_CONVER_ESQUER_MAX = VAL_E1_CONVER_ESQUER_MAX[0:5]
                    VAL_E1_CONVER_DIREIT_MIN = VAL_E1_CONVER_ESQUER_MIN
                    VAL_E1_CONVER_DIREIT_MAX = VAL_E1_CONVER_ESQUER_MAX
                except:
                    print('Erro')
                finally:
                    pass
            else:
                VAL_E1_CONVER_ESQUER_MIN = ''
                VAL_E1_CONVER_ESQUER_MAX = ''
                VAL_E1_CONVER_DIREIT_MIN = ''
                VAL_E1_CONVER_DIREIT_MAX = ''


    # VAL_E1_SETBAC_MIN e MAX - valores sempre iguais
    VAL_E1_SETBAC_MIN = "-5,00"
    VAL_E1_SETBAC_MAX = "5,00"

    # VAL_E1_ANGULO_IMPULS_MIN e MAX - valores sempre iguais
    VAL_E1_ANGULO_IMPULS_MIN = "-2,00"
    VAL_E1_ANGULO_IMPULS_MAX = "2,00"
    VAL_E4_ANGULO_IMPULS_MIN = "-2,00"
    VAL_E4_ANGULO_IMPULS_MAX = "2,00"	
    VAL_E1_CAMBER_ESQUER_MAX = ""
    # VAL_E1_CAMBER_ESQUER_MIN e MAX
    # VAL_E1_CAMBER_DIREIT_MIN e MAX
    for line in resultado.split('\n'):
        if 'Camber diant.' in line:  
            if not '--' in line:  
                try:
                    conv = re.sub("Camber diant. ", "", line)
                    VAL_E1_CAMBER_ESQUER_MIN = conv.split()[0]
                    VAL_E1_CAMBER_ESQUER_MIN = VAL_E1_CAMBER_ESQUER_MIN.split("°")[0]
                    VAL_E1_CAMBER_ESQUER_MAX = conv.split()[2]
                    VAL_E1_CAMBER_ESQUER_MAX = VAL_E1_CAMBER_ESQUER_MAX.split("(")[0]
                    VAL_E1_CAMBER_ESQUER_MAX = VAL_E1_CAMBER_ESQUER_MAX[0:5]
                    VAL_E1_CAMBER_DIREIT_MIN = VAL_E1_CAMBER_ESQUER_MIN
                    VAL_E1_CAMBER_DIREIT_MAX = VAL_E1_CAMBER_ESQUER_MAX
                except:
                    print('Erro')
                finally:
                    pass
            else:
                VAL_E1_CAMBER_ESQUER_MIN = ''
                VAL_E1_CAMBER_ESQUER_MAX = ''
                VAL_E1_CAMBER_DIREIT_MIN = ''
                VAL_E1_CAMBER_DIREIT_MAX = ''

    # VAL_E1_CASTER_ESQUER_MIN e MAX
    for line in resultado.split('\n'):
        if 'Caster ' in line:
            if not '--' in line:
                try:
                    conv = re.sub("Caster ", "", line)
                    VAL_E1_CASTER_ESQUER_MIN = conv.split()[0]
                    VAL_E1_CASTER_ESQUER_MIN = VAL_E1_CASTER_ESQUER_MIN.split("°")[0]
                    VAL_E1_CASTER_ESQUER_MAX = conv.split()[2]
                    VAL_E1_CASTER_ESQUER_MAX = VAL_E1_CASTER_ESQUER_MAX.split("(")[0]
                    VAL_E1_CASTER_ESQUER_MAX = VAL_E1_CASTER_ESQUER_MAX[0:5]
                    VAL_E1_CASTER_DIREIT_MIN = VAL_E1_CASTER_ESQUER_MIN
                    VAL_E1_CASTER_DIREIT_MAX = VAL_E1_CASTER_ESQUER_MAX
                except:
                    print('Erro')
                finally:
                    pass


            else:
                VAL_E1_CASTER_ESQUER_MAX = ''
                VAL_E1_CASTER_ESQUER_MAX = ''
                VAL_E1_CASTER_DIREIT_MIN = ''
                VAL_E1_CASTER_DIREIT_MAX = ''


    # VAL_E1_KPI_ESQUER_MIN e MAX
    for line in resultado.split('\n'):
        if 'KPI' in line:
            if not '--' in line:
                try:
                    conv = re.sub("KPI ", "", line)
                    VAL_E1_KPI_ESQUER_MIN = conv.split()[0]
                    VAL_E1_KPI_ESQUER_MIN = VAL_E1_KPI_ESQUER_MIN.split("°")[0]
                    VAL_E1_KPI_ESQUER_MAX = conv.split()[2]
                    VAL_E1_KPI_ESQUER_MAX = VAL_E1_KPI_ESQUER_MAX.split("(")[0]
                    VAL_E1_KPI_ESQUER_MAX = VAL_E1_KPI_ESQUER_MAX[0:5]
                    VAL_E1_KPI_DIREIT_MIN = VAL_E1_KPI_ESQUER_MIN
                    VAL_E1_KPI_DIREIT_MAX = VAL_E1_KPI_ESQUER_MAX
                except:
                    print('Erro')
                finally:
                    pass
            else:
                VAL_E1_KPI_ESQUER_MIN = ''
                VAL_E1_KPI_ESQUER_MAX = ''
                VAL_E1_KPI_DIREIT_MIN = ''
                VAL_E1_KPI_DIREIT_MAX = ''


    # VAL_E4_ANGULO_IMPULS_MIN e MAX
    VAL_E4_ANGULO_IMPULS_MIN = "-2,00"
    VAL_E4_ANGULO_IMPULS_MAX = "2,00"


    # VAL_E4_CAMBER_ESQUER_MIN e max
    # VAL_E4_CAMBER_DIREIT_MIN e MAX
    for line in resultado.split('\n'):
        if 'Camber tras. ' in line:
            if not '--' in line:
                try:
                    conv = re.sub("Camber tras. ", "", line)
                    VAL_E4_CAMBER_ESQUER_MIN = conv.split()[0]
                    VAL_E4_CAMBER_ESQUER_MIN = VAL_E4_CAMBER_ESQUER_MIN.split("°")[0]
                    VAL_E4_CAMBER_ESQUER_MAX = conv.split()[2]
                    VAL_E4_CAMBER_ESQUER_MAX = VAL_E4_CAMBER_ESQUER_MAX.split("(")[0]
                    VAL_E4_CAMBER_ESQUER_MAX = VAL_E4_CAMBER_ESQUER_MAX[0:5]
                    VAL_E4_CAMBER_DIREIT_MIN = VAL_E4_CAMBER_ESQUER_MIN
                    VAL_E4_CAMBER_DIREIT_MAX = VAL_E4_CAMBER_ESQUER_MAX
                except:
                    print('Erro')
                finally:
                    pass
            else:
                VAL_E4_CAMBER_ESQUER_MIN = ''
                VAL_E4_CAMBER_ESQUER_MAX = ''
                VAL_E4_CAMBER_DIREIT_MIN = ''
                VAL_E4_CAMBER_DIREIT_MAX = ''


    # VAL_E4_CONVER_ESQUER_MIN e MAX
    # VAL_E4_CONVER_DIREIT_MIN e MAX

    for line in resultado.split('\n'):
        if 'Conv. tras. ' in line:
            if not '--' in line:
                try:
                    conv = re.sub("Conv. tras. ", "", line)
                    VAL_E4_CONVER_ESQUER_MIN = conv.split()[0]
                    VAL_E4_CONVER_ESQUER_MIN = VAL_E4_CONVER_ESQUER_MIN.split("°")[0]
                    VAL_E4_CONVER_ESQUER_MAX = conv.split()[2]
                    VAL_E4_CONVER_ESQUER_MAX = VAL_E4_CONVER_ESQUER_MAX.split("(")[0]
                    VAL_E4_CONVER_ESQUER_MAX = VAL_E4_CONVER_ESQUER_MAX[0:5]
                    VAL_E4_CONVER_DIREIT_MIN = VAL_E4_CONVER_ESQUER_MIN
                    VAL_E4_CONVER_DIREIT_MAX = VAL_E4_CONVER_ESQUER_MAX
                except:
                    print('Erro')
                finally:
                    pass
            else:
                VAL_E4_CONVER_ESQUER_MIN = ''
                VAL_E4_CONVER_ESQUER_MAX = ''
                VAL_E4_CONVER_DIREIT_MIN = ''
                VAL_E4_CONVER_DIREIT_MAX = ''

    try:
      linhaincluir = [contador, modelo, ano, marca, aro, VAL_DIVERG_CURVAS_MIN, VAL_DIVERG_CURVAS_MAX, VAL_E1_CONVER_MIN, VAL_E1_CONVER_MAX, VAL_E1_SETBAC_MIN, VAL_E1_SETBAC_MAX, VAL_E1_ANGULO_IMPULS_MIN, VAL_E1_ANGULO_IMPULS_MAX, VAL_E1_CAMBER_ESQUER_MIN, VAL_E1_CAMBER_ESQUER_MAX, VAL_E1_CASTER_ESQUER_MIN,
                    VAL_E1_CASTER_ESQUER_MAX, VAL_E1_KPI_ESQUER_MIN, VAL_E1_KPI_ESQUER_MAX, VAL_E1_CONVER_ESQUER_MIN, VAL_E1_CONVER_ESQUER_MAX, VAL_E1_CAMBER_DIREIT_MIN, VAL_E1_CAMBER_DIREIT_MAX, VAL_E1_CASTER_DIREIT_MIN, VAL_E1_CASTER_DIREIT_MAX, VAL_E1_KPI_DIREIT_MIN, VAL_E1_KPI_DIREIT_MAX, VAL_E4_ANGULO_IMPULS_MIN, VAL_E4_ANGULO_IMPULS_MAX, VAL_E4_CAMBER_ESQUER_MIN,	VAL_E4_CAMBER_ESQUER_MAX, VAL_E4_CONVER_ESQUER_MIN, VAL_E4_CONVER_ESQUER_MAX, VAL_E4_CAMBER_DIREIT_MIN, VAL_E4_CAMBER_DIREIT_MAX, VAL_E4_CONVER_DIREIT_MIN, VAL_E4_CONVER_DIREIT_MAX]
      with open('templatecarro.csv', 'a') as f:
        f.write("\n")
        for line in linhaincluir:
            f.write(f"{line};")
    except:
      print('Erro')
    finally:
      pass

    os.remove("analise.png")
    bot.click(126, 1293)
    contador = contador + 1




# print(marca)
# print(modelo)
# print(ano)
# print(conv)
# print(VAL_DIVERG_CURVAS_MIN)
# print(VAL_DIVERG_CURVAS_MAX)
# print(VAL_E1_CONVER_MIN)
# print(VAL_E1_CONVER_MAX)
# print(VAL_E1_CAMBER_ESQUER_MIN)
# print(VAL_E1_CAMBER_ESQUER_MAX)
# print(VAL_E1_CASTER_ESQUER_MIN)
# print(VAL_E1_CASTER_ESQUER_MAX)
# print(VAL_E4_CONVER_ESQUER_MIN)
# print(VAL_E4_CONVER_ESQUER_MAX)
# print(VAL_E4_CONVER_DIREIT_MIN)
# print(VAL_E4_CONVER_DIREIT_MAX)
# abc--123-789-ABC-XYZ
#splitresultado = resultado.split()
# print(splitresultado)
#marca = splitresultado[1]
#modelo = splitresultado[3]
# ano