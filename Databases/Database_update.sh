
#This script updates all the databases within IVON to include all available proteins in UNIPROT assigned to each GO term.



echo "Database updating begin."


DATE=`date +%Y-%m-%d`

mkdir ${DATE}_FASTA_files

cd ${DATE}_FASTA_files


wget "http://www.uniprot.org/uniprot/?query=go%3A%22cytolysis+by+virus+of+host+cell%22&sort=score&format=fasta" -O Cytolysis_by_virus_of_host_cell.fasta 
wget "http://www.uniprot.org/uniprot/?query=go%3A%22cytolysis+by+virus+of+host+cell%22&sort=score&format=fasta" -O  Cytolysis_by_virus_via_pore_formation_in_host_cell_membrane.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22DNA-directed+DNA+polymerase%22&sort=score&format=fasta" -O  DNA-directed_DNA_polymerase_complex.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22DNA-directed+RNA+polymerase%22&sort=score&format=fasta" -O  DNA-directed_RNA_polymerase_complex.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22DNA+polymerase+activity%22&sort=score&format=fasta" -O  DNA_polymerase_activity.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22endocytosis+involved+in+viral+entry+into+host+cell%22&sort=score&format=fasta" -O  Endocytosis_involved_in_viral_entry_into_host_cell.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22fusion+of+virus+membrane+with+host+endosome+membrane%22&sort=score&format=fasta" -O  Fusion_of_virus_membrane_with_host_endosome_membrane.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22fusion+of+virus+membrane+with+host+plasma+membrane%22&sort=score&format=fasta" -O  Fusion_of_virus_membrane_with_host_plasma_membrane.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22helical+viral+capsid%22&sort=score&format=fasta" -O  Helical_viral_capsid.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22icosahedral+viral+capsid%22&sort=score&format=fasta" -O  Icosahedral_viral_capsid.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22integrase+activity%22&sort=score&format=fasta" -O  Integrase_activity.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22membrane+fusion+involved+in+viral+entry+into+host+cell%22&sort=score&format=fasta" -O  Membrane_fusion_involved_in_viral_entry_into_host_cell.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22modulation+by+virus+of+host+morphology+or+physiology%22&sort=score&format=fasta" -O  Modulation_by_virus_of_host_morphology_or_physiology.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22negative+regulation+of+viral+process%22&sort=score&format=fasta" -O  Negative_regulation_of_viral_process.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22pore+formation+by+virus+in+membrane+of+host+cell%22&sort=score&format=fasta" -O  Pore_formation_by_virus_in_membrane_of_host_cell.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22positive+regulation+of+viral+process%22&sort=score&format=fasta" -O  Positive_regulation_of_viral_process.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22rna-directed+dna+polymerase%22&sort=score&format=fasta" -O  RNA-directed_DNA_polymerase_complex.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22RNA-directed+RNA+polymerase+complex%22&sort=score&format=fasta" -O  RNA-directed_RNA_polymerase_complex.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22RNA+polymerase+activity%22&sort=score&format=fasta" -O  RNA_polymerase_activity.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22regulation+of+defense+response+to+virus+by+virus%22&sort=score&format=fasta" -O  Regulation_of_defense_response_to_virus_by_virus.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22transport+of+virus+in+host,+cell+to+cell%22&sort=score&format=fasta" -O  Transport_of_virus_in_host,_cell_to_cell.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22viral+budding%22&sort=score&format=fasta" -O  Viral_budding.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22viral+budding+from+plasma+membrane%22&sort=score&format=fasta" -O  Viral_budding_from_plasma_membrane.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22viral+entry+via+permeabilization+of+inner+membrane%22&sort=score&format=fasta" -O  Viral_entry_via_permeabilization_of_inner_membrane.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22viral+envelope%22&sort=score&format=fasta" -O  Virus_envelope.fasta
wget "http://www.uniprot.org/uniprot/?query=go%3A%22virus+tail%22&sort=score&format=fasta" -O  Virus_tail.fasta


echo "Compressing files"

gzip *


echo "Databases updated."




