import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), X = Integer.parseInt(st.nextToken());
        st =new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        // 값 받아옴과 동시에 비교 수행, 바로 출력
        while(st.hasMoreTokens()){
            int target = Integer.parseInt(st.nextToken());
            if(target < X)
                sb.append(target).append(" ");
        }
        System.out.println(sb);
    }
}