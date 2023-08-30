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
                print("Tanlangan raqam -> " + data[selected_number_id])
                with open("soldNumbers.txt", "a") as file_sold:
                    sold = file_sold.write("+" + data[selected_number_id] + "\n")
                break
            else:
                print("Dastur to'xtadi!")
                break
