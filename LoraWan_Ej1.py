import time
import ttn

app_id = "tuna-ubidots"
access_key = "ttn-account-v2.nkjCQGuDsek3gZtcvXSQyen0__tenq7Ex53uvvWWqX4"




def uplink_callback(msg,client):
    print("Uplink recibido de: ",msg.dev_id)
    print(msg)


   


handler = ttn.HandlerClient(app_id,access_key)

#usando cliente mqtt

mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
#time.sleep(60)

try:
    while True:
        time.sleep(1)        
except KeyboardInterrupt:
    pass