import Foundation

func solution(_ num_list:[Int]) -> Int {
    let tmp = num_list.filter {$0 < 0}
    
    return num_list.firstIndex(of: tmp.first ?? -1) ?? -1
}