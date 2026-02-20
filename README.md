# Dog Breed Identification Using Transfer Learning

Dog Breed Identification is a deep learning–based application designed to automatically identify the **breed of a dog from an image** using transfer learning techniques.
The system analyzes visual features such as fur texture, facial structure, and body shape to provide **accurate and fast breed predictions**, helping pet owners, veterinarians, and researchers.

---

## Team Details

| Field | Information |
|------|------------|
| **Team ID** | LTVIP2026TMIDS66155 |
| **Team Size** | 4 |
| **Team Leader** | K Nagasudha |
| **Member 1** | Gandhi Sivanjaneyulu |
| **Member 2** | M Naresh |
| **Member 3** | Shaik Abdul Rahiman |

---

## Project Demo

https://drive.google.com/  
https://drive.google.com/file/d/1QVb4dB_Q4HIDHHXyRBH5p_BjaVwr-siO/view?usp=sharing

---

## Technologies Used

| Category | Technology |
|--------|-----------|
| Programming Language | Python |
| Deep Learning | TensorFlow, Keras |
| Image Processing | OpenCV, NumPy |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Web Framework | Flask |
| Interface | HTML, CSS |
| Platform | Google Colab |
| Repository | GitHub |

---

## Dataset

- **Source:** Kaggle
- **Dataset Name:** Dog Breed Identification
- **Link:** https://www.kaggle.com/c/dog-breed-identification

The dataset consists of thousands of labeled dog images belonging to multiple breeds. These images are used for training, validation, and testing of the deep learning model.

---

## Project Setup

### 1. Clone the Repository
```bash
git clone <your-github-repo-link>
cd dog_breed_identification
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv .venv
```

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / Mac**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

If requirements.txt is not available:
```bash
pip install tensorflow keras flask numpy pandas matplotlib opencv-python
```

### 4. Train the Model
```bash
python train.py
```

This process performs:
- Image preprocessing
- Feature extraction using transfer learning
- Model training and validation

The trained model is saved as:
```
dog_breed_model.h5
```

### 5. Run the Web Application
```bash
python app.py
```

Open the browser and navigate to:
```
http://127.0.0.1:5000/
```

Upload a dog image and click **Predict** to view the identified breed.

---

## Project Structure
```
dog_breed_identification/
│
├── app.py
├── train.py
├── dog_breed_model.h5
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── css/
└── dataset/
```

---

## Expected Results

- Accurate identification of dog breeds
- Fast predictions using transfer learning
- User-friendly web interface
- Reliable and repeatable results

---

## Future Enhancements

- Support for more dog breeds
- Improve accuracy using advanced models (ResNet, EfficientNet)
- Mobile application integration
- Cloud deployment for real-time usage

---

## Conclusion

Dog Breed Identification using Transfer Learning demonstrates the effectiveness of deep learning and computer vision in real-world image classification tasks. By combining transfer learning with a web-based interface, the project delivers an efficient and practical solution for automated dog breed recognition.

---

## License

This project is developed for **educational and academic purposes only**.
