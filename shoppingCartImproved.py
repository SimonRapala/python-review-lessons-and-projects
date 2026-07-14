groceryCart = []
groceryList = {
    "produce": [
        {"item": "Bananas", "quantity": 5, "price": 2.50},
        {"item": "Spinach", "quantity": 2, "price": 3.99},
        {"item": "Avocados", "quantity": 3, "price": 1.50}
    ],
    "dairy and eggs": [
        {"item": "Milk", "quantity": 7, "price": 5.49},
        {"item": "Eggs", "quantity": 3, "price": 3.29},
        {"item": "Greek Yogurt", "quantity": 2, "price": 4.99}
    ],
    "meat and protein": [
        {"item": "Chicken Breasts", "quantity": 2, "price": 9.99},
        {"item": "Tofu", "quantity": 2, "price": 2.29},
        {"item": "Turkey", "quantity": 1, "price": 10.99}
    ],
    "pantry staples": [
        {"item": "Quinoa", "quantity": 3, "price": 4.50},
        {"item": "Olive Oil", "quantity": 4, "price": 12.99},
        {"item": "Butter", "quantity": 5, "price": 5.99 }
    ]
}

def normalizeAisleInput(shopperChoice):
    if shopperChoice in ["dairy", "dairy and", "eggs", "and eggs", "dairy and eggs"]:
        return "dairy and eggs"
    elif shopperChoice in ["meat", "meat and", "and protein", "protein", "meat and protein"]:
        return "meat and protein"
    elif shopperChoice in ["pantry", "staples", "pantry staples"]:
        return "pantry staples"
    elif shopperChoice == "produce":
        return "produce"
    else:
        return "No"
    

def purchase(aisle):
    itemName = input("What Do You Want To Buy(q to leave)?").lower().strip()
    if itemName == "q":
        return False

    
    for product in aisle:

        if product["item"].lower() == itemName:
            numberOf = int(input("How many would You Like? "))

            # if numberOf > product.get("quantity"):
            #     print(f"The max is {product.get('quantity')}!")
            # else:
            price = product.get("price")
            cost = price * numberOf
            print(f"Cost Is {cost:.2f}")
            return cost

    print("Item Not Found")
    return False



    


def main():
    shopperName = input("What Is Your Name: ")
    wallet = int(input("How Much Money Do You Have Today:" ))

    firstPass = True
    while True:
        if firstPass is True:
            firstPass = False
            print("Where Would You like To Start Today?")
            aisle = input("Produce | Dairy and Eggs | Meat and Protein | Pantry Staples | (q to leave)\n").lower().strip()

            if aisle == "q":
                break
            else:
                aisle = normalizeAisleInput(aisle)

                if aisle == "No":
                    print("Not A Valid Input!!!")
                    pass
                else:
                    aisleList = groceryList.get(aisle)
                    for item in aisleList:
                        print("-------------",)
                        for attribute in item:
                            print(f"{attribute}: {item.get(attribute)}", end=" ")
                            print("\n-------------")
                        print()

                    purchase(aisleList)



        else:
            print("What Else Would You Like You Look At Today?")
            aisle = input("Produce | Dairy and Eggs | Meat and Protein | Pantry Staples | (q to leave)\n").lower().strip()

            if aisle == "q":
                break
            else:
                aisle = normalizeAisleInput(aisle)

                if aisle == "No":
                    print("Not A Valid Input!!!")
                    pass
                else:
                    aisleList = groceryList.get(aisle)
                    for item in aisleList:
                        print("-------------",)
                        for attribute in item:
                            print(f"{attribute}: {item.get(attribute)}", end=" ")
                            print("\n-------------")
                        print()


if __name__ == "__main__":
    main()