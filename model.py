from keras.models import Sequential
from keras.layers import Dense
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
# define base model
def baseline_model(input_shape,output_shape):
	# create model
    model = Sequential()
    model.add(Dense(256, input_dim=input_shape, activation='relu'))
    model.add(Dense(186,activation ="relu"))
    model.add(Dense(100,activation ="relu"))
    model.add(Dense(output_shape))
    optimizer = Adam(lr=0.001)
    model.compile(loss=keras.losses.MeanSquaredError(),optimizer=optimizer)
    return model

#change loss: ['mean_squared_error','logcosh']
#loss: mean_squared_error :  
#loss: huber: keras.losses.Huber()
#loss: MeanSquaredLogarithmicError : keras.losses.MeanSquaredLogarithmicError()