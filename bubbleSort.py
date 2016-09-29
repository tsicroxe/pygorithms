import random, datetime

#prints start time
start = datetime.datetime.now()
print start

# Begins our function
def bubbleSort(array):

    #Sets initial count greater than 0 to initialize
    count = 1

    #Keeps looping through the for loop until it does not detect the if statement
    while(count > 0):

        # Resets count to 0 to catch errors
        #print count
        count = 0

        # For loop to detect if numbers are greater and switches them
        for i in range(len(array)-1):
            if(array[i] > array[i+1]):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                count += 1
                # print array
            else:
                continue

    # print count
    return array

#creates a random sample of 100 numbers from 0 to 10000
array = random.sample(range(0, 10001), 100)
print(bubbleSort(array))

#prints ending time
end = datetime.datetime.now()
print end
