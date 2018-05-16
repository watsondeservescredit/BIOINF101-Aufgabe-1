from itertools import product
#quick hack script. replace K in kmer function and DNA in check_mer_count function with your data. 
#returns the most occured mers and their reverse also the maximum count these achieved in the line below

#this function reverses the sequence (c) bioinfo 101
def reverse(input_sequence):
    reverse_complement = ''
    n = len(input_sequence) - 1
    while n >= 0:
        if input_sequence[n] == 'A':
            reverse_complement += 'T'
            n = n-1
        elif input_sequence[n] == 'T':
            reverse_complement += 'A'
            n = n-1
        elif input_sequence[n] == 'C':
            reverse_complement += 'G'
            n = n-1
        else:
            reverse_complement += 'C'
            n = n-1
    return reverse_complement


#this function makes all possible kmers. replace k with your k.
def kmer():
    k = 14
    keywords = [''.join(i) for i in product("ATCG", repeat = k)]
    return keywords

#this functions returns the numbers of counts the mer and its reverse appear in dna sequence. replace dna with your string.
def check_mer_count(mer,mer_reverse):
    dna="GGTTGGCTGGTATCGAAATCACCGCAGCATTGAACGAGGTTGGCTGAACGATGGTATCGGCAGCATTGAACGAGCAGCATTGAACGAAAATCACCTGGTATCGGGTTGGCTGGTATCGTGAACGATGAACGAGCAGCATTGGTATCGTGGTATCGTGAACGAGCAGCATAAATCACCTGGTATCGAAATCACCAAATCACCGGTTGGCGCAGCATAAATCACCTGAACGATGGTATCGTGGTATCGTGGTATCGAAATCACCTGGTATCGTGGTATCGGGTTGGCAAATCACCGGTTGGCGCAGCATGCAGCATAAATCACCAAATCACCGCAGCATGGTTGGCGCAGCATGGTTGGCAAATCACCGCAGCATTGAACGAGGTTGGCGGTTGGCTGAACGATGAACGATGAACGAGCAGCATTGAACGATGAACGAAAATCACCAAATCACCGGTTGGCGCAGCATGGTTGGCTGAACGAGGTTGGCTGAACGAGGTTGGCTGGTATCGTGGTATCGTGGTATCGTGAACGATGGTATCGGGTTGGCGCAGCATTGGTATCGAAATCACCGCAGCATGGTTGGCAAATCACCTGGTATCGGGTTGGCGGTTGGCGGTTGGCGGTTGGCTGAACGAAAATCACCTGAACGAAAATCACCGGTTGGCTGGTATCGTGAACGAGGTTGGCAAATCACCTGGTATCGAAATCACCTGAACGAGGTTGGCAAATCACCAAATCACCGCAGCATGCAGCATAAATCACCGGTTGGCGCAGCATGGTTGGCTGAACGAAAATCACCTGGTATCGAAATCACCTGAACGATGGTATCGTGGTATCGTGGTATCGTGGTATCGTGGTATCG" 						    
    mer_count=dna.count(mer)
    mer_reverse_count=dna.count(mer_reverse)
    return mer_count + mer_reverse_count

#this is the actual function that returns the solution
max_mers = []
max_count = 0
for mer in kmer():
    count = check_mer_count(mer,reverse(mer))
    #edge case: all occurencies 0 useless
    #if mer occurs as often as current max just append to max mer list
    if max_count == count:
        max_count = count
        max_mers.append(mer)
        max_mers.append(reverse(mer))
    #if mer appears more often then current max replace current list with mer
    elif max_count < count:
        max_count = count
        max_mers = [mer]
        max_mers.append(reverse(mer))

ret_max_mers = ' '.join(max_mers)
print(ret_max_mers)
print(max_count)
