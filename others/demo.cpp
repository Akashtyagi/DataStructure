#include <iostream>
using namespace std;

int main()
{
    int arr_count;
    cout << "Size ";
    std::cin >> arr_count;
    cin.ignore();  // Used as cin leaves a 'n' after it due to which getline function does not work.

    string input_line;
    cout << "Input array ";
    std::getline(cin,input_line);

    int arr[arr_count] = {0};
    int j = 0;
    for(int i=0;input_line[i]!='\0';i++)
    {
        if(input_line[i] == ' ')
        {
            j++;
        }
        else
        {
            arr[j] = arr[j]*10+(input_line[i]-48);
        }
    }

    cout<<"Reversed Array: ";
    for(int i=j;i>=0;i--)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
