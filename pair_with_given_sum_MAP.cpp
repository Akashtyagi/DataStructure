// Find pair of digit from a list that gives sum as 10. Using MAP.

#include<iostream>
#include<unordered_map>
using namespace std;

void findPair(int arr[],int sum,int len)
{
    std::unordered_map<int,int> umap;

    for(int i=0;i<len;i++)
    {
        if(umap.find(sum-arr[i]) != umap.end())
        {
            cout << "Found pair for "<<arr[i]<< " and "<<sum-arr[i]<<endl;
            return;
        }
        umap[arr[i]] = i;

    }
}

int main()
{
    int arr[] = {8,7,2,5,3,1};
    int sum = 10;

    int len = sizeof(arr)/sizeof(arr[0]);
    findPair(arr,sum,len);
    return 0;
}
