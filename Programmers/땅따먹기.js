function solution(land) {

    let answer = 0; 
    for(let i=0; i<land.length; i++){
        for(let j=0; j<land[i].length; j++){
            if(i===0){
                continue
            }
            else{
                let arr = land[i-1].slice()
                arr[j] = 0 
                land[i][j] += Math.max.apply(null, arr)
                answer  = Math.max(land[i][j], answer)
            }
        }       
    }
        console.log(answer)
        return answer
    }

let land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

solution(land)