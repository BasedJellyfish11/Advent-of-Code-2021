check_low_points <- function(x){
  copy <- x
  for (i in 1:length(x)) {
    if(i == 1){
      x[i] <- copy[i]<copy[i+1]
      next
    }
    if(i==length(x)){
      x[i] <- copy[i] < copy[i-1]
    }
    else
      x[i] <- copy[i] < copy[i-1] && copy[i] < copy[i+1]
    
  }
  
  
  return(x)
}

input <- read.fwf('../input', c(rep(1, 100)))

lowpoints_horizontal <- t(apply(input, 1, check_low_points))
lowpoints_vertical <- apply(t(input), 1, check_low_points)

sum(input[lowpoints_horizontal & lowpoints_vertical] + 1)

basins <- input != 9
 