//3. WAP to check whether the number is prime or not.
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
int main(){
	int n,d=0;
	cin>>n;
	for(int i=1;i<n;i++){
		if(n%i==0){
			d++;
			if(d>2){
				cout<<"Element is not Prime"<<endl;
				break;
			}
		}
	}
	if(d<=2){
		cout<<"Element is Prime"<<endl;
	}
//	getch();
	return 0;
}
