//1. WAP to insert new element at given index number in the array.
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
int main(){
    int r=0,e,in,arr[10]={1,3,5,6,8,9};
    cin>>e>>in;
    for(int i=0;i<10;i++){
        if(i==in){
            r=arr[i];
            arr[i]=e;
        }
        if(r!=0){
            arr[i+1]=arr[i+1]+r;
            r=arr[i+1]-r;
            arr[i+1]=arr[i+1]-r;
        }
    }
    for(int i=0;i<10;i++){cout<<arr[i]<<" ";}
    return 0;
}
