data = [
        {
        "id":"332",
        "name":"Reconstruct Itinerary",
        "desc":'''Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.''',
        "type":["DFS", "Graph"],
        "solution":'''
        vertices = set()
        adj = {}
        for ticket in tickets:
            vertices.add(ticket[0])
            if ticket[0] in adj: adj[ticket[0]] += [[ticket[1], 0]]
            else: adj[ticket[0]] = [[ticket[1], 0]]
        for v in vertices: adj[v].sort()
        
        self.ans = None
        def visit(place, cur):
            if len(cur) == len(tickets):
                self.ans = cur + [place]
                return
            if place not in adj: return
            nexts = adj[place]
            for nxt in nexts:
                if not self.ans and not nxt[1]:
                    nxt[1] = 1
                    visit(nxt[0], cur + [place])
                    nxt[1] = 0
                
        visit("JFK", [])
        return self.ans
        '''
        },
        {
        "id":"331",
        "name":"Verify Preorder Serialization of a Binary Tree",
        "desc":'''One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.Each comma separated value in the string must be either an integer or a character '#' representing null pointer.''',
        "type":["Stack"],
        "solution":'''
        stk = []
        arr = preorder.split(',')
        for ch in arr:
            if ch == '#':
                while stk and stk[-1] == '#':
                    stk.pop()
                    if not stk: return False
                    stk.pop()
            stk += [ch]
        if len(stk) == 1 and stk[0] == '#': return True
        return False
        '''
        },
        {
        "id":"330",
        "name":"Patching Array",
        "desc":'''Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.''',
        "type":["Greedy"],
        "solution":'''
        reach = 0
        cnt = 0 
        for num in nums:
            if reach >= n: 
                return cnt
            while num > reach + 1:
                cnt += 1
                reach = reach * 2 + 1
                if reach >= n:
                    return cnt
            reach += num
        while reach < n:
            cnt += 1
            reach = reach * 2 + 1
        return cnt
        '''
        },
        {
        "id":"329",
        "name":"Longest Increasing Path in a Matrix",
        "desc":'''Given an integer matrix, find the length of the longest increasing path. From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
        ''',
        "type":["DP"],
        "solution":'''
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        
        def visit(x, y, dp):
            if dp[x][y]: return dp[x][y]
            dp[x][y] = 1
            for i, j in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=i<m and 0<=j<n:
                    if matrix[i][j] > matrix[x][y]:
                        dp[x][y] = max(dp[x][y], visit(i, j, dp) + 1)
            return dp[x][y]
            
        dp = [[0] * n for i in xrange(m)]
        return max(visit(i, j, dp) for i in xrange(m) for j in xrange(n))
        '''
        },
        {
        "id":"327",
        "name":"Count of Range Sum",
        "desc":''' Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive. Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.  
        ''',
        "type":["BST", "BIT", "Divide and Conquer"],
        "solution":'''
        prefix = [0]
        n = len(nums)
        for num in nums:
            prefix += [ prefix[-1] + num ]
        bst = BST(n)
        cnt = 0 
        for i in xrange(n, 0, -1):
            bst.insert(prefix[i])
            cnt += bst.queryGE(prefix[i-1] + lo)
            cnt -= bst.queryGE(prefix[i-1] + hi + 1)
        return cnt
        '''
        },
        {
        "id":"326",
        "name":"Power of Three",
        "desc":''' Given an integer, write a function to determine if it is a power of three.
        ''',
        "type":["Math"],
        "solution":'''
        if not n:
            return False
        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False
        '''
        },
        {
        "id":"324",
        "name":"Wiggle Sort II",
        "desc":''' Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
        ''',
        "type":["Sort"],
        "solution":'''
        def partition3way(a, lo, hi):
            lt, gt = lo, hi
            i = lo
            m = random.randrange(lo, hi)
            v = a[m]
            while i <= gt:
                c = cmp(a[i], v)
                if c < 0:
                    exch(a, lt, i)
                    lt += 1
                    i += 1
                elif c > 0:
                    exch(a, gt, i)
                    gt -= 1
                else:
                    i += 1
            return lt, gt
        
        def kthSmallestWithDuplicates(arr, k):
            lo, hi = 0, len(arr)-1
            while lo < hi:
                lt, gt = partition3way(arr, lo, hi)
                if k < lt:
                    hi = lt-1
                elif gt < k:
                    lo = gt+1
                else:
                    return lo, hi
            return lo, hi

        n, m = len(nums), len(nums)>>1
        l, r = kthSmallestWithDuplicates(nums, m)
        '''
        },
        {
        "id":"323",
        "name":"Number of Connected Components in an Undirected Graph",
        "desc":'''Number of Connected Components in an Undirected Graph
        ''',
        "type":["DFS","BFS","Union Find"],
        "solution":'''
        a = [0] * n
        sz = [1] * n
        for i in xrange(n):
            a[i] = i
        
        def root(i):
            while a[i] != i:
                a[i] = a[a[i]]
                i = a[i]
            return i
        
        def union(i, j):
            i = root(i)
            j = root(j)
            if i == j:
                return
            if sz[i] < sz[j]:
                a[i] = j
                sz[j] += sz[i]
            else:
                a[j] = i
                sz[i] += sz[j]
        
        for x, y in edges:
            union(x, y)

        ans = set([])
        for i in xrange(n):
            ans.add(root(i))
        return len(ans)
        '''
        },
        {
        "id":"321",
        "name":"Create Maximum Number",
        "desc":'''Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.
        ''',
        "type":["Greedy"],
        "solution":'''
        def array(nums, k):
            stk = []
            for i, num in enumerate(nums):
                while stk and len(nums) - i + len(stk) > k and stk[-1] < num: stk.pop()
                if len(stk) < k: stk += [num]
            return stk

        def merge(nums1, nums2):
            a, b, l = deque(nums1), deque(nums2), len(nums1) + len(nums2)
            return [max(a, b).popleft() for _ in xrange(l)]

        l1, l2 = len(nums1), len(nums2)
        if l1 == 0: return array(nums2, k)
        if l2 == 0: return array(nums1, k)
        i = max(0, k-l2)
        ans = []
        while i <= k and i <= l1:
            candi = merge(array(nums1, i), array(nums2, k-i))
            if candi > ans: ans = candi
            i += 1
        return ans
        '''
        },
        {
        "id":"320",
        "name":"Generalized Abbreviation",
        "desc":'''
        word => ['w1r1', 'w1rd', 'w2d', 'w3', '1o1d', '1o2', '1or1', '1ord', 'wo1d', 'wo2', '2r1', '2rd', 'wor1', '3d', 'word', '4'] 
        ''',
        "type":["Backtracking"],
        "solution":'''
        n = len(word)
        if n == 0:
            return [""]

        ans = []
        def dfs(w, cur):
            if not w:
                ans.append(cur)
            for i in xrange(1, len(w)+1):
                if not cur:
                    dfs(w[i:], cur+w[:i])
                    dfs(w[i:], cur+str(i))
                elif cur[-1] in "1234567890":
                    dfs(w[i:], cur+w[:i])
                else:
                    dfs(w[i:], cur+str(i))
                    
        dfs(word, "")
        '''
        },
        {
        "id":"318",
        "name":"Maximum Product of Word Lengths",
        "desc":''' Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
        ''',
        "type":["Backtracking"],
        "solution":'''
        n = len(words)
        if n <= 1:
            return 0
        p = [2**i for i in xrange(26)]
        dct = [0] * n
        for i, word in enumerate(words):
            for ch in word:
                dct[i] |= p[ord(ch)-0x61]

        ans = 0
        for i in xrange(n):
            for j in xrange(i):
                if dct[i] & dct[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        '''
        },
        {
        "id":"317",
        "name":"Shortest Distance from All Buildings",
        "desc":'''0 -- can visit, 1 -- building, 2 -- block, shortest distance from all 1
        ''',
        "type":["BFS"],
        "solution":'''
        total = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    total += 1
        dists = [[0]*n for i in xrange(m)]
        cnts = [[0]*n for i in xrange(m)]

        def bfs(x0, y0):
            visit = [[0]*n for i in xrange(m)]
            cnt = 1
            q = deque()
            q.append((x0,y0,0))
            visit[x0][y0] = 1
            while q:
                x, y, d = q.popleft()
                for i, j in ((x-1,y),(x,y-1),(x+1,y),(x,y+1)):
                    if 0 <= i < m and 0 <= j < n and not visit[i][j]:
                        if grid[i][j] == 0:
                            q.append((i,j,d+1))
                            dists[i][j] += d+1
                            cnts[i][j] += 1
                        elif grid[i][j] == 1:
                            cnt += 1
                        visit[i][j] = 1
            return cnt

        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == 1:
                    cnt = bfs(x,y)
                    if cnt != total: return -1
        t = [dists[i][j] for i in xrange(m) for j in xrange(n) if cnts[i][j] == total]
        if not t:
            return -1
        return min(t)
        '''
        },
        {
        "id":"316",
        "name":"Remove Duplicate Letters",
        "desc":'''Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
        ''',
        "type":["Stack"],
        "solution":'''
        cnts = [0] * 26
        for ch in s: cnts[ord(ch)-0x61]+=1
        stk = []
        marked = [0] * 26
        for ch in s:
            if marked[ord(ch)-0x61]:
                cnts[ord(ch)-0x61] -= 1
                continue
            while stk and ch < stk[-1] and cnts[ord(stk[-1])-0x61]:
                a = stk.pop()
                marked[ord(a)-0x61] = 0
            stk.append(ch)
            marked[ord(ch)-0x61] = 1
            cnts[ord(ch)-0x61] -= 1
        return ''.join(stk)
        '''
        },
        {
        "id":"315",
        "name":"Count of Smaller Numbers After Self",
        "desc":'''You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
        ''',
        "type":["BST", "BIT", "Divide and Conquer"],
        "solution":'''
        def getSum(self, T, idx):
            ans = 0
            while idx:
                ans += T[idx]
                idx -= idx & (-idx)
            return ans
        
        def update(self, T, idx, val):
            while idx <= len(T)-1:
                T[idx] += val
                idx += idx & (-idx)

        if not nums: return []
        n = len(nums)
        padding = min(nums)
        if padding <= 0: nums = [a + 1 - padding for a in nums]
        m = max(nums)
        T = [0] * (m+1)
        ans = []
        t = 0
        for num in nums[::-1]:
            ans.append(self.getSum(T, num-1))
            self.update(T, num, 1)
        return ans[::-1]
        '''
        },
        {
        "id":"313",
        "name":"Super Ugly Number",
        "desc":''' Write a program to find the nth super ugly number. Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
        ''',
        "type":["Math", "Heap"],
        "solution":'''
        q = [(p, 0, p) for p in primes]
        uglyNums = [1]
        s = set([1] + [p for p in primes])
        for i in xrange(1,n):
            x, idx, p = heappop(q)
            uglyNums.append(x)
            while uglyNums[idx] * p in s:
                idx+=1
            heappush(q, (uglyNums[idx] * p, idx, p))
            s.add(uglyNums[idx]*p)
        return uglyNums[-1]
        '''
        },
        {
        "id":"312",
        "name":"Burst Balloons",
        "desc":''' Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
        ''',
        "type":["DP"],
        "solution":'''
        myNums = [1]
        for num in nums:
            if num:
                myNums.append(num)
        myNums.append(1)
        n = len(myNums)
        F = [[0] * n for i in xrange(n)]
        for i in xrange(1,n-1):
            F[i-1][i+1] = myNums[i-1]*myNums[i]*myNums[i+1]
        for i in xrange(2,n):
            for start in xrange(0, n-i):
                end = start + i
                for k in xrange(start+1, end):
                    F[start][end] = max(F[start][end], F[start][k] + F[k][end] + myNums[start]*myNums[k]*myNums[end])
        return F[0][n-1]
        '''
        },
        {
        "id":"310",
        "name":"Minimum Height Trees",
        "desc":''' For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
        ''',
        "type":["BFS"],
        "solution":'''
        if self.n == 1:
            return [0]
        leafs = self.getLeafs()
        cnt = self.n
        while cnt > 2:
            newLeafs = []
            cnt -= len(leafs)
            for v in leafs:
                w = self.adj[v].pop()
                self.adj[w].remove(v)
                if len(self.adj[w]) == 1:
                    newLeafs.append(w)
            leafs = newLeafs

        return leafs

    def findMinHeightTrees(self, n, edges):
        G = Graph(n)
        for e in edges:
            G.addEdge(e[0], e[1])

        return G.getMinHeight()
        '''
        },
        {
        "id":"309",
        "name":"Best Time to Buy and Sell Stock with Cooldown",
        "desc":''' Say you have an array for which the ith element is the price of a given stock on day i.  Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).  After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day) 
        ''',
        "type":["DP", "DFA"],
        "solution":'''
        n = len(prices)
        s0, s1, s2 = [0]*n, [0]*n, [0]*n
        s1[0], s2[0] = -prices[0], -1e100
        for i in xrange(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
        return max(s0[n-1], s2[n-1])
        '''
        },
        {
        "id":"305",
        "name":"Number of Islands II",
        "desc":''' Give a list of place, find after each place added, the count of total islands
        ''',
        "type":["Union Find"],
        "solution":'''
        ans = []
        cnt = 0
        root = {}

        def findRoot(x):
            while x != root[x][0]:
                root[x][0] = root[root[x][0]][0]
                x = root[x][0]
            return x

        for i, j in positions:
            cnt += 1
            root[i*n+j] = [i*n+j, 1]
            for x, y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                if 0<=x<m and 0<=y<n and x*n+y in root:
                    other = findRoot(x*n+y)
                    this = findRoot(i*n+j)
                    if this != other:
                        if root[other][1] < root[this][1]:
                            root[other][0] = this
                            root[this][1] += root[other][1]
                        else:
                            root[this][0] = other
                            root[other][1] = root[this][1]
                        cnt -= 1
            ans += [cnt]
        '''
        },
        {
        "id":"302",
        "name":"Smallest Rectangle Enclosing Black Pixels",
        "desc":''' 
        ''',
        "type":["Binary Search"],
        "solution":'''
        def findTop(lo, hi):
            while lo < hi:
                m = (lo+hi)>>1
                if '1' in image[m]: hi = m
                else: lo = m + 1
            return lo

        def findBottom(lo, hi):
            while lo < hi:
                m = (lo+hi)>>1
                if '1' in image[m]: lo = m + 1
                else: hi = m
            return lo 

        def findLeft(lo, hi, M):
            while lo < hi:
                m = (lo+hi)>>1
                if any(image[x][m]=='1' for x in xrange(M)): hi = m
                else: lo = m + 1
            return lo

        def findRight(lo, hi, M):
            while lo < hi:
                m = (lo+hi)>>1
                if all(image[x][m]=='0' for x in xrange(M)): hi = m
                else: lo = m + 1
            return lo
        
        return (findRight(y+1, n, m)-findLeft(0, y, m))*(findBottom(x+1, m)-findTop(0, x))
        '''
        },
        {
        "id":"298",
        "name":"Binary Tree Longest Consecutive Sequence",
        "desc":''' 
        ''',
        "type":["Tree"],
        "solution":'''
        def visit(root, i):
            if not root: return
            self.ans = max(self.ans, i)
            if root.left and root.left.val == root.val+1: visit(root.left, i+1)
            else: visit(root.left, 1)
            if root.right and root.right.val == root.val+1: visit(root.right, i+1)
            else: visit(root.right, 1)

        visit(root, 1)
        '''
        },
        {
        "id":"295",
        "name":"Find Median from Data Stream",
        "desc":''' Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
        ''',
        "type":["Heap"],
        "solution":'''
        m = self.findMedian()
        if num <= m:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)
        if len(self.left)-len(self.right)>1:
            heappush(self.right, -heappop(self.left))
        if len(self.right)-len(self.left)>1:
            heappush(self.left, -heappop(self.right))
        '''
        },
        {
        "id":"294",
        "name":"Flip Game II",
        "desc":''' 
        ''',
        "type":["Backtracking"],
        "solution":'''
        if s in self.cache:
            return self.cache[s]
        a = self.generatePossibleNextMoves(s)
        if not a:
            self.cache[s] = False
            return False
        for t in a:
            if not self.judge(t):
                self.cache[s] = True
                return True
        self.cache[s] = False
        return False
        '''
        },
        {
        "id":"293",
        "name":"Flip Game",
        "desc":''' 
        ''',
        "type":["String"],
        "solution":'''
        n = len(s)
        if n <= 1:
            return []
        ans = []
        for i in xrange(n-1):
            if s[i] == s[i+1] == '+':
                ans.append(s[:i]+'--'+s[i+2:])
        return ans
        '''
        },
        {
        "id":"289",
        "name":"Game of Life",
        "desc":''' Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article): 
Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
        ''',
        "type":["Array", "Bits"],
        "solution":'''
        for i in xrange(m):
            for j in xrange(n):
                cnt = sum(1 for x,y in ((i+1,j+1),(i+1,j),(i+1,j-1),(i,j+1),(i,j-1),(i-1,j+1),(i-1,j),(i-1,j-1)) if 0<=x<m and 0<=y<n and board[x][y] & 0b01 == 1)
                if cnt in [2, 3] and board[i][j] & 0b01 == 1:
                    board[i][j] = 0b11
                if cnt is 3 and board[i][j] & 0b01 == 0:
                    board[i][j] = 0b10

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = (int) (board[i][j] & 0b10 > 1) 
        '''
        },
        {
        "id":"288",
        "name":"Unique Word Abbreviation",
        "desc":''' 
        ''',
        "type":["Hash"],
        "solution":'''
        for s in dictionary:
            s2 = self.get(s)
            if s2 in dct:
                dct[s2] = -1
            else:
                dct[s2] = s
        self.dct = dct
        '''
        },
        {
        "id":"284",
        "name":"Peeking Iterator",
        "desc":''' Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
        ''',
        "type":["Design"],
        "solution":'''
        self.i = iterator
        if iterator == None:
            self.n = None
            self.ni = None
        elif iterator.hasNext():
            self.ni = copy.copy(iterator)
            self.n = self.ni.next()

        '''
        },
        {
        "id":"282",
        "name":"Expression Add Operators",
        "desc":''' Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
        ''',
        "type":["Backtracking"],
        "solution":'''
def calc(idx, cur, pre, path):
            if idx == len(num):
                if cur + pre == target:
                    self.ans.append("".join(map(str, path)))
                return
            n = 0
            for i in xrange(idx, len(num)):
                n *= 10
                n += ord(num[i])-0x30
                path += ['+', n]
                calc(i+1, cur + pre, n, path)
                path.pop()
                path.pop()
                path += ['-', n]
                calc(i+1, cur + pre, -n, path)
                path.pop()
                path.pop()
                path += ['*', n]
                calc(i+1, cur, pre*n, path)
                path.pop()
                path.pop()
                if num[idx] == '0':
                    break

        n = 0
        for i in xrange(len(num)):
            n *= 10
            n += ord(num[i])-0x30
            calc(i+1, 0, n, [n])
            if num[0] == '0':
                break
        '''
        },
        {
        "id":"281",
        "name":"Zigzag Iterator",
        "desc":'''
        ''',
        "type":["Design"],
        "solution":'''
    def __init__(self, v1, v2):
        self.v = [v1, v2]
        self.ids = [0, 1]
        self.idx = 0
        self.q = Queue()
        self.push()
    def push(self):
        nxt = []
        for i in self.ids:
            if self.idx < len(self.v[i]):
                self.q.put(self.v[i][self.idx])
                nxt.append(i)
        self.ids = nxt
        self.idx += 1
    def next(self):
        ans = self.q.get()
        if self.q.empty(): self.push()
        return ans
    def hasNext(self):
        return not self.q.empty()
        '''
        },
        {
        "id":"280",
        "name":"Wiggle Sort",
        "desc":'''
        ''',
        "type":["Sort"],
        "solution":'''
        def partition3way(a, lo, hi):
            m = random.randrange(lo, hi)
            v = a[m]
            lt, gt, i = lo, hi, lo
            while i <= gt:
                c = cmp(a[i], v)
                if c < 0:
                    exch(a, lt, i)
                    lt += 1
                    i += 1
                elif c > 0:
                    exch(a, gt, i)
                    gt -= 1
                else:
                    i += 1
            return lt, gt

        def midDiv(a):
            lo, hi = 0, len(a)-1
            m = len(a) >> 1
            while lo < hi:
                lt, gt = partition3way(a, lo, hi)
                if m < lt:
                    hi = lt-1
                elif gt < m:
                    lo = gt+1
                else:
                    return
        '''
        },
        {
        "id":"279",
        "name":"Perfect Squares",
        "desc":''' Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.  For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
        ''',
        "type":["DP"],
        "solution":'''
        i = 1
        a = [1]
        while a[-1] < n:
            i+=1
            a.append(i**2)
        marked = [0 for i in xrange(n+1)]
        q = [0]
        cnt = 0
        while 1:
            cnt += 1
            nxt = []
            for num in q:
                for d in a:
                    if num+d == n:
                        return cnt
                    if num+d < n and not marked[num+d]:
                        marked[num+d] = 1
                        nxt.append(num+d)
            q = nxt
        '''
        },
        {
        "id":"276",
        "name":"Paint Fence",
        "desc":''' 
        ''',
        "type":["DP"],
        "solution":'''
        if n == 1: return k
        if k == 1:
            if n > 2: return 0
            else: return 1
        dp = [0] * n
        dp[0] = k
        dp[1] = k*k
        for i in xrange(2,n):
            dp[i] = (dp[i-1]+dp[i-2])*(k-1)
    
        return dp[n-1]
        '''
        },
        {
        "id":"274",
        "name":"H-Index",
        "desc":'''A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each. 
        ''',
        "type":["Sort", "Hash"],
        "solution":'''
        n = len(citations)
        a = [0 for i in xrange(n+1)]
        for i in xrange(n):
            if citations[i]>=n:
                a[n]+=1
            else:
                a[citations[i]]+=1
        s = 0
        for i in xrange(1,n+1):
            s += a[n+1-i]
            if s >= n+1-i:
                return n+1-i

        return 0
        '''
        },
        {
        "id":"272",
        "name":"Closest Binary Search Tree Value II",
        "desc":''' k closest value
        ''',
        "type":["Stack", "BST"],
        "solution":'''
        def visitL(node):
            if len(self.small_k) == k or not node: return
            visitL(node.right)
            if len(self.small_k) < k: self.small_k += [node.val]
            visitL(node.left)

        def floorK(node):
            if not node: return
            if node.val <= target:
                floorK(node.right)
                if len(self.small_k) < k: self.small_k += [node.val]
                visitL(node.left)
                return
            return floorK(node.left)

        def visitR(node):
            if len(self.great_k) == k or not node: return
            visitR(node.left)
            if len(self.great_k) < k: self.great_k += [node.val]
            visitR(node.right)

        def ceilK(node):
            if not node: return
            if node.val >= target:
                ceilK(node.left)
                if len(self.great_k) < k: self.great_k += [node.val]
                visitR(node.right)
                return
            return ceilK(node.right)
        '''
        },
        {
        "id":"271",
        "name":"Encode and Decode Strings",
        "desc":'''
        ''',
        "type":["Design"],
        "solution":'''
    def encode(self, strs):
        ans = ""
        for s in strs:
            ans += str(len(s))
            ans += '#'
            ans += s
        return ans

    def decode(self, s):
        ans = []
        cnt = 0
        n = len(s)
        i = 0
        while i < n:
            ch = s[i]
            if ch in '1234567890':
                cnt *= 10
                cnt += ord(ch)-0x30
                i += 1
            elif ch == '#':
                ans += [s[i+1:i+1+cnt]]
                i += cnt+1
                cnt = 0
        return ans
        '''
        },
        {
        "id":"270",
        "name":"Closest Binary Search Tree Value",
        "desc":'''
        ''',
        "type":["BST"],
        "solution":'''
        def floor(root, target):
            if not root: return 
            if root.val == target: return root
            if root.val > target: return floor(root.left, target)
            r = floor(root.right, target)
            if r: return r
            else: return root
        
        def ceil(root, target):
            if not root: return
            if root.val == target: return root
            if root.val < target: return ceil(root.right, target)
            l = ceil(root.left, target)
            if l: return l
            else: return root
        '''
        },
        {
        "id":"269",
        "name":"Alien Dictionary",
        "desc":'''
        ''',
        "type":["Topological Sort"],
        "solution":'''
        vertices = [0]*26
        adj = [ set() for _ in xrange(26) ]
        for w in words:
            for ch in w:
                vertices[ord(ch)-0x61]=1

        def addEdge(w1, w2):
            for i in xrange(min(len(w1),len(w2))):
                if w1[i] != w2[i]:
                    adj[ord(w1[i])-0x61].add(ord(w2[i])-0x61)
                    return

        if len(words) == 0: return ''
        for w1, w2 in zip(words[:-1], words[1:]): addEdge(w1, w2)

        unfinish = [0] * 26
        marked = [0] * 26
        self.post = []
        self.cycle = 0

        def dfs(v):
            marked[v] = 1
            unfinish[v] = 1
            for w in adj[v]:
                if self.cycle: return
                if not marked[w]: 
                    dfs(w)
                if marked[w] and unfinish[w]: 
                    self.cycle = 1
                    return

            unfinish[v] = 0
            self.post += [v]

        for i in xrange(26):
            if vertices[i] and not marked[i]:
                dfs(i)
        if self.cycle: return ""
        '''
        },
        {
        "id":"266",
        "name":"Palindrome Permutation",
        "desc":'''
        ''',
        "type":["Hash"],
        "solution":'''
        dct = {}
        for ch in s:
            if ch in dct: dct[ch]+=1
            else: dct[ch]=1
        cnt = 0
        for k in dct.keys():
            if dct[k] & 1 == 1:
                if cnt: return False
                cnt += 1
        return True
        '''
        },
        {
        "id":"261",
        "name":"Graph Valid Tree",
        "desc":'''
        ''',
        "type":["Graph"],
        "solution":'''
        adj = [ [] for _ in xrange(n) ]
        if len(edges) < n-1: return False
        for v, w in edges:
            adj[v].append(w)
            adj[w].append(v)
        marked = [0] * n

        def dfs(v, last):
            marked[v] = 1
            for w in adj[v]:
                if w != last:
                    if not marked[w]: 
                        if not dfs(w, v): return False
                    else: return False
            return True

        if not dfs(0, -1): return False
        for i in xrange(n):
            if not marked[i]:
                return False
        return True
        '''
        },
        {
        "id":"259",
        "name":"3Sum Smaller",
        "desc":'''
        ''',
        "type":["Two Pointers"],
        "solution":'''
        nums.sort()
        n = len(nums)
        if n < 3: 
            return 0
        ans = 0
        for i in xrange(n-2):
            lo, hi = i+1, n-1
            while lo < hi:
                if sum([nums[i], nums[lo], nums[hi]]) < target:
                    ans += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return ans
        '''
        },
        {
        "id":"257",
        "name":"Binary Tree Paths",
        "desc":'''Given a binary tree, return all root-to-leaf paths.
        ''',
        "type":["Tree"],
        "solution":'''
    def visit(self, x, path):
        if not x:
            return
        if not path:
            path = str(x.val)
        else:
            path += '->' + str(x.val)
        if x.left == None and x.right == None:
            self.ans.append(path)
            return
        self.visit(x.left, path)
        self.visit(x.right, path)
        '''
        },
        {
        "id":"253",
        "name":"Meeting Rooms II",
        "desc":'''
        ''',
        "type":["Sort"],
        "solution":'''
        arr = []
        for i in intervals:
            arr.append((i.start, 1))
            arr.append((i.end, 0))
        arr.sort()
        cur = 0
        ans = 0
        for i, t in arr:
            if t == 1:
                cur += 1
            else:
                cur -= 1
            ans = max(ans, cur)

        return ans
        '''
        },
        {
        "id":"251",
        "name":"Flatten 2D Vector",
        "desc":'''
        ''',
        "type":["Design"],
        "solution":'''
    def __init__(self, vec2d):
        self.data = [ v for v in vec2d if len(v) != 0]
        self.i = 0
        self.j = 0

    def next(self):
        ret = self.data[self.i][self.j]
        self.j += 1
        if self.j == len(self.data[self.i]):
            self.i += 1
            self.j = 0
        return ret

    def hasNext(self):
        return self.i < len(self.data) and self.j < len(self.data[self.i])
        '''
        },
        {
        "id":"249",
        "name":"Group Shifted Strings",
        "desc":''' az - ba, a - z
        ''',
        "type":["Hash"],
        "solution":'''
        def getKey(s):
            a = ord(s[0])
            key = 1
            for ch in s:
                key <<= 4
                t = ord(ch)-a
                if t < 0:
                    t += 26
                key += t
            return key

        for s in strings:
            k = getKey(s)
            if k in ans:
                ans[k].append(s)
            else:
                ans[k] = [s]
        ret = []
        for k in ans:
            ans[k].sort()
            ret.append(ans[k])
        return ret
        '''
        },
        {
        "id":"247",
        "name":"Strobogrammatic Number II",
        "desc":''' 
        ''',
        "type":["Backtracking"],
        "solution":'''
        def find(n): 
            if n == 0: return []
            if n == 1: return ['0','1','8']
            ans = []
            t = find(n-2)
            if t:
                for s in t:
                    for c in dct:
                        ans += [c+s+dct[c]]
            else:
                for c in dct:
                    ans += [c+dct[c]]
                        
            return ans

        candi = find(n)
        ans = []
        for n in candi:
            if n[0] != '0':
                ans += [n]
        return ans
        '''
        },
        {
        "id":"246",
        "name":"Strobogrammatic Number",
        "desc":''' 
        ''',
        "type":["Hash"],
        "solution":'''
        dct = {'6':'9', '9':'6', '0':'0', '1':'1', '8':'8'}
        i, j = 0, len(num)-1
        while i <= j:
            if num[i] in dct and num[j] in dct and dct[num[i]] == num[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        '''
        },
        {
        "id":"240",
        "name":"Search a 2D Matrix II",
        "desc":''' 
        ''',
        "type":["Binary Search"],
        "solution":'''
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False 

        i, j = 0, n-1
        while i < m and j >= 0: 
            c = cmp(target, matrix[i][j])
            if c == 0:
                return True
            elif c < 0:
                j-=1
            else:
                i+=1
        return False
        '''
        },
        {
        "id":"230",
        "name":"Kth Smallest Element in a BST",
        "desc":''' 
        ''',
        "type":["BST"],
        "solution":'''
    def visit(self, x, k):
        if not x or self.ans:
            return
        self.visit(x.left, k)
        self.idx += 1
        if self.idx == k:
            self.ans = x.val
            return
        self.visit(x.right, k)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ans = None
        self.idx = 0
        self.visit(root, k)
        return self.ans
        '''
        },
        {
        "id":"228",
        "name":"Summary Ranges",
        "desc":''' Given a sorted integer array without duplicates, return the summary of its ranges.
        ''',
        "type":["Array"],
        "solution":'''
        if not nums:
            return []
        start = nums[0]
        last = nums[0]
        ret = []
        for n in nums[1:]:
            if n == last + 1:
                last += 1
            else:
                if start != last:
                    ret.append("%d->%d" % (start, last))
                else:
                    ret.append(str(start))
                start = n
                last = n

        if start != last:
            ret.append("%d->%d" % (start, last))
        else:
            ret.append(str(start))
        '''
        },
        {
        "id":"224",
        "name":"Basic Calculator",
        "desc":''' Implement a basic calculator to evaluate a simple expression string. The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
        ''',
        "type":["Stack"],
        "solution":'''
        ans = 0
        plus = 1
        n = 0
        stack = []
        for ch in s:
            if ch == ' ':
                continue
            elif ch == '(':
                stack.append((ans, plus))
                ans = 0
                plus = 1
            elif ch == ')':
                n = ans + plus * n
                ans, plus = stack.pop()
            elif ch == '+':
                ans += (plus * n)
                plus = 1
                n = 0
            elif ch == '-':
                ans += (plus * n)
                plus = -1
                n = 0
            else:
                n *= 10
                n += int(ch)
        ans += (plus * n)
        '''
        },
        {
        "id":"218",
        "name":"The Skyline Problem",
        "desc":''' A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
        ''',
        "type":["Heap"],
        "solution":'''
        ret = []
        LRH = buildings
        i, n = 0, len(buildings)
        alivesHR = []
        
        while i < n or alivesHR:
            if not alivesHR or (i < n and -alivesHR[0][1] >= LRH[i][0] ):
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(alivesHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
                h = -alivesHR[0][0]
                if not ret or ret[-1][1] != h:
                    ret.append([x, h])
            else:
                x = -alivesHR[0][1]
                while alivesHR and -alivesHR[0][1] <= x:
                    heappop(alivesHR)

                if not alivesHR:
                    h = 0
                else:
                    h = -alivesHR[0][0]
                if ret[-1][1] != h:
                    ret.append([x, h])
        return ret
        '''
        },
        {
        "id":"214",
        "name":"Shortest Palindrome",
        "desc":''' Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
        ''',
        "type":["String"],
        "solution":'''
        t = s + '#' + s[::-1]
        nxt = [0]
        for i in range(1, len(t)):
            x = nxt[i-1]
            while x > 0 and t[i] != t[x]:
                x = nxt[x-1]
            if t[i] == t[x]:
                nxt.append(x + 1)
            else:
                nxt.append(0)
        n = nxt[-1]
        return s[len(s):n-1:-1]+s
        '''
        },
        {
        "id":"208",
        "name":"Implement Trie",
        "desc":''' Implement a trie with insert, search, and startsWith methods.
        ''',
        "type":["Trie"],
        "solution":'''
class Trie(object):

    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self.put(self.root, word, 0)

    def put(self, x, word, d):
        if not x: x = TrieNode()
        if d == len(word):
            x.val = 1
            return x
        ch = word[d]
        x.next[ord(ch)-0x61] = self.put(x.next[ord(ch)-0x61], word, d+1)
        return x
        
    def search(self, word):
        x = self.root
        if not x: return False
        for w in word:
            if x.next[ord(w)-0x61]: x = x.next[ord(w)-0x61]
            else: return False
        return x.val != None
        
    def startsWith(self, prefix):
        x = self.root
        if not x: return False
        for w in prefix:
            if x.next[ord(w)-0x61]: x = x.next[ord(w)-0x61]
            else: return False
        return True
        '''
        },
        {
        "id":"200",
        "name":"Number of Islands",
        "desc":''' Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
        ''',
        "type":["DFS", "BFS", "Union Find"],
        "solution":'''
        self.m = m
        self.n = n

        cnt = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, i, j)
        return cnt
        
    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if x >= 0 and x < self.m and y >= 0 and y < self.n and grid[x][y] == '1':
                self.dfs(grid, x, y)
        '''
        },
        {
        "id":"173",
        "name":"Binary Search Tree Iterator",
        "desc":''' Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
        ''',
        "type":["BST", "Stack", "Design"],
        "solution":'''
    def __init__(self, root):
        self.s = []
        x = root
        while x:
            self.s.append(x)
            x = x.left

    def hasNext(self):
        return len(self.s) != 0

    def next(self):
        x = self.s.pop()
        r = x.right
        while r:
            self.s.append(r)
            r = r.left
        return x.val
        '''
        },
        {
        "id":"166",
        "name":"Fraction to Recurring Decimal",
        "desc":''' Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.  If the fractional part is repeating, enclose the repeating part in parentheses.
        ''',
        "type":["Hash"],
        "solution":'''
		l = len(str(denominator))
		n = 10 ** l
		p = numerator / denominator
		q = numerator % denominator
		ans = str(p) + "."
        dct = set()
		while q not in dct:
			dct.add(q)
			q += n
			s = str(q / denominator)
			a = ['0' for i in xrange(l - len(s))]
			ans += ''.join(a)
			ans += s
			q %= denominator
		if q == 0:
			if ans[-2] == '.': ans = ans[:-2]
			else: ans = ans[:-1]
		else:
			i = ans.rfind(str(q))
			ans = ans[:i] + '(' + ans[i:] + ')'
		return ans
        '''
        },
        {
        "id":"163",
        "name":"Missing Ranges",
        "desc":''' [0, 1, 3, 50, 75], 0, 99 ==> [2, 4->49, 51->74, 76->99]
        ''',
        "type":["Array"],
        "solution":'''
        start = lower
        nums.append(upper+1)
        ans = []
        for num in nums:
            if num == start:
                pass
            elif num == start+1:
                ans += [str(start)]
            else:
                ans += [str(start)+'->'+str(num-1)]
            start = num + 1
        return ans
        '''
        },
        {
        "id":"162",
        "name":"Find Peak Element",
        "desc":''' A peak element is an element that is greater than its neighbors.  Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.  The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
        ''',
        "type":["Binary Search"],
        "solution":'''
		n = len(nums)
		if n <= 1:
			return 0
		for i in range(1, n):
			if nums[i-1] > nums[i]:
				return i-1
		return n-1
        ------
		n = len(nums)
		l, r = 0, n-1
		while l <= r:
			m = (l+r) >> 1
			if l == r:
				return l
			if nums[m]<nums[m+1]:
				l = m+1
			else:
				r = m
        '''
        },
        {
        "id":"159",
        "name":"Longest Substring with At Most Two Distinct Characters",
        "desc":'''
        ''',
        "type":["DP"],
        "solution":'''
        n = len(s)
        if n <= 2: return n
        dp = [ [0]*2 for i in xrange(n) ]
        ss = [s[0]]
        dp[0][0] = 1
        dp[0][1] = 1

        for i in xrange(1,n):
            if s[i] == s[i-1]:
                dp[i][0] = dp[i-1][0]+1
                dp[i][1] = dp[i-1][1]+1
            else:
                dp[i][0] = 1
                if s[i] in ss:
                    dp[i][1] = dp[i-1][1]+1
                else:
                    dp[i][1] = dp[i-1][0]+1
                    ss = [s[i-1], s[i]]
        return max(dp[i][1] for i in xrange(n))
        '''
        },
        {
        "id":"158",
        "name":"Read N Characters Given Read4 II",
        "desc":'''
        ''',
        "type":["Design"],
        "solution":'''
    def __init__(self):
        self.remain = 0
        self.cur = 0
        self.buf4 = ['']*4

    def read(self, buf, n):
        total = 0

        while total < n:
            if self.remain == self.cur:
                self.remain = read4(self.buf4)
                self.cur = 0
                if self.remain == 0:
                    return total
            buf[total] = self.buf4[self.cur]
            self.cur += 1
            total += 1
            
        return total
        '''
        },
        {
        "id":"155",
        "name":"Min Stack",
        "desc":'''
        ''',
        "type":["Design"],
        "solution":'''
	def __init__(self):
		self.stack = []
		self.mins = []

	def push(self, x):
		self.stack.append(x)        
		if self.mins == [] or x <= self.mins[-1]:
			self.mins.append(x)

	def pop(self):
		t = self.stack.pop()
		if t == self.mins[-1]:
			self.mins.pop()

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.mins[-1]
        '''
        },
        {
        "id":"146",
        "name":"LRU Cache",
        "desc":'''
        ''',
        "type":["Design"],
        "solution":'''
	def __init__(self, capacity):
		self.capacity = capacity - 1
		self.n = 0
		self.head = None
		self.tail = None
		self.map = {}

	def get(self, key):
		if self.capacity == -1 or self.head == None or key not in self.map:
			return -1
		if self.head.key == key:
			return self.head.val
		if self.tail.key == key:
			t = self.tail
			self.tail = self.tail.prev
			t.prev = None
			t.next = self.head
			self.head.prev = t
			self.head = t
			return self.head.val

		cur = self.map[key]
		
		cur.prev.next = cur.next
		cur.next.prev = cur.prev

		cur.next = self.head
		self.head.prev = cur
		cur.prev = None
		self.head = cur
		return self.head.val

	def set(self, key, value):
		if self.head == None:
			self.head = ListNode(key, value)
			self.tail = self.head
			self.map[key] = self.head
			return
		cur = self.head
		if cur.key == key:
			cur.val = value
			return

		if self.get(key) == -1:
			# not found
			t = ListNode(key, value)
			self.map[key] = t
			t.next = self.head
			self.head.prev = t
			self.head = t
			if self.n < self.capacity:
				self.n += 1
			else:
				self.map.pop(self.tail.key)
				p = self.tail.prev
				p.next = None
				self.tail = p
		else:
			# found, already move to head
			self.head.val = value
        '''
        },
        {
        "id":"140",
        "name":"Word Break II",
        "desc":''' Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.  Return all such possible sentences.
        ''',
        "type":["DP"],
        "solution":'''
		n = len(s)
		a = []
		for i in range(n+1):
			a.append([0 for i in range(n+1)])
		dp = [0 for i in range(n+1)]
		dp[0] = 1
		for i in range(n):
			for j in range(i+1, n+1):
				if dp[i] and s[i:j] in wordDict:
					dp[j] = 1
					a[i][j] = 1

		self.ans = []
		if not dp[n]:
			return self.ans
		self.dfs(a, 0, n, [])
		r = []
		for ss in self.ans:
			last = 0
			t = ""
			for i in ss:
				t += s[last:i] + " "
				last = i
			r.append(t[:-1])
		return r

		
	def dfs(self, a, cur, n, route):
		if cur == n:
			self.ans.append(copy.copy(route))
			return
		for i in range(cur+1, n+1):
			if a[cur][i] == 1:
				route.append(i)
				self.dfs(a, i, n, route)
				route.pop()
        '''
        },
        {
        "id":"66",
        "name":"Plus One",
        "desc":''' Given a non-negative number represented as an array of digits, plus one to the number.  The digits are stored such that the most significant digit is at the head of the list.
        ''',
        "type":["Array"],
        "solution":'''
		for i in digits:
			if i != 9:
				break
        else:
			return [1] + ([0] * len(digits))

		for i in range(len(digits)-1,-1,-1):
			if digits[i] == 9: digits[i] = 0
			else:
				digits[i] += 1
		        return digits
        '''
        },
        {
        "id":"57",
        "name":"Insert Interval",
        "desc":''' Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
        ''',
        "type":["Sort"],
        "solution":'''
		start = newInterval.start
		end = newInterval.end
		t = ''
		ans = []
		if len(intervals) == 0:
			return [newInterval]

		for i in intervals:
			if t == '' and start > i.end:
				ans.append(i)
			elif t == '' and end < i.start:
				t = 'x'
				ans.append(newInterval)
				ans.append(i)
			elif t == '' and start < i.start and end <= i.end:
				t = 'x'
				newInterval.end = i.end
				ans.append(newInterval)
			elif t == '' and start >= i.start and end <= i.end:
				t = 'x'
				ans.append(i)
			elif t == '' and start > i.start:
				t = 'i'
				newInterval.start = i.start
			elif t == '' and start <= i.start:
				t = 'i'
			elif t == 'i' and end > i.end:
				pass
			elif t == 'i' and end >= i.start and end <= i.end:
				newInterval.end = i.end
				ans.append(newInterval)
				t = 'x'
			elif t == 'i':
				ans.append(newInterval)
				ans.append(i)
				t = 'x'
			elif t == 'x':
				ans.append(i)
		if newInterval.end > intervals[-1].end:
			ans.append(newInterval)
		return ans
        '''
        },
        {
        "id":"56",
        "name":"Merge Intervals",
        "desc":''' Given a collection of intervals, merge all overlapping intervals.
        ''',
        "type":["Sort"],
        "solution":'''
		l = []
		ans = []
		for i in intervals:
			l.append((i.start, 0))
			l.append((i.end, 1))
		l.sort()
		s = []
		for a, b in l:
			if b == 0: s.append(a)
			else:
				t = s.pop()
				if len(s) == 0:
					i = Interval(t, a)
					ans.append(i)
		return ans
        '''
        },
        {
        "id":"44",
        "name":"Wildcard Matching",
        "desc":''' Implement wildcard pattern matching with support for '?' and '*'.
        ''',
        "type":["Backtracking"],
        "solution":'''
		l1 = len(s)
		l2 = len(p)
		if (l1 == 0 and l2 == 0) or (l1 == 1 and l2 == 1 and p[0] == '?') or (l1 == 1 and l2 == 1 and p[0] == '*') or (l1 == 1 and l2 == 1 and s[0] == p[0]):
			return True
		elif l1 > 0 and l2 == 0: return False
		firstf = False
		endf = False
		if p[0] != '*': firstf = True
		if p[l2-1] != '*': endf = True
		ps = p.split('*')
		while '' in ps: ps.remove('')
		for i in xrange(len(ps)):
			t = self.find(s, ps[i])
			if i == 0 and firstf:
				if t != 0: return False
			elif i == len(ps)-1 and endf:
				t = self.find(s[len(s)-len(ps[i]):], ps[i])
				if t != 0: return False
				else: return True
			if t == -1: return False
			s = s[t+len(ps[i]):]
		if firstf and endf and len(s) > 0: return False
		else: return True

	def find(self, s, p):
		for i in xrange(len(s)-len(p)+1):
			f = True
			for j in xrange(len(p)):
				if s[i+j] != p[j] and p[j] != '?':
					f = False
			if f:
				return i
		return -1
        '''
        },
        {
        "id":"23",
        "name":"Merge k Sorted Lists",
        "desc":'''Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
        ''',
        "type":["Divide and Conquer", "Heap"],
        "solution":'''
from Queue import PriorityQueue
		n = len(lists)
		pq = PriorityQueue()
		for i in xrange(n):
			if lists[i] != None:
				pq.put( (lists[i].val, i) )
				lists[i] = lists[i].next
		curr = ListNode(-1)
		head = curr
		
		while pq.qsize() > 0:
			val, i = pq.get()
			t = ListNode(val)
			curr.next = t
			curr = t
			if lists[i] != None:
				pq.put( (lists[i].val, i) )
				lists[i] = lists[i].next

		return head.next
        '''
        },
        {
        "id":"22",
        "name":"Generate Parentheses",
        "desc":''' Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.  For example, given n = 3, a solution set is: "((()))", "(()())", "(())()", "()(())", "()()()"
        ''',
        "type":["Backtracking"],
        "solution":'''
	def solve(self, cur, n, stk, res, ans):
		if cur == n and len(res) == n * 2:
			ans.append(res)
			return
		if stk > 0:
			stk -= 1
			self.solve(cur, n, stk, res + ")", ans)
			stk += 1
		if cur < n:
			cur += 1
			stk += 1
			self.solve(cur, n, stk, res + "(", ans)
			stk -= 1
			cur -= 1
        '''
        },
        {
        "id":"20",
        "name":"Generate Parentheses",
        "desc":''' Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
        ''',
        "type":["Stack"],
        "solution":'''
		stack = []
		for i in s:
			if i in '{([': stack.append(i)
			elif i in '})]':
				if len(stack) == 0: return False
				j = stack.pop()
				if (i == '}' and j == '{') or (i == ')' and j == '(') or (i == ']' and j == '['): continue
				else: return False
			else:
				return False
	    return len(stack) == 0
        '''
        },
        {
        "id":"4",
        "name":"Median of Two Sorted Arrays",
        "desc":''' There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
        ''',
        "type":["Binary Search"],
        "solution":'''
	def mid(self, A):
		l = len(A)
		if l == 0: return 0
		if l % 2 == 0: return (A[l/2-1]+A[l/2])/2.
		else: return A[l/2]

	def find3m(self, A):
        A.sort()
		return A[1]

	def find4m(self, A):
        A.sort()
		return (A[1]+A[2])/2.

	def findMedianSortedArrays(self, A, B):
		la, lb = len(A), len(B)
		ma, mb = self.mid(A), self.mid(B)
		if la == lb == 1: return (A[0]+B[0])/2.
		if la == 0: return mb
		if lb == 0: return ma
		if ma == mb: return ma
		if la > lb:
            A, B = B, A
            ma, mb = mb, ma
            la, lb = lb, la

		if la == 1 and lb % 2 == 0:
			if A[0] >= B[lb/2-1] and A[0] <= B[lb/2]: return A[0]
			elif A[0] < B[lb/2-1]: return B[lb/2-1]
			elif A[0] > B[lb/2]: return B[lb/2]
		elif la == 1 and lb % 2 == 1:
			if A[0] >= B[lb/2-1] and A[0] <= B[lb/2+1]: return (A[0]+B[lb/2])/2.
			elif A[0] < B[lb/2-1]: return (B[lb/2-1]+B[lb/2])/2.
			elif A[0] > B[lb/2+1]: return (B[lb/2+1]+B[lb/2])/2.
		elif la == 2 and lb == 2:
			return self.find4m(A+B)
		elif la == 2 and lb % 2 == 0:
			return self.find4m([B[lb/2], B[lb/2-1], max(A[0], B[lb/2-2]), min(A[1], B[lb/2+1])])
		elif la == 2 and lb % 2 == 1:
			return self.find3m([max(A[0], B[lb/2-1]), min(A[1], B[lb/2+1]), B[lb/2]])

		if la % 2 == 0:
			k = la / 2 - 1
		else:
			k = la / 2
		if ma > mb:
			return self.findMedianSortedArrays(A[:la-k], B[k:])
		else:
			return self.findMedianSortedArrays(A[k:], B[:lb-k])		
        '''
        }
        ]

