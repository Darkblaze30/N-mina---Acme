def menu():
  print("""
      (1) Registro de empleados
      (2) Registro de inansistencias
      (3) Registro de bonos extra-legales
      (4) Calculo nomina
      (0) Salir
""")
  respuesta = input("     que desea hacer ")
  return respuesta

def CreacionDB():
  try:
    file = open("empleadosDB.json", "r")
    file.close
    return file
  except FileNotFoundError:
    file = open("empleadosDB.json", "w")
    file.write("[]")
    file.close
