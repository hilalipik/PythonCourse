from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn import metrics
import joblib
from joblib import dump, load

feature_names = 0
target_names = 0

def create_module(test_size, neighbors):
    global feature_names, target_names

    # Import tha data
    iris = load_iris()

    feature_names = iris.feature_names
    target_names = iris.target_names

    # Split the data, Training set / Test set
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # Create a model
    knn = KNeighborsClassifier(n_neighbors=neighbors)
    knn.fit(X_train, y_train)

    # Check the output and improve

    #y_pred = knn.predict(X_test)
    #print(f"Accuracy for \n\ttrain size - {1-test_size}\n\ttest size - {test_size}\n\tneighbors - {neighbors}\n is:", metrics.accuracy_score(y_test, y_pred))
    return knn

def main():
    global feature_names, target_names

    # After testing and improving, test_size=0.4, neighbors=3 are the chosen variables
    knn = create_module(0.4,3)
    
    # Mimic a scenario where the module is created on the server and sent prepared to the client
    joblib.dump(knn, 'mlbrain.joblib')
    model = joblib.load('mlbrain.joblib')

    sample = []
    print("Enter features for each iris (0 to stop)")
    stop = 1
    while stop != '0':
        item = []
        for feature in feature_names:
            while 1:
                try:
                    item.append(float(input(f'Enter {feature}:')))
                except ValueError:
                        print("Only enter numbers.")
                        continue
                break
        stop = input("OK! Another iris? (0 to stop) ")
        sample.append(item)

    predictions = model.predict(sample)
    predict_species = [target_names[p] for p in predictions]
    print("predictions:" , ', '.join(predict_species))

if __name__ == "__main__":
    main()