#Este es un ejemplo de condicional compuesto
print("sistemas para calcular el promedio de alumnos")
nombre = input("Danos tu nombre: ")

mate = float(input(nombre + " ¿Cual es tu nota en matematicas?"))
fisi = float(input(nombre + " ¿Cual es tu nota en fisica?"))
quimi = float(input(nombre + " ¿Cual es tu nota en quimica?"))

promedio = (mate + fisi + quimi)/3

if promedio>= 6:
   print('Felicidades '+ nombre + '"aprobastes" con un promedio de: ', promedio)
   print('Felicidades '+ nombre + '"aprobastes" con un promedio de: ', round(promedio,2))
else:
   print("Lo sentimos "+ nombre + " has 'reprobado' con un promedio de: ", promedio)
   print("Lo sentimos "+ nombre + " has 'reprobado' con un promedio de: ", round(promedio,2))

print("FIN")