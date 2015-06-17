#FastqIndex

This is a library/tool for fast access of fastq files. It makes use of indexing each read in a fastq file and sorting the results, this allows for binary search across files. 

## Installation
If you don't want it install globally, use the --user flag.
    python setup.py install

## Building index

It's important to note that the library will sort the reads lexographically inside of python. For very large python files this takes A LOT of memory. You can presort the fastq files
and then use the -s flag to tell the program not to sort the files. To presort a fastq file use the included sort_fastq.sh script. You may also edit this file or use whatever command you'd 
prefer. Just note that the files MUST be sorted lexographically for the BinaryLookup to properly function.
 
    FastqIndex -f to_index.fastq -c index_name
  
## Usage
Take a look at test/test.py for an example of creating an index and accessing random id's with both methods. Briefly, there are two classes, BinaryLookup and DictionaryLookup. BinaryLookup makes use of binary search to find reads, which is useful for huge fastq files, where as DictionaryLookup reads the entire index into memory. This is more efficient if you have enough memory and are doing a large number of lookups. To perform a lookup, 
    lookup = BinaryLookup("test/test_index", "test/PE-173.40k.fastq")
    lookup.find_entry(read_id)

    lookup = DictionaryLookup("test/test_index", "test/PE-173.40k.fastq")
    lookup.find_entry(read_id)
Where read_id is the id WITHOUT the newline character in your fastq file. It will return a list for each portion of the fastq file.

## TODO
Implementing some encoding for the index. Right now the generated indexes are relatively large and pretty much only exist to make lookup easy. With compression/encoding this could be much faster and efficient.

## Testing

Only simple tests are implemented right now. It just creates an index for a random fastq file and asserts that both lookups return the same results. Run the test with:
    make test
