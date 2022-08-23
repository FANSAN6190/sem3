//5. WAP to convert a binary number into decimal.
#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int a,b,d=0;
    cin>>a;
    for(int i=0;a!=0;i++){
        d=d+(a%10)*pow(2,i);
        a=a/10;
    }
    cout<<d<<endl;
    return 0;
}
