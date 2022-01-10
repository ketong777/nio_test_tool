import os
import sys
import serial
import time


class tbox_control_class():
    time = ""

    def __init__(self, port, username, password):
        self.username = username
        self.password = password
        if not (os.path.exists(os.getcwd() + "\\log\\")):
            os.makedirs(os.getcwd() + "\\log\\")
        try:
            self.s = serial.Serial(port, 115200, timeout=1)
            print("连接成功")
        except Exception as e:
            print("串口错误")

    def login(self):
        with open(os.getcwd() + "\\log\\" + self.time + r".txt", "a") as op:
            op.write("---test case print---\n")
            op.close()
        self.s.write('\n'.encode())
        time.sleep(2)
        self.s.write(('%s\n' % self.username).encode())
        time.sleep(1)
        self.s.write(('%s\n' % self.password).encode())
        time.sleep(3)
        app_output = self.s.readlines()
        output = "\n".join([i.decode().strip() for i in app_output])
        time.sleep(1)
        with open(os.getcwd() + "\\log\\" + self.time + r".txt", "a") as op:
            op.write(str(output))
            op.close()
        self.s.flushOutput()

    def adaptertest_option(self, option):
        self.s.write('adaptertest.app.target\n'.encode())
        time.sleep(1)
        print(option)
        for input_num in option.split(","):
            self.s.write(('%s\n' % input_num).encode())
            time.sleep(1)
        time.sleep(3)
        self.s.write(chr(0X03).encode())
        time.sleep(2)
        app_output = self.s.readlines()
        output = "\n".join([i.decode().strip() for i in app_output])
        time.sleep(1)
        with open(os.getcwd() + "\\log\\" + self.time + r".txt", "a") as op:
            op.write(str(output))
            op.close()
        self.s.flushOutput()

    def s_close(self):
        self.s.write(chr(0X03).encode())
        time.sleep(2)
        self.s.write('exit\n'.encode())
        app_output = self.s.readlines()
        output = "\n".join([i.decode().strip() for i in app_output])
        time.sleep(1)
        with open(os.getcwd() + "\\log\\" + self.time + r".txt", "a") as op:
            op.write(str(output))
            op.close()
        self.s.flushOutput()
        self.s.close()

    def send_command(self, command):
        self.s.write(('%s\n' % command).encode())
        time.sleep(5)
        app_output = self.s.readlines()
        output = "\n".join([i.decode().strip() for i in app_output])
        time.sleep(1)
        with open(os.getcwd() + "\\log\\" + self.time + r".txt", "a") as op:
            op.write(str(output))
            op.close()
        self.s.flushOutput()

    def check_network_pass(self, command):
        self.s.write(('%s\n' % command).encode())
        time.sleep(5)
        self.s.write(chr(0X03).encode())
        time.sleep(1)
        app_output = self.s.readlines()
        output = "\n".join([i.decode().strip() for i in app_output])
        time.sleep(1)
        with open(os.getcwd() + "\\log\\" + self.time + r".txt", "a") as op:
            op.write(str(output))
            op.close()
        self.s.flushOutput()
        if '64 bytes from' in output:
            return True
        else:
            print(output)
            return False

    def check_network_fail(self, command):
        self.s.write(('%s\n' % command).encode())
        time.sleep(5)
        self.s.write(chr(0X03).encode())
        time.sleep(1)
        app_output = self.s.readlines()
        output = "\n".join([i.decode().strip() for i in app_output])
        time.sleep(1)
        with open(os.getcwd() + "\\log\\" + self.time + r".txt", "a") as op:
            op.write(str(output))
            op.close()
        self.s.flushOutput()
        if 'ping: bad address' in str(output) or "ping: sendto: Network is unreachable" in str(output):
            return True
        else:
            print(output)
            return False

    def get_time(self):
        self.s.write('date\n'.encode())
        time.sleep(1)
        app_output = self.s.readlines()
        output = "\n".join([i.decode().strip() for i in app_output])
        time.sleep(1)
        with open(os.getcwd() + "\\log\\" + self.time + r".txt", "a") as op:
            op.write(str(output))
            op.close()
        self.s.flushOutput()
