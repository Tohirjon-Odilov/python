# Code snippet from t1_t5.py
from sys import exit
from os import system


def write_file(selected_number_id: str, data: list) -> None:
    print("+------+-----------------------------+")
    print("Tanlangan raqam -> " + "\033[1;31m" + data[selected_number_id] + "\033[0m")
    print("+------+-----------------------------+")
    print("Tanlangan raqamni rostdan ham sotib olmoqchimisiz?")
    is_bought = input(
        "<<1>> Ha sotib olaman <<2>> Orqaga qaytish <<3>> Bekor qilish\n>>> "
    )
    if is_bought == "1":
        print("Keling rasmiylashtiramiz!")
        user_name = input("Ismingizni kiriting: ")
        with open("soldNumbers.txt", "a") as file_sold:
            file_sold.write(user_name + "," + data[selected_number_id] + "\n")
        with open("telphone.txt", "w") as update_file:
            for j in range(len(data)):
                if data[j] != data[selected_number_id]:
                    if len(data) == j:
                        update_file.write(data[j])
                        break
                    update_file.write(data[j] + "\n")
        exit("\033[1;33mRaqam sotib olindi.\nTanlovingiz uchun rahmat!")
    elif is_bought == "3":
        exit("\033[1;31mDastur to'xtadi!\033[1;0m")


def bought_number(pagination: str, data: list) -> None:
    """
    !!!
    """
    if pagination == "1":
        ...
    elif pagination == "2":
        selected_number_id = int(input("Id bo'yicha tanlang:\n>>> "))
        if selected_number_id != 0:
            selected_number_id -= 1
            write_file(selected_number_id, data)
        else:
            exit("\033[1;31mDastur to'xtadi!\033[1;0m")


def select_number(
    data: list, selected_company_code: str, count: int, change_count: int
) -> None:
    """
    Companya bo'yicha sortlab user'ga telefon raqamlarni chiqarib beradi. Funksiya hech nima qaytarmaydi.
    """
    system("clear")
    print("+------+--------------------+")
    for data_id, i in enumerate(data, 1):
        if i[5:7] == selected_company_code:
            print("| \033[1;34m%-4s\033[0m | \033[1;32m%s\033[0m |" % (data_id, i))
            print("+------+--------------------+")
            count += 1
        if count == change_count:
            change_count += 15
            pagination = input("Next <<1>>  Buy number <<2>>  Close <<3>>\n>>> ")
            bought_number(pagination, data)


def serched_number_to_list(data: list, searched_number: str) -> None:
    """
    User tomonigdan kiritilgan taxminiy raqamlarni chop etadi. Dastur hech nima qaytarmaydi.
    """
    print("+------+--------------------+")
    filtred_number = list()
    for data_id, data_element in enumerate(data, 1):
        if searched_number in data_element:
            filtred_number.append(data_element)
            print(
                "| \033[1;34m%-4s\033[0m | \033[1;32m%s\033[0m |"
                % (data_id, data_element)
            )
            print("+------+--------------------+")
    try:
        bought_number("2", data)
    except Exception as e:
        print(e + "\nDastur to'xtadi!")
