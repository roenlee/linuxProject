'''
Description: 
Version: 1.0
Autor: Arvin
Date: 2021-01-24 20:15:26
LastEditors: Arvin
LastEditTime: 2021-01-24 20:34:26
'''
import serial
import time

try:
    portx = 'COM5'
    bps = 9600
    timex = 5
    ser = serial.Serial(portx, bps, timeout=timex)
    print("串口详情参数：", ser)

    print(ser.baudrate)
    wstr = '王'
    wbyte = wstr.encode('utf-8')
    print(wbyte)
    result = ser.write("Hello".encode('utf-8'))

    time.sleep(1)
    if ser.in_waiting:
        rbyte = ser.read(20)
        print("接收的字节为：", rbyte)
        rstr = rbyte.decode('utf-8')
        print("接收的字符串为：", rstr)
    
    time.sleep(2)
    print("------数据接收完毕------")
    ser.close()

except Exception as e:
    print('Error is % s' % e)