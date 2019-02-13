#################################
#
# @Author: Anthony Sciarini
# @Version: 02/13/2019
#
#################################

#Libs
import csv
from sets import Set
import copy

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

'''
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
					#Update matrix dictionary.
			 		matrix_dict[atr[0]].add(atr[1])
					#Update gene list.
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

'''

'''
###########################
#PRINT DATA IN WIDE FORMAT#
###########################

print headers

sum = 0
for sample in sample_list:
	
	#Mark what genes the sample has mutaitons for
	for gene in matrix_dict[sample]:
		gene_dict[gene] = 1		

	#--- Print data ---# 
	print sample
	print gene_dict

	#Print put the genes that are marked
	gene_str = ''
	for gene in master_gene_list:
		gene_str += str(gene_dict[gene]) +','
		sum = sum + gene_dict[gene]
	print sample +','+ gene_str

	#Refresh gene dict
	for gene in master_gene_list:
		gene_dict[gene] = 0;
#print 
#print
#print 'Total number of unique mutations: ' + str(sum)
'''


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

#################################################
#GET AND PRINT WIDE DATA BY RESCANNING LONG DATA#
#################################################
sample_list = Set([])
gene_list = Set([])
u_smpl_yr = Set([]) 
sample_gene_hash = {}

###################################################################################
#SCAN THROUGH FILE ONCE TO MAKE GENE LIST, SAMPLE LIST, AND SAMPLE GENE HASH TABLE#
###################################################################################
with open('TCGA_MET500_LONG.csv') as csvfile:

        reader = csv.DictReader(csvfile)

	#Make sample list and gene list
	for row in reader:
		sample_list.add(row['sample.id'])
		gene_list.add(row['gene'])
	
	for sample in sample_list:
		tmp_gene_hash = {}
		
		#make tmp gene hash
		for gene in gene_list:
			tmp_gene_hash[gene] = 0
			
		#Put sample into list
		sample_gene_hash[sample] = copy.deepcopy(tmp_gene_hash)

##################################################################
#SCAN THROUGH FILE A SECOND TIME TO BUILD SAMPLE GENE HASH TABLE #
##################################################################	
with open('TCGA_MET500_LONG.csv') as csvfile:
	
	reader = csv.DictReader(csvfile)

	for row in reader:
		smpl = row['sample.id']
		g = row['gene']

		sample_gene_hash[smpl][g] = 1

###############################
#PRINT OUT DATA IN WIDE FORMAT#
###############################

##############
#BUILD HEADER#
##############
header = 'sample.id,'
for gene in gene_list:
	header += gene +','
print header

################
#BUILD EACH ROW#
################
summation = 0
for sample in sample_list:
	ln = ''
	ln = sample +','

	for gene in gene_list:
		ln += str(sample_gene_hash[sample][gene]) +','
		summation += sample_gene_hash[sample][gene]

	print ln
#print 
#print 
#print 'summation : ' + str(summation) 		


	###########################################################	Keep for reference, used to make long data
	#for row in reader:
	#	u_smpl_yr.add(row['sample.id'] +'_'+ row['gene'])
	#	#print row['sample.id'] +'_'+ row['gene']

	#for sample in u_smpl_yr:
	#	sample_gene = sample.split('_')
	#	print sample_gene[0] +','+ sample_gene[1]
	#	sample_list.add(sample_gene[0])
	############################################################		

