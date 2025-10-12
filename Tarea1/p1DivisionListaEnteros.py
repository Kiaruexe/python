from typing import List, Tuple

def divideNegativePositive(nums: List[int]) -> Tuple[List[int], List[int]]:

    negative = [x for x in nums if x < 0]
    positive = [x for x in nums if x > 0]

    negative.sort()   
    positive.sort()   

    return negative, positive


if __name__ == "__main__":
    a = [3, -1, 0, -5, 2, -2, 7, 0]
    neg, pos = divideNegativePositive(a)
    print("Negativos:", neg)  
    print("Positivos:", pos)  
