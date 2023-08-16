# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [x for x in arr[1:] if x <= pivot]
#         greater = [x for x in arr[1:] if x > pivot]
#         return quicksort(less)+[pivot]+quicksort(greater)
    


# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         total = 0
        
#         if len(nums) == 3:
#             for num in nums:
#                 total += num
            
#             if total == 0:
#                 return [nums]
#             else:
#                 return []
#         else:
#             # i = nums[0]
#             result_list = []
#             for i in range(len(nums)):
#                 for j in range(1, len(nums)):
#                     for k in range(1, len(nums)):
#                         j_value = nums[j]
#                         k_value = nums[k]
#                         if i != j_value and i != k_value and j_value!= k_value:
#                             if i + j_value + k_value == 0:
#                                 # if i!=j_value and i!=k_value and j_value!=k_value:
#                                 ordered_list = quicksort(arr=[i, j_value, k_value])
#                                 result_list.append(ordered_list)

#                         else:
#                             continue
            

#         unique_list = list(set(tuple(sublist) for sublist in result_list))
#         return unique_list


# # [[-2,-1,3],[-2,0,2],[-1,0,1]]
# nums=[-1,0,1,2,-1,-4]   
# sol = Solution()
# print(sol.threeSum(nums))





class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]: 
        nums.sort() # sorting cause we need to avoid duplicates, with this duplicates will be near to each other
        l=[]
        for i in range(len(nums)):  #this loop will help to fix the one number i.e, i
            if i>0 and nums[i-1]==nums[i]:  #skipping if we found the duplicate of i
                continue 
			
			#NOW FOLLOWING THE RULE OF TWO POINTERS AFTER FIXING THE ONE VALUE (i)
            j=i+1 #taking j pointer larger than i (as said in ques)
            k=len(nums)-1 #taking k pointer from last 
            while j<k: 
                s=nums[i]+nums[j]+nums[k] 
                if s>0: #if sum s is greater than 0(target) means the larger value(from right as nums is sorted i.e, k at right) 
				#is taken and it is not able to sum up to the target
                    k-=1  #so take value less than previous
                elif s<0: #if sum s is less than 0(target) means the shorter value(from left as nums is sorted i.e, j at left) 
				#is taken and it is not able to sum up to the target
                    j+=1  #so take value greater than previous
                else:
                    l.append([nums[i],nums[j],nums[k]]) #if sum s found equal to the target (0)
                    j+=1 
                    while nums[j-1]==nums[j] and j<k: #skipping if we found the duplicate of j and we dont need to check 
					#the duplicate of k cause it will automatically skip the duplicate by the adjustment of i and j
                        j+=1   
        return l
    
# [[-2,-1,3],[-2,0,2],[-1,0,1]]
nums=[-1,0,1,2,-1,-4]   
sol = Solution()
print(sol.threeSum(nums))