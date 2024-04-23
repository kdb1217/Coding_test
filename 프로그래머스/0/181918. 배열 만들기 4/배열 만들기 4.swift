import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var cnt: Int = 0
    var answer: [Int] = []
    while cnt < arr.count {
        if answer.isEmpty {
            answer.append(arr[cnt])
            cnt += 1
        } else {
            if answer.last! < arr[cnt] {
                answer.append(arr[cnt])
                cnt += 1
            }
            else {
                answer.removeLast()
            }
        }
    }
    return answer
}