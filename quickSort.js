/**
* Idea is to create a pivot as last number of the array
* then create a left array which has all the value less than pivot and right array which has all the value greater than pivot
* retun left[] + pivot + right[]
* do the quick sort on left array and right array until they are perfectly sort
*/

const quickSort = (arr) => {
	if(arr.length <= 1){
  	return arr;
  }
  
  const pivot = arr[arr.length - 1];
  const left = [];
  const right = [];
  
  for(let i = 0; i < arr.length - 1; i++){
  	if(arr[i] <= pivot) {
    	left.push(arr[i]);
    } else {
    	right.push(arr[i]);
    }
  }
  
	return [...quickSort(left), pivot, ...quickSort(right)];
}

console.log(quickSort([5,4,9,7,6]));
