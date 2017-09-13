import glob
import subprocess
import sys
import argparse



print 'IVON started.'
sys.stdout.flush()
#Read in information

parser = argparse.ArgumentParser() #simplifys the wording of using argparse as stated in the python tutorial

# Basic input output files
parser.add_argument("-i", type=str, action='store',  dest='input', help="Input genome FASTA file.") 

parser.add_argument("-f", type=str, action='store',  dest='folder', help="Input folder name containing genome annotation files only.") 


args = parser.parse_args()


novel_genome = str(args.input)
FOLDER = str(args.folder)








#Look through annotation files

print 'Annotation files being read.'
sys.stdout.flush()


results = {}
for dim_file in glob.glob(FOLDER + '/*'):
    print dim_file
    for line in open(dim_file,'r'):
        timber = line.replace('\n','').split('\t')
        cds = timber[0]
        hit = dim_file.split('/')[1].split('-RAN')[0]
        bit = float(timber[11])
        if bit >40:
            if cds in results:
                prev = results[cds]
                if prev[0] > bit:
                    continue
                else:
                    results[cds] = [bit,hit]
            else:
                results[cds] = [bit,hit]




print 'Reducing annotations.'
sys.stdout.flush()


#Reduce to needed information
unique_results = []
for k,v in results.iteritems():
    if v[1] in unique_results:
        continue
    else:
        unique_results.append(v[1])


        



print 'IVON barcode being assigned.'
sys.stdout.flush()



#Produce barcode

one = 0
two = 0
three = 0
four = 0

if 'RNA-directed_DNA_polymerase_complex' in unique_results:
    one = 1

if 'DNA-directed_DNA_polymerase_complex' in unique_results:
    two = 1

if 'RNA-directed_RNA_polymerase_complex' in unique_results:
    three = 1

if 'DNA-directed_RNA_polymerase_complex' in unique_results:
    four = 1

#print one, two, three, four
first_value = 0

if one + two + three + four == 0:
    first_value = 0
elif one + two + three + four == 1:
    if one == 1:
        first_value = 1
    if two == 1:
        first_value = 2
    if three == 1:
        first_value = 3
    if four == 1:
        first_value = 4

elif one + two + three + four == 2:
    if one + two == 2:
        first_value == 5
    if one + three == 2:
        first_value = 6
    if one + four == 2:
        first_value = 7
    if two + three == 2:
        first_value = 8
    if two + four == 2:
        first_value = 9
    if three + four == 2:
        first_value = 10

elif one + two + three + four == 3:
    if one + two + three == 3:
        first_value = 11
    if one + two + four == 3:
        first_value = 12
    if one + three + four == 3:
        first_value = 13
    if two + three + four == 3:
        first_value = 14

elif one + two + three + four == 4:
    first_value = 15


second_value = 0

if 'Integrase_activity' in unique_results:
    second_value = 1
#print str(first_value) + '.' + str(second_value) + '.-'



one = 0
two = 0

if 'Icosahedral_viral_capsid' in unique_results:
    one = 1

if 'Helical_viral_capsid' in unique_results:
    two = 1


third_value = 0

if one + two == 1:
    if one ==1:
        third_value = 1# Its Icosahedral
    elif two ==1:
        third_value = 2# Its helical
elif one + two == 2:
    third_value = 3 #Both helical and Icosahedral regions


#print str(first_value) + '.' + str(second_value) + '.' + str(third_value) + '.-'






fourth_value = 0

if 'Virus_tail' in unique_results:
    fourth_value = 1
#print str(first_value) + '.' + str(second_value) + '.' + str(third_value) + '.' + str(fourth_value) + '.-'




fifth_value = 0

if 'Virus_envelope' in unique_results:
    fifth_value = 1
#print str(first_value) + '.' + str(second_value) + '.' + str(third_value) + '.' + str(fourth_value) +'.' + str(fifth_value) + '.-'





#Reasoning; http://viralzone.expasy.org/all_by_species/936.html

sixth_value = 0

