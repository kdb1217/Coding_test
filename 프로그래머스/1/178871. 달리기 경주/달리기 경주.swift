import Foundation
/*
풀이계획
1. calling반복문을 돌린다.
2. calling의 반복문 값과 해당하는 players의 인덱스를 찾고 1을 뺀값과 스왑한다.
시간초과 실패
두번째 풀이 계획
1. players의 이름과 등수를 딕셔너리로 만들어서 
2. 이름이 불릴때 위와 같이 반복한다.
*/
func solution(_ players:[String], _ callings:[String]) -> [String] {
    var playersInfo = Dictionary(uniqueKeysWithValues: players.enumerated().map { ($1, $0) })
    var playerArr = players
    
    callings.forEach { i in
        let tmp = playersInfo[i]! //현재 바꾸고 하는 사람 인덱스
        let player = playerArr[tmp - 1]
        
        playersInfo[i]! -= 1
        playersInfo[player]! += 1
        playerArr.swapAt(tmp, tmp-1)
    }
    return playerArr
}