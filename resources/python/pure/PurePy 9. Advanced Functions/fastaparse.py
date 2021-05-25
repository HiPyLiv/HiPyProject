def fasta_parser(pFile):
    '''
    Generator, reads from opened fasta file and yields dictionaries
    with the following fields.
       'seq' -> full DNA sequence
       'name' -> name of sequence
    Lines starting with > are headers, signalling new sequence
    records.
    Lines starting with ; are comments, which should be skipped.
    '''
    genedict = {}
    sequence = []
    for line in pFile:
        if line[0] == ';':
            continue
        elif line[0] == '>':
            genedict['name'] = line.split()[0][1:]
        elif line[0] in "TGAC":
            sequence.append(line.strip("\n"))
        else:
            genedict['seq'] = ''.join(sequence)
            yield genedict
            sequence = []
            genedict = {}
    genedict['seq'] = ''.join(sequence)
    yield genedict


with open("genes-short.fasta") as genefile:
    genelist = [gene for gene in fasta_parser(genefile)]


for gene in genelist:
    print(gene)
