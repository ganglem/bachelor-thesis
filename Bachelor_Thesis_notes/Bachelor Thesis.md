Tags: #bachelorthesis #paper  

In this thesis you have to make attack path analyses on different internal vehicle network architectures and compare them based on which provides more security with regards attack paths. 

The first step would be creating multiple different [[Architecture diagrams]]. 

Then you have to write a program, which reads files of a vehicle network topology, maps this to a list of entry point and target [[ECU]]s, and generates a list of all possible [[Attack Path]]. 
To get a quick and early result, this list should be sorted by the number of hops over each gateway. 

The next step would be giving each entry point, gateway and connection a [[Rating]] on how big the attack feasibility for this element is. 

Then, attack paths can be calculated - e.g. with the formula of the #paper 

At last, you have to decide on a criteria on how to rate the different topologies and compare them with it.