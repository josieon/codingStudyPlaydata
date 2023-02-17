import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String[] str = new String[numbers.length];
        for(int i = 0; i < numbers.length; i++)
            str[i] = Integer.toString(numbers[i]);
        Arrays.sort(str, new Comparator<String>(){
            @Override
            public int compare(String e1, String e2){
                return (e2+e1).compareTo(e1+e2);
            }
        });
        String answer = "";
        if(str[0].matches("0"))
            return "0";
        else
            for(String s : str)
                answer += s;
        return answer;
        // System.out.println(Arrays.toString(str));
        // return null;
    }
}