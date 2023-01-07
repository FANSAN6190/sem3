/*2.Write a menu driven program using switch-case to insert the node at beginning,
    from specified position and at the end of linked list.*/
//******************************************************
//*This program is developed by Fanindra Saini(211B116)*
//******************************************************
/*#include <iostream>
using namespace std;
struct node{
    int info;
    node *next;
};
node *insert_at_end(node *start, node *newnode);
node *insert_at_beginning(node *start, node *newnode){
    newnode->next = start;
    start = newnode;
    return start;
    
}
node *insert_at_loc(node *start, node *newnode, int i){
    node *temp = start;
    if(i==1){
        start=insert_at_beginning(start,newnode);
    }
    else if(start!=NULL){
        i=i-2;
        while (--i){
            temp = temp->next;
        }
        newnode->next = temp->next; 
        temp->next = newnode;
        delete temp;
        return start;
    }
    return start;
}
node *insert_at_end(node *start, node *newnode){
    node *temp = start;
    if (start == NULL){start=newnode;}
    else{
        while (temp->next != NULL){
            temp = temp->next;
        }   
        newnode->next = NULL;
        temp->next = newnode;                
    }
    delete temp;
    return start;
}
void display(node *start){
    node *temp = start;
    while (temp != NULL){
        cout << temp->info << endl;
        temp = temp->next;
    }
    delete temp;
}
int main(){
    node *start=NULL;
    node *newnode;
    int ins_at;
    cout << "Insert at Beginning : 1\nInsert at Specific Position: 2\nInsert at End : 3 " << endl;
    while (true){
        cout<<"-------------"<<endl;
        display(start);
        cout<<"-------------"<<endl;
        cout << "Choose one of the option : ";
        cin >> ins_at;
        if (ins_at == 0){break;}
        cout << "Enter the Value = ";
        cin >> newnode->info;
        switch (ins_at){
        case 1:
            cout << "check 1" << endl;
            start = insert_at_beginning(start, newnode);
            cout << "check 2" << endl;
            break;
        case 2:
            int i;
            cout << "Enter the location = ";
            cin >> i;
            start = insert_at_loc(start, newnode, i - 1);
            break;
        case 3:
            start = insert_at_end(start, newnode);
            break;
        default:
            cout << "Wrong Input";
            break;
        }
    }
}*/

#include<iostream>
using namespace std;
class node{
    public:
    int data;
    node *next;
};
node * in_at_beg(node*start,int ele){
    node * newnode=new node();
    newnode->data=ele;
    if(start==NULL){
        start=newnode;
    }
    else{
        newnode->next=start;
        start=newnode;
    }
    return start;
}
node * in_at_end(node * start,int ele){
    node *newnode=new node();
    node * temp=start;
    newnode->data=ele;
    if(start==NULL){
        start=newnode;
    }
    else{
        while (temp->next!=NULL){
            temp=temp->next;
        }
        newnode->next=temp->next;
        temp->next=newnode;
    }
    return start;
}
node * in_at_loc(node * start,int ele,int loc){
    node * newnode=new node();
    newnode->data=ele;
    if(start==NULL){
        start=newnode;
    }
    else{
        node * temp=start;
        while(loc){
            temp=temp->next;
            loc-=1;
        }
        newnode->next=temp->next;
        temp->next=newnode;
    }
    return start;
}
void display(node * start){
    node *temp=start;
    while (temp!=NULL){
        cout<<temp->data<<endl;
        temp=temp->next;
    }
    delete temp;
}
int main(){
    int ch;
    node * start=NULL;
    while(ch){
        cout<<"-----------------------"<<endl;
        cout<<"Enter the Choice : ";
        cin>>ch;
        int ele,loc;
        
        switch(ch){
            case 0:
            break;
            case 1:
            cout<<"Enter the element : ";
            cin>>ele;
            start=in_at_beg(start,ele);
            break;
            case 2:
            cout<<"Enter the element : ";
            cin>>ele;
            cout<<"Enter the Location : ";
            cin>>loc;
            start=in_at_loc(start,ele,loc);
            break;
            case 3:
            cout<<"Enter the element : ";
            cin>>ele;
            start=in_at_end(start,ele);
            break;
            case 4:
            display(start);
            break;
            default:
            cout<<"Wrong Input!!!"<<endl;
            break;
        }
        cout<<"-----------------------"<<endl;
    }
}
