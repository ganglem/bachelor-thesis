Tags: #paper #model-based #automotive 

## Abstract

[[Model-Based Security Testing]] is introduced using an [[EFSM]].


## Introduction

### Problem
- Methods for security testing, such as pentests, are usually carried out manually in late phases of development.
	- Vulnerabilites can only be eliminated in late stages
- Standards like [[ISO 21434]], [[UN R155]]
	
### Solution
- [[Model-Based Security Testing]]


## Background and Related Work

- [[Model-Based Testing]]
- [[Model-Based Security Testing]]
- [[Attack Path Generation Based on Attack and Penetration Testing Knowledge]]
- [[Automation in Automotive Security by Using Attacker Privileges]]


## Automotive Security Model

### **A. [[E - E Architecture]]**

### **B. Security Measures and Further Development Artifacts to protect vehicles against attacks**
- E.g. data encryption, [[SecOC]], access control

### **C. [[Attack]] Characteristics**
- violated security property: reason why attack is possible in the first place
- exploited vunerability: effect of an attack to a system
- **[[Attacker Privileges]]**

### **D. Creating the Security Model**
1. create basis
	- [[E - E Architecture]] basis
	- environmental entities
		- communication
		- influences
		- [[Attacker]]
	- [[Vulnerability]]
2. apply [[Attacker Privileges]]
	- to gain a specific privilege on the gateway, a vulnerability must be exploited

**This model is based on [[EFSM]]**
- Model elements: [[Attacker Privileges]]
- Transitions: [[Vulnerability]]



## Proof of Concept

- Attacker can connect to any interface to carry out attacks
- Demonstration by choosing different entry points and as a result different [[Attack Path]]
- Security model is used to represent security-related characteristics of a vehicular network
- Analyze model for attack paths
- Model contained several attack paths that were executed on the real vehicle and was able to describe attack path
	- prior identification could have led to further measures
- abstract view serves to identify all possible attack paths in a system
	- attatch possible exploits with [[STRIDE]] classification

- incremental approach allows redefinition of attack paths
- thus can be used at different stages during development


## Discussion

- Identification of attack paths is very similar to performing a [[TARA]]
- this approach considers security requirements or measures unlike TARA
- potential to couple TARA
- Prioritization due to large number of vehicular components
- attacker already has some privileges