Mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

Mode_multiple <- function(x) {
  ux <- unique(x)
  tab <- tabulate(match(x, ux))
  ux[tab == max(tab)]
}

# Part one
df <- read.fwf('../input', widths = rep(1, 12))

gamma_value <- base::strtoi(base::paste0(sapply(df, Mode), collapse = ""), base = 2)
epsilon_value <- base::strtoi(base::paste0(sapply(sapply(df, Mode), function (x) ifelse( any(x == 0), 1, 0)), collapse = ""), base = 2)

print (gamma_value * epsilon_value)

#Part two 

df_o2 <- df
for (i in colnames(df_o2)){ # Loops are awful and should be avoided in this lang but idk how to avoid this one because the transformations are successive, you cannot do them all at the same time
  mode <- Mode_multiple(df_o2[,i])
  if(length(mode) == 1){
    df_o2 <- subset(df_o2,df_o2[,i]  == mode)
  }else{    
    df_o2 <- subset(df_o2,df_o2[,i]  == 1)
  }
    
}

df_co2 <- df
for (i in  colnames(df_co2)){ # Loops are awful and should be avoided in this lang but idk how to avoid this one because the transformations are successive, you cannot do them all at the same time
  mode <- Mode_multiple(df_co2[,i])
  if(length(mode) == 1){
    df_co2 <- subset(df_co2,df_co2[,i]  != mode)
    
  }else{
    df_co2 <- subset(df_co2,df_co2[,i]  == 0)
  }
  
  if(nrow(df_co2) == 1){
    break
  }
}

o2_value <- base::strtoi(base::paste0(df_o2, collapse = ""), base = 2)
co2_value <- base::strtoi(base::paste0(df_co2, collapse = ""), base = 2)
print (o2_value * co2_value)
