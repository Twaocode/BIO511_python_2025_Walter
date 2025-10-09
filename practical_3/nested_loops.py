sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['ATG', 'TAA', 'TGA', 'TAG']

for sequence in sequences:
    for codon in codons:
        if codon in sequence:
            if codon == 'ATG':
                print("startcodon " + codon + " is in " + sequence)
                if codon == 'ATG' and 'TGA' or 'TAA' or 'TAG':
                    print(sequence + " contains both start and stop codons")
            elif codon == 'TGA' or 'TAA' or 'TAG':
                print("stopcodon " + codon + " is in " + sequence)

data1 =dict ({"Startcodon" : 'ATG', "stopcodon":['TAA', 'TGA', 'TAG']})
for key_purpose, value_codon in data1.items(): 
    print(key_purpose)
    print(value_codon)

start = 'ATG'
stop = 'TAA'
stop1 = 'TGA'
stop2 = 'TAG'

for sequence in sequences:
    if start in sequence:
        indexstart = sequence.find(start)
        indexstop = sequence.find(stop)
        indexstop2 = sequence.find(stop2)
        indexstop1 =sequence.find(stop1)
        if indexstart < indexstop or indexstart < indexstop2 or indexstart < indexstop1:
            print('for ' + sequence + ' start codon occurs before stop codon')
        elif indexstart > indexstop or indexstart > indexstop1 or indexstart > indexstop2:
            print('for ' + sequence + ' stop codon occurs befor start codon')
    else:
        print(sequence + ' contains no start codon')



data2 = dict({'pat_001': ['bacZZt98', 'bac889Ytd'], 'pat_002': ['bac0GFrr'], 'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']})

# Loop through the dict printing each key and each value as a list.
for key_patient, value_bact_list in data2.items():  
  print(key_patient)
  print(value_bact_list)

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

for key_patient, value_bact_list in data2.items():  
  print(key_patient)
  print(value_bact_list)
  'bac889Ytd' in value_bact_list

mlist = []

for value_bact_list in data2.values():
    for bact in value_bact_list:
        if bact in mlist:
            continue
        elif mlist != bact:
            mlist.append(bact)

print(mlist)

for key in data2.keys():
    print(key)


mdict = {}

for value_bact_list in data2.values():
    for bact in value_bact_list:
        if bact not in mdict:
            mdict[bact] = []
        elif bact in mdict:
            continue

print(mdict)
print(f"Data2 ITEMS: {data2.items}") #dict
for key in data2.keys():
    print(key, 'has quantity', data2[key])


for key_patient, value_bact_list in data2.items():
    for key_bact in mdict:
        if key_bact in data2[key_patient]:
            mdict[key_bact].append(key_patient)
        else:
            continue


print(mdict)
(list(data2.keys())[list(data2.values()).index(bacZZt98)]).append(key_patient)
            

print(mdict)

