halveSeq <- function(low = 0, up = 127, char = "F") {
  if ( char == "F" | char == "L" ) {
    up <-  up - ( up - low + 1 ) / 2
  } else {
    low <- low + ( up - low + 1 ) / 2 
  }
  list(low = low, up = up)
} 

getSeatId <- function(x, V = 128, H = 8) {
  splt_x <- strsplit(x, "")[[1]]
  xv <- splt_x[1:7]
  xh <- splt_x[8:10]
  
  low <- 0
  up <- V - 1
  for ( char in xv ) {
    rg_row <- halveSeq(low, up, char)
    low <- rg_row$low
    up <- rg_row$up
  }
  
  Row <- low
  
  low <- 0
  up <- H - 1
  for ( char in xh ) {
    rg_col <- halveSeq(low, up, char)
    low <- rg_col$low
    up <- rg_col$up
  }
  
  Col <- low
  
  Row * 8 + Col
}

input <- readLines("./Data/day_5.txt")
All_ID <- sapply(input, getSeatId)
Range_ID <- range(All_ID)
My_ID <- setdiff(Range_ID[1]:Range_ID[2], All_ID)



