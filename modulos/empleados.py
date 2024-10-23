import json
import datetime

def traerInfo():
  file = open("empleadosDB.json", "r")
  empleados = json.load(file)
  return empleados

def guardarInfo(datos):
  file = open("empleadosDB.json", "w")
  json.dump(datos,file, indent=4)
  file.close()
 
def buscarEmpleado(datos, identificacion):
  empleadoEncontrado = False
  validar = False
  for empleado in datos:
    if empleado["identificacion"] == identificacion:
       empleadoEncontrado = empleado
       validar = False
  if validar:
    return empleadoEncontrado    
  else:
      return empleadoEncontrado


def registroEmpleados():
  infoDB = traerInfo()
  identificacion = input("numero de identificacion --> ").strip()
  nombre = input("digite el nombre --> ").capitalize().strip()
  cargo = input("digite el cargo --> ").strip()
  try:
    salario = int(input("digite el salario --> "))
  except ValueError:
    print("debe ingresar un numero, vuelve a intentar")
    return
  
  infoDB.append({
    "identificacion": identificacion,
    "nombre": nombre,
    "cargo": cargo,
    "salario": salario,
    "inasistenciasTotal": 0,
    "bonosTotal": 0,
    "inasistenciasInfo": [],
    "bonosInfo": []
  }
  )
  print(infoDB)
  guardarInfo(infoDB)



def registroInasistencias():
  infoDB = traerInfo()
  identificacion = input("numero de identificacion --> ").strip()
  Empleado = buscarEmpleado(infoDB, identificacion)
  if Empleado:
    fecha = input("ingrese la fecha de la inasistencia DD/MM/YYYY --> ")
    if len(fecha) == 10:
      Empleado["inasistenciasTotal"] += 1
      Empleado["inasistenciasInfo"].append(
        {"fecha": fecha}
      )
      guardarInfo(infoDB)
    else:
      print("fecha invalida, intente de nuevo")
  else:
    print("no se encontro un empleado con este numero de indentificacion: ",identificacion)

def registroBonos():
  infoDB = traerInfo()
  identificacion = input("numero de identificacion --> ").strip()
  Empleado = buscarEmpleado(infoDB, identificacion)
  if Empleado:
    fecha = input("ingrese la fecha DD/MM/YYYY --> ")
    if len(fecha) == 10:
      concepto = input("ingrese el concepto --> ")
      valor = int(input("ingrese el valor --> "))      
    
      Empleado["bonosTotal"] += valor
      Empleado["inasistenciasInfo"].append(
        {
          "fecha": fecha,
          "concepto": concepto,
          "valor": valor,
        }
      )
      guardarInfo(infoDB)
    else:
      print("fecha invalida, intente de nuevo")
  else:
    print("no se encontro un empleado con este numero de indentificacion: ",identificacion)


def calcularNomina():
  infoDB = traerInfo()
  for empleado in infoDB:
    nomina = ""
    descuento = (empleado["salario"] * 4) / 100
    valorDia = empleado["salario"] / 30    
    descuentoInasistencia = valorDia * empleado["inasistenciasTotal"]
    salarioPagar = empleado["salario"] + empleado['bonosTotal'] - (descuento * 2) - descuentoInasistencia
    nomina += (f"          nombre: {empleado['nombre']}\n")
    nomina += (f"          identificacion: {empleado['identificacion']}\n")
    nomina += (f"          cargo: {empleado['cargo']}\n")
    nomina += (f"          salario: {empleado['salario']}\n\n")
    nomina += (f"descuento por salud: {descuento}\n")
    nomina += (f"descuento por pension: {descuento}\n")
    if empleado["salario"] < 2000000:
      transporte = empleado["salario"] * 0.1
      nomina += (f"auxilio de transporte: {transporte}\n")
      salarioPagar += transporte
    nomina += (f"descuento por {empleado['inasistenciasTotal']} inasistencias: {descuentoInasistencia}\n")
    nomina += (f"bonos: {empleado['bonosTotal']}\n")
    nomina += (f"salario a pagar: {salarioPagar}\n")
    file = open(f"{empleado['identificacion']}.txt", "w")
    file.write(nomina)
  print("Nominas generadas")
  


  # formatofecha = fecha.split("/")
  #   print(formatofecha[1])