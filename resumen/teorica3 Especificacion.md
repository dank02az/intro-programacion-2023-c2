
# Especificacion

Es un **contrato** entre el programador de una funcion y el usuario de esa funcion.
Describe **cual es el problema** y que **propiedades** deberian tener sus soluciones.

1.  Decribe el **que**.
2.  **No** describe el como.

#### ¿Por qué escribir la especificación del problema?

- Nos ayuda a entender mejor el problema
- Nos ayuda a construir el programa
- Nos ayuda a prevenir errores: (testing y verificacion)


### Partes de una especificacion

* <u>**pre-condicion**</u>:  Es el **requiere** de la especificacion,
 __condiciona__ a los **parametros de entrada** de una funcion.

* <u>**post-condicion**</u>: Es el **asegura** de la especificacion, 
__condiciona__ los __valores de salida__ en funcion de los valores de entrada.

Los parametros de entrada manejan diferentes **Tipos de datos** y **Clases de Datos**:

### Tipos de datos 

Es un **conjunto de valores** provisto de una serie de operaciones para esos valores.

Ejemplos :

- Tipo
  * __Integer__  :: { suma, resta, division...etc }
  * __Floating__ :: { suma, resta ...etc }
  * __Boolean__ :: { tabla de verdad...}



#

Los tipos que se manejan en la materia son:

+ Basicos:
  - Reales
  - Enteros
  - Booleans
  - Chars
+ Enumerados
+ Uplas 
+ Secuencias

#

### Uplas vs Secuencias

* _**Uplas**_ : Las uplas pueden tener **multiples tipo de datos**.

* _**Secuencias**_ : Solo manejan **un solo tipo de Dato**

#

### Problema con la Especificacion

- ##### <u>Sobre-Especificar</u>: 
Proporsiona __demasiada informacion__ a la especificacion y vuelve la solucion al problema mas complejo de los deberia ser. 
  1.  Tiene un __requiere muy laxo__ o bien un __asegura muy restrictivo.__

- ##### <u>Subespecificar</u>: 
No Proporsiona __suficiente informacion__ a la especificacion y vuelve la solucion del problema mas ambigua y menos clara de entender
   1. Tiene un __requiere muy restrictivo__ o bien un __asegura muy permisivo__.




















