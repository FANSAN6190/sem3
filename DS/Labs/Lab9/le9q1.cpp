#include<iostream>
#include<stdlib.h>
using namespace std;
class Stack{
    int *top;
    int *arr;
    int siz;
public:
    Stack(int n){
        siz=n;
        arr=new int(siz);
        for(int i=0;i<siz;i++){
            arr[i]=0;
        }
        *top=-1;
        cout<<*top<<endl;
    }
    int push(int e){
        if(isFull()){
            cout<<"Stack Overflow"<<endl;
            return *top;
        }
        else{
            cout<<*top<<endl;
            (*top)++;
            arr[*top]=e;
            return *top;
            cout<<*top<<endl;
        }
    }
    int pop(){
        if(isEmpty()){
            cout<<"Stack Underflow"<<endl;
            return *top;
        }
        else{
            int r=arr[*top];
            (*top)--;
            return r;
        }
    }
    int isEmpty(){
        if((*top)==-1){
            cout<<"Stack is Empty"<<endl;
            return 1;
        }
        return 0;
    }

    int isFull(){
        if((*top)==siz-1){
            cout<<"Stack is Full"<<endl;
            return 1;
        }
        return 0;
    }
    void display(){
        for(int i=0;i<=(*top);i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
};
int main(){
    int n,choice;
    cout<<"Enter the Size of Stack : ";
    cin>>n;
    Stack stk(n);
    while(choice!=4){
        cout<<"***Stack Menu***\n1. Push\n2. Pop\n3. Display\n4. Exit"<<endl;
        cout<<"Enter your choice(1-4): ";
        cin>>choice;
        cout<<"****************"<<endl;
        int ele;
        switch(choice){
        case 1:
            cout<<"Enter element to push : ";
            cin>>ele;
            stk.push(ele);
            break;
        case 2:
            ele=stk.pop();
            cout<<"Deleted element is "<<ele<<endl;
            break;
        case 3:
            stk.display();
            break;
        case 4:
            exit(0);
            break;
        default:
            cout<<"Invalid Input, Try Again"<<endl;
            break;
        }
        cout<<"****************"<<endl<<endl;
    }
    return 0;
}
