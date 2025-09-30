import socket

BUFFER_SIZE = 4096

def tcp_client(host="", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            if data.startswith(b"TEMPO: "):
                print(data.decode())

def udp_client(host="", port=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"START", (host, port))
        while True:
            data, _ = s.recvfrom(BUFFER_SIZE)
            if data.startswith(b"TEMPO:"):
                print(data.decode())
                break

if __name__ == "__main__":
    print("1 - TCP\n2 - UDP")
    escolha = input("Escolha o protocolo: ")
    if escolha == "1":
        tcp_client()
    else:
        udp_client()
