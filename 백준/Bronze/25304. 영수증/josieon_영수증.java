import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // X의 범위가 1,000,000,000. 참고로, int의 범위는 2,147,483,647까지.
        long X = Long.parseLong(br.readLine());
        int N = Integer.parseInt(br.readLine());
        long total = 0;
        // N개의 아이템 값 계산
        while(N-- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            total += Integer.parseInt(st.nextToken()) * Integer.parseInt(st.nextToken());
        }
        // 비교해서 출력
        if(total == X)
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}