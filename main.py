import socket
import sys

def scan_ports(host, start_port, end_port):

    """
    Scan de portas em um host ou IP que retora uma lista de portas abertas.
    
    Args(Argumentos):
        host (str): Endereço de IP ou Hostname de um destino.
        start_port (int): número inicial de portas a ser analisado.
        end_port (int): Porta final a ser analisada num range específico.

    Returns(Retorno):
        list: Lista de portas abertas num range específico.
    """

    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Timeout for the connection attempt
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Como utilizar: python scan_ports.py <IP> <start_port> <end_port>")
        sys.exit(1)

    ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    open_ports = scan_ports(ip, start_port, end_port)
    if open_ports:
        print(f"Portas abertas no {ip}: {open_ports}")
    else:
        print(f"Não foram encontradas portas abertas no {ip} dentro do range de portas: {start_port}-{end_port}")