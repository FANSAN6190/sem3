/*4.Write a time efficient program for finding the element which appears maximum number of times in the array.
Sample input:2, 4, 5, 6, 8, 9, 10, 13, 2, 3, 2 Sample output:2   [as 2 is coming three times]*/
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0,k=0;i<n;i++){
        cin>>arr[i];
    }
    int e,m = 0;
    for (int i=0;i<n;i++){
        int c=0;
        for (int j=0;j<n;j++) {
            if (arr[i]==arr[j])
                c++;
        }
        if(c>m){
            m=c;
            e=arr[i];
        }
    }
    cout<<"Element Appeared Maximum nunber of times = "<<e<<endl;
}

    