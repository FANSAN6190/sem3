/*1. WAP to implement a function Rdm(n) which returns an array of random numbers{between 0 to 99},
where n is the size of array. (Hint: use dynamic memory allocation concept)*/
#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
int *rdm(int n);
void print_arr(int arr[],int n);
int main()
{
    int n;
    srand(time(NULL));
    cin>>n;
    int *ar=rdm(n);
    print_arr(ar,n);
}
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
        cout<<arr[i]<<endl;
    }
}