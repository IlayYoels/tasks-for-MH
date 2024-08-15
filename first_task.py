kma_file = open("kill_me_already.txt", "r")
list = kma_file.read().split()
dict_list = []
def shortening(word, dict_list):
    i = 0
    for item in dict_list:
        if item["value"] == word:
            return i
        i += 1

    return -1


for word in list:
    x = shortening(word, dict_list)
    if x == -1:
        dict = {"value": word, "count": 1}
        dict_list.append(dict)
    else:
        dict_list[x]["count"] += 1


SDL = (sorted(dict_list,reverse=True, key=lambda order: order["count"]))


def finally_finishing():
    try:
        N = int(input("please type the amount of words you want to receive "))
        if N>len(dict_list):
            N = len(dict_list)
        print("your words are: ")

        for i in range(N):
            print(SDL[i]["value"])
    except TypeError:
        print("i will give you one more try")
        finally_finishing()
        pass

    
print(SDL)
finally_finishing()



