/*3. WAP to implement the selection sort and show the output of each pass.*/
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
#include "le6q1.h"
using namespace std;
int main(){
    int n,min;
    cin>>n;
    int *arr=rdm(n);
    
    for(int j,i=0;i<n;i++){
        min=i;
        for(j=i+1;j<n;j++){
            if(arr[min]>arr[j]){
                min=j;
            }
        }
        if(min!=i){
                int tem=arr[min];
                arr[min]=arr[i];
                arr[i]=tem;
            }
        print_arr(arr,n);
    }
}