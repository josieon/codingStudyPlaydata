import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while(T-- > 0){
            int n = Integer.parseInt(br.readLine());
            for(int i = n/2; i > 1; i--){
                if(isPrime(i) && isPrime(n-i)){
                    sb.append(i).append(" ").append(n-i).append("\n");
                    break;
                }
            }
        }
        System.out.println(sb);
    }
    public static boolean isPrime(int n){
        if(n == 1 || n == 0)
            return false;
        for(int i = 2; i <= Math.sqrt(n); i++)
            if(n % i == 0)
                return false;
        return true;
    }
}