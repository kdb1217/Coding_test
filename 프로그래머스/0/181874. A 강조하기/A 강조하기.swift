import Foundation

func solution(_ myString:String) -> String {
    
    return myString.map {String($0 == "a" || $0 == "A" ? $0.uppercased() : $0.lowercased())}.joined()
}