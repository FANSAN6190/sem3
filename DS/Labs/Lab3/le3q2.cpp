/*2. WAP to implement the linear search. Use function concept, if element is found then
return index number of element otherwise return -1;*/
#include<iostream>
using namespace std;
int ls(int n);
int arr[7]={6,3,5,1,9,4,8};
int main(){
    int n;
    cin>>n;
    cout<<ls(n)<<endl;
}
int ls(int n){
    for(int i=0;i<7;i++){
        if(arr[i]==n)
            return i;
    }
    return -1;
}
