
class a:
    def __init__(self,color):
        self.value = "red"

    def get_value(self):
        return self.value
    
v1=a("red")
v2=v1
print(v2.get_value())
v2.value="blue"
print(v2.get_value())
print(v1.get_value())