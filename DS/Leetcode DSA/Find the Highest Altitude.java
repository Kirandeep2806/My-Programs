class Solution {
    public int largestAltitude(int[] gain) {
        int n = gain.length, max_altitude=0, curr_altitude = 0;
        for(int i=0; i<n; i++) {
            curr_altitude += gain[i];
            if(max_altitude < curr_altitude)
                max_altitude = curr_altitude;
        }
        return max_altitude;
    }
}