import socket
import ssl

hostname = 'sandbox.api.visa.com'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
    


hostname = 'sandbox.api.visa.com'
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('D:\\Rabbit\\YIGIM\\Work\\Magnet\\Original_Area\\Java_8\\Adapters\\Visa\\certificate\\v2\\original\\cert.crt'.replace("\x0b", "\\"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())