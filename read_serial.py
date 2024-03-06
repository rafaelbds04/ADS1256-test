import serial, time

ser = serial.Serial('COM3', 960000000000)

#ser = serial.Serial('COM13', 9600)

# open a csv file and write the data to it
f = open('data.csv', 'w')
# write the header
# f.write('millis,lat,lng,satellites,hour,minute,second,pressure,temperature,altitude,bmp388_pressure,imu_data_0,imu_data_1,imu_data_2,imu_data_3,imu_data_4,imu_data_5,imu_data_6,imu_data_7,imu_data_8,imu_data_9,imu_data_10,imu_data_11,bmp388_temperature,bmp388_altitude,shunt_voltage,bus_voltage,current,power,total_voltage')

# f.write('millis,alt\n')

time.sleep(6)
ser.write("C\n".encode())

while True:
    line = ser.readline()
    print(line)
    f.write(line.decode('utf-8'))