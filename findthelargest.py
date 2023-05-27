count=0
array=[]
while count < 5:
    number= int(input('please enter the number: '))
    array.append(number)
    count = count +1
def findLargestNum(nums):
    largest = nums[0]
    for i in nums:
        if i in nums:
            if i > largest:
                largest = i
    return largest
print(findLargestNum(array))