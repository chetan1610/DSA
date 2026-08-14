class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums)==1:
            print(nums)
        i=0
        j=1
        while (j<len(nums)):
            if (nums[i]==0):
                if(nums[j]!=0):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    i+=1
            
                j+=1

            if (nums[i]!=0):
                j+=1
                i+=1
        print(nums) 
        