Tags: #paper #automotive 

## Introduction

### Background
- new car technologies
- [[E - E Architecture]] changes
- [[Ethernet]] is replacing or complementig [[CAN]]
- [[ECU]]s are combined into singular, more powerful ECUs
- service-oriented communicaiton with [[AUTOSAR]]
- [[V2X]]
- [[UNECE]] has issued regulations to standardize cybersecurity
- addressed in [[ISO 21434]], [[SAE J3061]]

### Main Point
- algorithm for automated generation and rating of attack paths using the [[Attack]] building blocks and attack feasibility


## Background and related work

- provide a framework for the execution of a [[TARA]] to achieve a general cybersecurity concept
- [[EVITA]]
- [[TVRA]]
- [[HEAVENS]]
- [[STRIDE]]
- [[SAHARA]]
- [[Attack Path]]

## Setting

### 3.1 Reference architecture

- Domain-based [[E - E Architecture]] because traditional topologies with a central [[Gateway]] are limited regarding the overall network bandwidth
- features an [[Ethernet]] backbone network and connects various Domain Controllers
- DCs connected to low bandwith [[CAN FD]] sub-networks consisting of smaller [[ECU]]s
- various domains
	- [[TCU]], [[VANET]]s, comfort domain, energy domain, infotainment domain, drive domain, diagnostic domain ([[OBD]])

### 3.2 Definition of use cases

- to show attack feasibility rating can be used to analyze [[Attack Path]]s of certain threat scenarios, we define three typical example use cases
- #### Electric driving 
	- Electric driving process, [[Attack]]s performed during driving
- #### Conductive charging
	- electric charging of the battery, [[OEM]]
- #### OTA firmware update


## 4 Attack surface assessment

### 4.1 Definition of attack assets
- #### [[Cryptographic key]]s
	- feasibility to break cryprographic algorithms or illegaly acquire or modify cryptographic keys
	- [[HSM]], [[TPM]]
- #### Wireless on-car interfaces communications
	- enable [[Attacker]] to perform remote attacks without physical access
	- via [[WiFi]], [[Cellular]], [[GPS]], [[Bluetooth]]
- #### Wired on-car interfaces communications
	- [[Attacker]] has physical access
	- exposed interfaces such as [[OBD]], debug interfaces like  [[JTAG]], [[USB]], AUX, not directly accessible interfaces to [[CAN]], [[CAN FD]], [[FlexRay]], [[Ethernet]], PLC
- #### On-car [[ECU]]s
	- [[Vulnerability]] like [[DoS]], disabling, config change, flashing, execution of malicious code
- #### On-car sensors


### 4.2 Attack feasibility rating

- based on [[ISO 21434]] and [[EVITA]]
	- Dimensions
		- 
	- [[Attack feasibility]]
		- Very Low
		- Low
		- Medium
		- High


### 4.3 Discussion on different path calculation methods

- **Sum** *(sum up all values per category along the path)*
	- accumulated reach the limits of the model more easily
	- fine-grained differentiation between longer attack paths is no longer possible
	- short but difficult path results in a lower score than a long but simple path
- **Average** *(average per category along the path)*
	- attack paths with mostly moderate values are evaluated equally with attack paths with strongly varying values
	- attack path with mostly moderate values is feasibile than an attack path with only one high value
- **Maximum** *(maximum values per category along the attack path)*
	- fine-grained differentiation of longer attack opaths while at the same time recognizing difficult attacks with low feasibility
	- medium-coring paths have less aggregated feasibility as opposed to short high-scoring paths
- **Hybrid-weighted sum**
	- attacks are weighted according to their difficulty to overcome the drawbacks from the **Sum** approach
	- weight = 𝑡𝑖𝑚𝑒𝜂 + 𝑒𝑥𝑝𝑒𝑟𝑖𝑒𝑛𝑐𝑒𝜂 + 𝑘𝑛𝑜𝑤𝑙𝑒𝑑𝑔𝑒𝜂 + 𝑜𝑝𝑝𝑜𝑟𝑡𝑢𝑛𝑖𝑡𝑦𝜂 + 𝑒𝑞𝑢𝑖𝑝𝑚𝑒𝑛𝑡𝜂
	- *For example, if the attack graph has paths up to a length of 4, this results in a minimal weight of a feature to be 4. 𝜂 is chosen so large that a difficult attack path of length 1 is weighted equally or higher than an easy attack path of full length. The short attack path has a weight of 2 so if we choose 𝜂 = 2 both attacks have an equal weight so the length of an attack path gets less important with respect to the difficulty of the attack. This allows more difficult attacks to compete better with long paths. To derive the attack feasibility of a path, the maximum values occurring for the 5 dimensions along the path are summed up. The path with the lowest weight value is considered as the most feasible attack path. This approach combines the advantages of the Maximum and Sum approach. Our method works with all functions described above, however, because of the drawbacks in some of them, we selected the Hybrid Weighted Sum model
	

