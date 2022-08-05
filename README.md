# Fastq_stats_plot
Read fastq file, calculate qc statistics and generate plot.

1. fastq_scores_stats.py - Python script to calculate average and std dev.
Example usage -
python fastq_scores_stats.py -f H4sample.fastq

2. H4sample.fastq - Input file to python script.
3. fastq_stats.txt - Output file from the python script.
4. fastqc_plot.R - R script to create plot using the output from python script.
Example usage -
Rscript fastqc_plot.R

5. fastqc_plot.pdf - Plot from R script.
