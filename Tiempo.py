import datetime
t = datetime.datetime.now()
print(t)
#fecha=(t.year).str()+'-'+(t.month).str()
#print('Fecha',fecha)
#print('hour:',t.hour)
fecha=str(t.year)+'-'+str(t.month)+'-'+str(t.day)
hora=str(t.hour)+':'+str(t.minute)+':'+str(t.second)
print(fecha+' '+hora)

