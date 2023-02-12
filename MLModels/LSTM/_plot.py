import matplotlib.pyplot as plt


def plot(**params):
	
	history = params.get("history")

	plt.plot(history.history['accuracy'], label='train')
	plt.plot(history.history['val_accuracy'], label='validation')
	plt.legend();
	plt.show()

	plt.plot(history.history['loss'], label='train')
	plt.plot(history.history['val_loss'], label='validation')
	plt.legend();
	plt.show()