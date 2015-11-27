from pylab import *

x = linspace(0, 5, 10)
y = x ** 2              #use ** instead of ^ for power 

figure(1)
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('y = x^2')
show()

figure(2)
subplot(1,2,1)
plot(x, y, 'r--')
xlabel('x')
ylabel('y')
title('y = x^2')
subplot(1,2,2)
plot(y, x, 'g*-')
xlabel('y')
ylabel('x')
title('x = sqrt(x)')
show()

%reset


