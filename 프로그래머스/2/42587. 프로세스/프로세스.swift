import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var arr: [(Int,Int)] = [] 
    for i in 0..<priorities.count {
        arr.append((i,priorities[i]))
    }
    var answer: [(Int,Int)] = []
    while priorities.sorted(by: { $0 > $1}) != answer.map ({ $0.1 }) {
        let first = arr[0]
        if first.1 == arr.map({ $0.1 }).max()! {
            arr.removeFirst()
            answer.append(first)
        } else {
            arr.removeFirst()
            arr.append(first)
        }
    }
    return answer.map { $0.0}.firstIndex(of: location)! + 1
}