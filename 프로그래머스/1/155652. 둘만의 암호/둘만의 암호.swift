import Foundation

/*
풀이계획
1. 전부 아스키 코드로 바꾸고 배열에 저장한다.
2. skip또한 배열로 저장한다.
3. while문을 통해서 index만큼 늘린다. 중간에 범위를 벗어나면 다시 a로 돌아간다. 그리고 skip에 해당하는 아스키 코드가 나오면 인덱스를 늘리지 않는다.
*/
// 아스키 코드 a: 97, A: 65, Z: 90, z: 122 
func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    var sAscii = s.map { Int(UnicodeScalar(String($0))!.value) }
    var skipAscii = skip.map { Int(UnicodeScalar(String($0))!.value) }
    var arr = skipAscii.map { $0 + 26}
    skipAscii += arr
    var answerAscii: [Int] = []
    
    for i in 0..<sAscii.count {
        var cnt: Int = 0
        while cnt < index {
            if skipAscii.contains(sAscii[i]) {
                while skipAscii.contains(sAscii[i]) {
                    sAscii[i] += 1
                }
            } else {
                sAscii[i] += 1
                if skipAscii.contains(sAscii[i]) {
                    while skipAscii.contains(sAscii[i]) {
                        sAscii[i] += 1
                }
            }
                cnt += 1
            }
            
            if sAscii[i] >= 123  {
                let tmp = sAscii[i] - 122
                 sAscii[i] = 97 + (tmp - 1)
                
            } else if sAscii[i] >= 91 && sAscii[i] < 97 {
                 let tmp = sAscii[i] - 90
                 sAscii[i] = 65  + (tmp - 1)
            }
        }
    }
    var answer = sAscii.map { String(UnicodeScalar($0)!) }
    return answer.joined()
}