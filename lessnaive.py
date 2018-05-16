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
	#reverse the string otherwise its not reverse 
    return reverse_complement[::-1]

def FrequentWords(text, k):
	pats = [] #datastructure to hold the patterns during operation
	max_pats = []  	# Ausgabeliste, alle Pattern mit maximalem count
	FrequentPatterns={} #dict to save count of current pattern
	COUNT=[]  #saves how often patterns appear that are saved in pats
	#iterates over text and increments the patterncount in the hashmap
	for i in range(0, len(text) -k + 1):
		# extract current pattern (k-mer)
		pattern = text[i:i+k]
		if pattern in FrequentPatterns:
        		FrequentPatterns[pattern] += 1
    		else:
        		FrequentPatterns[pattern] = 1
	#calculates count of pattern and its reverse and saves in lists
	for pat, count in FrequentPatterns.items():
		pat_reversed = reverse(pat)
		reverse_count = 0
		if pat_reversed in FrequentPatterns:
			reverse_count = FrequentPatterns[pat_reversed]
		sum_count = count + reverse_count
		pats.append(pat)
		COUNT.append(sum_count)
	#find max value
	max_count = max(COUNT)
	#find patterns with max count and append to max_pats
	for index, value in enumerate(COUNT):
		if value == max_count:
			max_pats.append(pats[index])
	list(set(max_pats))  # remove duplicates
	ret_max_mers = ' '.join(max_pats)
	return ret_max_mers
dna="CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG"

k=12
print(FrequentWords(dna,k))
