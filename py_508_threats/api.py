from datetime import datetime


class write_file:
    def send(self, name, message) -> None:
        date = datetime.now().strftime("%X")
        with open("data.txt", "a") as file:
            file.write(f"{name}|{message}|{date}\n")
        # return name

    def get_all(self):
        with open("data.txt", "r") as file:
            data = file.read().split("\n")[:-1]
            all_data = list()
            for i in data:
                data_to_list = i.split("|")
                all_data.append(dict(name=data_to_list[0],message=data_to_list[1],date=data_to_list[2]))
        return all_data

# print(write_file().get_all_message())