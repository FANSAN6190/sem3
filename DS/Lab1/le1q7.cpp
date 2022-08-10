//7.WAP to sort the array and ask the choice from user for ascending/descending
#include<iostream>
using namespace std;
int main(){
    int arr[5]={1,2,3,4,5};
    cout<<arr[1];
    for(int i=0;i<5;i++){
        if(arr[i]<arr[i+1]){
            arr[i]=arr[i]+arr[i+1];
            arr[i+1]=arr[i]-arr[i+1];
            arr[i]=arr[i]-arr[i+1];
        }

    }
    for(int i=0;i<5;i++){
        cout<<i<<endl;
    }
}

