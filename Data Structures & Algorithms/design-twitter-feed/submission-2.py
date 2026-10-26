class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.following[userId] | {userId}:
            if self.tweets[uid]:
                i = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][i]
                heapq.heappush(heap, (-t, tid, uid, i - 1))
        res = []
        while heap and len(res) < 10:
            if heap:
                _, tid, uid, i = heapq.heappop(heap)
                res.append(tid)
                if i >= 0:
                    t, tid2 = self.tweets[uid][i]
                    heapq.heappush(heap, (-t, tid2, uid, i - 1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
