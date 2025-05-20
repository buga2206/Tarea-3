import ssl, socket

HOST, PORT = '127.0.0.1', 8443

# Crear contexto de cliente sin validación estricta
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        # Enviar mensaje simple
        ssock.sendall("hello desde cliente".encode('utf-8'))
        # Recibir respuesta
        resp = ssock.recv(1024).decode('utf-8')
        print(f"respuesta del servidor: {resp}")