### 4.4 Threat agent identification

- **Thief and Owner**  
	- financially motivated 
	- Owner additionally could be motivated by passion
	- capabilities regarding Specialist Expertise, Knowledge of the Item or Component, and Equipment are basic
	- Owner has unlimited access to his car while 
	- Thief can only access the car as long as the Owner does not interrupt him
- **Terrorist**
	- motivated by ideology 
	- capabilities regarding Specialist Expertise, Knowledge of the Item or Component, and Equipment are also basic
	- Window of Opportunity as moderate because we assume that the potential to threaten the owner is higher for the Terrorist
- **Organized Crime and Mechanic**
	- financially motivated
	- more sophisticated capabilities regarding Specialist Expertise, Knowledge of the Item or Component, and Equipment 
	- Window of Opportunity is rated the same as the Terrorist because of the same threat potential.
	- Mechanic, Window of Opportunity is  easy since he may attack the vehicle undisturbed once it is in his garage for repair or maintenance
- **Hacktivist and Foreign Government** 
	- motivated by ideology 
	- additionally passion for the Hacktivist
	- financial for the Foreign Government-
	- highest capabilities regarding Specialist Expertise and -
	- high capabilities regarding Equipment and Knowledge of the Item or Component.-
	- easy Window of Opportunity, the Foreign Government may (legally) seize a vehicle and may execute their attacks

## 5. Automated attack path generation

### 5.1 Directed Weighted graph generation

- automated method creates a directed graph by chaining the single attack steps together according to the defined preconditions and locations
- directed attack graph that represents all possible attack paths 
- [[BellmanFord algorithm]]
- weighted according to the attack feasibility of the attack step which is the destination of the edge


### 5.2 [[Attack Path]] generation

- calculate the shortest loop-free paths with respect to the weight of all attacks
 
 
``Algorithm 1 Prepare shortest path in attack graph 
	 ``G ← initialize AttackGraph 
	 ``EntryNodes ← {} 
	 ``𝑣𝑆𝑡𝑎𝑟𝑡 ← 𝑛𝑒𝑤𝑁𝑜𝑑𝑒 
		 ``for all node ∈ G.nodes do 
			 ``if |G 𝑇 .edges[node]| = 0 then 
			 ``EntryNodes ← EntryNodes ∪ {node} 
			 ``G.edges[vStart].𝑎𝑝𝑝𝑒𝑛𝑑(node, 0) 
		 ``end if 
	 ``end for 
	 ``G.nodes ← G.nodes ∪ {vStart} 
	 ``for all edge ∈ G.edges do 
		 ``(v,u)=edge 
		 ``weight = 𝑢.𝑡𝑖𝑚𝑒𝜂 + 𝑢.𝑒𝑥𝑝𝑒𝑟𝑖𝑒𝑛𝑐𝑒𝜂 + 𝑢.𝑘𝑛𝑜𝑤𝑙𝑒𝑑𝑔𝑒𝜂 + 𝑢.𝑜𝑝𝑝𝑜𝑟𝑡𝑢𝑛𝑖𝑡𝑦𝜂 + 𝑢.𝑒𝑞𝑢𝑖𝑝𝑚𝑒𝑛𝑡𝜂
		 ``edge.𝑤𝑒𝑖𝑔ℎ𝑡 = weight 
	 ``end for 
	 ``𝑠ℎ𝑜𝑟𝑡𝑒𝑠𝑡𝑃𝑎𝑡ℎ𝑠 ← BellmanFord(G.nodes,G.edges, vStart) 
	 ``return 𝑠ℎ𝑜𝑟𝑡𝑒𝑠𝑡𝑃𝑎𝑡ℎ𝑠


### 5.3 Threat Path extraction

- predefined threats are mapped to the path nodes that consist of attack step and location
- shortest path from the virtual start to the target is calculated
- compared with the other shortest paths to other targets of the same threat
- the shortest path for a threat is returned

