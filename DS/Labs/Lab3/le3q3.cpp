/*3. WAP to delete an element from an array, use search algorithm to find the index number
of given number; if element to be deleted is not found then print “Error: element not found ”. */
#include<iostream>
using namespace std;
int ls(int n);

int main(){
    int i,e,f=0;
    int arr[7]={6,3,5,1,9,4,8};
    cin>>e;
    for(i=0;i<7;i++){
        if(arr[i]==e){
            f=1;
        }
        if(f==1){
            arr[i]=arr[i+1];
        }
    }
    if(f==1){
        arr[i-1]=0;
    }
    else{
        cout<<"Error: element not found."<<endl;
    }
    for(int i=0;i<7;i++){
        cout<<arr[i]<<" ";
    }
}


