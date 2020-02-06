// Given an unsorted array of integers, print all elements which are greater than all elements present to its right.

#include<iostream>
#include<stack>
using namespace std;

void find(int arr[],int n)
{
    stack<int> stk;

    for(int i=0;i<n;i++)
    {
        while(!stk.empty() && stk.top()<arr[i])
            stk.pop();
        stk.push(arr[i]);
    }

    while(!stk.empty())
    {
        cout << stk.top() << " ";
        stk.pop();
    }
}

int main()
{
    int arr[] = {10,4,6,3,5,1};
    int n = sizeof(arr)/sizeof(arr[0]);

    find(arr,n);
    return 0;
}
