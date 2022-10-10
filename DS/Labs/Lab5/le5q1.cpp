/*1.Write a program to implement binary search algorithm. Assume user will enter the sorted array. */
#include <iostream>
using namespace std;
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n,x,l=0,r,f=-1;
    cin>>n;
    int arr[n];
    r=n-1;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cin>>x;
    while(l<=r){
        int mid=(l+r)/2;
        if(x==arr[mid]){
            f=mid;
            break;
        }
        else if(x<arr[mid])
            r=mid-1;
        else if(arr[mid]<x)
            l=mid+1;
    }
    cout<<f<<endl;
    return 0;
}