``Algorithm 2 Extract shortest attack path of threat 
	``Path ← ∅ 
	``for all target ∈ threat do 
		``𝑇 ← target 
		``Path𝑡𝑎𝑟𝑔𝑒𝑡 ← target 
		``while 𝑇 ≠ vStart do 
			``print 𝑇 
			``Path𝑡𝑎𝑟𝑔𝑒𝑡 ← Path𝑡𝑎𝑟𝑔𝑒𝑡 ∪ 𝑠ℎ𝑜𝑟𝑡𝑒𝑠𝑡𝑃𝑎𝑡ℎ𝑠.𝑝𝑟𝑒𝑑𝑒𝑐𝑒𝑠𝑠𝑜𝑟[𝑇] 
			``𝑇 ← 𝑠ℎ𝑜𝑟𝑡𝑒𝑠𝑡𝑃𝑎𝑡ℎ𝑠.𝑝𝑟𝑒𝑑𝑒𝑐𝑒𝑠𝑠𝑜𝑟[𝑇] 
		``end while 
		``if 𝑤𝑒𝑖𝑔ℎ𝑡(Path𝑡𝑎𝑟𝑔𝑒𝑡) < 𝑤𝑒𝑖𝑔ℎ𝑡(Path) then 
			``Path = Path𝑡𝑎𝑟𝑔𝑒𝑡 
		``end if 
	``end for
	``return Path


### 5.4 Most Feasibile path calculation

- set of shortest paths is used to calulate the most feasibile attack


## 6. Exemplary application on threats derived from the use cases

### 6.1. Definition of threat scenarios

- [[ISO 21434]]
- [[DoS]]
- garbage messages 
- disabling relevant [[ECU]]s
- message manipulation
- message interception
- message injection
- [[UNECE]] threats have been defined


### 6.2. Definition of attack paths
### 6.3. Attack path analysis

- shows that our approach is also applicable to reflect adaptations of the E/E architecture with regard to the attack surface assessment

### 6.5. Discussion with respect to other rating approaches

- proposed attack feasibility rating concept is based on the attack-potential based approach
	- not the only approaches for attack feasibility rating compliant with [[ISO 21434]]
- ##### Attack-potential based approaches
	- major advantage of attack-potential based approaches is provided by the high flexibility and the detailed coverage of many different aspects relevant for the evaluation of attacks
	- even the prescriptions given by [[ISO 21434]] are very flexible and allow the adaption to individual needs
	- largely accepted strategy in the automotive area
	- [[EVITA]] method
	- disadvantage is provided by the high complexity of estimating all the different parameters
	- mapping of individual conditions to the parameter values is not obvious, and the final results of the rating may depend on the individual expertise of the team performing the risk analysis
	- already developed approaches in the automotive area do not completely comply with [[ISO 21434]]
- ##### [[CVSS]] based approaches
	- provides a complete standard scheme with a value scale
	- attack feasibility is called exploitability 
	- [[ISO 21434]] compliant approach just demands the usage of the base exploit metrics group with the four parameters attack vector, attack complexity, privileges required, and user interaction according to CVSS V 3.1 
	- estimation of the parameters is much easier to handle
	- direct mapping to numerical values with always the same scale allows easier comparison of different CVSS based approaches
	- disadvantage of much lower flexibility to be adapted to individual applications
	- attack complexity that only has two values low and high
	- not well suited for the automotive area, in particular with respect to the parameters of required privileges and user interaction which are less relevant for this application area
- ##### Attack vector-based approaches
	- Pure attack vector-based approaches are even simpler than [[CVSS]] based approaches
	- only consider this one parameter is also present in the CVSS scheme
	- [[ISO 21434]] only demands the consideration of the predominant attack vector
	- attack vector-based approaches are even less suited for automotive applications than CVSS based approaches
- ##### Prioritization of our focus
	- obviously predominate in the automotive area
	- different types of attacks against EVs are very complex and manifold, and in Section 6.1 we have already seen some examples for [[UNECE]] threat scenarios with different attack endpoints
	- flexible consideration of different parameters is very important
	- [[CVSS]] practically combines the parameters of elapsed time, expertise, equipment, and knowledge of item or component
	- rating with just the two different values of high and low must be done
	- decision will be difficult whether the implementation of further security technology is considered necessary to reach the value low.
	- [[EVITA]] method, show up the eligibility of this type of approach for this application area. The previously mentioned obstacles of existing solutions can be easily overcome, lack of compliance to[[ISO 21434]] may be eliminated with slight adaptions of the schemes