import Foundation
/*
풀이계획
1. 숫자만 기록하고 있는 배열을 만든다
2. 글자만 기록하고 있는 배열을 만든다.
3. 반복문안에 Fo
*/
func solution(_ dartResult:String) -> Int {
    var roundScore = dartResult.split(whereSeparator: { !$0.isNumber }).compactMap { Int($0) }
    let options = dartResult.split(whereSeparator: { $0.isNumber })
    
    for i in 0..<3 {
        options[i].forEach { j in
            if j == "D" {
                roundScore[i] *= roundScore[i]
                
            } else if j == "T" {
                roundScore[i] = roundScore[i] * roundScore[i] * roundScore[i]
                
            } else if j == "*" {
                if i == 0 {
                    roundScore[i] *= 2
                } else {
                    roundScore[i] *= 2
                    roundScore[i - 1] *= 2
                }
            } else if j == "#" {
                roundScore[i] *= -1
            }
        }
    }
    print(roundScore)
    return roundScore.reduce(0, +)
}