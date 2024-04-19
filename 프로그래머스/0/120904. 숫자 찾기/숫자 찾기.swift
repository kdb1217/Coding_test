import Foundation

func solution(_ num:Int, _ k:Int) -> Int {
    if let answer = String(num).map{String($0)}.firstIndex(of: String(k)) {
        return answer + 1
    } else {
        return -1
    }
}