# Code snippet from t1_t5.py


def select_number(
    data: list, selected_company_code: str, count: int, change_count: int
) -> None:
    for data_id, i in enumerate(data):
        if i[4:6] == selected_company_code:
            print("| %-4s | +%s |" % (data_id, i))
            print("+------+--------------------+")
            count += 1
        if count == change_count:
            change_count += 15
            pagination = input("Next <<1>>  Buy number <<2>>  Close <<3>>\n>>> ")
            if pagination == "1":
                print("+------+--------------------+")
                continue
            elif pagination == "2":
                selected_number_id = int(input("Id bo'yicha tanlang: "))
                print("+------+--------------------+")
                print(
                    "Tanlangan raqam -> "
                    + "\033[1;31m +"
                    + data[selected_number_id]
                    + "\033[0m"
                )
                print("+------+--------------------+")
                print("Tanlangan raqamni rostdan ham sotib olmoqchimisiz?")
                is_bought = input(
                    "<<1>> Ha sotib olaman <<2>> Orqaga qaytish <<3>> Bekor qilish\n>>> "
                )
                if is_bought == "1":
                    with open("soldNumbers.txt", "a") as file_sold:
                        sold = file_sold.write("+" + data[selected_number_id] + "\n")
                    print("Raqam sotib olindi.\nTanlovingiz uchun rahmat!")
                    break
                elif is_bought == "2":
                    change_count -= 15
                    continue
                elif is_bought == "3":
                    print("Dastur to'xtadi!")
                    break
            else:
                print("Dastur to'xtadi!")
                break
