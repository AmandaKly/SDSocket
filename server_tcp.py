import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(3)
print("Servidor iniciado")
print("Aguardando requisição do cliente..")

connection, address = server.accept()
print("cliente conectado :", address)
msg = ''

while True:
    data = connection.recv(1024)
    msg = data.decode()

    print("Equação recebida")
    resultado = 0
    listaOperacao = msg.split()
    if listaOperacao == []:
        break
    print(listaOperacao)
    operacao1 = listaOperacao[0]
    operacao2 = listaOperacao[1]
    n1 = int(operacao1)
    n2 = int(operacao2)

    resultado = n1 + n2

    print("Enviando resultado para cliente")
    output = str(resultado)
    connection.send(output.encode())
connection.close()
