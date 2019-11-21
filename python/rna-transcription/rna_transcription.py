def to_rna(dna_strand):
	rna = ""
	for nuc in dna_strand:
		if nuc=="G":
			rna+="C"
		if nuc=="C":
			rna+="G"
		if nuc=="T":
			rna+="A"
		if nuc=="A":
			rna+="U"
	return rna 
	
