const data = [4, 3, 6, 8, 7, 5, 2, 1]

const stackSequence = (data) => {
  let count = 1
  let result = []
  const stack = []
  for(let i=0; i<data.length; i++){
    while (count <= data[i]) {
      stack.push(count)
      count += 1
      result.push('+')
    }
    if (stack.slice(-1)[0] == data[i]) {
      stack.pop()
      result.push('-')
    } else {
      console.log('NO')
      return
    }
  }
  result = result.join(' ')
  console.log(result)
}

stackSequence(data)