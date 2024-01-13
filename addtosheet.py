import gspread
from datetime import datetime
from pytz import timezone

def addRow(text):
    #Loguearse con los credenciales
    gc = gspread.service_account(filename='Clave/key.json')
    
    #Abrir la hoja en la pagina 1
    sh = gc.open("Cerveza2024").sheet1

    #Guardar los strings con la fecha y hora
    mad = timezone('Europe/Madrid')
    dt = datetime.now(mad)
    dia = dt.strftime("%d/%m/%Y")
    hora = dt.strftime("%H:%M")

    # Append the formatted date and hour to the target cell
    sh.append_row([dia, hora, text], value_input_option="USER_ENTERED")
