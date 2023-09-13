class Core:
    def insert_food(self, food, file_name):
        with open("products/" + file_name + ".txt", "a") as file:
            file.write(food)

    def remove_food(self, food, file_name):
        with open("products/" + file_name + ".txt", "r") as file:
            lines = file.readlines()
            lines = " ".join(lines).split("\n")

        with open("products/" + file_name + ".txt", "w") as file:
            for line in lines:
                if line.split("|")[0].strip().lower() != food.lower() and line != "":
                    file.write(line.strip() + "\n")

    # def insert_basket(self, basket):
    #     with open("products/baskets.txt", "a") as file:
    #         file.write(basket)

    # def insert_drink(self, drink):
    #     with open("products/drinks.txt", "a") as file:
    #         file.write(drink)

    # def insert_sweat(self, sweat):
    #     with open("products/sweats.txt", "a") as file:
    #         file.write(sweat)

    # def insert_ice_cream(self, ice_cream):
    #     with open("products/ice_creams.txt", "a") as file:
    #         file.write(ice_cream)
