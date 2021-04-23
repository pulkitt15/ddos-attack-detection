#  Software Engineering Project (CSE - 381)

This repository contains source code for the Software Engineerin Project, IIT (BHU) Varanasi - Finding DDoS Attack Sources.
  > **Guided By**: [Dr. A.K. Tripathi](https://www.iitbhu.ac.in/dept/cse/people/aktripathicse), Professor, CSE, IIT (BHU) Varanasi.<br/>
  > **Mentored By**: Ms. Dipty Tripathi, Research Scolar, CSE, IIT (BHU) Varanasi.
  
 ## Finding DDoS Attack Sources
 - The objective of the project is to "Implement an algorithm to find source of attack." 
 - The source of the project is the **python implementation** of the algorithm proposed in the paper **[Finding DDoS attack sources: Searchlight localization algorithm for network tomography](https://ieeexplore.ieee.org/document/5982570#:~:text=Publication%20%7C%20IEEE%20Xplore-,Finding%20DDoS%20attack%20sources%3A%20Searchlight%20localization%20algorithm%20for%20network%20tomography,communications%20on%20a%20national%20level.) by Omer Demir and Bilal Khan**
 - The paper proposes SLANT algorithm (short for, ‘Searchlight Localization Algorithm for Network Topography’) for localizing the attack sources using information collected over sequences of DDoS attacks. 
 - The proposed method is based on the assumption that the same Botnet execute various DDoS attacks over time. This assumption is based on the argument that a Botnet requires significant investment and exposure to risk, and hence, is likely to be used multiple times.

### Usage
The paper experiments the SLANT algorithm on an artificial network, character by:
- Number of nodes in the network, |V|
- Number of attacking nodes, |D|
- Number of DDoS attacks, n
- Agent Density, k
- Threshold, t

To run the source code, open terminal, change directory to the source code folder, and run the following command:
> python3 interface.py

The interface.py would then ask for |V|, |D|, n, k and t as input. The output of the the algorithm is a suspicion map, s, which maps each node of the network to a suspicion value of being the attacker. Based on threshold, suscipion set is created out of the suspicion map. The nodes in the suspicion set are the attackers of the DDoS attack, according to the SLANT algorithm.  

To measure the performance of the SLANT algorithm, FPR and FNR measures are used.
