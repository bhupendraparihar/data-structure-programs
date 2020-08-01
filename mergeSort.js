const stitch = (left, right) => {
	const result = [];
  
  while(left.length && right.length) {
  	if(left[0] <= right[0]){
    	result.push(left.shift());
    } else {
    	result.push(right.shift());
    }
  }
  
  while(left.length) {
  	result.push(left.shift());
  }
  while(right.length) {
  	result.push(right.shift());
  }
  
  return result;
}

const mergeSort = (nums) => {
	if(nums.length < 2) return nums;
  
  const middle = Math.floor(nums.length/2);
  const left = nums.slice(0, middle);
  const right = nums.slice(middle, nums.length);
  
  const sortedLeft = mergeSort(left);
  const sortedRight = mergeSort(right);
  
  return stitch(sortedLeft, sortedRight);
}

console.log(mergeSort([5,4,9,7,6]));
