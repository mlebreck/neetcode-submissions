class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> map = new HashSet<>();

        for (int num : nums) {
            if (!map.add(num)) return true;
        }
        return false;
    }
}