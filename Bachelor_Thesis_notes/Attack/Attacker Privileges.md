Tags: #attack #model-based #todograph
Related: [[Automation in Automotive Security by Using Attacker Privileges]]

*As defined in [[Model-Based Security Testing of Vehicle Networks]]
and mentioned in [[Attack Path Generation Based on Attack and Penetration Testing Knowledge]]

Transition model is based on [[EFSM]]

- **Read/Write**: read/write data on a communication system
		- channels are not protected by secrity measures
			- immediately gains access
		- interpretation needed otherwise
- **Execute**: execute functions (triggerig diagnostics on [[ECU]])
- **Read**: read or extract data from component (firmware of [[ECU]])
- **Write**: write data on component ([[Buffer Overflow]] on [[ECU]])
- **Full Control**: [[root privileges]]

[[Attacker]] needs to reach on of those privileges in order to access further attached communication systems and components

E.g.:

- [[Attacker]] connects to the vehicle via [[OBD]]
- [[OBD]] is connetced to Central [[Gateway]] via [[CAN]]
- Central [[Gateway]] is used to gain access to the internal vehicle network
