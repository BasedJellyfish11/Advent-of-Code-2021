input <- read.fwf('../input', rep(1, 10))
input_padded <- rbind(NA, cbind(NA, input, NA), NA)

step <- function(input_padded) {
  input_padded <- input_padded + 1
  while (sum(!is.na(input_padded[input_padded >= 10])) > 0) {
    flashers <- input_padded >= 10
    input_padded[flashers] <- 0
    indices <- which(flashers, arr.ind = T)
    for (row in 1:nrow(indices)) {
      # N
      input_padded[indices[row, "row"] - 1, indices[row, "col"]] <-
        ifelse(input_padded[indices[row, "row"] - 1, indices[row, "col"]] == 0, 0, input_padded[indices[row, "row"] - 1, indices[row, "col"]] + 1)
      # NE
      input_padded[indices[row, "row"] - 1, indices[row, "col"] + 1] <-
        ifelse(input_padded[indices[row, "row"] - 1, indices[row, "col"] + 1] == 0, 0, input_padded[indices[row, "row"] - 1, indices[row, "col"] + 1] + 1)
      # E
      input_padded[indices[row, "row"], indices[row, "col"] + 1] <-
        ifelse(input_padded[indices[row, "row"], indices[row, "col"] + 1] == 0, 0, input_padded[indices[row, "row"], indices[row, "col"] + 1] + 1)
      # SE
      input_padded[indices[row, "row"] + 1 , indices[row, "col"] + 1] <-
        ifelse(input_padded[indices[row, "row"] + 1, indices[row, "col"] + 1] == 0, 0, input_padded[indices[row, "row"] + 1, indices[row, "col"] + 1] + 1)
      # S
      input_padded[indices[row, "row"] + 1, indices[row, "col"]] <-
        ifelse(input_padded[indices[row, "row"] + 1, indices[row, "col"]] == 0, 0, input_padded[indices[row, "row"] + 1, indices[row, "col"]] + 1)
      # SW
      input_padded[indices[row, "row"] + 1, indices[row, "col"] - 1] <-
        ifelse(input_padded[indices[row, "row"] + 1, indices[row, "col"] - 1] == 0, 0, input_padded[indices[row, "row"] + 1, indices[row, "col"] - 1] + 1)
      # W
      input_padded[indices[row, "row"], indices[row, "col"] - 1] <-
        ifelse(input_padded[indices[row, "row"], indices[row, "col"] - 1] == 0, 0, input_padded[indices[row, "row"], indices[row, "col"] - 1] + 1)
      #NW
      input_padded[indices[row, "row"] - 1, indices[row, "col"] - 1] <-
        ifelse(input_padded[indices[row, "row"] - 1, indices[row, "col"] - 1] == 0, 0, input_padded[indices[row, "row"] - 1, indices[row, "col"] - 1] + 1)
    }
    
    
  }
  
  return(input_padded)
}

flash_count <- 0
for (i in 1:100) {
  input_padded <- step(input_padded)
  flash_count <-flash_count + sum(!is.na(input_padded[input_padded == 0]))
}

current_step <- 100

while (sum(input_padded[!is.na(input_padded)]) != 0) {
  input_padded <- step(input_padded)
  current_step <- current_step + 1
}

format(flash_count, scientific = F)
format(current_step, scientific = F)