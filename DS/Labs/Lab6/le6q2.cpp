//2. WAP to implement the bubble sort and show the output of each pass.
#include<iostream>
#include "le6q1.h"
using namespace std;
int main(){
    int n;
    cin>>n;
    int *arr=rdm(n);
    print_arr(arr,n);
    cout<<endl;
    for(int i=0;i<n;i++){
        int f=0;
        for(int j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]){
                int t=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=t;
                f=1;
            }
        }
        if(f==0){break;}
        print_arr(arr,n);
    }
}
