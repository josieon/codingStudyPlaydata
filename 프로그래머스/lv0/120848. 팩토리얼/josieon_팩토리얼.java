// import java.util.*;
class Solution {
    public int solution(int n) {
        int[] fac = new int[12];
        fac[0] = 1;
        for(int i = 1; i < 12; i++)
            fac[i] = fac[i-1] * i;
        int answer = 0;
        while(fac[answer] <= n)
            answer++;
        // System.out.println(Arrays.toString(fac));
        return answer-1;
    }
}