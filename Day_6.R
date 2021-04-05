library(magrittr)
numAllyes <- function(x) {
  l <- length(x)
  if ( l == 1 ) {
    num <- nchar(x)
  } else {
    ans <- strsplit(x, "")
    current <- letters
    for (i in 1:l) {
      all_yes <- intersect(current, ans[[i]])
      current <- all_yes
    }
    num <- length(all_yes)
  }
  num
}

input <- "./Data/Day_6.txt" %>% 
  readLines %>% 
  paste(collapse = ";") %>% 
  strsplit(";;") %>% 
  .[[1]]

p1 <- input %>% 
  gsub(";", "", .) %>% 
  strsplit("") %>% 
  sapply(function(x) length(unique(x))) %>% 
  sum

p2 <- input %>% 
  gsub(";", " ", .) %>% 
  strsplit(" ") %>% 
  sapply(numAllyes) %>% 
  sum

cat("Part 1:", p1)
cat("Part 2:", p2)