library(magrittr)

# Part_1 ------------------------------------------------------------------

processInput <- function(x) {
  x <- list(x)
  names(x) <- x[[1]][1]
  x[[1]] <- x[[1]][-1]
  x
}

Bags <- "./Data/day_7.txt" %>% 
  readLines %>% 
  gsub(" bags contain ", ";", .) %>% 
  strsplit(";") %>% 
  sapply(processInput)

getOutermostBag <- function(bag_list, innermost) {
  ans <- c()
  queue <- c(innermost)
  bag_color <- names(bag_list)
  
  while( length(queue) != 0) {
    current <- queue[1]
    queue <- queue[-1]
    for ( i in bag_color ) {
      if ( i %in% ans ) next
      if ( grepl(current, bag_list[[i]]) ) {
        queue <- c(queue, i)
        if ( !(i %in% ans) ) ans <- c(ans, i)
      }
    }
  }
  ans
}

p1 <- getOutermostBag(Bags, "shiny gold")
cat("Part 1:", length(p1))

# Part_2 ------------------------------------------------------------------


extract_numbers <- function(x) {
  y <- as.numeric(unlist(sapply(x, strsplit, "\\D+")))
  y[is.na(y)] <- 0
  y
}

get_n_lower <- function(color, d) {
  pattern <- paste(color, ".*contain ")
  rule <- d[unlist(sapply(pattern, grep, d))]
  gsub(".*contain ", "", rule)
}

totalNumOfBags <- function(rules_path, Outermost) {
  bag <- Outermost
  old <- i <- 1
  d <- readLines(rules_path)
  result <- c()
  
  while (!identical(unique(bag), "no other")) {
    n_lower_bags <- get_n_lower(bag, d)
    n <- lapply(n_lower_bags, extract_numbers)
    
    vec <- Map("*", old, n)
    result[i] <- sum(unlist(vec))
    
    old <- unlist(vec)
    old <- old[old != 0]
    
    bag <- gsub(" ?\\d ?|\\.| bags?", "", n_lower_bags)
    bag <- unlist(strsplit(bag, ","))
    i <- i + 1
  }
  sum(result)
}

p2 <- totalNumOfBags("./Data/day_7.txt", "shiny gold")
cat("Part 2:", p2)