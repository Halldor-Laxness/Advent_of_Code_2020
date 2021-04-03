
Map <- read.table("./Data/day_3.txt", comment.char = "", stringsAsFactors = FALSE)
Map <- sapply(1:nrow(Map), function(i) strsplit(Map[i, ], ""))
Map <- t(as.data.frame(Map))
rownames(Map) <- 1:nrow(Map)
colnames(Map) <- 1:ncol(Map)

Num_Trees <- function(Mat, Right = 1, Down = 1, Tree = "#") {
  i <- 1
  j <- 1
  num <- 0
  while (i <= nrow(Mat)) {
    if (Mat[i, j] == Tree) {
      num = num + 1
      # print(c(Mat[i, j], i, j))
    }
    i <- i + Down
    j <- j + Right
    if (j > ncol(Mat)) {
      j <- j %% ncol(Mat)
      if (j == 0) j <- ncol(Mat)
    }
  }
  num
}

Cumprod_Trees <- function(Mat, Slopes, Tree = "#") {
  cp <- 1
  for (i in 1:nrow(Slopes)) {
    num <- Num_Trees(Mat, Slopes[i, 1], Slopes[i, 2], Tree)
    print(num)
    cp <- cp * num
  }
  cp
}

Move_Slope <- matrix(c(1, 3, 5, 7, 1,
                       1, 1, 1, 1, 2),
                     ncol = 2)
Cumprod_Trees(Map, Move_Slope)




