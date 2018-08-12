#R functions to do the summation of the rows in the TCGA MET500 Long matrix

sum_rows <- function(wdf_file_name, ldf_file_name) {
	
	wide_data <- as.read.csv(wdf_file_name)
	long_data <- as.read.csv(ldf_file_name)

	for (row in 1:nrow(wdf_file_name)
}
