import socket

BUFFER_SIZE = 4096

def tcp_client(host="", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        buffer = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            buffer += data

        if b"TEMPO:" in buffer:
            tempo_info = buffer.split(b"TEMPO:")[-1]
            print("Tempo de transferência TCP calculado pelo servidor: " + tempo_info.decode().strip())

def udp_client(host="", port=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"START", (host, port))
        while True:
            data, _ = s.recvfrom(BUFFER_SIZE)
            if data.startswith(b"TEMPO:"):
                tempo_valor = data.decode().replace("TEMPO:", "").strip()
                print("Tempo de transferência do arquivo em UDP calculado pelo servidor: " + tempo_valor + " segundos")
                break

if __name__ == "__main__":
    print("1 - TCP\n2 - UDP")
    escolha = input("Escolha o protocolo: ")
    if escolha == "1":
        tcp_client()
    else:
        udp_client()
