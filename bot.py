def mostrar_mensaje(lista):
      contador = 1
      for dato in lista:
          print(f"{contador} - {dato}")
          contador+=1

print("Bienvenido. ¿En qué te puedo ayudar?")

print("Cuento con estas funciones: \n")
print("1. Menú")
print("2. Promociones")
print("3. Horario \n")
print("¿Qué opción deseas? (Elige el núm)")

option = int(input())

# mutables = cambian
# inmutables = no cambian
menu  = ["Quesadillas","Torta de Jamón", "Hot Cakes", "Huevo con chorizo", "Spaguetti"]

promociones = ["Martes 2x1", "Viernes de HotCakes", "Lunes de 3x2"]

horario = {

  "Lunes": "9am a 1pm",
  "Martes": "9am a 12pm",
  "Miercoles": "9am a 2pm",
  "Jueves": "9am a 3pm",
  "Viernes": "9am a 1pm",

}

contador = 1

if option == 1:
  print("Elegiste el servicio de Menú")
  mostrar_mensaje(menu)

elif option == 2:
  print("Elegiste el servicio de promociones")
  mostrar_mensaje(promociones)
      
elif option == 3:
  print("Elegiste el servicio de horarios")
  print('Nuestro horario es')

  for dia, horario in horario.items():    
        print(f'{dia} - {horario}')
        
while option<0 or option>3:
    print("No elegiste una opción válida, vuelve a elegirlo.")
    option = int(input())


print("Deseas elegir otra opción?")
option = int(input())