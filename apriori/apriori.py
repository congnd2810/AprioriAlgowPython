def createCandidate(data, minSupport):
    listCandidate = dict()
    list = []
    list1 = []
    for line in data:
        for item in line:
            if item not in listCandidate:
                listCandidate[item] = int(1)
            else:
                listCandidate[item] += int(1)

    for candidate in listCandidate:
        if listCandidate.get(candidate) >= minSupport:
            list.append([[candidate], listCandidate.get(candidate)])
            list1.append(candidate)
    return list, list1


if __name__ == '__main__':
    data = []
    dataFile = "test1.txt"
    with open(dataFile, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))

    minSupport = input()
    minSupport = int(minSupport)

    listCandidate, list = createCandidate(data, minSupport)
    listTempCandidate = listCandidate.copy()
    k = len(list)
    templist = []

    for x in range(k):  # create candidates with 1,2,3,4 item satisfies min support
        for i in range(len(listTempCandidate)):  # creates candidate with k item

            temp = 0

            for j in range(k):
                if list[j] == listTempCandidate[i][0][len(listTempCandidate[i][0]) - 1]:
                    temp = j

            for j in range(temp + 1, k):
                templist.append([listTempCandidate[i][0][0:len(listTempCandidate[i][0])] + list[j:j + 1], 0])

        for line in data:  # removed unsatisfied candidates
            for i in range(len(templist)):

                TF = 1

                for j in range(len(templist[i][0])):
                    if templist[i][0][j] not in line:
                        TF = 0

                if TF == 1:
                    templist[i][1] += 1

        counttemplist = len(templist) - 1

        while counttemplist >= 0:

            if templist[counttemplist][1] < minSupport:
                templist.__delitem__(counttemplist)
            counttemplist -= 1

        for x in templist: # add candidate in listCandidate satified
            listCandidate.append(x)

        if len(templist) == 0:
            break

        listTempCandidate = templist.copy()
        templist.clear()
        # end big loop

    for x in listCandidate:
        print(x)
