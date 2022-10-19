//8. WAP to find out nCr factor of given numbers.
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
 int fact(int n){  
    int f=1;  
        for(int i=1;i<=n;i++){f=f*i;}
        return f;
    }
int main(){
    int n,r,res;
    cin>>n>>r;
    res=fact(n)/(fact(n-r)*fact(r));
    cout<<res<<endl;
    return 0;
}