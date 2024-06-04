import Foundation

func solution(_ citations:[Int]) -> Int {
    var answer: [Int] = []
    for i in 1...10000 {
        let origin: Int = citations.filter { $0 >= i }.count
        
        if origin >= i {
            answer.append(i)
        }
    }
    return answer.max() ?? 0
}