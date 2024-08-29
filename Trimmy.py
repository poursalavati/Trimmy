# Naser Poursalavati
# me-at-poursalavati.com
# 29082024
import subprocess
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) < 4:
    print("Usage: python script.py [-v] <input_file> <input_fasta> <output_fasta>")
    sys.exit(1)

# Check if the verbose flag is provided
verbose = False
if sys.argv[1] == '-v':
    verbose = True
    input_file = sys.argv[2]
    input_fasta = sys.argv[3]
    output_fasta = sys.argv[4]
else:
    input_file = sys.argv[1]
    input_fasta = sys.argv[2]
    output_fasta = sys.argv[3]

# Open the input file and read its contents
with open(input_file, 'r') as file:
    lines = file.readlines()

# Open the output file in write mode
with open(output_fasta, 'w') as outfile:
    # Loop through each line in the input file (skipping the header)
    for line in lines[1:]:
        # Extract the ID, start, and end positions from the line
        id, start, end = line.strip().split()
        
        if verbose:
            print(f"Processing ID: {id}")
        
        # Use seqkit grep to extract the sequence with the matching ID
        grep_cmd = f"seqkit grep -p {id} {input_fasta}"
        grep_process = subprocess.Popen(grep_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        grep_stdout, grep_stderr = grep_process.communicate()
        
        if grep_process.returncode != 0:
            if verbose:
                print(f"[ERROR] seqkit grep failed for ID: {id}")
                print(f"[ERROR] {grep_stderr.decode('utf-8')}")
            continue
        
        # Use seqkit subseq to trim the sequence based on the start and end positions
        subseq_cmd = f"seqkit subseq -r {start}:{end}"
        subseq_process = subprocess.Popen(subseq_cmd, shell=True, stdin=subprocess.PIPE, stdout=outfile, stderr=subprocess.PIPE)
        subseq_stdout, subseq_stderr = subseq_process.communicate(input=grep_stdout)
        
        if subseq_process.returncode != 0:
            if verbose:
                print(f"[ERROR] seqkit subseq failed for ID: {id}")
                print(f"[ERROR] {subseq_stderr.decode('utf-8')}")
            continue

if verbose:
    print(f"Trimmed sequences saved to {output_fasta}")
