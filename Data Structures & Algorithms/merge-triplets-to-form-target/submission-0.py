class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = False

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                if x == target[0]:
                    a = True
                if y == target[1]:
                    b = True
                if z == target[2]:
                    c = True

        return a and b and c