//
stack::emplace
//adds a new element at the top of the stack, above its current top element 
stack::empty()
while(!myStack.empty()){
}

//******************
stack::pop()
//removes the element on the top of the stack, effectively reducing its size by one

stack::push()
//insert a new element at the top of the stack, this member function effectively calls the member 
//function push_back
stack::size
//***************************SWAP*****************************************
stack::swap
void swap(stack&x); 
// stack::swap
#include <iostream>       // std::cout
#include <stack>          // std::stack

int main ()
{
  std::stack<int> foo,bar;
  foo.push (10); foo.push(20); foo.push(30);
  bar.push (111); bar.push(222);

  foo.swap(bar);

  std::cout << "size of foo: " << foo.size() << '\n';
  std::cout << "size of bar: " << bar.size() << '\n';

  return 0;
}
//foo now size of 2 bar 3
//****************************TOP***********************

