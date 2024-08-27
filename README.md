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
Registrar usuario: registrar un usuario y grabarlo en un archivo para luego validarlo a la hora de iniciar sesión. <br>
Iniciar sesión usuario: validar que el usuario que quiere comprar este en el archivo de usuarios registrados.<br>
"Próximos shows": ordenar los shows por fecha de realización.<br>
Seleccionar un show: mostrar una lista de espectáculos disponibles para comprar.<br>
Seleccionar tipo de entrada: ubicación [platea, campo, etc.]<br>
Seleccionar asiento especifico: una vez elegido el tipo de entrada poder elegir una ubicación [columna/fila].<br>
Acceder a formulario de pago: se colocará CARD, fecha de expiración. código de seguridad, nombre/apellido, dirección. Se deberá validar el formato de cada campo. Por ejemplo: fecha de expiración deberá tener formato fecha AA/MM. <br>
Guardar datos de compra: show, ubicación, día, horario, precio, nombre/apellido (en un archivo de compras).<br>
Consultar entradas compradas: leer el archivo de compras y recuperar los datos del usuario que compró la entrada.<br>
Crear fecha: desde un usuario de administrador crear una nueva función para una banda determinada. <br>


-------------------------------------------
Especificaciones técnicas:
-------------------------------------------
registrar_Usuario: recibe un archivo, pide usuario y contraseña; y lo graba en el archivo y devuelve True o False si pudo grabar. <br>
logear_Usuario: recibe usuario y contraseña, valida si está en el archivo y devuelve True o False si lo encontró.<br>
order_Show: recibe una lista de shows, las ordena por fecha y devuelve la lista ordenada. <br>
seleccionar_Show: recibe una lista y se selecciona una y muestra ubicaciones por pantalla.<br>
seleccionar_asiento: recibe una matriz, pide al usuario que seleccione una ubicación y de estar disponible la reserva.<br>
formulario_de_pago: solicita nombre, apellido, dirección, email, tarjeta, fecha de expiración y código de seguridad, valida los formatos y devuelve True si esta todo bien o False caso contrario.<br>
realizarCompra: recibe los datos de compra, y los graba en un archivo.<br>
consultarEntradas: accede al archivo de compras y muestra las compras de un usuario.<br>

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
