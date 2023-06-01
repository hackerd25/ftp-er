from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
def ip():
    ip = input("Local computer ip(It is going to crash if it doesnt work): ")
    return ip
def portchecker():
    port = int(input("Give a free ip higher than 1023(If you dont know just write 2121): "))
    if port < 1023 or port > 65535:
        print("Not in the limits.Try again: ")
        portchecker()
    return port
FTP_HOST = ip()
FTP_PORT = portchecker()

FTP_USER = "hackerd25"
FTP_PASSWORD = "2"
FTP_DIRECTORY = "/home/hackerd25/Documents/Visual Studio Code Projects/ftp-er/test"

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "Lets start pwning!"

    address = (FTP_HOST, FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()