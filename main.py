from modulos.utils import menu, CreacionDB
from modulos.empleados import registroEmpleados, registroInasistencias, registroBonos, calcularNomina

CreacionDB()
while True:
  respuesta = menu()
  match respuesta:
    case "1":
      registroEmpleados()
      input("presione ENTER para continuar")
    case "2":
      registroInasistencias()
      input("presione ENTER para continuar")
    case "3":
      registroBonos()
      input("presione ENTER para continuar")
    case "4":
      calcularNomina()
      input("presione ENTER para continuar")
    case "0":
      print("Saliendo....")
      break
    case _:
      print("Respuesta invalida")