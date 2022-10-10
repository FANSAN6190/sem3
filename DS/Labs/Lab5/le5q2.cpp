/*2.Write a function which accepts an array of integers along with the size of it. The numbers are  arranged  in  the  
list  in  increasing  order  until  a  particular  index  and  after  that  it  is arranged  in  decreasing  order.This  
function  should  find  and  return  the  index  position  at which the increasing list starts decreasing.Call this 
function from main function.*/
#include<iostream>
using namespace std;
int in_dec(int arr[],int n);
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<in_dec(arr,n)<<endl;
    return 0;
}
int in_dec(int arr[],int n){
    int i=0;
    while(arr[i]<arr[i+1]){
        i++;
    }
    return i+1;
}