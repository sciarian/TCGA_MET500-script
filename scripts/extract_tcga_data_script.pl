#!/usr/local/bin/perl

use strict;
use warnings;

my $directory = 'stddata__2016_07_15';

opendir (DIR, $directory) or die $!;


#############################
#OPEN CELL LINE MUTATION DIR#
#############################
while (my $file = readdir(DIR)) {
	

	print "\n\n";
	print "$file\n";
	
	my $sub_dir = "stddata__2016_07_15/$file";
	
	print "$sub_dir\n";

	##########################
	#OPEN DIR FOR EACH CANCER#
	##########################
	opendir (SUB_DIR, $sub_dir);

		#####################################
		#LOOP THROGH EACH FILE IN CANCER DIR#
		#####################################
		while (my $sub_file = readdir(SUB_DIR)){
					
			print "\t\t$sub_file\n";
			
			my $dir_name = "$sub_file";			

			############################
			#OPEN THE DIR WITH THE DATA#
			############################
			if ($dir_name == "20160715"){
				
				my $sub_sub_dir = "stddata__2016_07_15/$file/20160715"; 

				opendir(THE_DIR, $sub_sub_dir);
				
				########################################
				#LOOP THROUGH EACH FILE IN THE DATA DIR#
				########################################
				while(my $sub_sub_file = readdir(THE_DIR)){
					print "$sub_sub_file\n";
					
					###########################################################
					#IF THIS CANCER HAS DATA EXTRACT IT TO THE ALL_MAF_TXT DIR#
					###########################################################
					if(index($sub_sub_file,"gdac") != -1){
						my $cmd = "tar -xvf $sub_sub_dir/$sub_sub_file -C all_maf_txt";
						print "Attempting to carryout command: $cmd";
						system($cmd);
						print "\n\nDATA EXTRACTED\n\n";
						last;
					}
						
			}
			
				closedir(THE_DIR)
			}
		}
	closedir(SUB_DIR);
}
closedir(DIR);
