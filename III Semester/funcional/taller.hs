splitCola :: [Int] -> Int -> ([Int], [Int])
splitCola lst x = aux lst [] []
  where
    aux [] acum1 acum2 = (reverse acum1, reverse acum2)
    aux (a:r) acum1 acum2
      | a <= x = aux r (a : acum1) acum2
      | otherwise = aux r acum1 (a : acum2)

