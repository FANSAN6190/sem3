/*5. WAP to implement the quick sort and show the output of each pass.*/
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
#include "le6q1.h"
using namespace std;
int qsort(int arr[],int l,int h);
int n;
int main(){
    int min;
    cin>>n;
    int *arr=rdm(n);
    print_arr(arr,n);
    qsort(arr,0,n-1);
    print_arr(arr,n);
}

int qsort(int arr[],int l,int h){
    if(l<h){
        int piv=arr[h];
        int i=l-1;
        for(int j=l;j<h;j++){
            if(arr[j]<piv){
                i++;
                int tem=arr[i];
                arr[i]=arr[j];
                arr[j]=tem;
            }
        }
        int tem=arr[i+1];
        arr[i+1]=arr[h];
        arr[h]=tem;  
        print_arr(arr,n);       
        qsort(arr,l,i);
        qsort(arr,i+2,h);
    }
    return 0;
}
