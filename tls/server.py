import ssl, socket

HOST, PORT = '127.0.0.1', 8443
CERT, KEY = 'ssl/cert.pem', 'ssl/key.pem'

# Crear contexto TLS y cargar certificado y clave
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERT, KEY)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    print(f"servidor TLS escuchando en {HOST}:{PORT}")
    conn, addr = sock.accept()
    print(f"conexion de {addr}")
    with context.wrap_socket(conn, server_side=True) as ssock:
        # Recibir mensaje del cliente
        message = ssock.recv(1024).decode('utf-8')
        print(f"mensaje recibido: {message}")
        # Enviar saludo
        ssock.sendall("hello desde seridor".encode('utf-8'))