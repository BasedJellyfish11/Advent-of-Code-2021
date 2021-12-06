segment.getAllPoints <- function(segment) {
  
  if (segment["x1"] == segment["x2"]) {
    to_return <- data.frame(
      (c(rep(segment["x1"], (abs(segment["y1"] - segment["y2"]) + 1)))),
      segment["y1"]:segment["y2"]
      )
    
    colnames(to_return) <- c("x", "y")
    return(to_return)
  
  }
  
  slope <- (segment["y2"] - segment["y1"])/(segment["x2"] - segment["x1"])
  n <- (-slope)*segment["x1"] + segment["y1"]
  
  to_return <- data.frame(
    segment["x1"]:segment["x2"],
    sapply(segment["x1"]:segment["x2"], function(x) slope * x + n)
    )
  
  colnames(to_return) <- c("x", "y")
  return(to_return)
  
}

input <- read.csv('../input_sane', header = FALSE,col.names = c('x1', 'y1', 'x2', 'y2'))
input_p1 <- input[input$x1 == input$x2 | input$y1 == input$y2,]

points <- do.call("rbind", apply(input, 1, segment.getAllPoints))
unique_overlapping_points <- unique(points[duplicated(points),])

print(nrow(unique_overlapping_points))