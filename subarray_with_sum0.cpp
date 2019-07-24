/*

***Question*** Check if array has any subset in it whose sum is 0.
# Problem_link: https://www.techiedelight.com/check-subarray-with-0-sum-exists-not/
#
# Logic: The concept is to save sum of all values as we iterate in a set.
#        The sum value will keep changing with every iteration and will become same to any existing
#        sum-value only if values in between cancel each other i.e result sum to 0. As soon as we find that we stop.
#
# Example: sum-set= [2,4,6,8,4]
#             The last 4 will only come only if there are values after 4(first) whose sum resulted
#             to 6 & 8 and had -ve values which canceled 6 & 8 and again made sum to 4.
#             That means that sub-array between both 4 had sum of 0.
*/

#include<iostream>
#include<unordered_set>
using namespace std;

bool zerosumSubarray(int arr[],int len)
{
    unordered_set<int> sum_set;
    sum_set.insert(0); // Starting with 0 as we can have subarray at the start.
    int sum = 0;

    for(int i=0;i<len;i++)
    {
        sum = sum+arr[i];

        if(sum_set.find(sum)!= sum_set.end())
        {
            return true;
        }
        else
        {
            sum_set.insert(sum);
        }
    }
    return false;
}

int main()
{
    int arr[] = {4,2,-3,-3,5,2};
    int len = sizeof(arr)/sizeof(arr[0]);

    zerosumSubarray(arr,len) ? cout << "Subarray found":
                                cout << "Subarray not found";


}










