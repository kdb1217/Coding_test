import Foundation

func solution(_ myString:String, _ pat:String) -> String {
    var arr: [String] = []
    for i in 0...myString.count {
        let tmp = String(myString.prefix(i))
        if String(tmp.suffix(pat.count)) == pat {
            arr.append(tmp)
        }
    }
    return arr.max()!
}