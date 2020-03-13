Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
* What is the worse case scenario if you try to extend the storage size of a dynamic array?

Dynamic arrays are created with a size greater than the current needed length to avoid needing to resize constantly. However, when filled to capacity, they do need to be resized which is an operation that runs in O(n). The worst-case scenario for adding to the front or back of an array triggers a resize operation and runs in O(n). In cases where the array's capacity hasn't been reached, appending runs in O(1). Accessing an array by index is an operation that runs in O(1).

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

Each block in a chain contains a timestamp, transaction information, index, previous hash, and proof. Chain integrity is maintained by each block's previous hash referring to a valid block. Attempting to change a value at a point in the chain requires successfully changing every block's previous hash which is too resource intensive to feasibly accomplish.
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

Proof of work is a hashed value based on the previous block's information. Finding a valid proof is rare and takes time and can only be successfully accomplished by a single actor (the first to register the proof). The client produces a proof and the server evaluates with its own algorithm. When accepted, the server adds the block to the chain and the work to find the next proof begins.
