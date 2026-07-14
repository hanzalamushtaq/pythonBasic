#Question 05: Cloud Server Configuration (Class vs Instance Attributes)
#Aik Server class banayein jahan class level 
#par provider_name = "AWS" ho aur instance level par
#server ki ip_address ho. Explain karein ke 
#humne provider name ko class level par kyun rakha.

class server:
    provider="AWS"
    def __init__(self,ip):
        self.ip=ip
    def serverDetails(self):
        return f"Provider: {self.provider},Server IP: {self.ip}"
    
s1=server("1.1.1.1")
s2=server("2.2.2.2")
print(s1.serverDetails())
print(s2.serverDetails())