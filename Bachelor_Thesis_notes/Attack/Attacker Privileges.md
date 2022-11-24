Tags: #attack #model-based

*As defined in [[Model-Based Security Testing of Vehicle Networks]]
and mentioned in [[Attack Path Generation Based on Attack and Penetration Testing Knowledge]]

- **Read/Write**: read/write data on a communication system
		- channels are not protected by secrity measures
			- immediately gains access
		- interpretation needed otherwise
- **Execute**: execute functions (triggerig diagnostics on [[ECU]])
- **Read**: read or extract data from component (firmware of [[ECU]])
- **Write**: write data on component ([[Buffer Overflow]] on [[ECU]])
- **Full Control**: [[root privileges]]

[[Attacker]] needs to reach on of those privileges in order to access further attached communication systems and components

