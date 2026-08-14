class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution=[]
        i=0
        j=len(numbers)-1
        while(i<=j):
            if ((numbers[i]+numbers[j])==target):
                solution.append(i+1)
                solution.append(j+1)
                break
            if((numbers[i]+numbers[j])>target):
                j-=1
            if((numbers[i]+numbers[j])<target):
                i+=1

        return solution