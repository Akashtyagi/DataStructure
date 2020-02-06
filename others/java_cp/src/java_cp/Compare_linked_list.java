package java_cp;

import java.util.Scanner;

public class Compare_linked_list {
	Node head;
	
	static class Node
	{
		int data;
		Node next;
		
		Node(int d)
		{
			data = d;
			next = null;
		}
	}
	
	public static int compare(Compare_linked_list llist1,Compare_linked_list llist2)
	{
		Node pointer1 = llist1.head;
		Node pointer2 = llist2.head;
		
		while(pointer1.next != null)
		{
			if(pointer2.next == null)
				return 0;
			else if(pointer1.data != pointer2.data)
			{
				return 0;
			}
			pointer1 = pointer1.next;
			pointer2 = pointer2.next;
		}
		return 1;
		
	}

	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		
		Linked_list llist = new Linked_list();
		int n = sc.nextInt();
//		for(int i =0;i<n;i++)
//		{
//			//list_values[i] = sc.nextInt();
//			llist = insertAtLast(llist,sc.nextInt());
//		}
		
	}

}
