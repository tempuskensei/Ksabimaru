#Hello to the first rendering of the time machine/memory device whatever you want to call it. This will allow me to collect my thoughts in a creative way while using python
x = 17
run = 10
def write(memory_input, date):
    with open("MEMORY.txt", "a") as f:
        f.write(date + ": " + memory_input)
        f.write(" \n")


def delete():
    with open("MEMORY.txt", "w") as f:
        f.write("")

def read(find_date):
    with open(r"MEMORY.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            
            if find_date in line:
                
                print(line)
                










print("""
 _        _______  _______  ______  _________ _______  _______  _______          
| \    /\(  ____ \(  ___  )(  ___ \ \__   __/(       )(  ___  )(  ____ )|\     /|
|  \  / /| (    \/| (   ) || (   ) )   ) (   | () () || (   ) || (    )|| )   ( |
|  (_/ / | (_____ | (___) || (__/ /    | |   | || || || (___) || (____)|| |   | |
|   _ (  (_____  )|  ___  ||  __ (     | |   | |(_)| ||  ___  ||     __)| |   | |
|  ( \ \       ) || (   ) || (  \ \    | |   | |   | || (   ) || (\ (   | |   | |
|  /  \ \/\____) || )   ( || )___) )___) (___| )   ( || )   ( || ) \ \__| (___) |
|_/    \/\_______)|/     \||/ \___/ \_______/|/     \||/     \||/   \__/(_______)
                                                                                 
""")
print("Welcome to the first iteration of KSUBAMIRAU V 1.0\n")

print("To write any data for the database, press 1.\n")
print("To find data for a specific date, press 2.\n")
print("To exit the program, press 3.\n")
print("To create the database file(for first-time-setup), press 4. You wont have to repeat this each time you start the program\n")


while run == 10:
    first_req = int(input("\nEnter your keyword request: "))

    if first_req == 0:
        delete()
        print("\nFactum, Vale")
        run = 9
        break
    
    if first_req == 3:
        print("\nVale")
        run = 9
        break


    if first_req == 2:
        find_date = input("\nEnter the date of said data and we shall try to find any traces: ")
        read(find_date)
        break

    if first_req == 5:
        f = open("myfile.txt", "x")


    elif first_req != int:
        print("\nPlease select a suitable input next time. Vale")
        run = 9
    else:
        print("\nPlease select a suitable input next time. Vale")
        run = 9
        break

    date = input("\nEnter the date in a xx/yy/zz format: ")
    
    while first_req == 1:
        memory_input = input("\nEnter a single item you want to engrave. Dont worry you can repeat this process as much as you like: ")
        write(memory_input, date)
        if input("\nSuccess! if you want to input something else as well, press y or if you want to quit press n: ") == "y":
           first_req = 1 
        else:
            first_req = 9000


