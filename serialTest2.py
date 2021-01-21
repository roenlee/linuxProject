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


STRGLO = ""
BOOL = True

#读数代码本体实现
def ReadData(ser):
    global STRGLO, BOOL
    
    while BOOL:
        if ser.in_waiting:
            RData = ser.read_all(ser.in_waiting).decode("gbk")
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
            threading.Thread(target = ReadData, args=(ser,)).start()
    except Exception as e:
        print("----Open error----: ", e)
    return ser, ret

# 关闭串口
def ClosePort(ser):
    global BOOL
    BOOL = False
    ser.close()

# 写数据
def WritePort(ser, text):
    result = ser.write(text.encode("gbk"))
    return result

# 读数据
def ReadPort():
    global STRGLO
    str = STRGLO
    STRGLO = "" # 清空当次读取
    return str

def strdata(strlength=100):
    random_str = ""
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789!@#$%^&*()'
    length = len(base_str) - 1
    for i in range(strlength):
        strdata += base_str[random.randint(0, length)]
    return strdata

if __name__ == "__main__":
    ser, ret = OpenPort("COM5", 9600, None)
    if(ret == True):
        sdata = strdata()
        count = WritePort(ser, sdata)
        print("写入字节数： ", count)
        # rdata = ReadPort()
        # if sdata == rdata:
        #     print("Loopback Success!")
        #     print("")
        # else: