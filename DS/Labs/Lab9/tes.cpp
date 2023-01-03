/*2. Write a menu-driven program to implement Stack using linked list with
     following options: 1.Push 2.Pop 3.Display 4.Exit*/
#include<iostream>
using namespace std;
class data_type{
    int int_data;
    char char_data;
    double double_data;
    data_type(int a=0,char *b="",double c=0.0){
        int_data=a;
        char_data=*b;
        double_data=c;
    }
};
class node{
    public:
    char data;
    node *next;
};
class Stack{
    public:
    node *top;
    Stack(){top=NULL;}
    void push(char ele){
        node *newnode=new node();
        newnode->data=ele;
        newnode->next=top;
        top=newnode;}
    int pop(){
        node *temp=top;
        if(top==NULL){
            cout<<"Stack underflow"<<endl;
            return -1; }
        else{
            int rem=top->data;
            top=top->next;
            return rem; }
    }
    void display(){
        node *temp=top;
        while(temp!=NULL){
            cout<<temp->data<<" ";
            temp=temp->next; }
        cout<<endl; }
};
int main(){
    int choice;
    node *start;
    //start->next=NULL;
    Stack stk;
    while(choice!=4){
        cout<<"***Stack Menu***\n1. Push\n2. Pop\n3. Display\n4. Exit"<<endl;
        cout<<"Enter your choice(1-4): ";
        cin>>choice;
        cout<<"****************"<<endl;
        char ele;
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
    }
}
