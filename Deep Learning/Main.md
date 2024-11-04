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
print(tensorRandom)
```
