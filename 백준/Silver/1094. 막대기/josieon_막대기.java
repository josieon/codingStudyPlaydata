import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[]  args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());    // 입력값
        PriorityQueue<Integer> pq = new PriorityQueue<>();    // 힙
        int len = 64;    // 초기 길이
        pq.add(64);
        int answer = 0;
        // 루프로 자르는 과정 수행
        while(X != len){
            int cur = pq.poll() / 2;
            pq.offer(cur);
            // 버려도 되는지 판단
            if(len-cur < X){
                pq.offer(cur);
            }
            else
                len -= cur;
        }
        System.out.println(pq.size());
    }
}