import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> answer = new ArrayList();
        int i = 1;
        while(N > 1){
            i++;
            while(N % i == 0){
                answer.add(i);
                N /= i;
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int j : answer){
            sb.append(j).append("\n");
        }
        System.out.println(sb);
    }
}