def shuffle(nums, n):
        shuffled_list = []
        for i in range(0,int(len(nums)/2 )):
            shuffled_list.append(nums[i])
            shuffled_list.append(nums[i + n])
        return shuffled_list


print(shuffle([2,5,1,3,4,7], 3))