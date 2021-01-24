'''
Description: Serial Port Loopback Test
Version: 1.0
Autor: Arvin
Date: 2021-01-21 21:46:35
LastEditors: Arvin
LastEditTime: 2021-01-21 22:24:52
'''
import time
import serial
import threading
import random
import serial.tools.list_ports

CODEGLO = 'utf-8'

def GetPort():
    port_list = list(serial.tools.list_ports.comports())
    port_list_0 = []
    if port_list:
        for portobj in port_list:
            port_list_0.append(portobj[0])
        port_serial = port_list_0[0]
        return port_serial
    else:
        print("没有找到串口设备，请检查设备连接是否正确！")

# 打开串口
# 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
# 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
# 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
def OpenPort(portx, bps, timeout):
    ret = False
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timeout)
        #判断是否打开成功
        if ser.is_open:
            ret = True
            return ser, ret
    except Exception as e:
        print("----Open error----: ", e)

# 关闭串口
def ClosePort(ser):
    global ret
    ser.close()
   
    if ser.is_open:
        print("串口关闭失败！")
    else:
        ret = False
        print("串口关闭成功！")

# 写数据
def WritePort(ser, text):
    result = ser.write(text)
    return result

# 读数据
def ReadData(ser):
    time.sleep(0.1) # 防止len_data返回为0

    len_data = ser.inWaiting()
    if len_data:
        rec_data = ser.read(len_data) #读缓冲区数据
        print("接收到的原始数据为：" ,rec_data)
        # rec_str = str(rec_data, encoding='utf-8')
        rec_str_temp = rec_data.decode(CODEGLO)

        rec_str = str(rec_str_temp)
      
        if rec_str != '':
            return rec_str
            print("接收数据: % s " % rec_str)

    else:
        print('接收数据缓冲区为空')


def bytedata(strlength=10):
    random_str = ""
    data_byte = ""
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789!@#$%^&*()-=_+`~/?.>,<'
    length = len(base_str) - 1
    for i in range(strlength):
        random_str += base_str[random.randint(0, length)]

    data_byte = random_str.encode(encoding=CODEGLO)
    
    return data_byte

if __name__ == "__main__":
   
    try:
        portx = GetPort()
        print(portx)

        ser, ret = OpenPort(portx, 9600, None)

        if ret:
            # sdata = bytedata(20)
            str0 = '王'
            
            sdata = str0.encode(encoding=CODEGLO)
            print(sdata)
            count = WritePort(ser, sdata)
            # print("写入的数据是：% s ", sdata)

            rdata = ReadData(ser)
            print('读取的数据：%s' % rdata)
            ClosePort(ser)


    except Exception as e:
        if ret:
            ClosePort(ser)
        print("----异常----：", e)