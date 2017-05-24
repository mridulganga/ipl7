#include <iostream>

using namespace std;

int main()
{
    int n,s,m=1,i,j;
    cin>>n;
    s=(n-1)/2;
    for(i=0;i<s;i++)
        cout<<" ";
    cout<<"*";
    for(i=0;i<s;i++)
        cout<<" ";
    cout<<endl;
    for(i=1;i<(n+1)/2;i++)
    {
         s--;
         for(j=0;j<s;j++)
            cout<<" ";
         cout<<"*";
         for(j=0;j<m;j++)
            cout<<" ";
         cout<<"*\n";
         m+=2;
    }
    return 0;

}
