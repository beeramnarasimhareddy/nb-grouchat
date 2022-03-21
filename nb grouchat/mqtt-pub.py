import paho.mqtt.client as mqtt

pub_clint=mqtt.Client()
pub_clint.connect('broker.hivemq.com',1883)
print('broker Connected')

pub_clint.publish('gpcet/iot','jai balaya ncs chowdary....')