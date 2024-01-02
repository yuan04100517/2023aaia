class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#先把數字排好
        ans =  [[ nums[0] ] ]#把最前面最小數字,放在2層方括號裡
        repeat = 0 #目前數字 nums[0]沒有重複
        N = len(nums)
        for i in range(1,N):#有幾個數字
            if nums[i] == nums[i-1]:#想比較 nums[i] vs. nums[i-1] 是否相同
                repeat += 1 #這裡處理重複 就repeat += 1
                if len(ans)<=repeat:# 目前層數不夠多
                    ans.append( [] )#增加一層樓
            else:# 沒又重複
                repeat = 0
            ans[repeat].append( nums[i] )
        return ans