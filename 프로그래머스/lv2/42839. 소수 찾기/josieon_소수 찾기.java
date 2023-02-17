import java.util.*;
class Solution {
    public static Set<Integer> set = new HashSet();
    public int solution(String numbers) {
        char[] arr = numbers.toCharArray();
        for(int i = 1; i <= arr.length; i++)
            permutation(arr, "", new boolean[arr.length], i);
        // System.out.println(set.toString());
        boolean[] isNotPrime = new boolean[9_999_999];
        isNotPrime[0] = isNotPrime[1] = true;
        for(int i = 2; i < Math.sqrt(9_999_999); i++){
            if(!isNotPrime[i]){
                for(int j = 2*i; j < 9_999_999; j += i)
                    isNotPrime[j] = true;
            }
        }
        int answer = 0;
        for(int i : set)
            if(!isNotPrime[i])
                answer++;
        return answer;
    }
    public void permutation(char[] arr, String word, boolean[] visited, int r){
        if(r == 0){
            set.add(Integer.parseInt(word));
            return;
        }
        else{
            for(int i = 0; i < arr.length; i++){
                if(visited[i])
                    continue;
                visited[i] = true;
                permutation(arr, word+arr[i], visited, r-1);
                visited[i] = false;
            }
        }
    }
}