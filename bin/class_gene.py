'''
NAME
    class_gene.py

VERSION
    1.0

Author
    Salvador Gonzalez Juarez <salglzj@lcg.unam.mx>

Description

    This program contains a class that contains some the features of a gene.

CATEGORY
    Gene features

USAGE
    % usage: class_gene.py

ARGUMENTS
    None
'''

# Defines a class which contains the features of an average gene.
class Gene:
    def __init__(self, name, sequence, start_position, end_position, chromosome = None, gene_type = None, organism = None):
        self.name = name
        self.sequence = self._set_sequence(sequence)
        self.start_position, self.end_position = self._set_positions(start_position, end_position)
        self.chromosome = chromosome
        self.gene_type = gene_type 
        self.organism = organism

    def get_gc_content(self):
        '''
        This function calculates the GC content of the sequence.
        :param self: str, the complete nucleotide sequence obtained from the self Gene class.
        :return float, the value of the GC percentage of the sequence.
        '''
        gc_content = ((self.sequence.count("G") + self.sequence.count("C")) / len(self.sequence)) * 100
        return gc_content

    def get_at_content(self):
        '''
        This function calculates the AT content of the sequence.
        :param self: str, the complete nucleotide sequence obtained from the self Gene class.
        :return float, the value of the AT percentage of the sequence.
        '''
        at_content = ((self.sequence.count("G") + self.sequence.count("C")) / len(self.sequence)) * 100
        return at_content

    def get_complement(self):
        '''
        This function generates the complemantary sequence of a nucleotide sequence, by changing the nucleotides of the sequence.
        :param self: str, the complete nucleotide sequence obtained from the self Gene class.
        :return str, complementary sequence of the nucleotide sequence.
        '''
        complement = self.sequence.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
        complement = complement.upper()
        complement = complement[::-1]
        return complement

    @staticmethod
    def _set_positions(start_position, end_position):
        '''
        This function checks that the edge values are correct.
        :param start_position: int, value of the start position of the gene in the chromosome.
        :param end_position: int, value of the end position of the gene in the chromosome.
        :return int, a correct value for the start_position.
        :return int, a correct value for the end_position.
        '''
        if end_position <= start_position or start_position <= 0:
            raise Exception("Edge values are not valid")
        return start_position, end_position

    @staticmethod
    def _set_sequence(sequence):
        '''
        This function checks that the letters of the sequence are correct.
        :param sequence: str, sequence of the gene.
        :return str, the same sequence, with capital letters.
        '''
        sequence = sequence.upper()
        for nucleotide in sequence:
            if (nucleotide != "A") and (nucleotide != "C") and (nucleotide != "T") and (nucleotide != "G"):
                raise Exception("Wrong nucleotides in the sequence") 
        return sequence

# Give values to each attribute of the class Gene.
gene = Gene("araC", "atcg", 1000, 1300, 2, "gene", "human")
print(gene.get_complement())