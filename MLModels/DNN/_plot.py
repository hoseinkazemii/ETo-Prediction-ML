import matplotlib.pyplot as plt


def plot(history):
	
	plt.plot(history.history['loss'], label='train')
	plt.plot(history.history['val_loss'], label='validation')
	plt.legend();
	plt.show()

	plt.plot(history.history['mean_squared_error'], label='train')
	plt.plot(history.history['val_mean_squared_error'], label='validation')
	plt.legend();
	plt.show()