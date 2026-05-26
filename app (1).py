import streamlit as st
import pandas as pd
import xlwings as xw
from io import BytesIO

# =====================
# Google Sheets URLs
# =====================
BASE_CLIENTES = "https://docs.google.com/spreadsheets/d/1W-JK9DkLNsxe-aMJSQHraeNGo7vLkTwi/export?format=xlsx&gid=1899195252"
MAESTRO_USUARIOS = "https://docs.google.com/spreadsheets/d/1wSVF0CU5W_LlsCt2VOsarn3piiQ54Nqk/export?format=xlsx&gid=230232766"

# =====================
# Funciones
# =====================
def cargar_excel(url):
    df = pd.read_excel(url)
    return df

def exportar_excel(df):
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer

def exportar_pdf_desde_excel(buffer_excel, nombre_pdf):
    with open("temp.xlsx", "wb") as f:
        f.write(buffer_excel.read())
    wb = xw.Book("temp.xlsx")
    ws = wb.sheets[0]
    ws.api.ExportAsFixedFormat(0, nombre_pdf)
    wb.close()

# =====================
# Cargar datos
# =====================
df_clientes = cargar_excel(BASE_CLIENTES)
df_usuarios = cargar_excel(MAESTRO_USUARIOS)

# =====================
# Interfaz Streamlit
# =====================
st.title("Sistema de Consulta de Clientes")

usuario = st.text_input("Usuario")
contrasena = st.text_input("Contraseña", type="password")
cliente_input = st.text_input("Cliente")

if st.button("Iniciar sesión"):
    if usuario in df_usuarios['usuario'].values:
        clave_correcta = df_usuarios.loc[df_usuarios['usuario'] == usuario, 'contrasena'].values[0]
        if contrasena == clave_correcta:
            clientes_permitidos = df_usuarios.loc[df_usuarios['usuario']==usuario, 'cliente_permitido'].values
            if cliente_input in clientes_permitidos:
                st.success(f"Login correcto. Cliente válido: {cliente_input}")
                df_filtrado = df_clientes[df_clientes['NOMBRE DEL CLIENTE'] == cliente_input]

                if st.button("Exportar Excel"):
                    buffer_excel = exportar_excel(df_filtrado)
                    st.download_button(
                        label="Descargar Excel",
                        data=buffer_excel,
                        file_name=f"{cliente_input}.xlsx",
                        mime="application/vnd.ms-excel"
                    )

                if st.button("Exportar PDF"):
                    buffer_excel = exportar_excel(df_filtrado)
                    exportar_pdf_desde_excel(buffer_excel, f"{cliente_input}.pdf")
                    with open(f"{cliente_input}.pdf", "rb") as pdf_file:
                        st.download_button(
                            label="Descargar PDF",
                            data=pdf_file,
                            file_name=f"{cliente_input}.pdf",
                            mime="application/pdf"
                        )
            else:
                st.error("Acceso denegado")
        else:
            st.error("Contraseña incorrecta")
    else:
        st.error("Usuario no encontrado")
