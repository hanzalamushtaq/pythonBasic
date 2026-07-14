#Question 08: Streaming Service Track (Parameterized Constructor)
#Ek Song class banayein jahan __init__ constructor 
#ke zariye user naye song ka title aur artist object
#banate waqt hi pass kar sake
class song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def display(self):
        return f"Title: {self.title}, Artist: {self.artist}"
    
s1=song("Believer", "Imagine Dragons")
print(s1.display())