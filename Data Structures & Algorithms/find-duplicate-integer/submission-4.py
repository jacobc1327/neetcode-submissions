class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

#output the repeated integer
#multiple indices point to the same next index, so following the indic
#[1,2,3,4,4] output 4
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
