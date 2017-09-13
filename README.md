# IVON
Integrative Viral Ontology Network





For the annotation of a viral genome against the IVON provided databases we suggest using the python code provided below. This script will annotate yours genome using DIAMOND (https://github.com/bbuchfink/diamond), however the script can easily be adapted to run your local sequence aligner (LSA) of choice. 

Before its use, you must convert each of the FASTA database files into the database format for your LSA of choice, in this example DIAMOND and so `*.dmnd` files are used within a folder called `DIAMOND_db`. With DIAMOND this can be achieved using the `diamond makedb --in DATABASE.fa -d DATABASE`. Your genome must also have been passed through a gene predictor such as Prodigal (https://github.com/hyattpd/Prodigal). This will provide  a fasta file containing coding regions that can be used as input by IVON.


```
import glob
import sys
import subprocess

novel_genome = 'GENOME.fasta'

for cfile in glob.glob('DIAMOND_db/*.dmnd'):
    print 'Comparing genome to... ' + cfile.split('/')[2].replace('.dmnd','')
    sys.stdout.flush()
    needed = cfile.replace('.dmnd','')
    bashCommand =  'diamond blastx -d ' + needed + ' -q ' + novel_genome + ' -a ' + novel_genome.split('/')[1] + '-OUTPUT/' + cfile.split('/')[2].split('.')[0] + '-RAN '
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    #print output
    
    bashCommand = '/Users/thomashitch/Programs/diamond-master/diamond view -a ' + novel_genome.split('/')[1] + '-OUTPUT/' + cfile.split('/')[2].split('.')[0] + '-RAN -o ' + novel_genome.split('/')[1] + '-OUTPUT/' + cfile.split('/')[2].split('.')[0] + '-RAN.m8'
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()    
    
```        
