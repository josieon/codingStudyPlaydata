import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken()), end = Integer.parseInt(st.nextToken());
        int[] arr = new int[end+1]; // 배열 생성
        // 배열에 값 할당
        outer:
        for(int i = 1; ; i++){
            for(int j = 0; j < i; j++){
                arr[i*(i-1)/2 + 1 +j] = i;
                if(i*(i-1)/2 + 1 +j == end)
                    break outer;
            }
        }
        // start부터 end까지 합산
        int answer = 0;
        for(int i = start; i <= end; i++)
            answer += arr[i];
        System.out.println(answer);
        
    }
}