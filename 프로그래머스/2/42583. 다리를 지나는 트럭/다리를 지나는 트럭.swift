import Foundation
    
func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    var bridge: [(Int, Int)] = []
    var idx: Int = 0
    var time: Int = 0
    
    while idx < truck_weights.count {
        time += 1
        
        let tmp = bridge.reduce(0) { $0 + $1.0}
        let truckWeight = truck_weights[idx]
        
        if tmp + truckWeight <= weight {
            bridge.append((truck_weights[idx], 0))
            idx += 1
        }
        
        bridge = bridge.map { ($0.0, $0.1 + 1) }
        bridge = bridge.filter { $0.1 < bridge_length }

    }
    
    if bridge.count > 0 {
        time += bridge_length - bridge.last!.1 + 1
    }
    
    
    return time
}