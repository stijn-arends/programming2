# from pytest import capfd
import pytest

from bin.dna import DNA
from bin.dna import NotDNAError


def test_init():
    dna = DNA('ACTGACTGACTA')

    assert all(c in "ACGT" for c in dna.seq), 'DNA sequence does not exists only of ACTG'

    assert len(dna.seq) % 3 ==0, 'DNA sequence is not a multiple of three'


def test_init_wrong():
    with pytest.raises(TypeError):
        dna = DNA(2)


def test_init_wrong_mutiple_three():
    with pytest.raises(ValueError):
        dna = DNA('ACTGACTGACTAA')


def test_init_wrong_sequence():
    with pytest.raises(NotDNAError):
        dna = DNA('AHAKJADWKLH1')


def test_print(capfd):
    dna = DNA('ACTGACTGACTA')

    print(dna)
    out, _ = capfd.readouterr()

    assert out.rstrip('\n') == dna.seq, "Print DNA object does not print the DNA sequence."


def test_add_nucs():
    dna = DNA('ACTGACTGACTA')
    # old = dna.seq
    # dna.seq = dna.seq + "ACG"
    assert dna.seq + "ACG" == "ACTGACTGACTAACG"


def test_add_wrong_type():
    with pytest.raises(TypeError):
        dna = DNA('ACTGACTGACTA')
        dna + 2


def test_add_wrong_length():
    with pytest.raises(ValueError, match = r"Can only add 3 nucleotides not: \d+"):
        dna = DNA('ACTGACTGACTA')
        dna + "ATCG"


def test_iterator():
    dna = DNA('ACTGACTGACTA')

    correct_codons = [dna.seq[i:i+3] for i in range(0, len(dna.seq), 3)]

    for i, codon in enumerate(dna):
        assert codon == correct_codons[i], f"Result is not expected. Expected = {correct_codons[i]}"
    

def test_immutability():
    dna = DNA('ACTGACTGACTA')

    id_before = id(dna.seq)
    dna.__seq = "ACTGTC"
    id_after = id(dna.seq)
    assert id_after == id_before, "seq object is not immutable"


def test_docstrings():

    for name, method in DNA.__dict__.items():
        assert method.__doc__ != None, f"Method: {name} doesn't contain a docstring"
            

