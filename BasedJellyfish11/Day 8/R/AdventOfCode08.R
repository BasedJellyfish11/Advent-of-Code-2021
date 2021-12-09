alphabetically_order_string_vector <-function(x){
  sapply(x, alphabetically_order_string)
}

alphabetically_order_string <- function(x){
  paste(sort(unlist(strsplit(x, ""))), collapse = "")
}

decode <- function(x){
  one <- min(x[nchar(x) == 2])
  four <- min(x[nchar(x) == 4])
  seven <- min(x[nchar(x) == 3])
  eight <- min(x[nchar(x) == 7])
  
  
  # This tests the amount of shared characters  
  six <- min(x[nchar(x) == 6 & 
              sapply(x, function(y){sum(!is.na(pmatch(unlist(strsplit(y, '')), unlist(strsplit(one, '')))))}) == 1])
  
  nine <- min(x[nchar(x) == 6 & 
                 sapply(x, function(y){sum(!is.na(pmatch(unlist(strsplit(y, '')), unlist(strsplit(four, '')))))}) == 4])
  
  three <- min(x[nchar(x) == 5 & 
                  sapply(x, function(y){sum(!is.na(pmatch(unlist(strsplit(y, '')), unlist(strsplit(one, '')))))}) == 2])
  
  two <- min(x[nchar(x) == 5 & 
                  sapply(x, function(y){sum(!is.na(pmatch(unlist(strsplit(y, '')), unlist(strsplit(four, '')))))}) == 2])
  
  five <- min(x[nchar(x) == 5 & 
                  sapply(x, function(y){sum(!is.na(pmatch(unlist(strsplit(y, '')), unlist(strsplit(six, '')))))}) == 5])
  
  
  x[x == one] <- 1
  x[x == two] <- 2
  x[x == three] <- 3
  x[x == four] <- 4
  x[x == five] <- 5
  x[x == six] <- 6
  x[x == seven] <- 7
  x[x == eight] <- 8
  x[x == nine] <- 9
  x[nchar(x) != 1] <- 0
  return(x)

}

input <- read.csv('../input', header = F, sep = " ")

input[] <- sapply(input, alphabetically_order_string_vector)
decodedinput <- t(apply(input,1, decode))

displayed <- decodedinput[,(ncol(decodedinput)-3):ncol(decodedinput)]
solution <- apply(displayed,1, function(x){strtoi(paste0(x, collapse=""), base = 10)})

print(length(displayed[displayed %in% c(1,4,7,8)])) # Part one
print(sum(solution)) # Part two
