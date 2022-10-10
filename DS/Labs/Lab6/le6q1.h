#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
int *rdm(int n);
void print_arr(int arr[],int n);
int *rdm(int n){
    int e;
    int *a=new int[n];
    srand((unsigned)time(NULL));
    for(int i=0;i<n;i++){
        e=rand()%100;
        *(a+i)=e;
    }  
    return a;
}
void print_arr(int *arr,int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}