import java.util.*;
class Solution {
    public int solution(int n) {
        ArrayList<Integer> arr = new ArrayList();
        while(n != 0){
            arr.add(n % 3);
            n /= 3;
        }
        int answer = 0;
        for(int i=0; i < arr.size(); i++){
            if(arr.get(i) == 0)
                continue;
            answer += Math.pow(3, arr.size() - i - 1) * arr.get(i);
        }
        return answer;
    }
}