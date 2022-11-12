node *node3,*node2,*node1;
    node *start=node1;
    node1->next=node2;
    node2->next=node3;
    node3->next=NULL;
    node1->data=10;
    node2->data=20;
    node3->data=30;