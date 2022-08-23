//2. WAP to find out series sum of 1^2 + 2^2 + �. + n^2
#include<iostream>
using namespace std;
int main(){
    int sn,n;
    cout<<"Enter thew value of n = ";
    cin>>n;
    sn=(n*(n+1)*(2*n+1))/6;
    cout<<"sum of n^2 terms = "<<sn<<endl;
    return 0;
}

