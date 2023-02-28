from ubidots import ApiClient
import serial
serPort = serial.Serial(port='COM6',baudrate=115200,bytesize=8,parity=serial.PARITY_NONE,rtscts=0)
serPort.flush()
serPort.readline()
api = ApiClient(token='BBFF-QMhSr6LbgDVIi7mqxDXhE0qK7FF77k')
print ('Connect to Ubidots')
humidity = api.get_variable('63fd85d15c4d74000ee9165f')
temperature = api.get_variable('63fd85d5beb0bb000ce559aa')
light =api.get_variable('63fd85e0d2b757000cc8d6a9')
while True :
  sensorRead = serPort.readline()
  sensorVar = sensorRead.split()
  if len(sensorVar) >= 3 :         
    humidityvar = float(sensorVar[0])
    tempvar = float(sensorVar[1])
    lt = float(sensorVar[2])
  
  print("Humidity: {0}, Temprature:{1}, Light Intensity : {2}".format(humidityvar, tempvar, lt))
  humidity.save_value({'value':humidityvar})
  temperature.save_value({'value': tempvar})
  light.save_value({'value': lt})