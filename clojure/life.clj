(ns life)



(defn cell-neighbours [x y]
  (let [deltas [-1 0 1]]
    (filter #(not= %1 [x y])
      (for [dx deltas dy deltas] [(+ x dx) (+ y dy)]))))

(count (cell-neighbours 2 0))



(filter #(not= %1 [3 4]) '([1 2] [3 4]))
