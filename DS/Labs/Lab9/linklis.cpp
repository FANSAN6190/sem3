#include<iostream>
using namespace std;
struct node{
    int info;
    node * next;
};
void in_at_beg(node *start);
int main(){
    node * start;
    node * newnode=new node();
    newnode->next=start->next;
    cout<<newnode->next<<" "<<start->next;
}