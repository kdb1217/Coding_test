import Foundation
/*
풀이계획
1. 두개의 cnt를 둔다.
2. 반복문을돌려서 cnt보다 해당인덱스가 작으면 No 리턴
*/
func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    var card1Index: Int = 0
    var card2Index: Int = 0
    
    for i in goal {
        if let cardIndex = cards1.firstIndex(of: i) {
            if cardIndex < card1Index || cardIndex - card1Index >= 2 {
                return "No"
            } else {
                card1Index = cardIndex
            }
        }
        
        if let cardIndex = cards2.firstIndex(of: i) {
            if cardIndex < card2Index || cardIndex - card2Index >= 2{
                return "No"
            } else {
                card2Index = cardIndex
            }
        }
    }
    
    return "Yes"
}