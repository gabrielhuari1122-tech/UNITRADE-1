# Sistema de Consulta de Clientes - Streamlit

## Descripción
Esta aplicación permite a los usuarios iniciar sesión, consultar la información de un cliente específico y exportar los resultados filtrados a Excel o PDF. La app está diseñada para leer los datos directamente desde Google Sheets, de manera que cualquier cambio realizado en los archivos se refleje automáticamente en la app.

## Archivos principales
- app.py: Código principal de la aplicación Streamlit.
- requirements.txt: Lista de librerías necesarias para ejecutar la app.
- .streamlit/config.toml: Configuración de la interfaz de Streamlit.

## Configuración y ejecución
1. Instalar Python 3.10+ si no está instalado.
2. Instalar las librerías necesarias:
3. Ejecutar la app desde la terminal:
4. La app cargará automáticamente los archivos de Google Sheets para la base de clientes y el maestro de usuarios.

## Uso de la app
1. Ingresar usuario y contraseña.
2. Ingresar el nombre del cliente que se desea consultar.
3. La app validará si el cliente está permitido para el usuario.
4. Una vez validado, se podrán usar los botones para:
- Exportar Excel: Descarga la información filtrada en un archivo Excel.
- Exportar PDF: Genera un PDF con el formato del Excel original.

## Notas importantes
- Los Google Sheets deben ser accesibles públicamente o compartidos con los permisos necesarios.
- La app siempre lee la versión más reciente de los Google Sheets.
- No hay opción de registro de usuarios; todos los usuarios deben estar incluidos en el maestro de usuarios.
- Para generar PDF manteniendo el formato de Excel, se utiliza xlwings.
