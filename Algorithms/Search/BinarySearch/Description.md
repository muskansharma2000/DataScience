**Short Description**\
The binary search is an algorithm that's used to find the location of an element inside a sorted list\

**Time Complexity**\
    Worst Case: `O(log(n))`\
    Best Case `O(1)`\

**Usage** \
The binary search algorithm is used when you want to determine the location of an element inside an array.
In order for the binary search to work properly, the list has to be sorted beforehand.\

**Functionality**\
The binary search algorithm is implemented recursively in most cases.\
As parameters it takes an array a, in which the element you are looking for is located,\
two integers left and right, which mark the bonds of an area inside the array and\
the wanted element e.\
Thus, the function header may look like the following: `def binary_search(a, left, right, e):`\
In the first run, the algorithm picks a random element from the array, which is most likely the element in the middle of the array.\
It then checks whether the picked element equals, is smaller than or greater then the element to be searched for.\
In the first case the algorithm simply returns the element's position.\
In the second or third case, the algorithm calls itself but with different bonds this time, depending on what the result of the above check was.\
These two steps are repeated until either the element was found or there are no elements left inside the bonds, meaning that the element is not in the list.\
// A recursive binary search function. 
//It returns  location of x in given array arr[l..r] is present, 
// otherwise -1 
