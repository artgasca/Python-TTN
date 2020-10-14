#Script para graficar datos de temperatura y humedad 
#conectandose a TTN

#imports para TTN
import time
import ttn


#Cuenta TTN
app_id = "tuna-ubidots"
access_key = "ttn-account-v2.nkjCQGuDsek3gZtcvXSQyen0__tenq7Ex53uvvWWqX4"

## imports para graficar
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

#Bandera para graficar dato nuevo
ready =False
#listas con datos para graficar
x,h,t = [],[],[]
#index auxiliar para contar en eje x
index = 0



#funcion para graficar
def animate(i):
    global ready
    #se revisa la bandera ready, que se pone en True cuando llega dato nuevo
    if ready:
        ready = False
        print('plotting update')        
        plt.cla()
        plt.plot(x,t,label='Temperatura')        
        plt.plot(x,h,label='Humedad')        
        plt.legend(loc='upper left')
        plt.legend()
        plt.tight_layout()
        
        
    else:
        print('waiting for new data')




def uplink_callback(msg,client):
    print("Uplink recibido de: ",msg.dev_id)
    print(msg)    
    global ready    
    ready = True
    global index    
    t.append(msg.payload_fields.temperature)
    h.append(msg.payload_fields.humidity)
    x.append(index)
    index = index+1

    

    
#manejador del cliente TTN    
handler = ttn.HandlerClient(app_id,access_key)

#usando cliente mqtt
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(3)


#funcion de animacion en grafica
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

#configuracion de la grafica
plt.tight_layout()
plt.xlabel('Timestamp')
plt.ylabel('Valor')
plt.title('LoRaWAN Demo')
plt.show()
print('Running')


try:
    while True:
       time.sleep(1)

except KeyboardInterrupt:
    pass