package AddBinary;

public class reverseStr {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[] s = new char[]{'h','e','l','l','o'};
		int slen = s.length;
		int b = s.length-1;
		 System.out.println(b);
		char temp; 
		for (int i=0 ;i<=b; i++){
            temp = s[i];
            System.out.println(s[i]);
            s[i]=s[b];
            System.out.println(s[i]);
            s[b]=temp;
            System.out.println(s[b]);
            b--;
            System.out.println( b);
	
		 }
		 System.out.println(s);

	}

}
