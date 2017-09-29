---
title: "Data Structures in QTL Viewer"
author: Gary Churchill
output: 
  github_document:
    md_extensions: +raw_html+markdown_in_html_blocks
---

#Data Structures in QTL Viewer


Data



annot.mrna - data.frame of annotations

rownames(annot.mrna) is an index number

colnames(annot.mrna)

	NAME	DATA TYPE	EXAMPLE	NOTE
1	id	character	ENMUSG00000000001	
2	symbol	Character	Gnai3	
3	chr	Character	3	
4	start	Integer	108107280	
5	end	Integer	108146146	
6	strand	Integer	-1	
7	middle_point	Integer	108126713	
8	nearest_snp	Integer	10472	snp_index
		


annot.protein – same as annot.mrna (if protein data)




annot.samples – data.frame of sample annotations

rownames(annot.samples) is the Mouse.ID

colnames(annot.samples)

	NAME	DATA TYPE	EXAMPLE	NOTE
1	Mouse.ID	Character	DO-0661	
2	Sex	character 	F	
3	Generation	Character	G8	
4	Age	Numeric	12	


covar – matrix of covariates data, samples (rows) x covariates (columns)
















covar_factors – data.frame of covar information

	NAME	DATA TYPE	EXAMPLE	NOTE
1	column_name	character	age	
2	display_name	character 	Age	


expr.mrna – matrix of expression data, samples (rows) x mrna (columns)

	Example:  R is the number of annot.mrna, S in the number of samples
















expr.protein – same as expr.mrna (if protein data)


G – matrix of samples by samples (kinship matrix)


raw.mrna – matrix of raw mrna data (counts out of emase)


raw.protein – same as raw.mrna (if protein data)


snps – data.frame of SNP data

rownames(snps) is same as marker

colnames(snps)


	NAME	DATA TYPE	EXAMPLE	NOTE
1	Marker	Character	1_40055	
2	Chr	character 	1	
3	bp	Numeric	0.040055	
4	cM	Numeric	0.000000	
5	Pos	Integer	40055	




Values



genoprobs – array 


Glist – list 


N – list 



Calculated Upon Load



probs <- probs_doqtl_to_qtl2(genoprobs, snps, pos_column = "bp")


map <- map_df_to_list(map = snps, pos_column = "bp")





R API on Github:

https://github.com/churchill-lab/qtl_api_docker/blob/master/R/qtlapi.R


