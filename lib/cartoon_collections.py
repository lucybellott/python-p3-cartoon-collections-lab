dwarf_names = ["Doc", "Dopey", "Bashful", "Grumpy"]
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
cheese = ["cheddar", "gouda", "camembert"]


def roll_call_dwarves(dwarf_names):
    counter = 1
    for dwarf in dwarf_names:
        print(f"{counter}. {dwarf}")
        counter +=1

def summon_captain_planet(planeteer_calls):
    result=[]
    for planet in planeteer_calls:
       result.append(f"{planet.capitalize()}!")
    return result

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False


def find_the_cheese(foods):
    for food in foods:
        if food in cheese:
            return food
    return None        


#roll_call_dwarves(dwarf_names)

summon_captain_planet(planeteer_calls)
