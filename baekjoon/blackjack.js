const target = 21;
const numbers = [5, 6, 7, 8, 9];


const solution = (numbers,target) => {
  let sum;
  let answer
  for(let i=0; i<numbers.length; i++){
    for(let j=i+1; j<numbers.length; j++){
      for(let k=j+1; k<numbers.length; k++){
        sum = numbers[i] + numbers[j] + numbers[k]
        if(sum <= target) {
          answer = sum
        } 
      }
    }
  }
  console.log(answer)
  return answer
}

solution(numbers,target)
//console.log(numbers[0])