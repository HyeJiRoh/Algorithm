import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        
        if(sides[0] + sides[1] > sides[sides.length-1]){
            return 1;
        } else return 2;
    }
}