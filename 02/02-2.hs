import Data.List

main = do
  file <- readFile "input.txt"
  let allLines = lines file
  let answerLength = length (head allLines) - 1
  let answers = map (map fst) (filter (matchLength answerLength) (map (filter isMatch) (map zipPair (pairs allLines))))
  print(answers)
  where
  pairs l = [(x, y) | (x:ys) <- tails l, y <- ys]
  zipPair x = zip (fst x) (snd x)
  isMatch p = fst p == snd p
  matchLength x l = length l == x
