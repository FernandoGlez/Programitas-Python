""" Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.
"""
import datetime
from datetime import datetime, date, timedelta
Hoy=datetime.now()
dia_nac=int(input("Día de nacimiento: "))
mes_nac=int(input("Mes de nacimiento: "))
year_nac=int(input("Año de nacimiento; "))
fecha_nac=datetime(year_nac,mes_nac,dia_nac)
meses=(int(Hoy.year)-int(fecha_nac.year))*12+int(Hoy.month)-int(fecha_nac.month)
print(meses)