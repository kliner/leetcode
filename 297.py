# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        ans = []
        while q:
            nxt = []
            for cur in q:
                if cur:
                    ans += [str(cur.val)]
                    nxt += [cur.left, cur.right]
                else:
                    ans += ['null']
            q = nxt
        return ','.join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s = data.split(',')
        if len(s) == 0 or s[0] == 'null':
            return None
        root = TreeNode(s[0])
        i = 1
        q = [root]
        while q:
            nxt = []
            for j, cur in enumerate(q):
                if s[i+j*2] == 'null':
                    cur.left = None
                else:
                    cur.left = TreeNode(s[i+j*2])
                if s[i+j*2+1] == 'null':
                    cur.right = None
                else:
                    cur.right = TreeNode(s[i+j*2+1])
                if cur.left:
                    nxt += [cur.left]
                if cur.right:
                    nxt += [cur.right]
            i += len(q)*2
            q = nxt
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    codec = Codec()
    print codec.serialize(None)
    codec.deserialize(codec.serialize(None))
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    a = codec.serialize(root)
    print a
    t = codec.deserialize(a)
    print t.val
    print t.left.val
    print t.left.right.val
