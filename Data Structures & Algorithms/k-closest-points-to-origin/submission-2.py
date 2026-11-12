class Solution:
    def eucledianDistance(self, x1: int, y1: int, x2: int, y2: int) -> float:
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_distances = []
        for i in range(len(points)):
            points_distances.append(
                (
                    self.eucledianDistance(points[i][0], points[i][1], 0, 0),
                    points[i]
                )
            )
        heapq.heapify(points_distances)
        results = []
        for _ in range(k):
            results.append(heapq.heappop(points_distances)[1])
        return results

# [[0,2],[2,0],[2,2]]
# [2, 2, sqrt(8)]
# [2, 2, sqrt(8)][:2]


        # implent eucledian distance. it runs O(1)
            # i belive x ** y is not O(1) fi not float
            # math.pow(x, y) is x^y and is O(1)
        # for each point 
            # get eucledian distance to origin and replace the point in the list points with the distance O(n)
            # heapify O(n)
            # pop k O(k)
        # so overall O(n) and space is O(1)