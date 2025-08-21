a = 5 # Se declara la variable a con valor 5
b = 10 # Se declara la variable b con valor 10
c = 15 # Se declara la variable c con valor 15

mayor = a # Se asume que a es el mayor inicialmente

if b > mayor: # Verifica si b es mayor que el valor actual de mayor
    mayor = b # Si b es mayor, actualiza mayor con el valor de b

if c > mayor: # Verifica si c es mayor que el valor actual de mayor
    mayor = c # Si c es mayor, actualiza mayor con el valor de c

print(f'El número mayor es {mayor}.') # Imprime el número mayor encontrado
