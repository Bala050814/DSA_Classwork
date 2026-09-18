class Solution:
    
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i=0
        j=len(numbers)-1
        while i<j:
           b=numbers[i]+numbers[j]
           if b==target:
            return[i+1,j+1]
           elif b>target:
            j-=1
           elif b<target:
            i+=1
