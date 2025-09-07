En la implementación siguiendo la programación dinamica, la complejidad en el peor caso es de O(V*N), donde V es la cantidad de vuelto que se tiene que dar y N siendo las diferentes denominaciones que el usuario va a elegir

Esto se debe a que en el cálculo principal, que son 2 bucles anidades, se tiene un ciclo for donde se itera desde 1 hasta el valor del vuelto y genera V iteraciones. Luego tenemos que en el bucle interior se iteran todas las denominaciones que el usuario haya elegido, y esto genera N iteraciones. Este cálculo es el que causa el peor caso de complejidad, resultando en una complejidad de O(V*N).


En los otros casos que pueden causar complejidad es cuando se tiene que ordenar las denominaciones, lo cual tiene una complejidad de O(N log N). Otro donde se crea la variable monedas en un ciclo for con las denominaciones, lo cual es una complejidad de O(N).

En conclusión el peor caso para este ejemplo viene del uso de 2 bucles anidados elevando la complejidad a una O(V*N).