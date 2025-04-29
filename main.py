import random
import time

fish_list_lake_okch = ["Largemouth Bass", "Black Crappie", "Bluegill", "Chain Pickerel", "Bowfin", "Sunshine Bass", "Florida Gar", "Bullhead Catfish", "Albino Channel Catfish"]
fish_list_amazon_river = ["Peacock Bass", "Red-Bellied Piranha", "Black Piranha", "White Piranha", "Arapaima", "Payara (Vampire Fish)", "Piraiba Catfish", "Redtail Catfish", "Jau Catfish", "Electric Eel", "Goliath Catfish", "Golden Dorado"]
fish_list_kenai_river = ["King Salmon", "Sockeye Salmon", "Coho Salmon", "Silver Salmon", "Rainbow Trout", "Dolly Varden", "Steelhead Trout", "White Sturgeon", "Arctic Char"]
fish_list_gb_reef = ["Coral Trout", "Red Emperor Snapper", "Spanish Mackerel", "Black Marlin", "Giant Trevally", "Dogtooth Tuna", "Sailfish", "Mahi-Mahi (Dorado)"]
fish_list_lock_ness = ["Brown Trout", "Atlantic Salmon", "European Eel", "Pike", "Perch", "Sea Trout", "Sturgeon", "Golden Perch (Albino Mutation)"]
fish_caught_count = {}
fish_prob_lake_okch = {
    "Largemouth Bass": 50,
    "Black Crappie": 40,
    "Bluegill": 35,
    "Chain Pickerel": 20,
    "Bowfin": 15,
    "Sunshine Bass": 10,
    "Florida Gar": 8,
    "Bullhead Catfish": 5,
    "Albino Channel Catfish": 1
}

fish_prob_amazon_river = {
    "Peacock Bass": 50,
    "Red-Bellied Piranha": 40,
    "Black Piranha": 35,
    "White Piranha": 30,
    "Arapaima": 15,
    "Payara (Vampire Fish)": 10,
    "Piraiba Catfish": 8,
    "Redtail Catfish": 8,
    "Jau Catfish": 7,
    "Electric Eel": 5,
    "Goliath Catfish": 3,
    "Golden Dorado": 1
}


fish_prob_kenai_river = {
    "King Salmon": 30,
    "Sockeye Salmon": 50,
    "Coho Salmon": 35,
    "Silver Salmon": 35,
    "Rainbow Trout": 40,
    "Dolly Varden": 30,
    "Steelhead Trout": 15,
    "White Sturgeon": 5,
    "Arctic Char": 1
}

fish_prob_gb_reef = {
    "Coral Trout": 50,
    "Red Emperor Snapper": 35,
    "Spanish Mackerel": 40,
    "Black Marlin": 15,
    "Giant Trevally": 25,
    "Dogtooth Tuna": 10,
    "Sailfish": 5,
    "Mahi-Mahi (Dorado)": 2
}

fish_prob_lock_ness = {
    "Brown Trout": 50,
    "Atlantic Salmon": 35,
    "European Eel": 30,
    "Pike": 25,
    "Perch": 40,
    "Sea Trout": 15,
    "Sturgeon": 5,
    "Golden Perch (Albino Mutation)": 1
}

fish_total = ""
def start():
    print("Hello, welcome to The Fishing Game! Please follow the instructions below, and enjoy!")
    while True:
        s = input("Enter the number for the location you'd like to use:\n1) Lake Okeechobee, Florida, USA\n2) Amazon River, Brazil\n3) Kenai River, Alaska, USA\n4) Great Barrier Reef, Australia\n5) Loch Ness, Scotland\n6) Species List\n7) Quit\n")

        if s.strip() == "1":
            lake_okch()
            start2()
        elif s.strip() == "2":
            amazon_river()
            start2()
        elif s.strip() == "3":
            kenai_river()
            start2()
        elif s.strip() == "4":
            gb_reef()
            start2()
        elif s.strip() == "5":
            lock_ness()
            start2()
        elif s.strip() == "6":
            species_list()
        elif s.strip() == "7":
            print("Thank you for playing The Fishing Game. Have a nice day!")
            print("Quitting...")
            break
        elif s.strip() != "1" or "2" or "3" or "4" or "5" or "6" or "7":
            print("Invaild Input\n\n")
            continue
        break

