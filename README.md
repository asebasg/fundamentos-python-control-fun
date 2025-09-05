# GA1 220501096 01 AA1 EV02 – Fundamentos de Python: estructuras de control y funciones.

## Estructuras en Python: Condicionales, iterativas y funciones

### Condicionales

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

### Iterativas

1. [Bucle For con Frutas](src/iterativas/1.bucle-for-frutas.py).
   Se declara una lista de frutas y se itera sobre ella usando un bucle for para imprimir cada fruta.

2. [Bucle For con Range](src/iterativas/2.bucle-for-range.py).
   Se itera desde 0 hasta 4 usando range(5) en un bucle for para imprimir cada número.

3. [Bucle For con Variaciones de Range](src/iterativas/3.bucle-for-range-variaciones.py).
   Se muestran variaciones del bucle for con range: números del 3 al 7, pares del 2 al 10 y cuenta regresiva del 10 al 1.

4. [Bucle For con Índice de Lista](src/iterativas/4.bucle-for-indice-lista.py).
   Se itera sobre los índices de una lista de nombres usando range(len()) para imprimir posición y nombre.

5. [Bucle For con Cadena](src/iterativas/5.bucle-for-cadena.py).
   Se itera sobre cada carácter de una cadena de texto usando un bucle for para imprimir cada letra.

6. [Bucle For con Diccionario](src/iterativas/6.bucle-for-diccionario.py).
   Se itera sobre las claves de un diccionario para imprimir cada clave y su valor.

7. [List Comprehension](src/iterativas/7.list-comprehension.py).
   Se crean listas usando list comprehension para calcular cuadrados y filtrar números pares.

8. [Bucles Anidados para Matriz](src/iterativas/8.bucles-anidados-matriz.py).
   Se usan bucles anidados para imprimir una matriz de multiplicación 3x3.

9. [Suma de los Primeros Números](src/iterativas/9.suma-primeros-numeros.py).
   Se calcula la suma de los primeros n números usando un bucle for.

10. [Números Primos](src/iterativas/10.numeros-primos.py).
    Se verifica y lista los números primos entre 2 y 19 usando una función y un bucle for.

11. [Temperaturas de la Semana](src/iterativas/11.temperaturas-semana.py).
    Se analiza una lista de temperaturas diarias para encontrar el día más caluroso, calcular el promedio y listar días por encima del promedio.

12. [Bucle While Contador](src/iterativas/12.bucle-while-contador.py).
    Se usa un bucle while para contar del 1 al 5 incrementando un contador.

13. [Bucle While Validación](src/iterativas/13.bucle-while-validacion.py).
    Se utiliza un bucle while para validar entrada de usuario hasta que se introduzca un número.

14. [Adivina el Número](src/iterativas/14.adivina-numero.py).
    Se implementa un juego de adivinanza con bucle while, pistas y límite de intentos.

15. [Simulación de Banco](src/iterativas/15.simulacion-banco.py).
    Se simula gastos bancarios con bucle while, break y continue para controlar el flujo.

16. [Bucle While Infinito](src/iterativas/16.bucle-while-infinito.py).
    Se implementa un bucle while infinito que pregunta al usuario si desea continuar y valida la respuesta.

17. [Factorial con While](src/iterativas/17.factorial-while.py).
    Se calcula el factorial de un número usando un bucle while.

18. [Raíz Cuadrada con While](src/iterativas/18.raiz-cuadrada-while.py).
    Se calcula la raíz cuadrada de un número usando el método de Newton con un bucle while.

19. [Número en Rango con While](src/iterativas/19.numero-rango-while.py).
    Se valida que un número introducido esté dentro de un rango usando un bucle while y manejo de excepciones.

20. [Imprimir Triángulo con While](src/iterativas/20.triangulo-while.py).
    Se imprime un triángulo de asteriscos de altura dada usando un bucle while.

21. [Bucle For con Break](src/iterativas/21.bucle-for-break.py).
    Se usa un bucle for con break para salir cuando se encuentra un número específico.

22. [Buscar Elemento en Lista](src/iterativas/22.buscar-elemento.py).
    Se implementa una función para buscar un elemento en una lista y retornar su índice.

23. [Bucle While con Salir](src/iterativas/23.bucle-while-salir.py).
    Se usa un bucle while infinito con break para salir cuando el usuario escribe 'salir'.

24. [Verificar Número Primo](src/iterativas/24.es-primo.py).
    Se implementa una función para verificar si un número es primo usando un bucle for.

25. [Bucle For con Continue](src/iterativas/25.bucle-for-continue.py).
    Se usa un bucle for con continue para saltar números pares e imprimir solo impares.

26. [Temperaturas Positivas](src/iterativas/26.temperaturas-positivas.py).
    Se filtra y muestra solo las temperaturas positivas de una lista usando continue.

27. [División con Continue](src/iterativas/27.division-continue.py).
    Se omite la división por cero en una lista de números usando continue.

28. [Suma de Valores Válidos](src/iterativas/28.suma-validos.py).
    Se suma solo los valores numéricos de una lista mixta usando continue para ignorar no numéricos.

29. [Suma con Límite](src/iterativas/29.suma-limite.py).
    Se suma números impares hasta un límite, omitiendo múltiplos de 3 y deteniendo si supera el límite.

30. [Bucles Anidados con Continue](src/iterativas/30.bucles-anidados-continue.py).
    Se demuestra continue en bucles anidados, saltando elementos específicos en el bucle interno.

31. [Bucles Anidados con Break](src/iterativas/31.bucles-anidados-break.py).
    Se usa break en bucles anidados con una bandera para salir de ambos bucles cuando se encuentra una condición.

32. [Validación de Contraseña](src/iterativas/32.validacion-contrasena.py).
    Se implementa una función para validar contraseñas con requisitos de longitud y caracteres, usando continue para optimización.

33. [Procesamiento de Transacciones](src/iterativas/33.procesamiento-transacciones.py).
    Se procesa una lista de transacciones bancarias, ignorando las no completadas o con montos inválidos usando continue.

34. [Bucle con Pass](src/iterativas/34.bucle-pass.py).
    Se demuestra el uso de pass en un bucle for para no hacer nada con números pares.

35. [Búsqueda de Primo con Else](src/iterativas/35.busqueda-primo-else.py).
    Se busca un número primo en una lista usando for-else, ejecutando el else si no se encuentra ninguno.

36. [Validar Edades](src/iterativas/36.validar-edades.py).
    Se valida una lista de edades usando for-else, verificando si todas son válidas o si hay alguna inválida.

37. [Buscar Usuario](src/iterativas/37.buscar-usuario.py).
    Se busca un usuario en una lista usando for-else, creando un nuevo perfil si no se encuentra.

38. [Analizar Datos](src/iterativas/38.analizar-datos.py).
    Se analiza una lista de valores con umbral usando for-else y pass para valores normales.

39. [Encontrar Raíz](src/iterativas/39.encontrar-raiz.py).
    Se calcula la raíz cuadrada usando el método de Newton con while-else para verificar convergencia.

40. [Sistema de Validación](src/iterativas/40.sistema-validacion.py).
    Se valida un formulario con campos requeridos y opcionales usando for-else y pass para opcionales.
