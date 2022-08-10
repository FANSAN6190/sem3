//6. WAP to convert a decimal into binary number.
#include<iostream>
using namespace std;
int main(){
    int d,b=0,m=1;
    cin>>d;
    for(int i=0;d!=0;i++){
        if(d%2==0){
            b=(b*10)+0;
            m=m*10;
        }
        else{
            b=(b*10)+1;
        }
        d=d/2;
    }
    for(int i=0;i;i++){
        B=B+b%10
    }
    cout<<b;
}
