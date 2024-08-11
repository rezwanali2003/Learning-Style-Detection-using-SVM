# Automatic Detection of Learning Styles in Learning Management Systems Using Literature-Based Methods and Support Vector Machines

## Overview

This project focuses on developing a system to automatically detect learning styles within Learning Management Systems (LMS) by combining literature-based methods with Support Vector Machines (SVM). The goal is to personalize e-learning experiences by accurately identifying the learning preferences of individual students, thereby enhancing the effectiveness of the learning process.

## Features

- **Learning Style Detection**: Automatically identifies learning styles using a combination of literature-based methods and SVM.
- **Data-Driven Approach**: Utilizes actual behavioral patterns during the online learning process for model building.
- **High Accuracy**: Achieves superior accuracy in detecting learning styles compared to traditional methods.
- **Scalability**: Capable of processing large datasets from various e-learning environments.
- **Flexibility**: Can be adapted to different LMS and educational contexts.

## Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)
- git (version control system)
- Flask (for the web application)

### Steps

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/learning-style-detection.git
   cd learning-style-detection
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Data Preparation

1. **Collect Learning Log Data**: Gather learning log data from your LMS. The dataset should include features such as user interactions, time spent on tasks, quiz scores, etc.

2. **Preprocess Data**: Use the provided preprocessing scripts to prepare the data for training the SVM model.

### Training the Model

1. **Run the training script**:
   ```sh
   python train.py --data_path path/to/your/dataset.csv
   ```

2. **Save the model**: The trained model will be saved as `model.pkl`.

### Deploying the Model

1. **Start the Flask app**:
   ```sh
   python app.py
   ```

2. **Make predictions**: Send POST requests to the API with student data to detect their learning styles.
   ```sh
   curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"user_id": 123, "feature1": value1, "feature2": value2, ...}'
   ```

### Example Request

```json
{
  "user_id": 123,
  "feature1": value1,
  "feature2": value2,
  ...
}
```

### Example Response

```json
{
  "learning_style": "visual"
}
```

## Project Structure

```
learning-style-detection/
├── app.py               # Flask API for model deployment
├── train.py             # Script to train the model
├── preprocess.py        # Script for data preprocessing
├── data/
│   ├── raw/             # Raw data files
│   └── processed/       # Processed data files
├── model.pkl            # Trained model
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Contributing

We welcome contributions to enhance this project. Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the project's coding standards and includes appropriate documentation.

## License


## Contact
Shaik Rezwan Ali - rezwanali.cs@gmail.com
