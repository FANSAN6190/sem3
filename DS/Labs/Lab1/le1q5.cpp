//5. WAP to replace a character by another character in a string. Take both the choices from the user.
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
//#include<conio.h>
using namespace std;
int main(){
	 string s="qwerty";
	 cout<<s<<endl;
	 char x,y;
	 cin>>x>>y;
	 for(int i=0;s[i]!='\0';i++){
			if(s[i]==x){
				s[i]=y;
			}
	 }
	 cout<<s<<endl;
//	 getch();
	 return 0;
}
