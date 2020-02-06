package java_cp;

import java.io.*;
import java.util.*;

public class stack_func {

	public static void main(String[] args) 
	{
		Stack st = new Stack();
		System.out.println(st);
		
		st.push(1);
		st.push(2);
		st.push(3);
		
		System.out.println("New Stack after push operations: "+st);
		
		st.pop();
		System.out.println("New pop operation: "+st);
	}
}