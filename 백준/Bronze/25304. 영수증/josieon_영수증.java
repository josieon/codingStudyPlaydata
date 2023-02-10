import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long X = Long.parseLong(br.readLine());
        int N = Integer.parseInt(br.readLine());
        long total = 0;
        while(N-- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            total += Integer.parseInt(st.nextToken()) * Integer.parseInt(st.nextToken());
        }
        if(total == X)
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}