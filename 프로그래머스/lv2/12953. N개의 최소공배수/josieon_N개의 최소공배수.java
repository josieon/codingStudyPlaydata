import java.util.*;
class Solution {
    public int solution(int[] arr) {
        Queue<Integer> list = new LinkedList();
        for(int i : arr)
            list.offer(i);
        while(list.size() > 1){
            int a = list.poll();
            int b = list.poll();
            list.offer(a/gcd(a,b)*b);
        }
        return list.poll();
    }
    public int gcd(int a, int b){
        if(b == 0)
            return a;
        return gcd(b, a%b);
    }
}