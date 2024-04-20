import Foundation

func solution(_ n:Int) -> [[Int]] {
    var arr = [[Int]](repeating: Array(repeating: 0, count: n), count: n)
    for i in 0..<n {
        for j in 0..<n {
            if i == j {
                arr[i][j] = 1
            }
        }
    }
    return arr
}