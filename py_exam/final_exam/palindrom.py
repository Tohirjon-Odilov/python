def palindrom(num: int) -> int:
    if num == str(num)[::-1]:
        return f"{num} => 0 {num}"
    palindrom_number = num
    count = 0
    while True:
        re_num = str(palindrom_number)[::-1]
        if palindrom_number != int(re_num):
            count += 1
            palindrom_number += int(re_num)
            continue
        return f"{num} => {count} {palindrom_number}"

print(palindrom(int(input())))

# def palindrom(nums: str):
#     num = nums
#     counts = 0
#     while True:
#         if nums == nums[::-1]:
#             return f"{num} => {counts} {nums}"
#         else:
#             counts += 1
#             nums = str(int(nums) + int(nums[::-1]))

# print(palindrom(input()))