class Zoo:
    def __init__(self, visitors_per_year=0, name="", number_of_animals=0, budget=0):
        self.__visitors_per_year = visitors_per_year  
        self.__name = name                             
        self.__number_of_animals = number_of_animals   
        self.__budget = budget                         

        
        self.public_integer = 0  
        self.public_string = ""  

    
    def get_visitors_per_year(self):
        return self.__visitors_per_year

    def get_name(self):
        return self.__name

    def get_number_of_animals(self):
        return self.__number_of_animals

    def get_budget(self):
        return self.__budget

    def set_budget(self, amount):
        if amount >= 0:
            self.__budget -= amount  
        else:
            print("Сума повинна бути позитивною")

    def set_visitors_per_year(self, visitors):
        self.__visitors_per_year = visitors

    def set_name(self, name):
        self.__name = name

    def set_number_of_animals(self, number):
        self.__number_of_animals = number

    def __str__(self):
        return f"Zoo(name={self.__name}, visitors_per_year={self.__visitors_per_year}, number_of_animals={self.__number_of_animals}, budget={self.__budget})"

    def __repr__(self):
        return f"Zoo({self.__visitors_per_year}, '{self.__name}', {self.__number_of_animals}, {self.__budget})"

    def __del__(self):
        print(f"Zoo {self.__name} is being deleted.")


def find_zoo_with_max_budget(zoos):
    if not zoos:
        return None  
    
    max_budget_zoo = zoos[0]
    for zoo in zoos[1:]:  
        if zoo.get_budget() > max_budget_zoo.get_budget():
            max_budget_zoo = zoo
    return max_budget_zoo

def main():
    zoo1 = Zoo(50000, "City Zoo", 150, 100000)
    zoo2 = Zoo(30000, "Wildlife Park", 80, 150000)
    zoo3 = Zoo(60000, "Safari Zoo", 200, 120000)

    
    for zoo in (zoo1, zoo2, zoo3):
        print(zoo)

    
    zoo1.set_budget(5000)

    
    max_budget_zoo = find_zoo_with_max_budget([zoo1, zoo2, zoo3])
    print(f"Зоопарк з максимальним бюджетом: {max_budget_zoo}")

if __name__ == "__main__":
    main()