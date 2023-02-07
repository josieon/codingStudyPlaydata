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
            System.out.println(A * B / gcd);
        }
    }
    public static int gcd(int A, int B){
        if(A == 0)
            return B;
        return gcd(B%A, A);
    }
}