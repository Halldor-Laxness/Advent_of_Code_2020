extractInfo <- function(filepath) {
  con <- file(filepath, "r")
  all_info <- c()
  info <- c()
  while (TRUE) {
    line <- readLines(con, n = 1)
    if ( length(line) != 0 ) {
      if ( line != "" ) {
        info <- paste(info, line, sep = " ")
      } else {
        all_info <- rbind(all_info, info)
        info <- c()
      }
    } else {
      all_info <- rbind(all_info, info)
      break
    }
  }
  close(con)
  all_info
}

validPassport <- function(filepath, fields) {
  num <- 0
  pp_info <- extractInfo(filepath)
  for(i in 1:nrow(pp_info)) {
    valid <- c()
    for ( field in fields ) {
      exist <- grepl(field, pp_info[i, ])
      valid <- c(valid, exist)
    }
    if ( all(valid) == TRUE ) num <- num + 1
  }
  num
}

data_path <- "./Data/day_4.txt"

fields_p1 <- c("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

fields_p2 <- c(
  "byr:19[2-9]\\d|200[0-2]",
  "iyr:20(1\\d|20)",
  "eyr:20(2\\d|30)",
  "hcl:#[0-9a-f]{6}",
  "ecl:(amb|blu|brn|gry|grn|hzl|oth)",
  "pid:\\d{9}( |$)",
  "hgt:(((1[5-8]\\d|19[0-3])cm)|((59|6\\d|7[0-6])in))"
)

cat("Part_1: # of valid passports:", validPassport(data_path, fields_p1))
cat("Part_2: # of valid passports:", validPassport(data_path, fields_p2))