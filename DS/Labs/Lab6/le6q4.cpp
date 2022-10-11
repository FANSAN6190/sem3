/*4. WAP to implement the insertion sort and show the output of each pass.*/
#include<iostream>
#include"le6q1.h"
using namespace std;
int main(){
    int n,min;
    cin>>n;
    int *arr=rdm(n);
    print_arr(arr,n);
    for(int i=1;i<n;i++){
        int key=arr[i];
        int j=i-1;
        while(j>=0 && arr[j]>key){
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=key;
        print_arr(arr,n);
    }
    
}
