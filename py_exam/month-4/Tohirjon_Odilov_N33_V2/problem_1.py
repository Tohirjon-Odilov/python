class Worker:
    def __init__(self, surname: str, position: str, salary: float) -> None:
        self.surname = surname
        self.postion = position
        self.salary = salary
        self.__improveSalary()
        self.__isEngineer()
    
    def __improveSalary(self) -> None:
        self.salary *= 1.15
        print(format(self.salary, '.2f'))
    
    def __isEngineer(self) -> None:
        if self.surname.find("Abdulla") != -1:
            self.postion += " injener"
    
    def __str__(self) -> str:
        return f"Surname: {self.surname}\nPosition: {self.postion}\nSalary: {format(self.salary, '.2f')}"

worker1 = Worker("Abdullayev", "Tizim Administratori", 6000)
worker2 = Worker("Jahongirova", "Dasturchi", 5000)
worker3 = Worker("Abdusamatov", "Moushn Dizayn", 100)
worker4 = Worker("Odilov", "Tarmoq Xavfsizligi", 8000)
worker5 = Worker("Abdullaxo'jayeva", "QA", 1500)


