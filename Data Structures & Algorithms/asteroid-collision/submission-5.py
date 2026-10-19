class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#if the most recently added to the stack has different sign than new encounter
#activate conditions, pop1 or popboth then insert
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:     # top moves right, new moves left
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                    continue          # it survives, so keep checking the next one
                elif abs(asteroid) < abs(stack[-1]):
                    break             # new asteroid destroyed
                else:
                    stack.pop()
                    break             # both destroyed
            else:
                stack.append(asteroid)   # runs only if we never hit `break`
        return stack