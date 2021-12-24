isWinner <- function(x) {
  nas <- is.na(x)
  any(rowSums(nas) == ncol(x)) ||
  any(colSums(nas) == nrow(x)) ||
  sum((diag(nas))) == nrow(x) ||
  sum(diag(nas[, nrow(x):1])) == nrow(x)
  
}

part1 <- function() {
  destroyed_input <- input
  for (number in number_sequence) {
    destroyed_input[destroyed_input == number] <- NA
    winners <- sapply(split(destroyed_input, rep(1:100, each = 5)), isWinner)
    
    if (any(winners)) {
      index <- min(which(winners == TRUE))
      bingo_win <- destroyed_input[(index * 5 - 4):(index * 5), ]
      print(sum(bingo_win, na.rm = TRUE) * number)
      break
    }
  }
}

part2 <- function() {
  destroyed_input <- input
  index = -1
  for (number in number_sequence) {
    destroyed_input[destroyed_input == number] <- NA
    winners <- sapply(split(destroyed_input, rep(1:100, each = 5)), isWinner)
    
    if (all(winners)) {
      bingo_win <- destroyed_input[(index * 5 - 4):(index * 5), ]
      print(sum(bingo_win, na.rm = TRUE) * number)
      break
    }
    else if (length(which(winners == FALSE)) == 1 && index == -1) {
      index <- min(which(winners == FALSE))
    }
  }
}


input <- read.fwf('../input',header = FALSE,skip = 2,widths = rep(3, 5)) # dude skip blank lines doesn't work for fwf wtf
input <- input[rowSums(is.na(input)) != ncol(input), ] #remove separators because bingos are a construct

number_sequence <- read.csv('../input', header = FALSE, nrows = 1)

part1()
part2()