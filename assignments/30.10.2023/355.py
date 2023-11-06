class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) 
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        for followee in self.followMap[userId]:
            temp = [(-t, id) for t, id, posteeId in self.tweetMap[followee]]
            maxHeap += temp
        temp2 = self.tweetMap.get(userId, [])
        maxHeap += [(-t, id) for t, id, posteeId in temp2]
        count = 10
        heapq.heapify(maxHeap)
        feed = []
        print(maxHeap)
        while count and maxHeap:
            curTime, tweetId = heapq.heappop(maxHeap)
            count -= 1
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)