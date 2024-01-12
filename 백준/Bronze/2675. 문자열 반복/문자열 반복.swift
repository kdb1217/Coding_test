import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

// 2675 문자열 반복 풀이계획
/*
 1. 문자열을 배열로 바꾼다.
 2. 하나의 빈 문자열을 선언하고 배열의 요소를 n만큼 반복해서 문자열에 더한다.
 3. 이 과정을 배열의 길이만큼 한다.
 4. 맨 처음 테스트 케이스의 반복만큼 한다. -> 함수화하면 좋을 것 같다.
*/

let inputNum: Int = Int(readLine()!)!

var answerArr: [String] = []
for _ in 1...inputNum {
    let input = readLine()!
    let result = input.components(separatedBy: " ")
    let tmp: String = repeatWord(repeatnum: Int(result[0]) ?? 0, inputString: result[1])
    answerArr.append(tmp)
}
for i in 0...answerArr.count - 1 {
    print(answerArr[i])
}

private func repeatWord(repeatnum: Int, inputString: String) -> String{
    var answerString: String = ""
    for i in 0...inputString.count - 1 {
        for _ in 1...repeatnum {
            answerString += String(inputString[i])
        }
    }
    return answerString
}
