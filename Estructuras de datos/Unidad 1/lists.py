#Create list of 10
personajes = ["1","2","3","4","5","6","7","8","9","10"]

#delete 3
personajes.pop(1)
personajes.pop(2)
personajes.pop(3)
print(personajes)
#add 5
personajes.append("Personaje owo")
personajes.append("Personaje 2 owo")
personajes.append("Personaje 3 owo")
personajes.append("Personaje 4 owo")
personajes.append("Personaje 5 owo")
print(personajes)
#show 1,5,7,10,2
print(personajes[1])
print(personajes[5])
print(personajes[7])
print(personajes[10])
print(personajes[2])
#Tuple with 10 favorite songs ordered by artists
Tuple = ("Song 1","Song 2","Song 3","Song 4","Song 5","Song 6","Song 7","Song 8","Song 9","Song 10")
#count
print(Tuple.count("Song 2"))
#index
print(Tuple.index("Song 1"))
#Create three sets with the data of your favorite series adding the name of the chapters as value, separated by season
season1 = {"Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5"}
season2 = {"Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5"}
season3 = {"Chapter 1", "Chapter 2.5", "Chapter 3", "Chapter 4", "Chapter 5"}

#Delete the chapters that you didn't like
season1.remove("Chapter 4")
season2.remove("Chapter 4")
#use intersection and issubset
inter = season1.intersection(season2).intersection(season3)
print(inter)
sub = season1.issubset(season2)
print(sub)
#Create a dictionary with 10 video games and producers
games = {"Game1":"owo1",
         "Game2":"owo2",
         "Game3":"owo3",
         "Game4":"owo4",
         "Game5":"owo5",
         "Game6":"owo6",
         "Game7":"owo7",
         "Game8":"owo8",
         "Game9":"owo9",
         "Game10":"owo10"
         }
#Delete 3
games.pop("Game1")
games.pop("Game2")
games.pop("Game3")
print(games)
#Method values and items
games.values()
print(games.items())

