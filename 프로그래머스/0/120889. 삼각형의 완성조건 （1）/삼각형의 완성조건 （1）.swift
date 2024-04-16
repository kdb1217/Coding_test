import Foundation

func solution(_ sides:[Int]) -> Int {
    var answerArr = sides.sorted()
    return answerArr.max()! < answerArr[0] + answerArr[1] ? 1 : 2
}