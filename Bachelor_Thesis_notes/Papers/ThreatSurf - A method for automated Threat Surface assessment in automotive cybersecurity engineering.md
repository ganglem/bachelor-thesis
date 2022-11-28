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

- provide a framewor for the execution of a [[TARA]] to achieve a general cybersecurity concept
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
	- [[TCU]], [[VANET]]s, [[comfort domain]], [[energy domain]], [[infotainment domain]], [[drive domain]], [[diagnostic domain]]

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

- based on [[ISO 21434]]