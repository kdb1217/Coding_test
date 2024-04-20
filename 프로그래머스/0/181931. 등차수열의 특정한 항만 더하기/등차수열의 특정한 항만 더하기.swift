import Foundation

func solution(_ a:Int, _ d:Int, _ included:[Bool]) -> Int {
    var arr: [Int] = []
    for i in stride(from: a, to: a+(d*included.count), by: d) {
        arr.append(i)   
    }
    
    return arr.indices.filter { included[$0] == true}.reduce(0) {$0 + arr[$1]}
}