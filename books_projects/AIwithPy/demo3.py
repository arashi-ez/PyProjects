class Book:
    def __init__(self, name, genre, author):
        self.name = name
        self.genre = genre
        self.author = author
        
    def __str__(self):
        return f'{self.name:10} {self.author:10} {self.genre:10}'
    
my_book = Book(name= "Castle", genre="Phylosophyical drama", author="Kafka" )
my_book2 = Book(name= "AI 2041 ", genre = "Educational", author="Kai-Fu Lee")
print(my_book)
print(my_book2)

