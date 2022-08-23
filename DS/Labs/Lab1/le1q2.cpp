//2. WAP to search an element in array.
#include<iostream>
//#include<conio.h>
using namespace std;
int main(){
	int e,arr[6]={2,5,3,1,7,8};
	cin>>e;
	for(int i=0;i<6;i++){
		if(e==arr[i]){
			cout<<"element found at index = "<<i<<endl;
			break;
		}
	}
//	getch();
	return 0;
}
