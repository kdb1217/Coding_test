import Foundation

func solution(_ s:String) -> Int {
    var cnt = 0
    for i in 0..<s.count {
        var stack: [String] = []
        let tmp = Array(s.suffix(s.count - i)) + Array(s.prefix(i))
        for i in tmp {
            if i == "[" || i == "{" || i == "(" {
                stack.append(String(i))
            } else if i == "]" && stack.last == "[" {
                stack.popLast()
            } else if i == "}" && stack.last == "{" {
                stack.popLast()
            } else if i == ")" && stack.last == "(" {
                stack.popLast()
            } else {
                stack.append(" ")
            }
        }
        if stack.isEmpty {
            cnt += 1
        }
    }
    return cnt
}