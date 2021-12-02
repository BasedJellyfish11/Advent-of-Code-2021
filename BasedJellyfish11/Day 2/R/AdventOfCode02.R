# Part one

df_input <- read.csv('../input', header = FALSE, sep = " ", col.names = c("direction", "number"))

df_input$x_movement <- with(df_input, ifelse(direction == 'forward', number, 0)) # we move in the x plane if it's forward
df_input$y_movement <- with(df_input, ifelse(direction == 'forward', 0, ifelse(direction == 'down', number, -number))) # we move in the y plane if it's down or up. if it's down, we move the numberM; if it's up, we move -number

result <- sum(df_input$x_movement) * sum(df_input$y_movement)
print(result)

# Part two

df_input$aim <- with(df_input, cumsum(y_movement)) # The aim is now stated to be a var that starts at 0 and is moved by what we thought was Y. this means it's the cumulative sum
df_input$y_movement <- with(df_input, ifelse(direction == "forward", aim*number, 0)) # The y is then stated to be moved by "forwards" and it's number*aim

result2 <- sum(df_input$x_movement) * sum(df_input$y_movement)
print(result2)