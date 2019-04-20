# person={
# 'name':'Minh',
# 'age':16
# }
# if  'name' in person:
#     print("True")
# else:
#     print ("NOPE")
# if 'nationality' in person:
#     print ("TRUE")
# else:
#     print ("NOPE")
pokedex={
'name':['raichu','Onix']
'description':['raichu has a regional variant that is Electric/Psychic. It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin.','Onix resembles a giant chain of gray boulders that become smaller towards the tail. It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.']


}
a=input("Enter pokemon name:")
if(a==pokedex['name']):
    print(pokedex['description'])