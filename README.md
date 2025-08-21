# Estructuras en Python: Condicionales, iterativas y funciones

## Condicionales

Condicionales if - else, if - elif - else, match - case y operadores ternarios. Cada ejercicio tendra una explicacion.

1. [Verificacion de edad](src/condicionales/1.verificacion-edad.py).
   Se declara una variable `edad` y se le asinga un valor, luego se aplica el condicional (mayor o igual a 18) para luego mostrar la respuesta.

2. [Temperatura](src/condicionales/2.temperatura.py).
   Se declara la variable `edad`, posteriormente se le asigna un valor. Luego se hace el condicional de si es mayor a 25 muestra como resultado que hace calor.

3. [Hora](src/condicionales/3.hora.py).
   Se declara la variable `hora` y en ella se inserta la hora deseada. Luego en un condicional con operador `and` se valida si es entre las 6 o 12 para posteriormente imprimir el mensaje de "Buenos dias".

4. [Votacion](src/condicionales/4.votacion.py).
   Se declara la variable `edad` con valor 17, luego se aplica un condicional if-else para verificar si la edad es mayor o igual a 18 y mostrar el mensaje correspondiente sobre la capacidad de votar.

5. [Contraseña](src/condicionales/5.contrasena.py).
   Se solicita al usuario que introduzca una contraseña y se verifica si es igual a "secreta123" para conceder o denegar el acceso.

6. [Par o Impar](src/condicionales/6.par-impar.py).
   Se declara un número y se verifica si es par o impar usando el operador módulo (%).

7. [Retiro Bancario](src/condicionales/7.retiro-bancario.py).
   Se simula un retiro bancario verificando si el saldo es suficiente para el monto solicitado.

8. [Signo del Número](src/condicionales/8.signo-numero.py).
   Se determina si un número es positivo, negativo o cero usando condicionales if-elif-else.

9. [Calificaciones](src/condicionales/9.calificaciones.py).
   Se asigna una calificación basada en el rango de la nota usando múltiples condiciones elif.

10. [Grupos de Edad](src/condicionales/10.grupos-edad.py).
    Se clasifica a una persona en grupos de edad (menor, adulto, mayor) usando condiciones con operadores de comparación.

11. [Colores](src/condicionales/11.colores.py).
    Se verifica el valor de una variable color usando condicionales if-elif para determinar y mostrar el color.

12. [Frutas con Match](src/condicionales/12.frutas-match.py).
    Se utiliza estructura match-case para identificar frutas introducidas por el usuario.

13. [Puntos y Coordenadas](src/condicionales/13.puntos-coordenadas.py).
    Se analizan coordenadas de puntos usando pattern matching con tuplas.

14. [Edad con Match](src/condicionales/14.edad-match.py).
    Se clasifican grupos de edad usando match-case con condiciones de guardia.

15. [Usuarios y Roles](src/condicionales/15.usuarios-roles.py).
    Se procesa una lista de usuarios y sus roles usando match-case con diccionarios.

16. [Listas con Match](src/condicionales/16.listas-match.py).
    Se analizan patrones en listas usando match-case con diferentes estructuras de listas.

17. [Crédito con Operador AND](src/condicionales/17.credito-operador-and.py).
    Se verifica elegibilidad para crédito usando el operador lógico AND.

18. [Fin de Semana con Operador OR](src/condicionales/18.fin-semana-operador-or.py).
    Se determina si es fin de semana usando el operador lógico OR.

19. [Parque con Operador NOT](src/condicionales/19.parque-operador-not.py).
    Se decide si se puede salir al parque usando el operador lógico NOT.

20. [Licencia de Conducir](src/condicionales/20.licencia-conducir.py).
    Se verifican requisitos para licencia de conducir usando operadores lógicos combinados.

21. [Precedencia de Operadores 1](src/condicionales/21.precedencia-operadores-1.py).
    Se demuestra la precedencia de operadores lógicos (AND tiene mayor precedencia que OR).

22. [Precedencia de Operadores 2](src/condicionales/22.precedencia-operadores-2.py).
    Se muestra el uso de paréntesis para cambiar la precedencia de operadores lógicos.

23. [Condicionales Anidados 1](src/condicionales/23.condicionales-anidados-1.py).
    Se implementa verificación de acceso con condicionales if anidados.

24. [Condicionales Anidados 2](src/condicionales/24.condicionales-anidados-2.py).
    Se muestra una alternativa a los condicionales anidados usando operador AND.

25. [Condicionales Anidados 3](src/condicionales/25.condicionales-anidados-3.py).
    Se implementa clasificación por edad y estado civil usando condicionales anidados.

26. [Licencia Anidada 1](src/condicionales/26.licencia-anidada-1.py).
    Se verifica elegibilidad para licencia de conducir usando condicionales if anidados múltiples.

27. [Licencia Anidada 2](src/condicionales/27.licencia-anidada-2.py).
    Se muestra una alternativa al ejercicio 26 usando operadores lógicos con elif.

28. [Acceso Anidado](src/condicionales/28.acceso-anidado.py).
    Se implementa verificación de acceso con usuario y contraseña usando condicionales anidados.

29. [Mayor de Tres Números 1](src/condicionales/29.mayor-tres-numeros-1.py).
    Se encuentra el mayor de tres números usando condicionales if anidados complejos.

30. [Mayor de Tres Números 2](src/condicionales/30.mayor-tres-numeros-2.py).
    Se muestra un enfoque alternativo para encontrar el mayor de tres números usando variable temporal.

31. [Operador Ternario 1](src/condicionales/31.operador-ternario-1.py).
    Se introduce el operador ternario básico para verificación de edad en una sola línea.

32. [Operador Ternario 2](src/condicionales/32.operador-ternario-2.py).
    Se usa operador ternario dentro de la función print para encontrar el máximo de dos números.

33. [Operador Ternario 3](src/condicionales/33.operador-ternario-3.py).
    Se implementa operador ternario anidado para clasificación por categorías de edad.

34. [Operador Ternario 4](src/condicionales/34.operador-ternario-4.py).
    Se combina operador ternario con list comprehension para clasificar números como par/impar.

35. [Operador Ternario 5](src/condicionales/35.operador-ternario-5.py).
    Se usa operador ternario para evitar división por cero y manejar errores.

36. [Cortocircuito AND](src/condicionales/36.cortocircuito-and.py).
    Se demuestra evaluación de cortocircuito con operador AND en listas vacías.

37. [Cortocircuito División](src/condicionales/37.cortocircuito-division.py).
    Se muestra cómo el cortocircuito evita división por cero en condiciones.

38. [Cortocircuito OR](src/condicionales/38.cortocircuito-or.py).
    Se ilustra evaluación de cortocircuito con operador OR para control de acceso.

39. [Cortocircuito Anidado](src/condicionales/39.cortocircuito-anidado.py).
    Se implementa lógica de cortocircuito usando condicionales anidados.

40. [Función Any](src/condicionales/40.funcion-any.py).
    Se utiliza la función any() para verificar si algún elemento de una lista es verdadero.

41. [Función All](src/condicionales/41.funcion-all.py).
    Se utiliza la función all() para verificar si todos los elementos de una lista son verdaderos.
