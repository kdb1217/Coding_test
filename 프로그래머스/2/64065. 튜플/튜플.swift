import Foundation
/*
풀이계획
1. [1], [1,2]일때 개수가 1인게 첫번째 개수가 2일때 1의 차집합이 두번째 숫자 이런식으로 계속하면 순서대로 추리가 가능하다.
*/
func solution(_ s:String) -> [Int] {
    var word = s
    var answer: [Int] = []
    word.removeFirst()
    word.removeFirst()
    word.removeLast()
    word.removeLast()
    word = word.replacingOccurrences(of: "},{", with: " ")
    var arr = word.split(separator: " ").map { $0 }
    arr.sort { $0.count < $1.count }
    if arr.count == 1 {
        return [Int(arr[0])!]
    } else {
        answer.append(contentsOf: arr[0].split(separator: ",").map { Int($0)! })
        for i in 0..<arr.count - 1 {
            let tmp = Set(arr[i].split(separator: ",").map { Int($0)! })
            let tmp2 = Set(arr[i + 1].split(separator: ",").map { Int($0)! })
            let number = tmp2.subtracting(tmp).first!
            
            answer.append(number)
        }
    }
    return answer
}