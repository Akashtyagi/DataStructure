// MERGE SORT
// https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php


#include<iostream>

void mergee(int arr[],int starti,int midi,int endi)
{
    int temp[endi-starti+1]; // Initalizing a temp array that contain sorted elements.


    int i=starti;
    int j=midi+1;
    int k=0;

    while(i<=midi && j<=endi)
    {
        if (arr[i]<arr[j])
        {
            temp[k] = arr[i];
            i=i+1;
        }
        else
        {
            temp[k] = arr[j];
            j=j+1;
        }
        k=k+1;
    }

    while(i<=midi)
    {
        temp[k] = arr[i];
        i=i+1;k=k+1;
    }

    while(j<=endi)
    {
        temp[k] = arr[j];
        j=j+1;k=k+1;
    }

    for(i=starti;i<=endi;i++)
    {
        arr[i] = temp[i-starti];
    }
}

void mergeSort(int arr[],int starti,int endi)
{
    if (starti<endi)
    {
        int midi = (starti+endi)/2;
        mergeSort(arr,starti,midi);
        mergeSort(arr,midi+1,endi);
        mergee(arr,starti,midi,endi);

    }
}


int main()
{
    int arr[5] = {4,6,3,7,1};
    mergeSort(arr,0,4);

    for(int i=0;i<5;i++)
    {
        std::cout<<arr[i];
    }
    return 0;
}
