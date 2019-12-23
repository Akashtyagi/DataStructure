#include<iostream>
#include<algorithm>
// Find pair of digit from a list that gives sum as 10.


void findpiar(int arr[],int sum,int len)
{
    std::sort(arr,arr+len);     //Sort the array in increasing order.

    int low = 0;
    int high = len-1;

    while(low < high)
    {
        if(arr[low] + arr[high] == sum)
        {
            std::cout<< "Pair found for "<< arr[low] << "and "<< arr[high];
            return ;
        }

        if((arr[low] +arr[high])<sum)
        {
            low+= 1;
        }
        else{ high = high -1;}


    }
    std::cout << "Pair not found";
}

int main()
{
    int arr[] = {8,7,2,5,3,1};
    int sum = 10;

    int len = sizeof(arr)/sizeof(arr[0]);
    std::cout << len<<std::endl;
    findpiar(arr,sum,len);
    return 0;
}