fusion = 0
endocytosis = 0
pore_mediated = 0
cell_to_cell_transport = 0
apoptotic_mimicry = 0
if 'Fusion_of_virus_membrane_with_host_endosome_membrane' in unique_results or 'Fusion_of_virus_membrane_with_host_plasma_membrane' in unique_results  or 'Membrane_fusion_involved_in_viral_entry_into_host_cell' in unique_results:
    fusion = 1
if 'Endocytosis_involved_in_viral_entry_into_host_cell' in unique_results:
    endocytosis = 1
if 'Pore_formation_by_virus_in_membrane_of_host_cell' in unique_results:
    pore_mediated = 1
if 'Transport_of_virus_in_host,_cell_to_cell' in unique_results:
    cell_to_cell_transport = 1
if 'Viral_entry_via_permeabilization_of_inner_membrane' in unique_results:
    apoptotic_mimicry = 1


if fusion + endocytosis + pore_mediated + cell_to_cell_transport + apoptotic_mimicry == 1:
    if fusion == 1:
        sixth_value = 1
    elif endocytosis == 1:
        sixth_value = 2
    elif pore_mediated == 1:
        sixth_value = 3
    elif cell_to_cell_transport == 1:
        sixth_value = 4
    elif apoptotic_mimicry == 1:
        sixth_value = 5

elif fusion + endocytosis + pore_mediated + cell_to_cell_transport + apoptotic_mimicry == 2:
    if fusion == 1:
        if endocytosis == 1:
            sixth_value = 6
        elif pore_mediated == 1:
            sixth_value = 7
        elif cell_to_cell_transport == 1:
            sixth_value = 8
        elif apoptotic_mimicry == 1:
            sixth_value = 9  
    elif endocytosis == 1:
        if pore_mediated == 1:
            sixth_value = 10
        elif cell_to_cell_transport == 1:
            sixth_value = 11
        elif apoptotic_mimicry == 1:
            sixth_value = 12         
    elif pore_mediated == 1:
        if cell_to_cell_transport == 1:
            sixth_value = 13
        elif apoptotic_mimicry == 1:
            sixth_value = 14        
    elif cell_to_cell_transport == 1:
        if apoptotic_mimicry == 1:
            sixth_value = 15 

elif fusion + endocytosis + pore_mediated + cell_to_cell_transport + apoptotic_mimicry == 3:
    if fusion == 1:
        if endocytosis == 1:
            if pore_mediated == 1:
                sixth_value = 16
            elif cell_to_cell_transport == 1:
                sixth_value = 17
            elif apoptotic_mimicry == 1:
                sixth_value = 18
        elif pore_mediated == 1:
            if cell_to_cell_transport == 1:
                sixth_value = 19
            elif apoptotic_mimicry == 1:
                sixth_value = 20
        elif cell_to_cell_transport == 1:
            if apoptotic_mimicry == 1:
                sixth_value = 21


    elif endocytosis == 1:
        if pore_mediated == 1:
            if cell_to_cell_transport == 1:
                sixth_value = 22
            elif apoptotic_mimicry == 1:
                sixth_value = 23
        elif cell_to_cell_transport == 1:
            if apoptotic_mimicry == 1:
                sixth_value = 24

    elif pore_mediated == 1:
        if cell_to_cell_transport == 1:
            if apoptotic_mimicry == 1:
                sixth_value = 25






elif fusion + endocytosis + pore_mediated + cell_to_cell_transport + apoptotic_mimicry == 4:
    if fusion == 1:
        if endocytosis == 1:
            if pore_mediated == 1:
                if cell_to_cell_transport == 1:
                    sixth_value = 26
                elif apoptotic_mimicry == 1:
                    sixth_value = 27

            elif cell_to_cell_transport == 1:
                if apoptotic_mimicry == 1:
                    sixth_value = 28
        elif pore_mediated == 1:
            if cell_to_cell_transport == 1:
                if apoptotic_mimicry == 1:
                    sixth_value = 29

    elif endocytosis == 1:
        if pore_mediated == 1:
            if cell_to_cell_transport == 1:
                if apoptotic_mimicry == 1:
                    sixth_value == 30


