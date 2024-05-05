import Foundation

// 1. 첫번째 배열의 [0]과 다른 [0]값을 찾는다 -> x1,x2 구하기
// 2. 배열의 두번쨰 [1]과 다른 값을 찾는다 -> y1, y2 구하기
func solution(_ dots:[[Int]]) -> Int {
    var x2: Int = 0
    var y2: Int = 0
    for i in dots {
        if i[0] != dots[0][0] {
            x2 = i[0]
        }
        if i[1] != dots[0][1] {
            y2 = i[1]
        }
    }
    return abs(dots[0][0] - x2) * abs(dots[0][1] - y2)
}