/*6. Assume you have given a start pointer of a singly linked list. Write a program
to find the middle node in the given linked list.*/
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
#include<iostream>
using namespace std;
struct node{
        int data;
        node *next;
};
int search_mid(node * start){
    int loc=1;
    node * temp=start;
    while(temp!=NULL){
        temp=temp->next;
        loc++;
    }
    int mid=loc/2;
    return mid;
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
    node *start;
    node *node1;
    node *node2;
    node *node3;
    start=node1;
    node1->next=node2;
    node2->next=node3;
    node3->next=NULL;
    node1->data=10;
    node2->data=20;
    node3->data=30;
    int loc=search_mid(start);
    cout<<loc<<endl;
}
