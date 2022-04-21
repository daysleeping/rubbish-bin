def twoSum(nums,target):
    a = 0
    b = 0
    while a != len(nums):
        print(f'A = {a}')
        while b != len(nums):
            print(f'B = {b}')
            if nums[a] + nums[b] == target and a != b:
                return [a,b]
            b += 1
        b = 0
        a += 1
