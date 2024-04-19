import Foundation

func solution(_ n_str:String) -> String {
    var arr = n_str.map{String($0)}
    print(arr)
    for i in n_str {
        if i == "0" {
            arr.removeFirst()
        } else {
            break
        }
    }
    return arr.joined()
}