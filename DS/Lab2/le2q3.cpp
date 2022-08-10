//3. WAP to find out GCD of two numbers.
#include<iostream>
using namespace std;
int main(){
    int a,b,cd;
    cout<<"Enter the 2 numbers = ";
    cin>>a>>b;
    for(int i=1;i<=a;i++){
        if(a%i==0 && b%i==0){
            cd=i;
        }
    }
    cout<<cd<<endl;
}
