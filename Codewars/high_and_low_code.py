def hig_and_low(numbers):
    nums = [int(num) for num in numbers.split()]
    return f'{max(nums)} {min(nums)}'


numbers = '23 4 -56 9 2 14 37'
print(hig_and_low(numbers))