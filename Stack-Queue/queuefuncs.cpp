
//********************************BACK**************************
//returns a reference to the last element in the queue
//This is the newest element in the queue;the last element pushed into the stack

// queue::back
#include <iostream>       // std::cout
#include <queue>          // std::queue

int main ()
{
  std::queue<int> myqueue;

  myqueue.push(12);
  myqueue.push(75);   // this is now the back

  myqueue.back() -= myqueue.front();

  std::cout << "myqueue.back() is now " << myqueue.back() << '\n';

  return 0;
}
//myqueue.back() is now 63  
//***************************emplace*********************
