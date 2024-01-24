import socket
import ssl

HOSTNAME = 'python.org'

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.minimum_version = ssl.TLSVersion.TLSv1_2
ctx.maximum_version = ssl.TLSVersion.TLSv1_3 #TLSv1_3
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.load_default_certs()
ctx.check_hostname = True

# ctx = ssl.create_default_context()

sock = socket.create_connection((HOSTNAME, 443))

ssock = ctx.wrap_socket(sock, server_hostname=HOSTNAME)

print(ssock.cipher())
print(ssock.version())