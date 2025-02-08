## M... Cover that I Could see in this Course?

- Introduction to  Tensors
- Getting information from Tensors
- Manipulate Tensors
- Tensors & Numpy
- Using GPU's with Tensor flow

### Using Tensor Flow =>
``` python
import tensorflow as tf
# * M... Create tensor Using tf.constant

#TODO: Create a Tensor
scalar = tf.constant(7)

#TODO: Create a Vector
vector = tf.constant([10,10])

#TODO: Create a Matrix
matrix = tf.constant([[10,7],[7,10]])

#* Umm... I thought that I got it
tensor = tf.constant([
		[
			[1,2,3],
			[3,2,1]
		],
		[
			[4,5,6],
			[6,5,4]
		],
		[
			[7,8,9],
			[9,8,7]
		]
 ])

```

**Now** can be explain something
- Scalar => is a single Number
- Vector => is a number with Direction 
- Matrix => is a Two Dimensional array of number with Direction
- Vector => is an n-dime array of number 

```python
import tensorflow as tf

change_tensor = tf.Variable(
	[
		3,2,1
	]
)

#* And if you wanna Change a Var you use
change_tensor[0].assign(0)

```

**Now** can be explain something
- M... The Tensors type *constant* don´t can be change... but Tensors type Variable can be Changes   

>[!IMPORTANT]
>**Um...** I am understand that get more precision about data Outputs... We can use a Random Tensors like a benchmark... How works those...

This works like... The neuronal are learning patterns right?...  But it need a more Tensors for Learn more Speed... so... we can create Tensors random that help you with neuronal networks to learn... And slowly adjusts them as it continually learn with more and more ***examples***

```python
tensorRandom = tf.random.Generator.from_seed(42)
tensorRandom = tensorRandom.normal(shape=(3,2))
```

>[!IMPORTANT]
>RULES that you´ll have on your mind when you create a Random Tensors
>
> >If neither the global seed nor the operation seed is set: A randomly picked seed is used for his OP.
> 
> >If the graph-level seed is set, but the operation is not: The system deterministically pick an operation seed in conjunction with the graph-level seed so that it gets a unique random sequence. Within the same version of TensorFlow and User-Code, this sequence is deterministic. However across different versions, this sequence might change. If the code depends on particular seeds to work, specify both graph-level and operation-level seeds explicitly.
> 
> >If the operation seed is set, but the global seed is not set: A default global seed ant the specified operation seed are used to determinate  the random sequence
> 
> >If both the global and the operation seed are set: Both seeds are used in conjunction to determine the random sequence
> 


**Otherwise** to make a Tensors

```python 
tensor_len = tf.ones([3,3]) 
```
Those create a Tensor Two-dimensional with a 3 Row and 3 Columns with a unique value that is One

```python
arr = tf.zeros(shape=(3,3,3))
```
**Or** use a zeros to create the same... but with Zeros

**Now** using a Lib Numpy can Create a tensors more Fast

```python
import numpy as np

arr = np.arange(1,25, dtype=np.int32)
tensor = tf.constant(arr, shape=(2,3,4))
print(tensor)
```

When we created a Array that have a range pre-made and only make insert a shape from tensor and Wala...


