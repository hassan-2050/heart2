import pickle
from sklearn.metrics import euclidean_distances  # or the correct import based on your usage

# Load the old model
with open('path_to_old_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Save the model with the current version of scikit-learn
with open('path_to_new_model.pkl', 'wb') as file:
    pickle.dump(model, file)
