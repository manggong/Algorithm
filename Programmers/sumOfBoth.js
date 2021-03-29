function solution(numbers) {
  var answer = [];
  
  for(let i=0; i<numbers.length; i++){
      for(let j=i+1; j<numbers.length; j++){
          answer.push(numbers[i] + numbers[j])
      }
  }
  answer = answer.sort((a,b)=>{return a-b})
  return Array.from(new Set(answer))
}