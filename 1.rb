# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  dct = {}
  for num in nums
    dct[num] = 1
  end
  for num in nums
    if dct.has_key?(target-num)
      a = [num, target-num]
      return a.min, a.max
    end
  end
end

p two_sum([2, 7, 11, 15], 9)
