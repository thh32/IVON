# Example

This example follows the use of DIAMOND and Prodigal to annotate a novel phage genome using IVON.

The genome of Ruminococcus flavefaciens 007c was searched using PHASTER (http://phaster.ca/) and identified the genome of an incorporated phage, present in `Ruminococcus_flavefaciens_007c.prophage.1.fasta`. 

Prodigal was utilised within the PROKKA annotation framework to identify the coding regions within the novel phages genome producing the file `Ruminococcus_flavefaciens_007c.prophage.1.CDS.ffn`.

The CDS file was then used as the query input and annotated against each of the IVON databases using DIAMOND producing the `.daa` files in `DIAMOND_annotations/Raw_output/`. These were converted into standard tabulated output using the `diamond view` command to produce the `.m8` files in `DIAMOND_annotations/Viewed_output/`.


The `Viewed_output` folder was then used as input by the `IVON_barcoder.py` script to assign the Ruminococcus flavefaciens 007c phage the IVON barcode of 2.0.0.0.0.0.0.0. This barcode only had positive identification of a gene against the DNA-directed_DNA_polymerase_complex database, hence a  2 was placed as the first barcode value. The lack of integrase identification suggests this may not actually be a phage and be a false positive identification by PHASTER.