elif fusion + endocytosis + pore_mediated + cell_to_cell_transport + apoptotic_mimicry == 5:
    sixth_value = 31


#print sixth_value
#print str(first_value) + '.' + str(second_value) + '.' + str(third_value) + '.' + str(fourth_value) +'.' + str(fifth_value) + '.' + str(sixth_value) + '.-'

#Reasoning; http://viralzone.expasy.org/all_by_species/936.html




one = 0
two = 0
three = 0
four = 0

if 'Modulation_by_virus_of_host_morphology_or_physiology' in unique_results:
    one = 1

if 'Negative_regulation_of_viral_process' in unique_results:
    two = 1

if 'Positive_regulation_of_viral_process' in unique_results:
    three = 1

if 'Regulation_of_defense_response_to_virus_by_virus' in unique_results:
    four = 1

#print one, two, three, four
seventh_value = 0

if one + two + three + four == 0:
    seventh_value = 0
elif one + two + three + four == 1:
    if one == 1:
        seventh_value = 1
    if two == 1:
        seventh_value = 2
    if three == 1:
        seventh_value = 3
    if four == 1:
        seventh_value = 4

elif one + two + three + four == 2:
    if one + two == 2:
        seventh_value == 5
    if one + three == 2:
        seventh_value = 6
    if one + four == 2:
        seventh_value = 7
    if two + three == 2:
        seventh_value = 8
    if two + four == 2:
        seventh_value = 9
    if three + four == 2:
        seventh_value = 10

elif one + two + three + four == 3:
    if one + two + three == 3:
        seventh_value = 11
    if one + two + four == 3:
        seventh_value = 12
    if one + three + four == 3:
        seventh_value = 13
    if two + three + four == 3:
        seventh_value = 14

elif one + two + three + four == 4:
    seventh_value = 15
    
    
    





lysis = 0
budding = 0
cell_to_cell_transport = 0

if 'Cytolysis_by_virus_of_host_cell' in unique_results or 'Cytolysis_by_virus_via_pore_formation_in_host_cell_membrane' in unique_results:
    lysis = 1

if 'Viral_budding' in unique_results or 'Viral_budding_from_plasma_membrane' in unique_results:
    endocytosis = 1

if 'Transport_of_virus_in_host,_cell_to_cell' in unique_results:
    cell_to_cell_transport = 1




eigth_value = 0



if lysis + budding + cell_to_cell_transport  == 0:
    eigth_value = 0
elif lysis + budding + cell_to_cell_transport  == 1:
    if lysis == 1:
        eigth_value = 1
    if budding == 1:
        eigth_value = 2
    if cell_to_cell_transport == 1:
        eigth_value = 3

elif lysis + budding + cell_to_cell_transport  == 2:
    if lysis + budding == 2:
        eigth_value == 4
    if lysis + cell_to_cell_transport == 2:
        eigth_value = 5
    if budding + cell_to_cell_transport == 2:
        eigth_value = 6


elif lysis + budding + cell_to_cell_transport == 3:
    eigth_value = 7




#print str(first_value) + '.' + str(second_value) + '.' + str(third_value) + '.' + str(fourth_value) +'.' + str(fifth_value) + '.' + str(sixth_value) + '.' + str(seventh_value)




Barcode = str(first_value) + '.' + str(second_value) + '.' + str(third_value) + '.' + str(fourth_value) +'.' + str(fifth_value) + '.' + str(sixth_value) + '.' + str(seventh_value) + '.' + str(eigth_value)


total_positives = 0
for i in Barcode.split('.'):
    if int(i) == 0:
        continue
    else:
        total_positives +=1



print 'IVON barcode for ' + novel_genome + '; ' + Barcode
print 'Number of positive values; ' + str(total_positives)



print 'Visit https://github.com/thh32/IVON to compare your IVON barcode to those of previously sequenced viral species.'
sys.stdout.flush()


