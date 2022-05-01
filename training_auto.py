from dataloader import process_data
import ast
import numpy as np
from autoencoder import baseline_model
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
#ast.literal_eval
f = open('../capture_ok.txt', "r")
data = f.readlines()
process_input,process_output = process_data(data)
#array
array_input = np.array(process_input)
array_output= np.array(process_output)
#input shape
input_shape = array_input.shape
print(input_shape[1])
output_shape = array_output.shape
print(output_shape[1])
# Split data
X_train,X_val,y_train,y_val=train_test_split(array_input, array_output, test_size=0.2)
print("Complete")
#base model
earlyStopping = EarlyStopping(monitor='val_loss', patience=10, verbose=0, mode='min')
mcp_save = ModelCheckpoint('modelbest.hdf5', save_best_only=True, monitor='val_loss', mode='min')
model = baseline_model(input_shape[1],output_shape[1])
model.fit(X_train,y_train,batch_size=16, validation_data=(X_val, y_val), epochs=200, verbose=1,callbacks=[earlyStopping,mcp_save])

val_pre = model.predict(X_val)
MAE = mean_absolute_error(val_pre,y_val)
print("MAE: ",MAE)
MSE = mean_squared_error(val_pre,y_val)
print("MSE: ",MSE)
RMSE = np.sqrt(mean_squared_error(val_pre,y_val))
print("RMSE: ",RMSE)
#Root Mean Squared Log Error(RMSLE)
RMSLE = np.log(np.sqrt(mean_squared_error(val_pre,y_val)))
print("RMSLE: ",RMSLE)
#R Squared (R2)
R2_Score = r2_score(val_pre,y_val)
print("R2_Score: ",R2_Score)