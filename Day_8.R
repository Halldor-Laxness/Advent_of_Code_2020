
processInput <- function(filepath) {
  df <- read.table(filepath, col.names = c("op", "arg"))
  df$jmp_val <- ifelse(df$op != "jmp", 1, df$arg)
  df$target <- (1 : nrow(df)) + df$jmp_val
  df
}

row_path <- function(x) {
  nxt <- hits <- i <- 1
  while (!any(duplicated(hits))) {
    nxt <- hits[i + 1] <- x[nxt, "target"]
    i <- i + 1
  }
  unique(hits)
}

sum_acc <- function(df, x) {
  df <- df[x, ]
  sum(df[df$op == "acc", "arg"], na.rm = TRUE)
}

playInfLoopGame <- function(filepath) {
  df <- processInput(filepath)
  sum_acc(df, row_path(df))
}

PlayOnePassGame <- function(filepath) {
  df <- processInput(filepath)
  
  nxt <- nrow(df)
  goal <- list()
  i <- 1
  
  while (length(nxt) > 0) {
    which(df$target %in% nxt) -> nxt -> goal[[i]]
    i + 1 -> i
  }
  
  goal <- unlist(goal)
  p <- row_path(df)
  candidate <- goal[(goal - 1) %in% p] - 1
  
  df[candidate, "jmp_val"] <- 1
  df$target <- 1:nrow(df) + df$jmp_val
  
  sum_acc(df, row_path(df))
}

cat("Part 1:", playInfLoopGame("./Data/day_8.txt"))
cat("Part 2:", PlayOnePassGame("./Data/day_8.txt"))