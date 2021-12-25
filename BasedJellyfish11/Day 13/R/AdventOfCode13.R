fold_horizontal <- function(input_matrix, along){
  base <- input_matrix[1:along,]
  fold <- input_matrix[nrow(input_matrix):(along + 2),]
  if (length(base) > length(fold)) {
    fold <- rbind(matrix(TRUE, nrow = nrow(base) - nrow(fold), ncol = ncol(base)),fold)
  }
  else {
    base <- rbind(matrix(TRUE, nrow = nrow(fold) - nrow(base), ncol = ncol(fold)),base)
  }
  
  return(fold & base)
}

fold_vertical <- function(input_matrix, along){
  base <- input_matrix[,1:along]
  fold <- input_matrix[,ncol(input_matrix):(along + 2)]
  if (length(base) > length(fold)) {
    fold <- cbind(matrix(TRUE, nrow = nrow(fold), ncol = ncol(base) - ncol(fold)),fold)
  }
  else {
    base <- cbind(matrix(TRUE, nrow = nrow(fold), ncol = ncol(fold) - ncol(base)),base)
  }
  
  return(fold & base)
}

input <- read.csv(text = paste0(head(readLines("../input"),-12), collapse = "\n"), header = F)
input <- input + 1
grid <- matrix(data = TRUE, nrow = max(input$V2), ncol = max(input$V1))


for (i in 1:nrow(input)) {
  grid[input[i, 2], input[i, 1]] <- FALSE # Remember that y is actually the row, because it's how deep it is
}

# I am inputting my folds manually because parsing them is hell in R (unless you use a lib ofc) and I cannot be bothered
# As explained by Suf, remember that folding by x is actually folding vertically, and that y is folding horizontally

yeah <- fold_vertical(grid,655)
format(length(yeah) - sum(yeah))
yeah <- fold_horizontal(yeah, 447)
yeah <- fold_vertical(yeah,327)
yeah <- fold_horizontal(yeah, 223)
yeah <- fold_vertical(yeah,163)
yeah <- fold_horizontal(yeah, 111)
yeah <- fold_vertical(yeah,81)
yeah <- fold_horizontal(yeah, 55)
yeah <- fold_vertical(yeah,40)
yeah <- fold_horizontal(yeah, 27)
yeah <- fold_horizontal(yeah, 13)
yeah <- fold_horizontal(yeah, 6)
yeah[yeah == FALSE] <- '#'
yeah[yeah == TRUE] <- '.'
View(yeah)
