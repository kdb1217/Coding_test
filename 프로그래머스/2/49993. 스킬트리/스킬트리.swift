import Foundation

/*
풀이계획
1.skill을 배열로 만들어서 각자의 skill트리에서 반복문을돌려서 skill의 인덱스를 찾는 반복문을 만든다.
2.정렬을 하지 않아도 정렬된 배열과 값이 같아야 하기 때문에 정렬된 값과 비교한다. 건너 뛰었을때에는 실패한다.
3. 스킬을 중간에 건너뛰었을때를 체크하는 로직 필요
3.값이 같으면 answer += 1
*/
func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    var answer: Int = 0
    let skillArr = skill.map { String($0) }
    
    for i in skill_trees {
        let tmp = i.map { String($0) }
        var tmpArr: [Int] = []
        var wordArr: [String] = []
        
        for i in skillArr {
            if let a = tmp.firstIndex(of: i) {
                tmpArr.append(a)
                wordArr.append(i)
            }
        }
        
        if tmpArr.sorted() == tmpArr && skill.prefix(wordArr.count) == wordArr.joined() {
            answer += 1
        }
    }
    return answer
}