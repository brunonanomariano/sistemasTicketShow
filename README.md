# sistemasTicketShow
-------------------------------------------
Integrantes
-------------------------------------------
-Mariano Bruno<br>
-Carolina Avellaneda<br>
-Stefania Berger<br>

-------------------------------------------
Definición de aplicación:
-------------------------------------------
Nombre: TicketShow.com<br>

La función principal de la aplicación será poder sacar entradas para diferentes espectáculos.<br>

-------------------------------------------
Funcionalidades y descripción:
-------------------------------------------
-Registrar usuario: registrar un usuario y grabarlo en un archivo para luego validarlo a la hora de iniciar sesión. <br>

-Iniciar sesión usuario: validar que el usuario que quiere comprar este en el archivo de usuarios registrados.<br>

-"Próximos shows": ordenar los shows por fecha de realización.<br>

-Seleccionar un show: mostrar una lista de espectáculos disponibles para comprar.<br>

-Seleccionar tipo de entrada: ubicación [platea, campo, etc.]<br>

-Seleccionar asiento especifico: una vez elegido el tipo de entrada poder elegir una ubicación [columna/fila].<br>

-Acceder a formulario de pago: se colocará CARD, fecha de expiración. código de seguridad, nombre/apellido, dirección. Se deberá validar el formato de cada campo. Por ejemplo: fecha de expiración deberá tener formato fecha AA/MM. <br>

-Guardar datos de compra: show, ubicación, día, horario, precio, nombre/apellido (en un archivo de compras).<br>

-Consultar entradas compradas: leer el archivo de compras y recuperar los datos del usuario que compró la entrada.<br>

-Crear fecha: desde un usuario de administrador crear una nueva función para una banda determinada. <br>


-------------------------------------------
Especificaciones técnicas:
-------------------------------------------

1.	Crear un usuario: El sistema pedirá que se ingrese un email y una contraseña. Se validará el formato del email y los requisitos de la contraseña (una mayúscula, un numero y un carácter especial). Si el email y la contraseña son inválidos, entonces se informa por pantalla y se vuelve a pedir que los ingrese de nuevo. Si los datos son válidos se validará que no exista el usuario en el archivo json. Si existe se vuelve a pedir los datos al usuario. Si no existe entonces se guarda usuario y contraseña en el archivo json. <br>
2.	Iniciar sesión: El sistema pedirá que se ingrese un mail y una contraseña. Se validará el formato del mail. Si el formato es invalido se avisará por pantalla y se pedirá que ingrese un mail valido. Si el formato es válido entonces se procede a buscar el usuario en el archivo Json. Si el usuario no existe entonces se informará por pantalla y se pedirá que ingrese el mail de nuevo. Si existe se validará que la contraseña coincida con la del usuario. Si la contraseña no coincide entonces se informará del error al usuario del error para que la reingrese. Si la contraseña coincide entonces se avanzará a la pantalla principal.<br>
3.	Verificar disponibilidad de show: se verificará cada una de las filas para determinar si hay ubicaciones disponibles y se informara un recuento total de dichas ubicaciones. Por ejemplo, si en la fila 1 hay diez lugares, en la 2 cero lugares y en la 3 cinco lugares, se devolverá que hay 15 lugares disponibles para ese show.<br>
4.	Seleccionar un show al que se quiere asistir: luego de calcular la disponibilidad para cada show, se mostrar por pantalla la fecha y la cantidad de lugares disponibles. El usuario elige una fecha deseada. Si la fecha deseada tiene 0 lugares disponibles se informará que no es posible comprar para esa fecha y se pedirá que elija otra. Si la fecha tiene lugares disponibles, entonces se avanza con la pantalla de selección de ubicaciones.<br>
5.	Aplicar descuentos al total del ticket según un cupón: consultar al usuario si tiene algún cupón de descuento y en caso de que lo tenga validar si el cupón que ingresa se encuentra dentro de la lista de cupones cargadas en el sistema. Si no existe se informara al usuario que el cupón no existe y se volverá a pedir que ingrese el cupón o que avance a la siguiente pantalla y se mostrara las ubicaciones con el precio de cada sector. Si existe se avanzar a la siguiente pantalla y se mostrara las ubicaciones con el precio de cada sector con el descuento aplicado. <br>
6.	Seleccionar una o más ubicaciones disponibles: se mostrará por pantalla las ubicaciones donde “O” significa que el lugar está disponible y “X” que el lugar no esta disponible. Se pedirá al usuario que ingrese la cantidad de entradas a comprar y luego se pedirá que indique que fila y columna desea comprar. Si las coordenadas que selección esta marcada con “X” se informara que no es posible comprar esa ubicación y se le pedirá que ingrese otra. Si la ubicación seleccionada se encuentra en “O” entonces se avanzará se calculará el total de la compra y se avanzara a la siguiente pantalla o se pedirá que ingrese la siguiente entrada (dependiendo de cuantas informó que iba a comprar).
7.	Finalizar compra y guardar información de compra: se mostrará el total de la compra, se pedirá al usuario que ingrese una tarjeta, se verificará que la tarjeta exista en el archivo json de tarjetas. Si la tarjeta no existe se informará al usuario y se pedirá que la ingrese nuevamente. Si la tarjeta existe entonces se recupera la información del saldo. Se valida que el saldo sea suficiente para abonar el tota de la compra. Si el saldo no es suficiente se informará al usuario y se regresará a la pantalla principal. Si se pudo efectuar la compra se informará por pantalla y se guardaran los datos del nombre de usuario, show, ubicaciones y total de la compra en un archivo. <br>
8.	Consultar compras hechas: se busca en el archivo de compras las compras del usuario. Si el usuario no tiene compras se informará por pantalla que no realizo ninguna compra. Si el usuario tiene una o mas compras, se mostrará por pantalla el detalle de las compras realizadas. <br>

-------------------------------------------
Segmentación de responsabilidades:	
-------------------------------------------
Función y responsable:<br>
Registrar_usuario	<br>
Logear_usuario	<br>
Order_show	<br>
Seleccionar_show	<br>
Seleccionar_asiento	<br>
Formulario_de_pago	<br>
Realizar_compra	<br>
Consultar_entradas	<br>
