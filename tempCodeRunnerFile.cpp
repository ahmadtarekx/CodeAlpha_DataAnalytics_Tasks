#include <iostream>
#include <cmath>
#include <pthread.h>
#include <bits/stdc++.h>

using namespace std;

void* newfunc(void* arg){
    int mynum = intptr_t(arg);
    cout<<"The number is: "<<mynum<<endl;
    return NULL;
}

int main(){

    pthread_t mythread ;

    pthread_create(&mythread,NULL, newfunc,(void*)505);
    pthread_join(mythread,NULL);

}
