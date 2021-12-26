input <- read.fwf('./input', rep(1,100))

increase <- function(m, inc){
  m <- m + inc
  m <- m %% 10
  m[m < inc] <- m[m < inc] + 1
  return(m)
}

input2 <- do.call(rbind, lapply(0:4, function(x) increase(input,x)))
input2 <- do.call(cbind, lapply(0:4, function(x) increase(input2,x)))

write.table(input2, file = './input2', row.names = F, col.names = F, sep = "")