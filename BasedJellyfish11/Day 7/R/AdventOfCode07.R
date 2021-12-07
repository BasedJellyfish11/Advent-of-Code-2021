input <- as.numeric(read.csv('../input', header = F))
print(sum(abs(input - median(input))))

# For p2 most people seem to use the avg, and that was my approach at first, but I got unlucky or whatever and my average rounded up instead of down which would be the real value I need

fuel <- Inf
for(i in 1:max(input)){
  distances <- sapply(input, function(x) abs(x-i))
  fuel_iter <- sapply(distances, function(x) max((cumsum(0:x))))
  if(sum(fuel_iter) < fuel){
    fuel <- sum(fuel_iter)
  }
}

print(fuel)