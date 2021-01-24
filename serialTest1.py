'''
Description: This is python serial port project
Version: 1.0
Autor: Arvin
Date: 2021-01-21 20:55:07
LastEditors: Arvin
LastEditTime: 2021-01-21 21:56:22
'''

import serial
import serial.tools.list_ports

class Communication():
    
    #initial
    def __init__(self, port, bps, timeout=1):
        self.port = port
        self.bps = bps
        self.timeout = timeout
        global Ret
        try:
            #Open serial port and get serial object
            self.main_engine = serial.Serial(self.port, self.bps, timeout=self.timeout)
            if (self.main_engine.is_open):
                Ret = True
        except expression as e:
            print("-----Open Failed----: ", e)

    def Print_Name(self):
        print(self.main_engine.name) #设备名字
        print(self.main_engine.port)#读或者写端口
        print(self.main_engine.baudrate)#波特率
        print(self.main_engine.bytesize)#字节大小
        print(self.main_engine.parity)#校验位
        print(self.main_engine.stopbits)#停止位
        print(self.main_engine.timeout)#读超时设置
        print(self.main_engine.writeTimeout)#写超时
        print(self.main_engine.xonxoff)#软件流控
        print(self.main_engine.rtscts)#软件流控
        print(self.main_engine.dsrdtr)#硬件流控
        print(self.main_engine.interCharTimeout)#字符间隔超时

    #Open serial port
    def Open_Engine(self):
        self.main_engine.open()

    #Close serial port
    def Close_Engine(self):
        self.main_engine.close()
        print(self.main_engine.is_open) #test port whether opened or not
    
    # print available serial port list
    @staticmethod
    def print_Used_Com():
        port_list = list(serial.tools.list_ports.comports())
        print(port_list)

    # 接收指定大小的数据
    # 从串口读size个字节。如果指定超时，则可能在超时后返回较少的字节；如果没有指定超时，则会一直等到收完指定的字节数。
    def Read_Size(self, size):
        return self.main_engine.read(size = size)
    
    # 接收一行数据
    # 使用readline()时应该注意：打开串口时应该指定超时，否则如果串口没有收到新行，则会一直等待。
    # 如果没有超时，readline会报异常。    
    def Read_Line(self):
        return self.main_engine.readline()

    #Send data
    def Send_data(self, data):
        self.main_engine.write(data)

    # 更多示例
    # self.main_engine.write(chr(0x06).encode("utf-8")) # 十六制发送一个数据
    # print(self.main_engine.read().hex()) # # 十六进制的读取读一个字节
    # print(self.main_engine.read())#读一个字节
    # print(self.main_engine.read(10).decode("gbk"))#读十个字节
    # print(self.main_engine.readline().decode("gbk"))#读一行
    # print(self.main_engine.readlines())#读取多行，返回列表，必须匹配超时（timeout)使用
    # print(self.main_engine.in_waiting)#获取输入缓冲区的剩余字节数
    # print(self.main_engine.out_waiting)#获取输出缓冲区的字节数
    # print(self.main_engine.readall())#读取全部字符。
    
    #接收数据
    #一个整型数据占两个字节
    #一个字符占一个字节    

    def Receive_data(self, way):
    # 循环接收数据，此为死循环，可用线程实现
        print("Start to receive data: ")

        while True:
            try:
                if self.main_engine.in_waiting:
                    if(way == 0):
                        for i in range(self.main_engine.in_waiting):
                            print("Receive Ascii data: " + str(self.Read_Size(1)))
                            data1 = self.Read_Size(1).hex() #convert to Hex data
                            data2 = int(data1, 16) 
                            if (data2 == "exit"): # Exit label
                                break
                            else:
                                print("Received Hex data:" + data1 + " Received dec data: " + str(data2))

                    if(way == 1):
                    #整体接收
                    # data = self.main_engine.read(self.main_engine.in_waiting).decode("utf-8")
                        data = self.main_engine.read_all()
                        if (data == "exit"): # Exit label
                            break
                        else:
                            print("Received ASCII data: ", data)

            except expression as e:
                print("Error is: ", e)

# Communication.print_Used_Com()
# Ret = False  # 是否创建成功标志

# Engine1 = Communication("com5", 9600, 1)
# if (Ret):
#     Engine1.Receive_data(0)

if __name__ == "__main__":
    com = Communication("com5", 9600, 1)
    com.Open_Engine()
    