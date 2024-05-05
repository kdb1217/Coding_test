import Foundation
// 기존의 변이 가장 큰 변일 경우
// 새로 추가될 변이 가장 큰 변일 경우

func solution(_ sides:[Int]) -> Int {
    var cnt = 0
    var arr = sides.sorted()
    cnt += arr[1] - (arr[1] - arr[0])
    cnt += arr.reduce(0, +) - arr[1] - 1
    return cnt
}