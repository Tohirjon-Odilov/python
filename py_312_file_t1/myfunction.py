# Code snippet from t1_t5.py


def select_number(
    data: list, selected_company_code: str, count: int, change_count: int
) -> None:
    for data_id, i in enumerate(data, 1):
        if i[5:7] == selected_company_code:
            print("| \033[1;34m%-4s\033[0m | \033[1;32m%s\033[0m |" % (data_id, i))
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
                if selected_number_id != 0:
                    selected_number_id -= 1
                print("+------+-----------------------------+")
                print(
                    "Tanlangan raqam -> "
                    + "\033[1;31m"
                    + data[selected_number_id]
                    + "\033[0m"
                )
                print("+------+-----------------------------+")
                print("Tanlangan raqamni rostdan ham sotib olmoqchimisiz?")
                is_bought = input(
                    "<<1>> Ha sotib olaman <<2>> Orqaga qaytish <<3>> Bekor qilish\n>>> "
                )
                if is_bought == "1":
                    print("Keling rasmiylashtiramiz!")
                    user_name = input("Ismingizni kiriting: ")
                    with open("soldNumbers.txt", "a") as file_sold:
                        file_sold.write(
                            user_name + "," + data[selected_number_id] + "\n"
                        )
                        # file_sold.write(data[selected_number_id] + "\n")
                    with open("telphone.txt", "w") as update_file:
                        for j in range(len(data)):
                            if data[j] != data[selected_number_id]:
                                if len(data) == j:
                                    update_file.write(data[j])
                                    break
                                update_file.write(data[j] + "\n")
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
