import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        // fib 배열
        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 1;
        // fibonacci 연산 수행
        for(int i = 2; i <= n; i++)
            fib[i] = fib[i-1] + fib[i-2];
        System.out.println(fib[n]);
    }
}
