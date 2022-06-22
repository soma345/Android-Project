package AddBinary;

public class twoSum2{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int target = -1;
		int[] numbers = {-1,0};
		int i =0 ; int j =numbers.length-1;
		while (i<j) {
			if(numbers[i]+numbers[j] == target) {
				System.out.print(i+1);
				System.out.print(j+1);
			}
			else if(numbers[i]+numbers[j] > target) {
				j--;
			}
			else {
				i++;
			}
		}
		System.out.println("abc");

	}

}
