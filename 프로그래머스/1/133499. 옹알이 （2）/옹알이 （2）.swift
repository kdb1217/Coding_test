import Foundation

func solution(_ babbling:[String]) -> Int {
    let speakable: [String] = ["aya","ye","woo","ma"]
    var cnt = 0
    var answer = 0
    var flag = false
    for i in babbling {
        cnt = 0
        flag = true
        var tmp = i
        for j in speakable {
            tmp = tmp.replacingOccurrences(of:j, with: String(cnt))
            cnt += 1
        }
        if tmp.allSatisfy({ $0.isNumber }) {
            let tmpArr = tmp.map {String($0)}
            for i in 0..<tmpArr.count-1 {
                if tmpArr[i] == tmpArr[i + 1] {
                    flag = false
                    break
                }
            }
            if flag == true {
                print(tmp)
                answer += 1
            }
        }
    }
    return answer
}