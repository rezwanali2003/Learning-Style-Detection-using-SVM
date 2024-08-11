from flask import Flask, render_template, request
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the provided data into a DataFrame
data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Age': [16, 16, 18, 21, 21, 21, 21, 21, 21, 21],
    'Read_Chalkboard': [3, 5, 3, 1, 4, 2, 3, 2, 5, 1],
    'Read_Instructions': [3, 4, 4, 3, 4, 3, 3, 3, 5, 3],
    'Understand_Read_Instructions': [4, 4, 3, 3, 4, 2, 4, 3, 5, 4],
    'Learn_Read': [3, 4, 3, 4, 5, 3, 3, 4, 5, 2],
    'Learn_Textbooks': [2, 3, 4, 4, 5, 3, 3, 4, 4, 3],
    'Tell_Instructions': [4, 3, 2, 2, 4, 3, 4, 5, 4, 3],
    'Learn_Tell': [3, 2, 4, 2, 4, 1, 4, 5, 4, 4],
    'Remember_Heard': [3, 4, 3, 2, 3, 4, 5, 5, 4, 2],
    'Learn_Lecture': [2, 3, 2, 2, 4, 3, 5, 5, 4, 2],
    'Learn_Listen': [3, 4, 2, 2, 4, 5, 3, 5, 4, 2],
    'Learn_Doing': [2, 3, 2, 4, 5, 1, 3, 5, 4, 5],
    'Learn_Doing_Better': [3, 4, 3, 4, 5, 2, 3, 1, 4, 5],
    'Enjoy_Experiments': [2, 3, 2, 4, 5, 4, 5, 5, 5, 5],
    'Understand_Role_Playing': [2, 4, 3, 4, 3, 1, 3, 5, 5, 5],
    'Understand_Role_Playing_Better': [3, 4, 3, 4, 4, 2, 4, 5, 5, 5],
    'Learner': ['K', 'A', 'A', 'K', 'A', 'V', 'K', 'V', 'A', 'K'],
}

df = pd.DataFrame(data)

# Map the learning styles to categories: 'Auditory', 'Visual', 'Kinesthetic'
style_mapping = {'A': 'Auditory', 'V': 'Visual', 'K': 'Kinesthetic'}
df['Learner'] = df['Learner'].map(style_mapping)

# Label encoding for 'Gender' and 'Learner' columns
le_gender = LabelEncoder()
le_learner = LabelEncoder()

df['Gender'] = le_gender.fit_transform(df['Gender'])
df['Learner'] = le_learner.fit_transform(df['Learner'])

# Features (X) and target variable (y)
X = df.drop(['Learner'], axis=1)  # Features excluding 'Learner'
y = df['Learner']

# Train SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = {
            'Gender': request.form['gender'],
            'Age': int(request.form['age']),
            'Read_Chalkboard': int(request.form['read_chalkboard']),
            'Read_Instructions': int(request.form['read_instructions']),
            'Understand_Read_Instructions': int(request.form['understand_read_instructions']),
            'Learn_Read': int(request.form['learn_read']),
            'Learn_Textbooks': int(request.form['learn_textbooks']),
            'Tell_Instructions': int(request.form['tell_instructions']),
            'Learn_Tell': int(request.form['learn_tell']),
            'Remember_Heard': int(request.form['remember_heard']),
            'Learn_Lecture': int(request.form['learn_lecture']),
            'Learn_Listen': int(request.form['learn_listen']),
            'Learn_Doing': int(request.form['learn_doing']),
            'Learn_Doing_Better': int(request.form['learn_doing_better']),
            'Enjoy_Experiments': int(request.form['enjoy_experiments']),
            'Understand_Role_Playing': int(request.form['understand_role_playing']),
            'Understand_Role_Playing_Better': int(request.form['understand_role_playing_better']),
        }

        # Convert 'Gender' to numerical value using label encoding
        user_data['Gender'] = le_gender.transform([user_data['Gender']])[0]

        # Prepare user data for prediction
        user_data_df = pd.DataFrame([user_data])

        # Predict learning style using the trained SVM model
        prediction = svm_model.predict(user_data_df)

        # Convert predicted label back to original class
        predicted_style = le_learner.inverse_transform(prediction)[0]

        return render_template('index.html', prediction=predicted_style)

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
