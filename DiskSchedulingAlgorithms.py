
#----------------SSTF Algorithm-------------------
def calculateTheDiff(processSet, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(processSet[i] - head)

def findMinInTheProcess(diff):
    index = -1
    minimum = 9999999999

    for i in range(len(diff)):
        if (not diff[i][1] and minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index


def shortestSeekFirstTime(processSet, head):
    if (len(processSet) == 0):
        return

    lenghtProcessSet = len(processSet)
    diff = [0] * lenghtProcessSet

    for element in range(lenghtProcessSet):
        diff[element] = [0, 0]

    print("diff at the first loop",diff)

    seek_count = 0
    seek_sequence = [0] * (lenghtProcessSet + 1)

    for element in range(lenghtProcessSet):
        seek_sequence[element] = head
        calculateTheDiff(processSet, head, diff)
        index = findMinInTheProcess(diff)
        diff[index][1] = True
        seek_count += diff[index][0]
        head = processSet[index]
    seek_sequence[len(seek_sequence) - 1] = head
    print("Total number of seek operation =", seek_count)
    print("Seek Sequence is")
    for element in range(lenghtProcessSet + 1):
        print(seek_sequence[element])
#--------------SCAN Algorithm------------------

# Driver code

if __name__=="__main__":
    numberOfProcess = int(input("Please enter your process sequence: "))
    head = int(input("Please enter your staring cyclinder: "))
    processSet =[]
    while len(processSet) < numberOfProcess:
        element = int(input("Enter your cyclinder sequence: "))
        processSet.append(element)

    shortestSeekFirstTime(processSet, head)

