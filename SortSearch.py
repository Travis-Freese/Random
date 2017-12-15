
#Sequential search takes a Target and a list to search through
def SequentialSearch(target, inputlist):
    for item in inputlist:  #iterates through the list
        if item == target:  #checks to see if the current item equals the target
            return True     #if found return 1
    return False            #if not found return 0

#Binary Search the parameters are a target and an inputlist also assumes the list is presorted
def BinarySearch(target, inputlist):
    lowerbound = 0
    upperbound = len(inputlist)-1
    found = False
    while lowerbound <= upperbound and (found not false): #while we search within valid bounds and when the target isn't found.
        mid = math.ceil((low+high)/2) #caluclates the mid piont of the inputlist.
        if inputlist[mid] == target:
            found = True
            break   #break is required to exit loop once the target is found.
        if (inputlist[mid] < target):
            low = mid + 1 #discard the lower half of the list
        if (inputlist[mid] > target):
            high = mid - 1 #dicard the upper half of the list
    return found #found is boolean


#Selection Sort Takes a list and sorts it. 
def SelectionSort(inputlist):
    for i in range(len(inputlist)): 
        smallest = i #the smallest is assumed to be the first in the unsorted section of the list
        for j in range(i+1,len(inputlist)):
            if inputlist[j] < inputlist[smallest]:  #compares the value of j to smallest.
                smallest = j
        if smallest != i: #if i is the smallest then it doesnt swap the numbers.
            small = inputlist[smallest]
            inputlist[smallest] = inputlist[i]
            inputlist[i] = small    # swap inputlist[i] = inputlist[smallest]
    return inputlist



#Insertion Sort 
def InsertionSort(inputlist):
    i = 1   #starts at 1 because it assumes the first item is sorted.
    while i < len(inputlist): 
        j = i 
        while j > 0 and inputlist[j-1] > inputlist[j]: #iterate through the sorted list until the value of the one before it is less than inputlist[i]
            con = inputlist[j]
            inputlist[j] = inputlist[j-1]
            inputlist[j-1] = con        #swap inputlist[j] and inputlist[j-1]
            j= j-1
        i = i+1

    return inputlist


#Merge is a supporting function for MergeSort
#Merge takes two list as its parameters
#Merge combines two list in sorted order 
def Merge(first, last):
    container = [] #container is used to store the sorted list
    while len(first) != 0 and len(last) != 0:   #Do this until the legth of both list equal 0
        if first[0] < last[0]: #if the begining of the first list is less than the first item in the second list.
            container.append(first[0]) #Adds the first element of the first list to the sorted array
            first.remove(first[0]) #Removes the first item from the first list
        else:   #This does the same but for the other case where the first element of the second list is larger. 
            container.append(last[0]) 
            last.remove(last[0])
    if len(first) == 0: #this if else statement plces the last item to be sorted into the sorted list.
        container += last
    else:
        container += first
    return container


#Merge Sort: Sorts a list using the merge sort algorrithm
def MergeSort(inputlist):
    if len(inputlist) < 2:  #this is the base case if a list has one or less elements it is sorted bt default.
           return inputlist 
    else:
        mid = len(inputlist)/2 #calculates mid point to split the list.
        first = MergeSort(inputlist[:mid]) # calls itself but this time with the first half of the list given to it previously
        last = MergeSort(inputlist[mid:])   #calls itself but with the second falf of the list given to it
        return merge(first, last) #Executes the merge function to merge the lists.
