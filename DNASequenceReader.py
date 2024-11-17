


class DNASequenceReader:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.validate()

    def validate(self):
        valid = ["A", "T", "G", "C"]
        for letter in self.sequence:
            if letter not in valid:
                raise ValueError("INVALID SEQUENCE")

    def reverse(self):
        return self.sequence[::-1]

    def complement(self):
        comp = {"A": "T", "C": "G", "G": "C", "T": "A"}
        c = ""
        for letter in self.sequence:
            c += comp[letter]
        return c

    def reverse_complement(self):
        return self.complement()[::-1]

    def convert_to_rna(self):
        c = ""
        for letter in self.sequence:
            if letter == "T":
                c += "U"
            else:
                c+= letter
        return c

if __name__ == "__main__":
    dna = DNASequenceReader("atgctt")
    print("The sequence: " + dna.sequence)
    print("The reverse: " + dna.reverse())
    print("The complement: " + dna.complement())
    print("The reverse-complement: " + dna.reverse_complement())
    print("converted to RNA: " +  dna.convert_to_rna())
