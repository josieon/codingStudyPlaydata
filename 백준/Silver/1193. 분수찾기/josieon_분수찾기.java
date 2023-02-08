import java.io.*;
public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int sum=0;
		int range=1;
		while(sum < N) {
			sum += range;
			range++;
		}
		if(range%2!=0) {	// 5/1, 7/1와 같은 형태
			System.out.println((N-((range*(range-1))/2-range+1))+"/"+(range-((N-((range*(range-1))/2-range+1)))));
		}
		else {		// 1/5, 1/7과 같은 형태
			System.out.println(range-((N-((range*(range-1))/2-range+1)))+"/"+(N-((range*(range-1))/2-range+1)));
		}
	}
}