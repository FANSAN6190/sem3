/*1. Write a function Insert_Beginning() to insert a new node at the beginning of
singly linked list. Call this function N time to create a linked list with N nodes.
Also write display function to print the linked list.*/
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
struct node{
        int data;
        node *next;
};
node *insert_Beginning(node * start, node * newnode){
    newnode->next=start;
    start=newnode;
    return start;
}
void display(node * start){
    node *tem=start;
    while (tem->next!=NULL){
        cout<<tem->data<<endl;
        tem=tem->next;
    }
    cout<<tem->data<<endl;
    delete tem;
}
int main(){
    node * start=NULL;
    int n,i=1;
    cin>>n;
    while(n--){
        node * newnode=new node();
        newnode->data=i;
        start=insert_Beginning(start,newnode);
        i++;
    } 
    display(start);
}
