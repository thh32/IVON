# IVON: Integrative Viral Ontology Network

## What is IVON?
IVON is a systematic classification system for viruses. By relying on only the genomic sequence of the query virus and its similarity to known genes (present in custom databases), IVON can assign the query virus a barcode. Each position within the barcoe represents a distinct viral feature from the type of polymerase present to method of interaction with its host. This sequence similarity based approach removes the methodological issues associated with current viral taxonomy such as morphology and host type and instead provides viral groupings based entirely on feature similarity.

## Barcode value table
This table identifies which databases require a match for each of the barcode values to be assigned. This theefore allows researchers to better understand the IVON barcoding system.

## IVON annotation
For the annotation of a viral genome against the IVON provided databases we suggest using the python code provided below. This script will annotate yours genome using DIAMOND (https://github.com/bbuchfink/diamond), however the script can easily be adapted to run your local sequence aligner (LSA) of choice. 

Before its use, you must convert each of the FASTA database files into the database format for your LSA of choice, in this example DIAMOND and so `*.dmnd` files are used within a folder called `DIAMOND_db`. With DIAMOND this can be achieved using the `diamond makedb --in DATABASE.fa -d DATABASE`. Your genome must also have been passed through a gene predictor such as Prodigal (https://github.com/hyattpd/Prodigal). This will provide  a fasta file containing coding regions that can be used as input by IVON.


```
import glob
import sys
import subprocess

novel_genome = 'GENOME_CDS.fa'

for cfile in glob.glob('DIAMOND_db/*.dmnd'):
    print 'Comparing genome to... ' + cfile.split('/')[2].replace('.dmnd','')
    sys.stdout.flush()
    needed = cfile.replace('.dmnd','')
    bashCommand =  'diamond blastx -d ' + needed + ' -q ' + novel_genome + ' -a ' + novel_genome.split('/')[1] + '-OUTPUT/' + cfile.split('/')[2].split('.')[0] + '-RAN '
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    #print output
    
    bashCommand = 'diamond view -a ' + novel_genome.split('/')[1] + '-OUTPUT/' + cfile.split('/')[2].split('.')[0] + '-RAN -o ' + novel_genome.split('/')[1] + '-OUTPUT/' + cfile.split('/')[2].split('.')[0] + '-RAN.m8'
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()    
    
```        


Once the genomes coding regions have been annotated against the IVON databases `IVON_barcoder.py` can be run to assign the viral genome an IVON barcode. `IVON_barcoder.py` can be run as shown below;

```
python IVON_barcoder.py -i GENOME_CDS.fa -f GENOME_CDS.fa-OUTPUT

```

This will then provide a barcode such as `1.0.0.0.1.0.12.0` (barcode for HIV) that can be compared to other barcoded viral species using the `NCBI_viral_species_barcode.txt` file.
