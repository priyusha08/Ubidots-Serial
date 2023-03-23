from ubidots import ApiClient
import serial
serPort = serial.Serial(port='COM6',baudrate=115200,bytesize=8,parity=serial.PARITY_NONE,rtscts=0)
serPort.flush()
serPort.readline()
api = ApiClient(token='token ID')
print ('Connect to Ubidots')
humidity = api.get_variable('ID1')
temperature = api.get_variable('ID2')
light =api.get_variable('ID3')
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

  
