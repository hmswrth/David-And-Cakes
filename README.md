# David-And-Cakes
David and Cakes

 

David loves Cakes and is much interested in baking. Hence he joined as a Manager at a famous bakery 'Cake Walk' which is called the cake lovers' paradise in the town. Because of the bakery's tantalising and delicious wide range of freshly baked cakes served in attractive cake boxes, people are seen always queuing up to have one of those boxes, which is why David's job is not so easy. Each cake box has a cost associated with it. The cake boxes are kept as a pile. He needs to handle two types of queries:

 

1) Customer Query:
When a customer demands a cake box, the box on the top of the pile is given and the customer is charged according to the cost of the box. This reduces the height of the pile by 1.
In case the pile is empty, the customer goes away empty-handed.

 

2) Baker Query:
The baker prepares a cake, wraps it in a box and adds it on top of the pile. And reports the cost of the box to David.
 

Help David manage the process.

 

Input Format:
First line contains an integer Q, the number of queries. Q lines follow.
A Type-1 (Customer) Query, is indicated by a single integer 1 in the line.
A Type-2 (Baker) Query, is indicated by two space separated integers 2 and Cwhere C is the cost of the box prepared.

 

Output Format:
For each Type-1 Query, output the price that customer has to pay i.e. cost of the box given to the customer in a new line. If the pile is empty, print "No Cake" (without the quotes).

 

Sample Input and Output:

Sample Input:

 6
1
2 5
2 7
2 9
1
1
 

Sample Output:

 No Cake
9
7
 

Explanation:

Initially, The pile is empty.
Baker adds a box with cost=5.
Baker adds a box with cost=7.
Baker adds a box with cost=9.
Customer takes the box on the top i.e. cost=9. Now box of cost=7 on top. Customer takes the box on the top i.e. cost=7.
