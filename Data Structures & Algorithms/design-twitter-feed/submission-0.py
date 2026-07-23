from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # User should always see their own tweets
        self.followMap[userId].add(userId)

        # Add the latest tweet of each followed user to the heap
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(maxHeap, (-time, tweetId, followee, index - 1))

        # Get the 10 most recent tweets
        while maxHeap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            # Push the next older tweet from the same user
            if index >= 0:
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(maxHeap, (-time, tweetId, followee, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)