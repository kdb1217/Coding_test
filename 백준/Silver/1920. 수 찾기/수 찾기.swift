import Foundation

let num = Int(readLine()!)!
let arr: [Int] = readLine()!.split(separator: " ").map {Int($0)!}
let num2 = Int(readLine()!)!
let arr2: [Int] = readLine()!.split(separator: " ").map {Int($0)!}

let arr1 = arr.sorted()
let setArr2 = Array(Set(arr2))

// 반복문을 통한 이분 탐색


for i in arr2 {
    var start = 0
    var end = arr1.count - 1
    var flag = 0
    while start <= end {
        let mid = ((start + end) / 2)
        
        if arr1[mid] == i {
            flag = 1
        }
        if arr1[mid] > i {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    print(flag)
}
