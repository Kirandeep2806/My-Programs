class Solution {
    public int search(int[] nums, int target) {
        int low=0, high=nums.length-1, mid=-1;
        boolean found=false;
        while(low <= high) {
            mid = (low+high)/2;
            if(nums[mid] == target) {
                found = true;
                break;
            }
            else if(nums[mid] > target)
                high = mid-1;
            else
                low = mid+1;
        }
        if(!found)
            return -1;
        return mid;
    }
}
