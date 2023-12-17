class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        for(int i = 0; i < my_string.length(); i++){
            String word = my_string.substring(i, i+1);
            answer += word.repeat(n);
        }
        return answer;
    }
}