def start2():
    print("Welcome back! Hope you enjoyed fishing at your last location.\nIf you'd like to continue fishing, please use the corresponding numbers to go to the location.\nIf you want to see the species list, please use the corresponding number.\nIf you'd like to stop playing, type 7.")
    while True:
        s = input("Enter the number for the location you'd like to use:\n1) Lake Okeechobee, Florida, USA\n2) Amazon River, Brazil\n3) Kenai River, Alaska, USA\n4) Great Barrier Reef, Australia\n5) Loch Ness, Scotland\n6) Species List\n7) Quit\n")

        if s.strip() == "1":
            lake_okch()
            start2()
        elif s.strip() == "2":
            amazon_river()
            start2()
        elif s.strip() == "3":
            kenai_river()
            start2()
        elif s.strip() == "4":
            gb_reef()
            start2()
        elif s.strip() == "5":
            lock_ness()
            start2()
        elif s.strip() == "6":
            species_list()
        elif s.strip() == "7":
            print("Thank you for playing The Fishing Game. Have a nice day!")
            print("Quitting...")
            break
        elif s.strip() != "1" or "2" or "3" or "4" or "5" or "6" or "7":
            print("Invaild Input\n\n")
            continue
        break

def fishing(location_name, fish_prob):
    print(f"Welcome to {location_name}! Have fun fishing!")
    while True:
        c = input("Type 1 to cast, and 2 to stop fishing! ")
        if c.strip() == "1":
            print("Nice cast! Wait until you see BITE appear, then press enter! Be quick, or you'll miss the fish!")
            time.sleep(random.uniform(2, 7))
            print("\nBITE!")
            start_time = time.time()
            input()
            reaction_time = time.time() - start_time
            if reaction_time < 1.0:
                catch = random.choices(list(fish_prob.keys()), weights=list(fish_prob.values()), k=1)[0]
                prob = fish_prob[catch]
                display_catch_message(catch, prob <= 5)
                fish_caught_count[catch] = fish_caught_count.get(catch, 0) + 1
            else:
                print("You missed the fish.")
        elif c.strip() == "2":
            return
        else:
            print("Improper Input, please try again.\n\n")
            continue

def lake_okch():
    fishing("Lake Okeechobee", fish_prob_lake_okch)

def amazon_river():
    fishing("Amazon River", fish_prob_amazon_river)

def kenai_river():
    fishing("Kenai River", fish_prob_kenai_river)

def gb_reef():
    fishing("Great Barrier Reef", fish_prob_gb_reef)

def lock_ness():
    fishing("Loch Ness", fish_prob_lock_ness)

def species_list():
    global fish_total
    global fish_list
    while True:
        s = input("Enter the number for the location you'd like to see the species of:\n1) Lake Okeechobee, Florida, USA\n2) Amazon River, Brazil\n3) Kenai River, Alaska, USA\n4) Great Barrier Reef, Australia\n5) Loch Ness, Scotland\n")

        if s.strip() == "1":
            print("\nThe species for Lake Okeechobee are: " + ", ".join(fish_list_lake_okch))
            print("\n")
            start()
        elif s.strip() == "2":
            print("\nThe species for the Amazon River are: " + ", ".join(fish_list_amazon_river))
            print("\n")
            start()
        elif s.strip() == "3":
            print("\nThe species for the Kenai River are: " + ", ".join(fish_list_kenai_river))
            print("\n")
            start()
        elif s.strip() == "4":
            print("\nThe species for the Great Barrier Reef are: " + ", ".join(fish_list_gb_reef))
            print("\n")
            start()
        elif s.strip() == "5":
            print("\nThe species for Lock Ness are: " + ", ".join(fish_list_lock_ness))
            print("\n")
            start()
        elif s.strip() != "1" or "2" or "3" or "4" or "5" or "6":
            print("Invaild Input, try again.\n")
            continue
        break

def display_catch_message(fish_name, is_rare):
    if is_rare:
        print(f"Nice Catch! You caught a super rare {fish_name}")
    else:
        print(f"Nice catch! You caught a {fish_name}")

start()