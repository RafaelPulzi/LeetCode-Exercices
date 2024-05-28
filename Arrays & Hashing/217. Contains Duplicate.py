"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            
numbers = [1, 0, 3, 4, 5]
solution = Solution()
result = solution.containsDuplicate(numbers)
print(result)


'''
In below we have some solutions that i got interest

user: michellejyyun
class Solution:
   def containsDuplicate(self, nums: List[int]) -> bool:
       if len(nums) == len(set(nums)):
           return False
       return True


user: rahulvarma5297       
# Here is a solution using hasmap
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        for (int num : nums) {
            if (seen.containsKey(num) && seen.get(num) >= 1)
                return true;
            seen.put(num, seen.getOrDefault(num, 0) + 1);
        }
        return false;
    }
}

# And by the same gou we have a solution using sort 
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1])
                return true;
        }
        return false;
    }
}


user: Unknowm
Program Used to achieve 44ms in this exercise, Analyse later 
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == '__main__':
    import json, sys
    with open('user.out', 'w') as f:
        for nums in map(json.loads, sys.stdin):
            result = contains_duplicate(nums)
            print(str(result).lower(), file=f)
    sys.exit()




'''



