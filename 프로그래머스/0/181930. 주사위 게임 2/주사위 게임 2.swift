import Foundation

func solution(_ a:Int, _ b:Int, _ c:Int) -> Int {
    var arr: Set<Int> = [a, b, c]
    if arr.count == 3 {
      return a + b + c  
    } else if arr.count == 2 {
        return (a + b + c) * (a * a + b * b + c * c)
    } else {
        return (a + b + c) * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c)
    }
}