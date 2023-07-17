import json

def helloWorld():
    print('Hello world')

def filterLetter(letter, data):
    filtered_arr = []
    for item in data:
        title = item['title']
        if title[0].upper() == letter:
            filtered_arr.append(item)

    return filtered_arr

def converter(value, amount):
    result = value / amount
    return result

кількість_гривень = int(input("Сумма в гривнях:"))
test = converter(кількість_гривень, 38.6)
print(test)

#
#
#
# if __name__ == "__main__":
#     with open("products.json", "r", encoding="utf-8") as file:
#         products = json.load(file)
#
#     print(filterLetter("F" products))
#     print(filterLetter())
#     print(filterLetter())
#
#
#     temp_arr = []
#     temp_k = []
#     for item in products:
#         title = item['title']
#         if title[0].upper() == "F":
#             temp_arr.append(item)
#         elif title[0].lover() == "k":
#             temp_k.append(item)


    # new_arr = []
    # for i in products:
    #     if len(i['title']) !=0
    #     print('title')

