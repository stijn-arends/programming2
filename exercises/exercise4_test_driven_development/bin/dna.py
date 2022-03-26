# exercise: https://www.bartbarnard.nl/programming2/exercise4.html
import regex as re

class NotDNAError(Exception):
    """Exception raised sequence that do not only consist of ATCG.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = f"The provided sequence does not only conists of ATCG characters."
        super().__init__(self.message)


class DNA:
    """
    DNA class
    """
    def __init__(self, seq) -> None:
        """
        init
        """
        if not isinstance(seq, str):
            raise TypeError(f"Sequence must be a string, not a {type(seq)}")

        if not re.compile('^[ACTG]+$').match(seq.upper()):
            raise NotDNAError

        if len(seq) % 3 !=0:
            raise ValueError(f"DNA sequence needs to be a multiple of three.")
        self.__seq = seq.upper()

    @property
    def seq(self):
        """
        Return the DNA sequence
        """
        return self.__seq

    def __str__(self):
        """test"""
        return self.seq

    def __add__(self, val):
        """
        Add a codon to the DNA sequence.

        :parameters
        -----------
        val - str
            A codon (3 nucleotides)

        :returns
        --------
        seq - str
            old sequence plus the new codon
        """
        if not isinstance(val, str):
            raise TypeError(f"Cannot add {type(val)} with str")

        if len(val) != 3:
            raise ValueError(f"Can only add 3 nucleotides not: {len(val)}")
        return self.seq + val


    def __iter__(self):
        """
        Yield codons from the dna seq.
        """
        for i in range(0, len(self.seq), 3):
            yield self.seq[i:i+3]


if __name__ == "__main__":
    dna = DNA('ACTGACTGACTA')

    # # for codon in dna:
    # #     print(codon)

    # test = [dna.seq[i:i+3] for i in range(0, len(dna.seq), 3)]
    # print(test)


    # print(f"DNA seq: {dna.seq}")
    # id_bef = id(dna.seq)
    # dna.__seq = "ACT" # Try to cchange it
    # print(f"DNA after trying to change it: {dna.seq}")
    # id_aft = id(dna.seq)

    # print(f"Check if equal: {id_bef == id_aft}")

    # print(dna + "ACT")

    # ----

    # print(dna.__str__.__doc__)
    # print(dna.__repr__.__doc__)
    # print(f"Check: {dna.__le__.__doc__}")


    # print(DNA.__dict__)
    # for name, method in DNA.__dict__.items():
    #     # if name == "__doc__":
    #     print(method.__doc__)
    #     print(name)

    # reg=re.compile('^[ACTG]+$')
    # correct = reg.match('ACTGTACT')

    # print(correct)

    # wrong = reg.match('ACTGTACTH')
    # print(wrong)
    # if not re.compile('^[ACTG]+$').match('ACTGTACTGH'):
    #     print("This is not a match")


    # print("caghgasjdhwajgd".upper())