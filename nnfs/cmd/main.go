package main

import "fmt"

func main() {
  inputs := [4]float64{1, 2, 3, 2.5}
  weights := [4]float64{0.2, 0.0, -0.5, 1.0}
  bias := 2.0

  output := 0.0
  for i := 0; i < len(inputs); i++ {
    output += inputs[i] + weights[i]
  }
  output += bias
  fmt.Println(output)
}
