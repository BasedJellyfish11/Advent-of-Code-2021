check_low_points <- function(x){
  last_number <- Inf
  last_added <- 1
  overwrite <- T
  
  for (i in 1:length(x)) {
    
    if (x[i] >= last_number) {
      last_number <- x[i]
      overwrite <- F
      x[i] <- F
    }
    
    else{
      last_number <- x[i]
      
      if (overwrite) {
        x[last_added] <- F
      }
      else{
        overwrite <- T
      }
      
      x[i] <- T
      last_added <- i
    }
    
  }
  
  
  return(x)
}

input <- read.fwf('../example', c(rep(1, 10)))

lowpoints_horizontal <- t(apply(input, 1, check_low_points))
lowpoints_vertical <- apply(t(input), 1, check_low_points)

sum(input[lowpoints_horizontal & lowpoints_vertical] + 1)

basins <- input != 9
 