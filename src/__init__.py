import tensorflow as tf

"""# ! print(tf.__version__)
# * M... Tensors about Like... Okay?

#TODO: Create a Tensor
scalar = tf.constant(7)
print(scalar)
print(scalar.ndim)


#TODO: Create a Vector
vector = tf.constant([10,10])
print(vector)
print(vector.ndim)


#TODO: Create a Matrix
matrix = tf.constant([[10,7],[7,10]])
print(matrix)
print(matrix.ndim)

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

print(tensor)
print(tensor.ndim)

"""

# * tf.Variable

"""#TODO: tf.Variable could be change variables tensor and... tf.constant can´t

changeable_tensor  = tf.Variable([0,1])
changeable_tensor[0].assign(1)
print(changeable_tensor)
"""

#TODO: Crate random Tensors 

    tensorRandom = tf.random.Generator.from_seed(42)
    tensorRandom = tensorRandom.normal(shape=(3,2))
    print(tensorRandom)