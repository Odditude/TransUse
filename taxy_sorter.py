
def get_unwanted_gene(a, b, c):
    """
    Prepares a file of unwanted genes, these genes does not have the approved  taxi.
    :param a: File with two columns: Gene, taxi
    :param b: List of allowed taxi
    :param c: Output file, see return
    :return: File with genes with unwanted species annotations.
    """
    gene_taxi_file = open(a)
    gene_taxi_lines = gene_taxi_file.readlines()[1:]
    wanted_taxi = b
    unwanted_gene = open(c, 'w+')
    counter = 0
    new_counter = 0

    for gene_taxi in gene_taxi_lines:
        counter += 1
        taxi = gene_taxi.split()[1]
        if taxi not in wanted_taxi:
            new_counter += 1
            newline = gene_taxi.split()[0] + '\n'
            unwanted_gene.write(newline)
    print("Sequences in total: " + str(counter))
    print("Unwanted sequences: " + str(new_counter))
    gene_taxi_file.close()
    unwanted_gene.close()


def get_desired_gene(j, k, l):
    """
    Searches through the entire gene list, if gene is not unwated it will be printed to output.
    Output will be used to sort fasta file through seqtk.
    :param a: The unwanted gene file from get_unwanted_gene.
    :param b: The gene names from the fasta file.
    :param c: Output, see return
    :return: A file with only the desired genes.
    """
    unwanted_gene_list = j
    full_gene_file = open(k)
    desired_genes = open(l, 'wt')
    counter = 0

    for gene in full_gene_file:
        with open(unwanted_gene_list) as j:
            if gene not in j.read():
                desired_genes.write(gene)
            else:
                counter += 1


    print("Filtered sequences: " + str(counter))
    full_gene_file.close()
    desired_genes.close()

def get_it_all(wanted_taxi,gene_taxi, gene_list, unwanted_genes, filtered_genes):
    print("Running: get_unwanted_gene")
    get_unwanted_gene(gene_taxi,wanted_taxi,unwanted_genes)
    print("Done running: get_unwanted_gene")
    print("Running: get_desired_gene")
    get_desired_gene(unwanted_genes,gene_list,filtered_genes)
    print("༼ つ ◕_◕ ༽つ  Done")

#=========#
# The run #
#=========#
# List of approved taxi
wanted_taxi = ['Streptophyta', 'Brassicales', 'fabids', 'Poales', 'Liliopsida', 'Eukaryota', 'Viridiplantae',
               'asterids', 'Chlorophyta']

# Input files
gene_taxi = r"Z:\Work\NorfabShare\Transcriptomics\Assemblies\DRAP\Hedin\eggNOG\gene_taxi_files\Young_Leaf-gene_taxi.txt"
gene_list = r"Z:\Work\NorfabShare\Transcriptomics\Assemblies\DRAP\Hedin\Gene_lists\Headers_hedin-youngLeaf.txt"

# Output files
unwanted_genes = r"Z:\Work\NorfabShare\Transcriptomics\Assemblies\DRAP\Hedin\eggNOG\unwated_genes\Young_Leaf_unwanted.txt"
filtered_genes = r"Z:\Work\NorfabShare\Transcriptomics\Assemblies\DRAP\Hedin\eggNOG\Filtered_Transcriptomes\Young_Leaf_filtered_list.txt"


get_it_all(wanted_taxi, gene_taxi, gene_list, unwanted_genes, filtered_genes)
