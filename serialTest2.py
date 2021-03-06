'''
Description: 
Version: 1.0
Autor: Arvin
Date: 2021-01-21 21:46:35
LastEditors: Arvin
LastEditTime: 2021-01-21 22:24:52
'''
import serial
import threading
import random
import serial.tools.list_ports

STRGLO = ""
BOOL = True

def GetPort():
    port_list = list(serial.tools.list_ports.comports())
    port_list_0 = []
    if port_list:
        for i in port_list:
            port_list_0.append(i[0])
        port_serial = port_list_0[0]
        return port_serial
    else:
        print("没有找到串口设备，请检查设备连接是否正确！")


#数据读取
def ReadData(ser):
    global STRGLO, BOOL
    
    len_data = ser.in_waiting()
    if len_data:
        STRGLO = ser.read(ser.in_waiting).decode('utf-8')
        print("Rec Data is: ", STRGLO)


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
        if(ser.is_open):
            ret = True
            return ser, ret
    except Exception as e:
        print("----Open error----: ", e)

# 关闭串口
def ClosePort(ser):
    global BOOL
    BOOL = False
    ser.close()

# 写数据
def WritePort(ser, text):
    result = ser.write(text)
    return result

# 读数据
def ReadPort():
    global STRGLO
    str = STRGLO
    STRGLO = "" # 清空当次读取
    return str

def bytedata(strlength=10):
    random_str = ""
    data_byte = ""
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789!@#$%^&*()'
    length = len(base_str) - 1
    for i in range(strlength):
        random_str += base_str[random.randint(0, length)]
    data_byte = random_str.encode(encoding='utf-8')
    return data_byte

if __name__ == "__main__":
    try:
        portx = GetPort()
        print(portx)

        ser, ret = OpenPort(portx, 9600, None)

        if(ret == True):
            sdata = bytedata(20)
            count = WritePort(ser, sdata)
            print("写入字节数： ", count)

    except Exception as e:
        print("串口调试失败！")