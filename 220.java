import java.util.TreeSet;

public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Integer> set = new TreeSet<>();
        if (nums == null || t < 0)
            return false;
        int n = nums.length;
        for (int i = 0; i < k; i++){
            if (set.contains(nums[i])) {
                return true;
            } else {
                Integer floor = set.floor(nums[i]);
                Integer ceil = set.ceiling(nums[i]);
                if (floor != null && floor >= nums[i] - t)
                    return true;
                else if (ceil != null && ceil <= nums[i] + t)
                    return true;
                set.add(nums[i]);
            }
        }
        for (int i = k; i < n; i ++) {
            if (set.contains(nums[i])) {
                return true;
            } else {
                Integer floor = set.floor(nums[i]);
                Integer ceil = set.ceiling(nums[i]);
                if (floor != null && floor >= nums[i] - t)
                    return true;
                else if (ceil != null && ceil <= nums[i] + t)
                    return true;
                set.add(nums[i]);
                set.remove(nums[i-k]);
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.containsNearbyAlmostDuplicate(new int[]{1, 2, 1}, 1, 0 ));
        System.out.println(solution.containsNearbyAlmostDuplicate(new int[]{1, 2, 1}, 2, 0 ));
        System.out.println(solution.containsNearbyAlmostDuplicate(new int[]{1, 9, 2}, 2, 0 ));
        System.out.println(solution.containsNearbyAlmostDuplicate(new int[]{1, 9, 2}, 2, 1 ));
    }
}

