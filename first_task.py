file = open("file_to_read.txt", "r")
list = file.read().split()
dict_list = []
def word_counter_for_list(word, dict_list):
    i = 0
    for item in dict_list:
        if item["value"] == word:
            return i
        i += 1

    return -1


for word in list:
    x = word_counter_for_list(word, dict_list)
    if x == -1:
        dict = {"value": word, "count": 1}
        dict_list.append(dict)
    else:
        dict_list[x]["count"] += 1


SDL = (sorted(dict_list,reverse=True, key=lambda order: order["count"]))


def answer():
    try:
        N = int(input("please type the amount of words you want to receive "))
        if N>len(dict_list):
            N = len(dict_list)
        print("your words are: ")

        for i in range(N):
            print(SDL[i]["value"])
    except TypeError:
        print("i will give you one more try")
        answer()
        pass


answer()



