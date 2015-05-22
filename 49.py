class Solution:
	# @param {string[]} strs
	# @return {string[]}
	def anagrams(self, strs):
		dic = {}
		ans = []
		for s in strs:
			a = list(s)
			a.sort()
			k = ''
			for i in a:
				k += i
			if k in dic:
				dic[k].append(s)
			else:
				dic[k] = [s]
		for s in dic.keys():
			if len(dic[s]) > 1:
				ans.extend(dic[s])
		return ans

test = Solution()
print test.anagrams(['12321','1234321','123','23432', '321', '13221'])
