import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    myString.filter{ Array(myString.map{[$0..<pat.count]}).joined() == pat}.count
}