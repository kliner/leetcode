# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  n1, n2 = 0, 0
  if not l1
    return l2
  end
  if not l2
    return l1
  end
    
  a = l1
  carry = 0
  while l1 and l2
    l1.val += l2.val + carry
    if l1.val >= 10
      carry = 1
      l1.val -= 10
    else
      carry = 0
    end
    end1 = l1
    end2 = l2
    l1 = l1.next
    l2 = l2.next
  end
  if l2
    end1.next = l2
  end
  last = end1
  end1 = end1.next
  while end1 and (carry == 1)
    end1.val += carry
    if end1.val == 10
      end1.val = 0
    else
      carry = 0
    end
    last = end1
    end1 = end1.next
  end
  if carry == 1
    last.next = ListNode.new(1)
  end
  return a
end

def pr(n)
  while n
    p n.val
    n = n.next
  end
  p '---'
end

l1 = nil
l2 = nil
pr(add_two_numbers(l1, l2))
l1 = ListNode.new(2)
l1.next = ListNode.new(4)
l1.next.next = ListNode.new(3)
pr(add_two_numbers(l1, l2))
l2 = ListNode.new(5)
l2.next = ListNode.new(6)
l2.next.next = ListNode.new(4)
pr(add_two_numbers(l1, l2))
l1 = ListNode.new(2)
pr(add_two_numbers(l1, l2))
l2 = ListNode.new(5)
l1 = ListNode.new(2)
l1.next = ListNode.new(4)
l1.next.next = ListNode.new(3)
pr(add_two_numbers(l1, l2))
l2 = ListNode.new(1)
l1 = ListNode.new(9)
l1.next = ListNode.new(9)
l1.next.next = ListNode.new(9)
pr(add_two_numbers(l1, l2))
l1 = ListNode.new(1)
l2 = ListNode.new(9)
l2.next = ListNode.new(9)
l2.next.next = ListNode.new(9)
pr(add_two_numbers(l1, l2))
l2 = ListNode.new(1)
l1 = ListNode.new(9)
pr(add_two_numbers(l1, l2))
l2 = ListNode.new(9)
l1 = ListNode.new(9)
pr(add_two_numbers(l1, l2))
