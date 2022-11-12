//6. WAP to convert a decimal into binary number.
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
int main(){
    int d,b=0,m=1,B=0;
    cin>>d;
    for(int i=0;d!=0;i++){
        if(d%2==0){
            b=(b*10)+0;
            if(b==0){m=m*10;}
        }
        else{b=(b*10)+1;}
        d=d/2;
    }
    for(int i=0;b!=0;i++){
        B=(B*10)+(b%10);
        b/=10;
        cout<<B<<" "<<b<<endl;
    }
    B=B*m;
    cout<<B;
}
