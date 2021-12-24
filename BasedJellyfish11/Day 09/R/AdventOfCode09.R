check_low_points <- function(x) {
  copy <- x
  for (i in 1:length(x)) {
    if (i == 1) {
      x[i] <- copy[i] < copy[i + 1]
      next
    }
    if (i == length(x)) {
      x[i] <- copy[i] < copy[i - 1]
    }
    else
      x[i] <- copy[i] < copy[i - 1] && copy[i] < copy[i + 1]
    
  }
  
  
  return(x)
}

floodfill <- function(row, col, tcol, rcol) {
  if (tcol == rcol)
    return()
  if (M[row, col] != tcol)
    return()
  M[row, col] <<- rcol
  if (row != 1)
    floodfill(row - 1, col    , tcol, rcol) # south
  if (row != nrow(M))
    floodfill(row + 1, col    , tcol, rcol) # north
  if (col != 1)
    floodfill(row    , col - 1, tcol, rcol) # west
  if (col != ncol(M))
    floodfill(row    , col + 1, tcol, rcol) # east
  return("filling completed")
}

input <- read.fwf('../input', c(rep(1, 100)))

lowpoints_horizontal <- t(apply(input, 1, check_low_points))
lowpoints_vertical <- apply(t(input), 1, check_low_points)

sum(input[lowpoints_horizontal & lowpoints_vertical] + 1)

M <- input != 9
basin_number <- 2
basin_sizes <- vector(mode = "numeric")
for (i in 1:ncol(M)) {
  for (j in 1:nrow(M)) {
    floodfill(j, i, TRUE, basin_number)
    basin_sizes <- c(basin_sizes, length(M[M == basin_number]))
    basin_number <- basin_number + 1
  }
}

prod(head(sort(basin_sizes, decreasing = TRUE), 3))