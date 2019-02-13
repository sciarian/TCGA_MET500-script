#################################
#
# @Author: Anthony Sciarini
# @Version: (>o_o)>
#
#################################

#Libs
import csv
from sets import Set

matrix_dict = {}
master_gene_list = Set([])
sample_list = Set([])

#matrix_dict = Set({})

#Returns true if the dictionary does not have the key
def key_not_exist(dict,key):
	for k in dict:
		if k == key:
			return False
	return True


#Grab TCGA data
with open('master.maf.txt') as fp:
	
	for line in fp:
		atr = line.split('\t')
		#Update dictionary matrix
		if atr[9] != 'Silent':
			if key_not_exist(matrix_dict,atr[0]):
				matrix_dict[atr[0]] = Set([])
				sample_list.add(atr[0])
				if atr[1] != 'Unknown':
			 		matrix_dict[atr[0]].add(atr[1])
			else:
				if atr[1] != 'Unknown':
					matrix_dict[atr[0]].add(atr[1])
			#Update gene list
			if atr[1] != 'Unknown':
		        	master_gene_list.add(atr[1])
		

#Grab Med500 data
with open('MET500.mut.data.csv') as csvfile:
	
	reader = csv.DictReader(csvfile)

        for row in reader:
                if key_not_exist(matrix_dict, str(row['sample.id'])):
			sample_list.add(row['sample.id'])
                        matrix_dict[str(row['sample.id'])] = Set([])
                        matrix_dict[str(row['sample.id'])].add(row['gene'])
                else:
			matrix_dict[str(row['sample.id'])].add(row['gene'])

		#Update gene list
		master_gene_list.add(row['gene'])




#MAkE A GENE DICTIONARY FOR THE LONG FORMAT
gene_dict = {}

for gene in master_gene_list:
        gene_dict[gene] = 0


headers = 'Sample.id,'
for gene in master_gene_list:
	headers += gene +','


#SIMPLIFY DATA




###########################
#PRINT DATA IN WIDE FORMAT#
##########################

#print headers

for sample in sample_list:
	
	gene_list = ''
	
	#Mark what genes the sample has mutaitons for
	for gene in matrix_dict[sample]:
		gene_dict[gene] = 1		

	#Print put the genes that are marked
	for gene in master_gene_list:
		gene_str = ''
		gene_str += str(gene_dict[gene]) +','
	print gene_str
	#Refresh gene dict
	for gene in master_gene_list:
		gene_dict[gene] = 0;

##gene_dict = {}
#
#for gene in master_gene_list#:
#	gene_dict[gene] = 0

'''
###########################
#PRINT DATA IN LONG FORMAT#
###########################
cnt = 0
for sample in sample_list:
	for gene in matrix_dict[sample]:
		if gene_dict[gene] == 0:
			print sample +','+ gene
			cnt = cnt + 1
			gene_dict[gene] = 1

	#Reset gene tarcker list
	for gene in master_gene_list:
		gene_dict[gene] = 0
	
print 'Total Sample: ' + str(cnt)
'''
'''
u_smpl_yr = Set([]) 
with open('TCGA_MET500_LONG_REDUNDANT.csv') as csvfile:

        reader = csv.DictReader(csvfile)

	for row in reader:
		u_smpl_yr.add(row['sample.id'] +'_'+ row['gene'])
		#print row['sample.id'] +'_'+ row['gene']

	for sample in u_smpl_yr:
		sample_gene = sample.split('_')
		print sample_gene[0] +','+ sample_gene[1]
'''
