/*1. WAP to implement a function Rdm(n) which returns an array of random numbers{between 0 to 99},
where n is the size of array. (Hint: use dynamic memory allocation concept)*/
#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
int rdm(int n,int *a);
int main()
{
    int n;
    srand((unsigned)time(NULL));
    cin>>n;
    int *a=new int[n];
    rdm(n,a);
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }

}
int rdm(int n,int *a){
    int e;
    srand((unsigned)time(NULL));
    for(int i=0;i<n;i++){
        e=(((float)rand()/RAND_MAX)*101)-1;
        *(a+i)=e;
    }
    return *a;
}
