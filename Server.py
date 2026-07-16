class Server:
    __i=100
    def __init__(self):
        Server.__i+=1
        self.__ID=f"Server-{Server.__i}"
    def showServer(self):
        return self.__ID
s1=Server()
s2=Server()
s3=Server()
servers=[s1,s2,s3]

for i in servers:
    print(i.showServer())
        