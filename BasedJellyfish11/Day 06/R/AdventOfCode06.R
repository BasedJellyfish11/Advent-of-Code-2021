bacterial_growth <- function(bacteria_matrix){
  
  next_iter <- bacteria_matrix[,ncol(bacteria_matrix)]
  bacteria_matrix[,2:ncol(bacteria_matrix)] <- bacteria_matrix[,1:ncol(bacteria_matrix) - 1]
  bacteria_matrix$day6 <- bacteria_matrix[,'day6'] + next_iter
  bacteria_matrix[,1] <- next_iter
  
  return(bacteria_matrix)
}

DAYS_TO_DUP <- 8

input <- read.csv('../input', header = FALSE)
lanternfish <- data.frame(t(sapply(DAYS_TO_DUP:0, function(x) as.numeric(length(input[input == x])))))
colnames(lanternfish) <- sapply((ncol(lanternfish) - 1):0, function(x) paste0('day', x, collapse = ''))

for (i in 1:256) {
  lanternfish <- bacterial_growth(lanternfish)
}

format(sum(lanternfish), scientific = FALSE)