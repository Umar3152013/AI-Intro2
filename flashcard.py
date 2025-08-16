class flshcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning = meaning
    def __str__(self):
        return self.word+'( '+self.meaning
flash=[]
print("welcome to flashcard application")

while(True):
    word=input("enter the name you want to add")
    meaning=input("enetr the meanig of the word:")
