# Problem Link: https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
from typing import List
def countCompleteDayPairs(hours: List[int]) -> int:
        remainder_count = {}
        countPairs = 0
        for i in range(len(hours)):
            remainder = hours[i]%24
            if remainder == 0: # Means that the current hours in itself form a day, so we can pair only with those hours which also make complete day, i.e whose remainder is 0.
                countPairs += remainder_count.get(remainder, 0)
            else: # This means that the current hours doesn't form a compelete day, so we will find how many more hours are needed to pair with the current hours to make complete days. For this we find for the remaining hours as key in the hashmap i.e. 24-remainder in the hashMap.
                countPairs += remainder_count.get(24-remainder, 0)
            remainder_count[remainder] = 1+remainder_count.get(remainder,0)
        return countPairs