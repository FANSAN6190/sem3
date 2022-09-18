/*4. WAP for checking whether there are any duplicated elements in the array or not?*/
#include<iostream>
using namespace std;
int main(){
    int arr[7]={6,2,11,3,4,6,1};
    int i,n;
    for(int i=0;i<7;i++){
        for(int j=i+1;j<7;j++){
            if(arr[i]==arr[j]){
                cout<<"Duplicate Element Found"<<endl;
                return 0;
            }
        }
    }
    cout<<"No Duplicate Element Found."<<endl;
    return 0;
}
