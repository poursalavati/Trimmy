# Trimmy
This script simply uses seqkit to trim sequences based on the input list and saves the trimmed sequences to a new output file.

## Usage

To use the script, run the following command:

```
python Trimmy.py [-v] <input_file> <input_fasta> <output_fasta>
```

- `-v`: Optional flag to enable verbose output (processing information and error messages).
- `<input_file>`: The file containing the IDs, start positions, and end positions.
- `<input_fasta>`: The input FASTA file containing the sequences to be trimmed.
- `<output_fasta>`: The output FASTA file where the trimmed sequences will be saved.

  ## Input File Format

The input file should be a tab-separated file with the following columns:

1. ID: The identifier of the sequence to be trimmed.
2. Start: The start position of the region to be trimmed (inclusive).
3. End: The end position of the region to be trimmed (inclusive).

Example input file:
```
ID      Start   End
seq1    1       100
seq2    50      200
seq3    75      150
```

Note: The first line of the input file should be a header line and will be skipped during processing.

## Dependencies

- Python 3.x
- seqkit (https://github.com/shenwei356/seqkit)

Make sure you have Python and seqkit installed on your system before running the script.

## Output

The trimmed sequences will be saved to the specified output FASTA file. If the `-v` flag is provided, the script will display processing information and error messages.
