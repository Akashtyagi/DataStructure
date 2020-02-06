package java_cp;
import java.util.*;

/*
	Create, Insert and print the Linked List
*/

public class Linked_list {
	Node head;
	
	static class Node // Subclass
	{
		int data;
		Node next;
		
		Node(int d) //Constructor
		{
			data = d;
			next = null;	
		}
	}
	
	
	public static Linked_list insertAtLast(Linked_list llist,int data)
	{
		Node new_node = new Node(data);
		new_node.next = null;
		if(llist.head == null){
			llist.head = new_node;
		}
		else{
			Node last = llist.head;
			while(last.next != null)
				{
					last = last.next;
				}
			last.next = new_node;
		}
		return llist;
	}
	
    static Node insertNodeAtHead(Node llist, int data) // take head as input
    {
        Node first = new Node(data);
        if (llist == null){
                llist = first;
            }
        else {
                Node last = llist;
                first.next = last;
                llist = first;
             }
        return llist;
    }
    
    static Node insertNodeAtPosition(Node head, int data, int position) 
    {
        Node newvalue = new Node(data);
        if(head==null)
        {
            head = newvalue;
        }
        else
        {
            int counter = 1;
            Node last = head;
            Node temp = head;
            while(last.next!=null)
            {
                if(counter==position)
                {
                    temp = last.next;
                    last.next = newvalue;
                    newvalue.next = temp;
                    return head;
                }
                last = last.next;
                counter++;
            }
            if(counter == position)
            {
                last.next = newvalue;

            }
        }
        return head;
    }
	
    static Node deleteNode(Node head, int position) 
    {
        if(head==null)
        {
            return head;
        }
        else
        {
            Node temp;
            Node last = head;
            int counter = 0;

            if(position==0)
            {
                head = head.next;
                return head;
            }
            while(last.next!=null)
            {
                if(counter==position-1)
                {
                    temp = last.next;
                    last.next = temp.next;
                    return head;
                }
                last = last.next;
                counter++;
            }
        }
        return head;
    }
    
    public static void printList(Linked_list llist)
	{
		Node pointer = llist.head;
		while(pointer!= null)
		{
			System.out.printf(pointer.data + " ");
			pointer = pointer.next;
		}
		System.out.println();
	}
	
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		
		Linked_list llist = new Linked_list();
		int n = sc.nextInt();
		for(int i =0;i<n;i++)
		{
			//list_values[i] = sc.nextInt();
			llist = insertAtLast(llist,sc.nextInt());
		}
		
		llist.head = insertNodeAtHead(llist.head,101);
		System.out.println("After adding element to the head");
		printList(llist);
		llist.head = insertNodeAtPosition(llist.head, 999, 3);
		System.out.println("After adding 999 to index 3");
		printList(llist);
		llist.head = deleteNode(llist.head, 2);
		System.out.println("After deleting node at index 2");
		printList(llist);
		
	}

}
