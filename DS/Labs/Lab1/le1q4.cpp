//4. WAP to calculate xy where x and y are two integer numbers entered by the user. [do not use pow() function]
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
//#include<conio.h>
using namespace std;
int main(){
	int x,y,a=1;
	cin>>x>>y;
	while(y--){
		a*=x;
	}
	cout<<a;
//	getch();
	return 0;
}
