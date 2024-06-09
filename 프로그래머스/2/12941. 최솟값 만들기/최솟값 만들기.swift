import Foundation
/*
풀이계획

*/

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    let arr1 = Array(zip(A.sorted(), B.sorted(by: >)))
    
    let sumArr1 = arr1.reduce(0) { sum, i in
        return sum + (i.0 * i.1)
    }
    // let sumArr2 = arr2.reduce(0) { sum, i in
    //     return sum + (i.0 * i.1)
    // }
    return sumArr1
}