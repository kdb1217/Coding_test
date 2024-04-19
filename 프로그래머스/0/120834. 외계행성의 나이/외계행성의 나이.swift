import Foundation

func solution(_ age:Int) -> String {
    var tmp = String(age).map {String($0)}
    for i in tmp.indices {
        if tmp[i] == "0" {
            tmp[i] = "a"
        } else if tmp[i] == "1" {
            tmp[i] = "b"
        } else if tmp[i] == "2" {
            tmp[i] = "c"
        } else if tmp[i] == "3" {
            tmp[i] = "d"
        } else if tmp[i] == "4" {
            tmp[i] = "e"
        } else if tmp[i] == "5" {
            tmp[i] = "f"
        } else if tmp[i] == "6" {
            tmp[i] = "g"
        } else if tmp[i] == "7" {
            tmp[i] = "h"
        } else if tmp[i] == "8" {
            tmp[i] = "i"
        } else if tmp[i] == "9" {
            tmp[i] = "j"
        }
    }
    return tmp.joined()
}