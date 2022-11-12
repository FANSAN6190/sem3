//7.WAP to sort the array and ask the choice from user for ascending/descending
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
int main(){
    int arr[10]={2,5,10,7,1,9,4,3,6,8};
    char ch;
    cin>>ch;
    for(int i=0;i<10;i++){
        for(int j=i;j<10;j++){
            if(arr[i]<arr[j] && ch=='d'){
                arr[j]=arr[j]+arr[i];
                arr[i]=arr[j]-arr[i];
                arr[j]=arr[j]-arr[i];
            } 
            else if(arr[i]>arr[j]&& ch=='a'){
                arr[j]=arr[j]+arr[i];
                arr[i]=arr[j]-arr[i];
                arr[j]=arr[j]-arr[i];
            }         
        }

    }
    for(int i=0;i<10;i++){ cout<<arr[i]<<endl;}
}

