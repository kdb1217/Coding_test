import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var failInfo: [Int: Double] = [:]
    var stageInfo: [Int: Double] = [:]
    
    for i in stages {
        failInfo[i, default: 0] += 1 
    }
    for i in 1...N {
        let total = failInfo.filter { $0.key >= i}.map { $0.value }.reduce(0.0, +)
        if total == 0 {
            stageInfo[i] = 0
        } else {
            stageInfo[i] = (Double(failInfo[i] ?? 0) / total)
        }
        
    }

    let tmp = stageInfo.keys.sorted { stageInfo[$0]! == stageInfo[$1]! ? $0 < $1 : stageInfo[$0]! > stageInfo[$1]! }
    return tmp
}