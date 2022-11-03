//1. WAP to find out largest element of an array.
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
//#include<conio.h>
using namespace std;
int main(){
	int l=0,ar[6]={4,2,1,5,3,6};
	for(int i=0;i<6;i++){
		if(ar[i]>l){l=ar[i];}
	}
	cout<<l<<endl;
//	getch(); 
	return 0;
}
