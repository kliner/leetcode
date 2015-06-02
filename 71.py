class Solution:
	# @param {string} path
	# @return {string}
	def simplifyPath(self, path):
		ss = path.split('/')
		ans = []
		for s in ss:
			if s == '' or s == '.':
				continue
			elif s == '..':
				if len(ans) > 0:
					ans.pop()
			else:
				ans.append(s)
		ret = ''
		for s in ans:
			ret += '/' + s
		if ret == '':
			ret = '/'
		return ret

test = Solution()
print test.simplifyPath("/../")
print test.simplifyPath("/home//foo/")
print test.simplifyPath("/a/./b/../../c/")

