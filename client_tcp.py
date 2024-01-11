from threading import *
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8888))

while True:
    print("Para encerrar, digite: 000 ")
    try:
          
        n1 = int(input('Digite o primeiro numero: '))
        if n1 == 000:
            break
        n2 = int(input('Digite outro número: '))
        
    except ValueError:
        print('Isso tá muito errado, fio, conserta ai.')
        break
        

    n1 = str(n1)

    n2 = str(n2)
    inp = (n1+" " " "+n2)
    print(inp)
    client.send(inp.encode())

    answer = client.recv(1024)
    print(f'A resposta é: '+answer.decode())
client.close()

# Thread1 = Thread(target=thread1)         
# Thread1.start()    

# Thread2 = Thread(target=thread2)
# Thread2.start()