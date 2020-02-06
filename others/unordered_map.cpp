//UNORDERED MAP

#include<iostream>
#include<unordered_map>
using namespace std;

int main()
{
    unordered_map<int, int> umap;

    umap[0] = 24;

    umap.insert({5,50});
    umap.insert({ {6,60},{7,70} });


    //cout << umap.find(5);
    cout << "First method of iteration over a map."<<endl;
    for(auto x : umap)
    {
        cout << x.first << "--> " <<  x.second << endl;
    }

    cout << "Second method of iteration over a map."<<endl;
    unordered_map<int,int>::iterator p;
    for(p = umap.begin(); p!= umap.end();p++)
    {
        cout << p->first << ", " << p->second <<endl;
    }


    return 0;
}
