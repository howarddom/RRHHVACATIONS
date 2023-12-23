import pyodbc
from datetime import datetime , date
from datetime import timedelta
import pandas as pd
import numpy as np
from tkinter import Tk
from dateutil.relativedelta import relativedelta

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\PabloGodin\EMPLEADOS.mdb;')
cursor = conn.cursor()
now = datetime.now()
t = timedelta(365.2)
t2 = timedelta(20)
#Clases
class Empleado:
    def __init__(self, id_usuario,nombre_usuario, apellido_usuario, fecha_ingreso):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario
        self.fecha_ingreso = fecha_ingreso
        self.antiguedad = calculo_dias_correspondientes
        pass


#Funciones:

#'feriados cuentan?'
def calcular_dias_habiles(fecha_inicio, fecha_fin):   
    
    dias_habiles = np.busday_count(fecha_inicio, fecha_fin)
    return dias_habiles

def ingresar_registro():
    cursor.execute('INSERT INTO TblEMPLEADOS VALUES ()')

def buscar_registros(apellido):
    cursor.execute('SELECT *FROM TblEmpleados WHERE Apellido= ?', (apellido))   
    resultado = cursor.fetchall()
    return resultado

def buscar_registro(id):
    cursor.execute('SELECT *FROM TblEmpleados WHERE IDEmpleado= ?', (id))   
    resultado = cursor.fetchone()
    return resultado 


def calculo_antiguedad(fecha_inicio, fecha_fin):
   
     dias_entre_fechas = np.arange(fecha_inicio, fecha_fin, np.timedelta64(1, 'D'))
     return dias_entre_fechas

def calculo_antiguedad():
     calculoantiguedad = now - resultado_busqueda[8]
     return calculoantiguedad
       
def calculo_dias_correspondientes():
     dia_inicio = date(2023,1,1)
     dia_final = date(2023,6,30)
     dias_corresp_antiguedad1 = 14
     dias_corresp_antiguedad2 = 21
     dias_corresp_antiguedad3 = 28
     dias_corresp_antiguedad4 = 35
     diashabiles = calcular_dias_habiles(resultado_busqueda[8].date(),now.date())
     
     if diashabiles <calcular_dias_habiles(dia_inicio,dia_final): 
        diashabilesint = int(diashabiles)
        diashabilesint = timedelta(diashabilesint)
        
        diashabilesint = diashabilesint / t2
        diashabilesint = int(diashabilesint)
        
        return (diashabilesint)
     elif (calculo_antiguedad() / t) >= 0.55 and (calculo_antiguedad() / t) < 5:
          return ( dias_corresp_antiguedad1)
     elif (calculo_antiguedad() / t >= 5) and (calculo_antiguedad() / t) < 10:
          return ( dias_corresp_antiguedad2)
     elif (calculo_antiguedad() / t >= 10) and (calculo_antiguedad() / t) < 15:
          return (dias_corresp_antiguedad3)
     elif calculo_antiguedad() / t >= 15:
          return ( dias_corresp_antiguedad4)
          
def dias_vigentes():
    
    return



e = Empleado ("","","","")

# nombre_usuario =""
# apellido_usuario=""
# id_usuario= ""
while e.apellido_usuario != "exit":
     e.apellido_usuario = input("Ingrese Apellido: ")
     resultado_busqueda = buscar_registros(e.apellido_usuario)
     if resultado_busqueda:
        for registro in resultado_busqueda:
            print("=" *50 ,"\n","ID: ", registro[0],"Nombre: ", registro[2],"Apellido: ",registro[1],"\n","=" *50 )
                   
        # """ id_usuario = input("Ingrese ID del empleado: ")
        # id_usuario = int(id_usuario) """
        while True: 
            try: 
                e.id_usuario = int(input(" Elegi numero de ID: ")) 
                break 
            except ValueError: 
                print(" Por favor ingrese un número válido.") 
            
        resultado_busqueda = buscar_registro(e.id_usuario)
        if resultado_busqueda:
            print ("\n","-" *50,"\n","Registro encontrado:", resultado_busqueda[1] + " ",resultado_busqueda[2],"\n")
            print ("-" *50,"\n"," Fecha de inicio :",resultado_busqueda[8],"\n")
            print ("-" *50,"\n"," Días hábiles trabajados: ",calcular_dias_habiles(resultado_busqueda[8].date(),now.date()),"\n")
            print ("-" *50,"\n"," Vacaciones correspondiente por antiguedad: ",calculo_dias_correspondientes(),"\n")
            print ("-" *50,"\n"," Dias trabajados: ",calculo_antiguedad(),"\n")
        else:
            print ("ID inexistente")

print("gracias vuelva prontos")        
        
        # resultado_busqueda == list(""):
        #     print("Usuario inexistente")
         
     




#     if nombre_usuario == "exit":
#         break
#     print(nombre_usuario)
#     apellido_usuario = input("Ingrese apellido a buscar: ")
#     resultado_busqueda = buscar_registro(nombre_usuario,apellido_usuario)
#     if resultado_busqueda:
#             print ("Registro encontrado:", resultado_busqueda[1] + " ",resultado_busqueda[2])
#             print ("Fecha de inicio :",resultado_busqueda[8])
#             print ("Días hábiles trabajados: ",calcular_dias_habiles(resultado_busqueda[8].date(),now.date()))
#             print ("Vacaciones correspondiente por antiguedad: ",calculo_dias_correspondientes())
#             print ("Dias trabajados: ",calculo_antiguedad())
                  
#     elif resultado_busqueda == list(""):
#          print("Usuario inexistente")
# conn.close() """






'devengar : te corresponde pero no te las tomaste'
'fowler newton'
'juniors 14 corridos' '7 con goce'
'primero de enero hasta el 31 de diciembre'
'1 cada 20 dias'