import Foundation

/* 풀이계획
1. 조합을 이용해 모든 3개의 수의 합을 하나의 리스트에 저장한다.
2. 반복문을 이용해 소수를 찾는다
*/
func solution(_ nums:[Int]) -> Int {
    var cnt = 0
    var sums: [[Int]] = combination(nums, 3)
    for i in sums {
        if findPrime(i.reduce(0, +)) { cnt += 1 }
    }
    return cnt
}

func combination<T: Comparable>(_ array: [T], _ n : Int) -> [[T]] {
    var result = [[T]]()
	if array.count < n { return result }
	
	func cycle(_ index: Int, _ now: [T]) {
		if now.count == n {
			result.append(now)
			return
		}
		
		for i in index..<array.count {
			cycle(i + 1, now + [array[i]])
		}
	}
	cycle(0, [])
    
	return result
}
func findPrime(_ num: Int) -> Bool {
    for i in 2..<num {
        if num % i == 0 {
            return false
        }
    }
    return true
}