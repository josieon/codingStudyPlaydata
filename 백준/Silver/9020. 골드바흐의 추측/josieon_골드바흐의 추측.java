import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());    // 테스트 케이스 수
        StringBuilder sb = new StringBuilder();
        while(T-- > 0){
            int n = Integer.parseInt(br.readLine());
            // 입력된 짝수의 1/2부터 감소시키면서 탐색
            for(int i = n/2; i > 1; i--){
                // i와 n-i 모두 소수인 경우 출력 및 반복문 중단
                if(isPrime(i) && isPrime(n-i)){
                    sb.append(i).append(" ").append(n-i).append("\n");
                    break;
                }
            }
        }
        System.out.println(sb);
    }
    // 소수 판별 함수
    public static boolean isPrime(int n){
        if(n == 1 || n == 0)
            return false;
        for(int i = 2; i <= Math.sqrt(n); i++)
            if(n % i == 0)
                return false;
        return true;
    }
}