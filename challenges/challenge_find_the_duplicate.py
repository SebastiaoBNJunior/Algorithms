from collections import Counter


def find_duplicate(nums):
    if not nums:
        return False
    if len(nums) == 1 or not all(isinstance(num, int) for num in nums):
        return False
    number, frequency = Counter(nums).most_common(1)[0]
    if frequency == 1 or number < 0:
        return False
    return number


print(find_duplicate([1, 2, 3, 3, 4, 5, 6]))
