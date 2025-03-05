import random

fish_list_lake_okch = ["Largemouth Bass", "Black Crappie", "Bluegill", "Chain Pickerel", "Bowfin", "Sunshine Bass", "Florida Gar", "Bullhead Catfish", "Albino Channel Catfish"]
fish_list_amazon_river = ["Peacock Bass", "Red-Bellied Piranha", "Black Piranha", "White Piranha", "Arapaima", "Payara (Vampire Fish)", "Piraiba Catfish", "Redtail Catfish", "Jau Catfish", "Electric Eel", "Goliath Catfish", "Golden Dorado"]
fish_list_kenai_river = ["King Salmon", "Sockeye Salmon", "Coho Salmon", "Silver Salmon", "Rainbow Trout", "Dolly Varden", "Steelhead Trout", "White Sturgeon", "Arctic Char"]
fish_list_gb_reef = ["Coral Trout", "Red Emperor Snapper", "Spanish Mackerel", "Black Marlin", "Giant Trevally", "Dogtooth Tuna", "Sailfish", "Mahi-Mahi (Dorado)"]
fish_list_lock_ness = ["Brown Trout", "Atlantic Salmon", "European Eel", "Pike", "Perch", "Sea Trout", "Sturgeon", "Golden Perch (Albino Mutation)"]
#below is test, global all values on the top
fish_prob_lake_okch = {
    "Largemouth Bass": 50,
    "Black Crappie": 30,
    "Bluegill": 15,
    "Chain Pickerel": 4,
    "Albino Channel Catfish": 1
}

fish_total = ""
def start():
    print("Hello, welcome to Fishing! Please follow the instructions below, and enjoy!")
    while True:
        s = input("Enter the number for the location you'd like to use:\n1) Lake Okeechobee, Florida, USA\n2) Amazon River, Brazil\n3) Kenai River, Alaska, USA\n4) Great Barrier Reef, Australia\n5) Loch Ness, Scotland\n6) Species List\n")

        if s.strip() == "1":
            #lake_okch()
            print("Test" + str(s))
        elif s.strip() == "2":
            #amazon_river()
            print("Test" + str(s))
        elif s.strip() == "3":
            #kenai_river()
            print("Test" + str(s))
        elif s.strip() == "4":
            #gb_reef()
            print("Test" + str(s))
        elif s.strip() == "5":
            #lock_ness()
            print("Test" + str(s))
        elif s.strip() == "6":
            species_list()
        elif s.strip() != "1" or "2" or "3" or "4" or "5" or "6":
            print("Invaild Input\n\n")
            continue
        break

def species_list():
    global fish_total
    global fish_list
    while True:
        s = input("Enter the number for the location you'd like to see the species of:\n1) Lake Okeechobee, Florida, USA\n2) Amazon River, Brazil\n3) Kenai River, Alaska, USA\n4) Great Barrier Reef, Australia\n5) Loch Ness, Scotland\n")

        if s.strip() == "1":
            print("The species for Lake Okeechobee are: " + ", ".join(fish_list_lake_okch))
        elif s.strip() == "2":
            print("The species for the Amazon River are: " + ", ".join(fish_list_amazon_river))
        elif s.strip() == "3":
            print("The species for the Kenai River are: " + ", ".join(fish_list_kenai_river))
        elif s.strip() == "4":
            print("The species for the Great Barrier Reef are: " + ", ".join(fish_list_gb_reef))
        elif s.strip() == "5":
            print("The species for Lock Ness are: " + ", ".join(fish_list_lock_ness))
        elif s.strip() != "1" or "2" or "3" or "4" or "5" or "6":
            print("Invaild Input\n\n")
            continue
        break

start()