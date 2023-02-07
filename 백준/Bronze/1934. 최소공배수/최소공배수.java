import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while(T-- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken()), B = Integer.parseInt(st.nextToken());
            int gcd = gcd(A, B);
            // 최소공배수 = 두 수의 곱 / 최대공약수
            System.out.println(A * B / gcd);
        }
    }
    // 최대공약수
    public static int gcd(int A, int B){
        if(A == 0)
            return B;
        return gcd(B%A, A);
    }
}
