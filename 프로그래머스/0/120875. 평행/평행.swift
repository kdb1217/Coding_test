import Foundation

/*
풀이 계획
1. 모든 경우의수를 생각해야 한다. [1,3] [2,4], [1,2],[3,4], [1,4],[2,3] 
2. 경우의 수 총 3개
*/

func solution(_ dots:[[Int]]) -> Int {
    
    if Double(dots[0][1] - dots[1][1])/Double(dots[0][0]-dots[1][0])
    == Double(dots[2][1] - dots[3][1])/Double(dots[2][0]-dots[3][0]) {
        return 1
    }
    if Double(dots[0][1] - dots[2][1])/Double(dots[0][0]-dots[2][0])
    == Double(dots[1][1] - dots[3][1])/Double(dots[1][0]-dots[3][0]) {
        return 1
    }
    if Double(dots[0][1] - dots[3][1])/Double(dots[0][0]-dots[3][0])
    == Double(dots[2][1] - dots[1][1])/Double(dots[2][0]-dots[1][0]) {
        return 1
    }
    return 0
}