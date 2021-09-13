# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from seventh import result
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ## model balancing data:
    # SMOTE
    # ADASYN
    # Under Sampling
    # Random Under Sampling
    # SMOTEENN
    # Over Sampling
    # Near Miss
    # none
    #(none = no balancing data)

    ## model Classifier:
    # SVM
    # LogisticRegression
    # KNN
    # MLP

    hasil=result('SMOTE','SVM')
    data=hasil.dataset
    # print(np.c_[ypred,hasil.label])
