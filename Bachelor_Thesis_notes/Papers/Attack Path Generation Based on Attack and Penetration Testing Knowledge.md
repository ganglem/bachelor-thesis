Tags: #paper #model-based #automotive #todograph 
See also: [[Model-Based Security Testing of Vehicle Networks]]


## Abstract

Based on the [[Model-Based Security Testing of Vehicle Networks]] approach with [[EFSM]] as a foundation, a database containing successful vehicular penetration tests is proposed to faciliate and **automate** [[Penetration Testing]] by generating [[Attack Path]]s


## Introduction

### Problem
- [[Security Testing]] is carried out in late stages of development
- [[Penetration Testing]] is carried out manually, experience-based, explorative
	- considered difficult to automate
- Due to high complexity of modern vehicles this appraoch is not feasible 
	
### Solution
- [[Model-Based Security Testing]] 
- automate [[Penetration Testing]] with the help of a database containing successful [[Penetration Testing]]
- [[Attack Path]]s are automatically generated


## Background and Related Work

- [[Model-Based Security Testing of Vehicle Networks]]
- [[Model-Based Testing]]
- [[Model-Based Security Testing]]
- [[Automation in Automotive Security by Using Attacker Privileges]]
- [[Security Testing]]
- [[Security Testing in the Automotive Domain]]


## Approach and Modeling Process

- [[Penetration Testing]]
- Security model based on [[E - E Architecture]]
- consider its entities which have an impact on the cyber security of a vehicle
- introduce concept of [[Attacker Privileges]]


## Attack Path Generation Using an Attack Database

- [[EFSM]]
	- event = [[Exploit]]
	- guard = [[Vulnerability]]
	- action = Privilege, Violated Security Property
- database describes which [[Vulnerability]] and [[Exploit]] can be used
	- attack taxonomy and classification
	- describes [[Attack]] steps, requirements, restricitons, component and interface
	- [[STRIDE]] to describe exploit of transition
	- [[CAPEC]], [[CWE]]
	- transitions can be described by database
- [[Attack Path]]s can be found exactly as described in the database
- [[Attack Path]]s can be composed of [[Attack]] steps found in the database
- possible to find new [[Attack Path]]s based on permutation of existing [[Attack]] steps


## [[Attack Path]] generation based on [[Penetration Testing]] experience

- handle and capture experience of a tester
- database can be seen as a collection of [[Attacker]] experience, behavior and knowledge
- creating database can be done iteratively over several penetration tests
- can be transferred to test scripts
- successful [[Attack]] steps are logged/recorded and transferred to database


## Discussion

- this appraoch is similar to [[TARA]] and can be coupled with it
- can be done previous to [[Penetration Testing]]
- risk that attack path is not transferable
	- can be circumvented by permutation of pervious attacks
- would make sense to carry out further testing activities, e.g. [[Black-Box Testing]]
- does not cover all aspects
- only knows that there is a [[Vulnerability]] but not the root of it