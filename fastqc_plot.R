#Script to create plot for fastq quality check.


library("ggplot2")
stats_file <- read.table("fastq_stats.txt", header=T)

pdf("fastqc_plot.pdf")
max_sd = stats_file$Avg + stats_file$Stdev
ymax_n = ifelse(max_sd <= 41, max_sd, 41)

ggplot(stats_file, aes(Cycle, Avg)) +
  geom_errorbar(aes(ymax = ymax_n , ymin = Avg - Stdev),
                position = "dodge") + geom_point(colour = "black", size = 0.5) + ylim(0,41) + xlim(1,151)


dev.off()
