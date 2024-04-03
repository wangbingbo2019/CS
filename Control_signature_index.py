import pandas as pd

def Control_Signature_Index(nodetype_file,linktype_file):
    """
    function: Control_Signature_Index
    Description: This function is used to indicate the control signature of each node in the directed network.
    input: nodetype_file: node type files with the suffix of “.nodetype” with 6 columns: #Name  K    Kin  Kout  Type-I  Type-II
            and linktype_file: Link type files with the suffix of “.linktype” with 3 columns: #Source  Target  Type
    output: Control_Signature_Result.txt: The output file with 5 columns: Node_name  Nr  Li  Nl  Lr ,which represent the node index and the 4-tuple control signature.
    """
    df_nodetype=pd.read_csv(nodetype_file, sep= ' ')#Documentation of node types
    df_linktype=pd.read_csv(linktype_file, sep = ' ')#Documentation of link types
    nodelist=[]
    for node in df_nodetype.iloc[:,0]:
        nodelist.append(str(node))

    Node_Location={}
    for node in nodelist:
        if df_nodetype.iloc[nodelist.index(node),2] == 0:#The node in-degree is 0
            Node_Location[node]=0
        if df_nodetype.iloc[nodelist.index(node),3] == 0:#The node out-degree is 0
            Node_Location[node]=1
        if df_nodetype.iloc[nodelist.index(node),2] > 0 and df_nodetype.iloc[nodelist.index(node),3] > 0:
            Node_Location[node]=2#The in-degree and out-degree are not zero.
            
    Link_Removal={}  
    sourcegene=set()
    targetgene=set()
    for i in range(0,len(df_linktype.index)):
        if df_linktype.iloc[i,2] == 0: #All critical edges in the network
            sourcegene.add(df_linktype.iloc[i,0])#Nodes whose outgoing edges are critical
            targetgene.add(df_linktype.iloc[i,1])#Nodes whose ingoing edge is critical
    allcritical_gene=sourcegene.intersection(targetgene)#Outgoing and incoming edges are critical nodes

    for node in nodelist:
        if node in allcritical_gene:#Outgoing and incoming edges are critical nodes
            Link_Removal[node]=0
        if node in sourcegene.difference( allcritical_gene):#whose outgoing edges are critical
            Link_Removal[node]=1
        if node in targetgene.difference( allcritical_gene):#whose ingoing edge is critical
            Link_Removal[node]=2
        else:#Outgoing and incoming edges are not critical nodes
            Link_Removal[node]=3

    out=open('Control_Signature_Result.txt','w')
    out.write('Node_name')
    out.write('\t')
    out.write('Nr')
    out.write('\t')
    out.write('Li')
    out.write('\t')
    out.write('Nl')
    out.write('\t')
    out.write('Lr')
    out.write('\n')
    for node in nodelist:
        out.write(str(node))
        out.write('\t')
        out.write(str(df_nodetype.iloc[nodelist.index(str(node)),4]))
        out.write('\t')
        out.write(str(df_nodetype.iloc[nodelist.index(str(node)),5]))
        out.write('\t')
        out.write(str(Node_Location[str(node)]))
        out.write('\t')
        out.write(str(Link_Removal[str(node)]))
        out.write('\n')
    out.close()

if __name__ == '__main__':
    nodetype_file='test.dat.nodetype'#node type files with the suffix of “.nodetype”
    linktype_file='test.dat.linktype'#Link type files with the suffix of “.linktype”
    Control_Signature_Index(nodetype_file,linktype_file)
    