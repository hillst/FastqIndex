.PHONY:	test

default: test

clean: 
	rm -rf *.pyc

test:
	python FastqIndex.py -c test/test_index -f test/PE-173.40k.fastq -b 70
	python test/test.py
	
