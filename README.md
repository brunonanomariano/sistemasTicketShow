# sistemasTicketShow
-------------------------------------------
Definición de aplicación:
-------------------------------------------
Nombre: TicketShow.com
La función principal de la aplicación será poder sacar entradas para diferentes espectáculos.

-------------------------------------------
Funcionalidades y descripción:
-------------------------------------------
Registrar usuario: registrar un usuario y grabarlo en un archivo para luego validarlo a la hora de iniciar sesión. 
Iniciar sesión usuario: validar que el usuario que quiere comprar este en el archivo de usuarios registrados.
"Próximos shows": ordenar los shows por fecha de realización.
Seleccionar un show: mostrar una lista de espectáculos disponibles para comprar.
Seleccionar tipo de entrada: ubicación [platea, campo, etc.]
Seleccionar asiento especifico: una vez elegido el tipo de entrada poder elegir una ubicación [columna/fila].
Acceder a formulario de pago: se colocará CARD, fecha de expiración. código de seguridad, nombre/apellido, dirección. Se deberá validar el formato de cada campo. Por ejemplo: fecha de expiración deberá tener formato fecha AA/MM. 
Guardar datos de compra: show, ubicación, día, horario, precio, nombre/apellido (en un archivo de compras).
Consultar entradas compradas: leer el archivo de compras y recuperar los datos del usuario que compró la entrada.
Crear fecha: desde un usuario de administrador crear una nueva función para una banda determinada


-------------------------------------------
Especificaciones técnicas:
-------------------------------------------
registrar_Usuario: recibe un archivo, pide usuario y contraseña; y lo graba en el archivo y devuelve True o False si pudo grabar.
logear_Usuario: recibe usuario y contraseña, valida si está en el archivo y devuelve True o False si lo encontró.
order_Show: recibe una lista de shows, las ordena por fecha y devuelve la lista ordenada.
seleccionar_Show: recibe una lista y se selecciona una y muestra ubicaciones por pantalla.
seleccionar_asiento: recibe una matriz, pide al usuario que seleccione una ubicación y de estar disponible la reserva.
formulario_de_pago: solicita nombre, apellido, dirección, email, tarjeta, fecha de expiración y código de seguridad, valida los formatos y devuelve True si esta todo bien o False caso contrario.
realizarCompra: recibe los datos de compra, y los graba en un archivo.
consultarEntradas: accede al archivo de compras y muestra las compras de un usuario.

-------------------------------------------
Segmentación de responsabilidades:	
-------------------------------------------
Función y responsable:
Registrar_usuario	
Logear_usuario	
Order_show	
Seleccionar_show	
Seleccionar_asiento	
Formulario_de_pago	
Realizar_compra	
Consultar_entradas	
