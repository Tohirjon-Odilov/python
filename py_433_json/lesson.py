# F4:

data = [
  {
    "id": 12345,
    "username": "johndoe",
    "firstName": "John",
    "lastName": "Doe",
    "email": "johndoe@example.com",
    "age": 30,
    "gender": "male",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "postalCode": "12345",
    "homePhoneNumber": "555-555-5555",
    "workPhoneNumber": "555-123-4567",
    "mobilePhoneNumber": "555-987-6543",
    "notificationsEnabled": True,
    "themePreference": "light",
    "membershipStatus": "active",
    "lastLogin": "2023-09-29T10:00:00Z"
  },
  {
    "id": 67890,
    "username": "janedoe",
    "firstName": "Jane",
    "lastName": "Doe",
    "email": "janedoe@example.com",
    "age": 28,
    "gender": "female",
    "address": "456 Oak St",
    "city": "Sometown",
    "state": "NY",
    "postalCode": "54321",
    "homePhoneNumber": "555-111-2222",
    "workPhoneNumber": "555-333-4444",
    "mobilePhoneNumber": "555-999-8888",
    "notificationsEnabled": True,
    "themePreference": "dark",
    "membershipStatus": "active",
    "lastLogin": "2023-09-28T14:30:00Z"
  },
  {
    "id": 78901,
    "username": "janesmith",
    "firstName": "Jane",
    "lastName": "Smith",
    "email": "janesmith@example.com",
    "age": 35,
    "gender": "female",
    "address": "789 Pine St",
    "city": "Anothercity",
    "state": "TX",
    "postalCode": "67890",
    "homePhoneNumber": "555-333-3333",
    "workPhoneNumber": "555-444-4444",
    "mobilePhoneNumber": "555-555-5555",
    "notificationsEnabled": False,
    "themePreference": "dark",
    "membershipStatus": "inactive",
    "lastLogin": "2023-09-27T09:45:00Z"
  },
  {
    "id": 56789,
    "username": "bobsmith",
    "firstName": "Bob",
    "lastName": "Smith",
    "email": "bobsmith@example.com",
    "age": 40,
    "gender": "male",
    "address": "567 Elm St",
    "city": "YetAnotherTown",
    "state": "FL",
    "postalCode": "45678",
    "homePhoneNumber": "555-777-7777",
    "workPhoneNumber": "555-888-8888",
    "mobilePhoneNumber": "555-666-6666",
    "notificationsEnabled": True,
    "themePreference": "light",
    "membershipStatus": "active",
    "lastLogin": "2023-09-28T18:15:00Z"
  },
  {
    "id": 10101,
    "username": "maryjones",
    "firstName": "Mary",
    "lastName": "Jones",
    "email": "maryjones@example.com",
    "age": 29,
    "gender": "female",
    "address": "101 Maple St",
    "city": "Maplecity",
    "state": "WA",
    "postalCode": "10101",
    "homePhoneNumber": "555-999-9999",
    "workPhoneNumber": "555-000-0000",
    "mobilePhoneNumber": "555-123-1234",
    "notificationsEnabled": True,
    "themePreference": "light"
  }
]

class Person:
    def __init__(self, json:dict) -> None:
        self.name = json["id"]
        self.username = json["username"]
        self.firstName= json["firstName"]
        self.lastName= json["lastName"]
        self.email= json["email"]
        self.age= json["age"]
        self.gender= json["gender"]
        self.address= json["address"]
        self.city= json["city"]
        self.state= json["state"]
        self.postalCode= json["postalCode"]
        self.homePhoneNumber= json["homePhoneNumber"]
        self.workPhoneNumber= json["workPhoneNumber"]
        self.mobilePhoneNumber= json["mobilePhoneNumber"]
        self.notificationsEnabled= json["notificationsEnabled"]
        self.themePreference= json["themePreference"]
        # self.membershipStatus= json["membershipStatus"]
        # self.lastLogin= json["lastLogin"]
    
    def __str__(self) -> str:
        return f"""Name: {self.name}
User name: {self.username}
First name: {self.firstName}
Last name: {self.lastName}
Email: {self.email}
Age: {self.age}
Gender: {self.gender}
Address: {self.address}
City: {self.address}
State: {self.state}
Postal code: {self.postalCode}
Home Phone number: {self.homePhoneNumber}
Work Phone number: {self.workPhoneNumber}
Mobile Phone number: {self.mobilePhoneNumber}
Notifications Enabled: {self.notificationsEnabled}
Theme Preference: {self.themePreference}
        """
        
for i in data:
    person = Person(i)
    print(person)
    