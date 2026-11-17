class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter = 0
        left = 0
        right = len(people) - 1
        people = sorted(people)

        while left <= right:
            if people[left] + people[right] <= limit:
                counter += 1
                left += 1
                right -= 1
            
            elif people[right] <= limit:
                counter += 1
                right -= 1

        return counter

