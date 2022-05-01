from keras.models import Sequential
from keras.layers import Dense,Input,Lambda
from keras.layers import Dense, Dropout, GlobalAveragePooling2D
from keras.models import Model
import keras
from tensorflow.keras import optimizers
from tensorflow.keras.optimizers import Adam
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from keras.constraints import unit_norm, max_norm

# define base model
def baseline_model(input_shape,output_shape):
	# this is the size of our encoded representations
    encoding_dim = 32  

    # this is our input placeholder
    input_img = Input(shape=(input_shape,))
    # "encoded" is the encoded representation of the input
    encoded = Dense(encoding_dim, activation='relu')(input_img)
    # "decoded" is the lossy reconstruction of the input
    decoded = Dense(output_shape)(encoded)

    # this model maps an input to its reconstruction
    autoencoder = Model(input_img, decoded)

    # this model maps an input to its encoded representation
    encoder = Model(input_img, encoded)

    # create a placeholder for an encoded (32-dimensional) input
    encoded_input = Input(shape=(encoding_dim,))
    # retrieve the last layer of the autoencoder model
    decoder_layer = autoencoder.layers[-1]
    # create the decoder model
    decoder = Model(encoded_input, decoder_layer(encoded_input))

    autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
    return autoencoder

#change loss: ['mean_squared_error','logcosh']
#loss: mean_squared_error :  
#loss: huber: keras.losses.Huber()
#loss: MeanSquaredLogarithmicError : keras.losses.MeanSquaredLogarithmicError()