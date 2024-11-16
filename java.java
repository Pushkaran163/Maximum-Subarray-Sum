public class java {

    // Approach 1: Brute Force

    public static int maxsubarraySum(int[] arr){
        int n = arr.length;
        int maxsum = arr[0];
        for(int i=0; i<n; i++){
            int currsum = 0;
            for(int j=i;j<n;j++){
                currsum = currsum + arr[i];
                maxsum = Math.max(maxsum, currsum);
            }
        }
        return maxsum;
    }

    // Approach 2: Kadane's Algorithm

    public static int maxsubarraySum2(int[] arr){
        int n = arr.length;
        int maxsum = 0;
        int currsum = 0;

        for(int i=0; i<n; i++){
            currsum = Math.max(currsum + arr[i]. arr[i]);
            maxsum = Math.max(maxsum, currsum);
        }
        return maxsum;
    }
}
