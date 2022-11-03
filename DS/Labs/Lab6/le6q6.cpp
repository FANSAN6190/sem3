/*6. WAP to implement the merge sort and show the output of each pass.*/
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
#include "le6q1.h"
using namespace std;
int merge_sort(int arr[],int l,int h);
int merge(int arr[],int l, int m1, int m2, int h);
int main(){
    int n;
    cin>>n;
    int *arr=rdm(n);
    print_arr(arr,n);
    merge_sort(arr,0,n-1);
    print_arr(arr,n);
    return 0;
}
int merge_sort(int arr[],int l,int h){
    if(l<h){
        int mid=(l+h)/2;
        merge_sort(arr,l,mid);///////
        merge_sort(arr,mid+1,h);
        merge(arr,l,mid-1,mid,h);
    }
    return 0;
}
int merge(int arr[],int l, int m1, int m2, int h){
    int c=l,lt=l,rt=m2;
    int tem_arr[h-l+1];
    while(l<=m1 && rt<=h){
        if(arr[lt]<=arr[rt]){
            tem_arr[c]=arr[lt];
            lt+=1;
        }
        else{
            tem_arr[c]=arr[rt];
            rt+=1;
        }
        c+=1;
    }
    while(l<=m1){
        tem_arr[c]=arr[lt];
        lt+=1;
        c+=1;
    }
    while (rt<=h){
        tem_arr[c]=arr[rt];
        rt+=1;
        c+=1; 
    }
    for(int i=l,j=0;i<=h;i++,j++){
        arr[i]=tem_arr[j];
    }
    return 0;
}