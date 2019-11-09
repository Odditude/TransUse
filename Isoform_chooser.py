import os

corset_cluster = open('Z:/Work/NorfabShare/Transcriptomics/Clusters/M02_clusters.txt')
output = open('Z:/Work/NorfabShare/Transcriptomics/Headers/M02_headers_aalen.txt', 'w')
headers = open('Z:/Work/NorfabShare/Transcriptomics/Headers/4Cultivars_Header.txt')

output.write("Cluster" + '\t' + "Transcript" + '\t' + "aalen" + '\n')


dic_aalen = dict()
dic_percent = dict()
dic_complete = dict()

for line in headers:
    gene = line.split(" ")[0][1:]
    aaq = line.split(";")[1]
    split_aaq = aaq.split(",")
    aalen, percent, complete = split_aaq[0], split_aaq[1], split_aaq[2]
    aalen = aalen.split("=")[1]
    dic_aalen[gene] = aalen
    dic_percent[gene] = percent
    dic_complete[gene] = complete


for cors in corset_cluster:
    sline = cors.split("\t")
    gene = sline[0]
    gene = gene.strip()
    cluster = sline[1]
    cluster = cluster.strip()
    key_aalen = dic_aalen[gene]
    line = cluster + '\t' + gene + '\t' + key_aalen + '\n'
    output.write(line)

corset_cluster.close()
output.close()
headers.close()


headers = open('Z:/Work/NorfabShare/Transcriptomics/Headers/M02_headers_aalen.txt')
cluster_csv = open('Z:/Work/NorfabShare/Transcriptomics/Clusters/M02_longest_aalen.txt', "w")

dic_headers = dict()


for value in headers:
    cluster = value.split()[0]
    gene = value.split()[1]
    aalen = value.split()[2]
    aalen = aalen.strip()
    if cluster in dic_headers:
        if dic_headers[cluster].split()[1] < aalen:
            dic_headers[cluster] = gene + ' ' + aalen
    else:
        dic_headers[cluster] = gene + ' ' + aalen

for key, val in dic_headers.items():
    cluster_csv.write(key + ' ' + val + '\n')
headers.close()


'''
for cluster in corset_cluster:
    sline = cluster.split("\t")
    gene = sline[0]
    gene = gene.strip()
    key_aalen = dic_aalen[gene]
    key_percent = dic_percent[gene]
    key_complete = dic_complete[gene]
    line = cluster.strip('\n') + '\t' + key_aalen + '\t' + key_percent + '\t' + key_complete + '\n'
    newopen.write(line)
'''
