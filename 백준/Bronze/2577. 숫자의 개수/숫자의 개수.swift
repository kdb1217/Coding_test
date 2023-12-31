import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

//var num: Int = Int(readLine()!)!
//for i in 0...num {
//    let input = readLine()!
//    let result = input.components(separatedBy: " ")
//    let repeatnum = Int(result[0])
//    answer(num: repeatnum ?? 0,text: result[i])
//}
//
//private func answer(num: Int, text: String)  {
//    
//}

var num1: Int = Int(readLine()!)!
var num2: Int = Int(readLine()!)!
var num3: Int = Int(readLine()!)!

let total: String = String(num1 * num2 * num3)

for i in 0...9 {
    let a: Character = Character(String(i))
    let tmp = total.filter {($0) == a }.count
    print(tmp)
}
