import Foundation

func solution(_ num_list:[Int]) -> Int {
    let odd = num_list.filter{ $0 % 2 == 1}.map{String($0)}.joined()
    let even = num_list.filter{ $0 % 2 == 0}.map{String($0)}.joined()
    return Int(odd)! + Int(even)!
}