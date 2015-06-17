import fastq_index
import sys
from fastq_lookup import DictionaryLookup, BinaryLookup

lookup1 = DictionaryLookup("test/test_index", "test/PE-173.40k.fastq")
lookup2 = BinaryLookup("test/test_index", "test/PE-173.40k.fastq")
to_lookup = []
count = 0

for line in open("test/PE-173.40k.fastq", 'r'):
    if count % 4 ==0:
        to_lookup.append(line.strip())
    count += 1


for id in to_lookup:
    res1 = lookup1.find_entry(id)
    res2 = lookup2.find_entry(id)
    if res1 != res2:
        print >> sys.stderr, "TEST FAILED", id
        sys.exit(-1)
    if res1[0] != id:
        print >> sys.stderr, "TEST FAILED", id
        sys.exit(-1)
    if res2[0] != id:
        print >> sys.stderr, "TEST FAILED", id
        sys.exit(-1)

print "TESTS PASSED"
