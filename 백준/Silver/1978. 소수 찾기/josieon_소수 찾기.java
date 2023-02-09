import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int answer = 0;
        // 반복문을 통해 소수인지 판별
        while(st.hasMoreTokens()){
            if(isPrime(Integer.parseInt(st.nextToken())))
                answer++;
        }
        System.out.println(answer);
        // 에라토스테네스의 체
        // boolean[] prime = new boolean[10_000_001];
        // for(int i = 2; i < 10_000_001; i++){
        //     if(!prime[i]){
        //         for(int j = i*2; j < 10_000_001; j += i){
        //             prime[j] = true;
        //         }
        //     }
        // }
    }
    public static boolean isPrime(int n){
        if(n == 1)
            return false;
        for(int i = 2; i <= Math.sqrt(n); i++){
            if(n % i == 0)
                return false;
        }
        return true;
    }
}