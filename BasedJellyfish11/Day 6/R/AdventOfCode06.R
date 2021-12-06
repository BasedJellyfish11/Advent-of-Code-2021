bacterial_growth <- function(bacteria_matrix){
  next_iter <- bacteria_matrix[,'day0']
  bacteria_matrix[,2:length(bacteria_matrix)] <- bacteria_matrix[,1:length(bacteria_matrix) - 1]
  bacteria_matrix$day6 <- bacteria_matrix[,'day6'] + next_iter
  bacteria_matrix$day8 <- next_iter
  return(bacteria_matrix)
}


input <- read.csv('../input', header = FALSE)
rownames(input) <- c('bacteria')
lanternfish <- data.frame(day8 = as.numeric(length(input[input == 8])),
                          day7 = as.numeric(length(input[input == 7])),
                          day6 = as.numeric(length(input[input == 6])),
                          day5 = as.numeric(length(input[input == 5])),
                          day4 = as.numeric(length(input[input == 4])),
                          day3 = as.numeric(length(input[input == 3])),
                          day2 = as.numeric(length(input[input == 2])),
                          day1 = as.numeric(length(input[input == 1])),
                          day0 = as.numeric(length(input[input == 0])))


for(i  in 1:256){
  lanternfish <- bacterial_growth(lanternfish)
}

format(sum(lanternfish), scientific = FALSE)