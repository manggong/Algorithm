function solution(bridge_length, weight, truck_weights) {
    let spentTime = 0
    let bridgeState = []
    let currentBridgeWeight = 0
    
    for(let i=0; i<bridge_length; i++){
        bridgeState.push(0)
    }
    
    let now_truck = truck_weights.shift()
    
    bridgeState.unshift(now_truck)
    bridgeState.pop(0)
    
    currentBridgeWeight += now_truck
    
    spentTime++
    
    while(currentBridgeWeight){
        
        currentBridgeWeight -= bridgeState.pop(0)
        
        now_truck = truck_weights.shift()
        
        if(now_truck + currentBridgeWeight <= weight){
            bridgeState.unshift(now_truck)
            currentBridgeWeight += now_truck
        } else {
            bridgeState.unshift(0)
            truck_weights.unshift(now_truck)
        }
        spentTime++
    }
    
    return spentTime
}