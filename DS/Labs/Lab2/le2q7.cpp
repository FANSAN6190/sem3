//7. WAP to display lower triangular matrix of a given n by n size matrix entered by user.
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int **arr = new int*[n]; 
    for(int i=0;i<n;i++){
        arr[i]=new int[n];
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(i+j+2<=(n+1)){
                arr[i][j]=0;
            }
            else{
                arr[i][j]=i+j+2;
            }
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<arr[i][j]<<"\t";
        }
        cout<<'\n';
    }
    for(int i=0;i<n;i++){
        delete [] arr[i];
    }
    delete [] arr;
    return 0;
}


