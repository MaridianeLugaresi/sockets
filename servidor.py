import socket
import time
import threading

BUFFER_SIZE = 4096
FILE_NAME = "file_example_MP4_1920_18MG.mp4"

def tcp_server(host="", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"[TCP] Servidor ouvindo em {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[TCP] Conexão de {addr}")
                with open(FILE_NAME, "rb") as f:
                    start = time.time()
                    while chunk := f.read(BUFFER_SIZE):
                        conn.sendall(chunk)
                    end = time.time()

                tempo = end - start
                conn.sendall(f"\nTEMPO: {tempo}".encode())
                print(f"[TCP] Arquivo enviado em {tempo}s")

def udp_server(host="", port=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"[UDP] Servidor ouvindo em {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            if data.decode() == "START":
                with open(FILE_NAME, "rb") as f:
                    start = time.time()
                    seq = 0
                    while chunk := f.read(BUFFER_SIZE):
                        header = f"{seq:010d}".encode()
                        s.sendto(header + chunk, addr)
                        seq += 1
                    end = time.time()

                tempo = end - start
                s.sendto(f"TEMPO: {tempo}".encode(), addr)
                print(f"[UDP] Arquivo enviado em {tempo}s para {addr}")

if __name__ == "__main__":
    threading.Thread(target=tcp_server, daemon=True).start()
    threading.Thread(target=udp_server, daemon=True).start()

    print("[SERVIDOR] Aguardando conexões TCP e UDP...")
    while True:
        time.sleep(1)