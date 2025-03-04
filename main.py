import random
fish_list = ["Bass", "Sunfish"] #make multi for each location
fish_total = []
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
        s = input("Enter the number for the location you'd like to see the species of:\n1) Lake Okeechobee, Florida, USA\n2) Amazon River, Brazil\n3) Kenai River, Alaska, USA\n4) Great Barrier Reef, Australia\n5) Loch Ness, Scotland\n6) Species List\n")

        if s.strip() == "1":
            for fish in fish_list:
                fish_total.append(fish)
            print(fish_total)
        elif s.strip() == "2":
            print("Test" + str(s))
        elif s.strip() == "3":

            print("Test" + str(s))
        elif s.strip() == "4":
            print("Test" + str(s))
        elif s.strip() == "5":
            print("Test" + str(s))
        elif s.strip() == "6":
            print("Test" + str(s))
        elif s.strip() != "1" or "2" or "3" or "4" or "5" or "6":
            print("Invaild Input\n\n")
            continue
        break

start()