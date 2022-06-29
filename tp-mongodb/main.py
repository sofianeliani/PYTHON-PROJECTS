import pymongo
import datetime
import matplotlib.pyplot as plt
client = pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')

db = client['python-tp']
cars = db['cars']
carsModel = cars["modele"]


# # Les listes des abscisses et ordonnées :
modelCarsY = cars.find({}, {"modele": 1})
modelCarsX = cars.find({},{"puissance" : 1})

y = []
x = []

menu_options = {
    1: 'Initialize database with mongoDB',
    2: 'View Graphic Data',
    3: 'View Console Data',
    4: 'Ajpouter un vehicule',
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    col_name = 'cars'
    if col_name in db.list_collection_names():
        print("La collection à déjà été initialisé")
    else:
        mylistCar = [
        { "numero": 1, "modele": "Volvo 960 Kombi aut", "cylindree": 125.00, "puissance": 79.00, "poids": 650.00, "conso":5.00},
        { "numero": 2, "modele": "Daihatsu Cuore", "cylindree": 50.00, "puissance": 60.00, "poids": 1000.00, "conso": 8.00},
        { "numero": 3, "modele": "Suzuki Swift 1.0 GLS", "cylindree": 90.00, "puissance": 70.00, "poids": 750.00, "conso": 7.00},
        { "numero": 4, "modele": "Fiat Panda Mambo L", "cylindree": 123.00, "puissance": 90.00, "poids": 647.00, "conso": 5.18},
        { "numero": 5, "modele": "VW Polo 1.4 60", "cylindree": 65.00, "puissance": 88.00, "poids": 798.00, "conso": 9.00},
        { "numero": 6, "modele": "Opel Corsa 1.2i Eco", "cylindree": 70.00, "puissance": 46.00, "poids": 657.00, "conso": 10.00},
        { "numero": 7, "modele": "Toyota Corolla", "cylindree": 80.00, "puissance": 59.00, "poids": 640.00, "conso": 8.00},
        { "numero": 8, "modele": "Seat Ibiza 2.0 GTI", "cylindree": 135.00, "puissance": 96.00, "poids": 598.00, "conso": 4.00},
        { "numero": 9, "modele": "Mitsubishi Galant", "cylindree": 111.00, "puissance": 124.00, "poids": 980.00, "conso": 2.00},
        { "numero": 10, "modele": "Nissan Primera 2.0", "cylindree": 75.00, "puissance": 111.00, "poids": 579.00, "conso": 7.50},
        ]
        # Init cars in database
        x = cars.insert_many(mylistCar)
        #print list of the cars added to database
        print(x.inserted_ids)

def option2():
    for car in modelCarsY:
        y.append(car['modele'])
        # print(car['modele'])

    for car in modelCarsX:
        x.append(car['puissance'])
        # print(car['puissance'])
    plt.figure(figsize=(10,10))
    plt.plot(x, y,"o")
    plt.show()

def option3():
    for car in modelCarsY:
        y.append(car['modele'])
        # print(car['modele'])

    for car in modelCarsX:
        x.append(car['puissance'])
        # print(car['puissance'])
    print(y)
    print(x)
def option4():
    def add_car(numero, modele, cylindree, puissance, poids, conso):
        document = {
            'numero': numero,
            'modele': modele,
            'cylindree': cylindree,
            'puissance': puissance,
            'poids': poids,
            'conso': conso,
            'Date Added': datetime.datetime.now()
        }
        return cars.insert_one(document)
    add_car(1, "Test add car", 00.00, 00.00, 00.00, 00.00)

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Good job Bernard ;)')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')





















