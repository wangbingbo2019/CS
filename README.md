# CS
Paper describing this work has been published in Frontiers of Computer Science (FCS) special column “Code & Data”.
Cited as:  Yaoqi SHOU, Bingbo WANG, Zitian YANG. TripletDGC: assessing critical cell types of disease genes by integrating single-cell genomics and human genetics. Front. Comput. Sci., 2025, 19(10): 1910919 https://doi.org/10.1007/s11704-025-41165-y
## This is the software package for indicating control signature of nodes in directed biological networks
### I. Operating environment
Python 3  
C++   
OS: LINUX
### II.Usage  
We proposed a novel 4-tuple index control signature to characterize the control properties of genes in directed biological networks.we take some test files for example to instruct this package.  
After the following steps, all the CS of nodes in directed networks will be obtained in the output file "Control_Signature_Result.txt".  
If the user want to identify CS in their own network, they should run steps 1 and 2 to obtain the CS of nodes in the network.  

**1. ControllabilityAnalysis_v1.0**  
We get this distribution package from Yang-Yu Liu[1]. This will read a network file and run the controllability analysis which is used to get control signature.  
For example:   
Enter the command in Linux terminal:   
./Parse ./test.dat  
./ControllabilityAnalysis ./test.dat  

**Input**: test.dat  

test.dat with 2 columns:  

Column1: node1 index  
Column2: node2 index  
One line means that there is a connection from node1 to node2  

**Output**: test.dat.linktype, test.dat.nodetype  

(1)test.dat.linktype with 3 columns:  

#source target linkType  
source: source node name  
target: target node name  
linkType: link classification: 0 (critical), 1(redundant), 2 (ordinary):     
classify interactions (links) as critical, redundant, or ordinary based on how the MDS changed 
when the interaction was absent. 

(2)test.dat.nodetype with 6 columns:  
#Name K Kin Kout TypeI TypeII  

Name: node index    
K: degree  
Kin: in-degree  
Kout: out-degree  
TypeI: Type-I node classification: 0 (critical), 1(redundant), 2 (ordinary):  
classify nodes as critical, redundant, and ordinary if removing the node increased, decreased, or had no effect on the size of the MDS 
$(N_D)$
TypeII: Type-II node classification: 0 (critical), 1(redundant), 2 (ordinary):  
classify nodes as critical, redundant, and ordinary if the node belonged to many MDSs, no MDSs, or to some but not all MDSs  

**2.Control_signature_index.py**  
This will obtain control signature for all nodes in directed network.    
**Input**: test.dat.linktype, test.dat.nodetype  

**Output**: Control_Signature_Result.txt  

Control_Signature_Result.txt with 5 columns: 

Node_name	Nr	Li	Nl	Lr  
Node_name: node index  
Nr: node removal (Nr), the impact on the size of MDS when a node is removed  
Li:  likelihood in MDSs (Li), the likelihood of a node to be in MDSs  
Nl:  node location (Nl), the node location in control paths  
Lr: link removal (Lr), the category of adjacent links, which indicates whether adjacent links of a node contain critical links  


## Description of supplementary tables  
Table S1 Gene list of 8 biological functional dataset.  

Table S2 Functional profile of genes with different control signatures

Table S3 Control signature of nodes in biological networks.  

Table S4 Biological enrichment of nodes from different networks 

Table S5 Disease module groups.  

Table S6 Quantification and literature verification of EGs in regulating disease core modules.  

Table S7 Pathway enrichment analysis results of schizophrenia.  

Table S8 Role as drug targets for schizophrenia.  

Table S9 Mapping between diseases and tissues.  

Table S10 Description of details in Figure.4C.  

## Orignal data
**IBN Integrated by the six networks.rar** contains the six curated directed network

## References  
[1]	LIU Y Y, SLOTINE J J, BARABÁSI A L. Controllability of complex networks.[J]. Nature, 2011, 473(7346): 167-173.  

