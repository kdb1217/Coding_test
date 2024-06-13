import Foundation

func solution(_ polynomial:String) -> String {
    var xCounter: Int = 0
    var numCounter: Int = 0
    var answer = ""
    var arr = polynomial.split(separator: " ").map{String($0)}
    for i in arr {
        if i.last! == "x" {
            if i.count == 1 {
                xCounter += 1
            } else {
                var tmp = i.map { String($0) }
                tmp.removeLast()
                let num = Int(tmp.joined())!
                xCounter += num
            }
        }
        if i.allSatisfy({ $0.isNumber }) {
            numCounter += Int(i)!
        }
    }
    if xCounter == 1 {
        answer += "x"
    } else if xCounter > 1 {
        answer += String(xCounter)+"x"
    }
    
    if numCounter > 0 && xCounter > 0 {
        answer += " + \(numCounter)"
    } else if numCounter > 0 {
        answer += "\(numCounter)"
    }
    return answer
}