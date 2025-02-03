class Cat:
    Name_Class = "Cats"
    def __init__(self, wool_color, eyes_color, name):
        self.wool_color = wool_color
        self.eyes_color = eyes_color
        self.name = name

    def purr(self):
        print("Meoww")

    def hiss(self):
        print("Ssssss")

    def scrabble(self):
        print("scraaaatch")

my_cat = Cat('Gray', 'Green', 'Tom') 
my_cat2 = Cat('White', 'blue', 'Joffrey') 

print(my_cat.name, my_cat.scrabble())
print(f"My cat's nick is: {my_cat.name}.")
print(f'My cat is color of: {my_cat.wool_color}.')
print(f'My cat eyes color is: {my_cat.eyes_color}.')
# my_cat2.purr()
Cat.purr(my_cat)

