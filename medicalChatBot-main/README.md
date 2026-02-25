# MedIntel AI – Intelligent Healthcare Assistant


# 🏥 MedIntel AI  
### Intelligent Healthcare Assistant
This repository presents an AI-powered medical chatbot developed to deliver intelligent, real-time healthcare assistance using advanced Natural Language Processing and Machine Learning techniques.

---
## 📑 Table of Contents  

- [Project Overview](#project-overview)  
- [Introduction](#introduction)  
- [Objectives](#objectives)  
- [Problem Statement](#problem-statement)  
- [Proposed Solution](#proposed-solution)  
- [System Architecture](#system-architecture)  
- [Dataset Description](#dataset-description)  
- [Methodology](#methodology)  
  - [Data Preprocessing](#data-preprocessing)  
  - [Model Implementation](#model-implementation)  
  - [Training Strategy](#training-strategy)  
  - [Evaluation Methodology](#evaluation-methodology)  
- [Performance Analysis](#performance-analysis)  
- [Results and Discussion](#results-and-discussion)  
- [Deployment Details](#deployment-details)  
- [Project Management](#project-management)  
- [Future Enhancements](#future-enhancements)  
- [References](#references)

---
## Introduction
---
### Project Background

In today’s world, getting quick medical advice is not always easy. Many people have to wait a long time to consult a doctor, especially in remote areas. To solve this problem, this project focuses on building an AI-based medical chatbot that can provide basic healthcare guidance.

The chatbot uses Natural Language Processing (NLP) to understand user questions and give helpful responses. It helps users learn more about their symptoms and health conditions and supports them in making better medical decisions.

---
## Motivation
---
By addressing the challenges mentioned, the chatbot aims to achieve the following objectives:
- Empower users to make informed decisions about their health and medical conditions, enhancing overall health literacy and promoting proactive healthcare management.
- Provide a convenient and efficient platform for users to access medical information anytime, anywhere, facilitating timely decision-making and intervention in healthcare matters.
This project will serve as a practical application of the concepts studied in the NLP course and reinforce our learning and showcasing the real-world relevance of the technologies and strategies employed in improving healthcare accessibility and patient outcomes.

---
## Problems and Solutions
---
### Problems
---
- Limited Access to Doctors: Many people face long waiting times, overloaded hospitals, distance from medical facilities, and financial difficulties, which make it hard to consult healthcare professionals easily.

- Delay in Seeking Treatment: A lack of awareness about symptoms or not understanding their seriousness often leads to late medical attention, especially in serious conditions like cancer.

- Technological Limitations: Earlier chatbots were mostly rule-based systems with limited ability to understand natural language. They could not learn or improve over time, which reduced their accuracy and effectiveness.

---
### Solutions
---
- Scalability: The system can manage a growing number of users without reducing performance or response quality.
- Availability: The chatbot remains active at all times and provides support to users 24/7.
- Data Management: User information is analyzed to generate useful insights and support personalized healthcare guidance.
- Quick Response: The chatbot delivers fast and accurate answers to user questions.
- Cost Effectiveness: The system helps reduce operational expenses by automating routine tasks and improving efficiency.

---
## Related Works

### 1. Buoy Health
---
<img width="1518" alt="Screenshot 2024-04-28 at 22 21 30" src="https://github.com/tanziltonmoy/Medical-Chatbot-for-Patients/assets/32629216/be348f35-cabf-4aa0-b173-87305f544815">

Features: Buoy Health is a conversational AI chatbot designed to provide personalized health assessments and guidance to users. It uses natural language processing to understand users' symptoms, medical history, and concerns, and then offers tailored recommendations such as possible conditions, next steps, and self-care advice. Buoy Health aims to empower users to make informed decisions about their health and navigate the healthcare system more effectively.
Objectives: The primary objective of Buoy Health is to improve healthcare access and outcomes by leveraging AI technology to deliver accurate and reliable health information and support to users. It aims to reduce unnecessary healthcare visits, alleviate patient anxiety, and facilitate early detection and management of medical conditions.
NLP Architecture: Buoy Health employs a combination of NLP techniques, including rule-based systems, machine learning models, and medical knowledge graphs. It uses advanced algorithms to analyze user input, extract relevant information, and match symptoms to potential conditions. The architecture may include components such as named entity recognition (NER), intent classification, and dialogue management systems.

---
### 2. Ada Health

<img width="1289" alt="Screenshot 2024-04-28 at 22 22 27" src="https://github.com/tanziltonmoy/Medical-Chatbot-for-Patients/assets/32629216/412bf33f-1187-48de-aa33-b00504beb8bc">


Features: Ada Health is an AI-driven health assessment platform that offers personalized symptom analysis and health advice through conversational interactions. Users can describe their symptoms to Ada, and the chatbot will ask relevant questions to gather more information and provide possible explanations and recommendations. Ada Health aims to empower individuals to manage their health proactively and seek appropriate medical care when needed.
Objectives: The main objective of Ada Health is to democratize access to healthcare by leveraging AI technology to deliver comprehensive and reliable health assessments and recommendations to users worldwide. It aims to augment healthcare services, improve health literacy, and promote early intervention and prevention of diseases.
NLP Architecture: Ada Health utilizes a sophisticated NLP architecture consisting of deep learning models, probabilistic algorithms, and medical knowledge bases. It employs techniques like natural language understanding (NLU), sentiment analysis, and probabilistic reasoning to interpret user input, generate hypotheses, and provide personalized health insights. The architecture may incorporate pretrained language models, medical ontologies, and domain-specific knowledge graphs to enhance accuracy and relevance.

---
## Gap Between Related Work

Most existing medical chatbots mainly focus on managing users’ medical history. They are useful for tracking ongoing health conditions, connecting patients with healthcare providers, and organizing past medical records. While these features are helpful for personalized healthcare management, they do not fully address broader healthcare needs such as improving health awareness, analyzing new symptoms accurately, or answering different types of medical questions in detail.

In contrast, this project aims to bridge that gap by focusing not only on medical history but also on improving users’ understanding of their health conditions and symptoms. The chatbot is designed to handle a wide range of medical queries and provide more informative responses. By using advanced language models such as Seq2Seq and GPT-2, the system is able to generate meaningful and context-aware answers. The goal is to create an intelligent and user-friendly chatbot that supports better health awareness, assists in symptom analysis, and encourages proactive healthcare management.

---
## Solution Requirements

- Use advanced Natural Language Processing techniques to accurately understand user questions and generate appropriate responses.
- Connect the system with an updated medical knowledge source to ensure reliable and current information.
- Perform multiple experiments and testing phases to select the best-performing model.
- Provide seamless integration with a web-based application for smooth user interaction.
- Design a simple and user-friendly interface to improve overall user experience and satisfaction

---
## System Architecture (Framework)

<img src="figures/System_Architecture_NLP.png">

## Dataset Information

We have used the MedQuad dataset from : 

- HuggingFace Dataset: [https://huggingface.co/datasets/keivalya/MedQuad-MedicalQnADataset](https://huggingface.co/datasets/keivalya/MedQuad-MedicalQnADataset)

--- 
## Methodology
### 1. Data Collection and Preprocessing

#### Datasets
- Sources: Leverage the MedQuad dataset and supplementary datasets from Huggingface and GitHub.

#### Data Preprocessing 
- We have used the GPT2TokenizerFast from the transformers library to tokenize text efficiently for processing with the GPT-2 model.
- Similarly, for the seq2seq model, we’re using NLTK library for carrying out the tokenization.
- Dataset is further splitted into training, validation and testing pairs on 80%, 10%, and 10% respectively


### 2. Model Development

- We have trained 2 models: Seq2Seq and GPT2.
- Integrate advanced NLP techniques like validation and perplexity,adaptation validation seq2seq for high quality performance.



### 3. Experimental Design

We conducted experiments to train and fine-tune two models, namely GPT-2 and Seq2Seq, for medical question-answering (QA) tasks. Below are the details of the experimental design and hyperparameters used for each model:

#### a. GPT-2 Model:
- Training Data: We utilized a dataset consisting of 143,250 samples for training the GPT-2 model.
- Fine-tuning: The GPT-2 model was fine-tuned on medical QA data to adapt it specifically for medical-related inquiries.
Hyperparameters for Fine-Tuning:
- Evaluation Strategy: Epoch-based evaluation
- Learning Rate: 2e-5
- Weight Decay: 0.01
- Number of Training Epochs: 3

#### b. Seq2Seq Model:
-Training Data: Similar to the GPT-2 model, we used the same dataset containing 143,250 samples for training the Seq2Seq model.
Hyperparameters:
- Hidden Layers: 512
- Number of Iterations: 15,000
- Teacher Forcing Ratio: 0.5
- Learning Rate Encoder: 0.0001
- Learning Rate Decoder: 0.0005
- Optimizer: Adam Optimizer

Both models were trained using these hyperparameters to optimize their performance for medical question-answering tasks. The choice of hyperparameters was based on experimentation and empirical observations to achieve a balance between model complexity, training efficiency, and task-specific requirements. Additionally, the evaluation strategy for both models involved monitoring performance metrics such as accuracy, loss, and convergence over the specified number of training epochs.


### 4. Evaluation

- Apply a suite of metrics, including BLEU, ROGUE.
- Expand evaluation to include precision, recall, and F1-score to gauge the relevance and accuracy of medical advice.

### 5. Result

From comparing the results between the GPT-2 and Seq2Seq models using various evaluation metrics, including BLEU, ROUGE, precision, recall, and F1-score, we observed the following outcomes:

##### GPT-2 Model:
- Achieved better scores across multiple evaluation metrics.
- Demonstrated decent performance overall.
- Showed relatively better human evaluation results compared to the automated metrics.

##### Seq2Seq Model:
- Displayed a decent performance but was outperformed by the GPT-2 model in most evaluation metrics.
- While it produced acceptable results, it did not achieve the same level of effectiveness as the GPT-2 model.
- Human evaluation revealed lower satisfaction compared to the GPT-2 model, suggesting limitations in generating relevant and accurate medical advice.

Overall, the GPT-2 model exhibited better performance across various evaluation metrics, indicating its superiority in generating paraphrases and providing medical advice with higher relevance and accuracy. The Seq2Seq model, while performing decently, fell short in comparison to the GPT-2 model, particularly in terms of human evaluation and certain automated metrics.


## Evaluation Metrics Scores

| SN | Metric | Seq2Seq | GPT2 |
|----|-------|----------|----------|
| 1 | BLUE Score | 0.1875| 0.3056 |
| 2 | ROUGE Score| 0.4170 | 0.3934|
| 3 | Precision  | 0.2648 | 0.3647 |
| 4 | Recall| 0.1485| 0.2485 |
| 5 | F1-Score | 0.1723| 0.2723 |

### 1. BLUE Score:
- The BLUE (Bilingual Evaluation Understudy) score measures the similarity between the generated text and human reference text.
- The Seq2Seq model achieves a BLUE score of 0.1875, indicating moderate similarity.
- In contrast, the GPT2 model achieves a higher BLUE score of 0.3056, indicating closer similarity to human reference text compared to Seq2Seq.

### 2. ROUGE Score:
- The ROUGE (Recall-Oriented Understudy for Gisting Evaluation) score assesses the overlap between the generated text and human reference text in terms of n-grams.
- The Seq2Seq model achieves a ROUGE score of 0.4170, indicating a relatively high overlap.
- However, the GPT2 model's ROUGE score is slightly lower at 0.3934, suggesting a slightly lower overlap with the reference text compared to Seq2Seq.

### 3. Precision:
- Precision measures the proportion of relevant information in the generated text.
- The Seq2Seq model achieves a precision score of 0.2648, indicating that about 26.48% of the generated text is relevant.
- In contrast, the GPT2 model achieves a higher precision score of 0.3647, indicating that about 36.47% of the generated text is relevant, which is notably higher than Seq2Seq.

### 4. Recall:
- Recall measures the proportion of relevant information in the reference text that is captured by the generated text.
- The Seq2Seq model achieves a recall score of 0.1485, indicating that about 14.85% of relevant information from the reference text is captured.
- The GPT2 model achieves a higher recall score of 0.2485, indicating that about 24.85% of relevant information from the reference text is captured, which is notably higher than Seq2Seq.

### 5. F1-Score:
- The F1-score is the harmonic mean of precision and recall, providing a balanced measure of both metrics.
- The Seq2Seq model achieves an F1-score of 0.1723.
- However, the GPT2 model achieves a higher F1-score of 0.2723, indicating better overall performance in terms of both precision and recall compared to Seq2Seq.

In summary, while the Seq2Seq model may excel in certain metrics like ROUGE score, the GPT2 model generally outperforms it across most metrics, including precision, recall, and F1-score, indicating its superior ability to generate text that closely resembles human-written text and captures relevant information from the reference text.

## Human Evaluation
| Category             | Rating (1-5) | Definitions and Criteria                                                                                                   |
|----------------------|--------------|----------------------------------------------------------------------------------------------------------------------------|
| Medical Accuracy     | 1-5          | 1 (Poor): Consistently incorrect, misleading. 2 (Fair): Often inaccurate, lacks detail. 3 (Average): Generally accurate, some errors. 4 (Good): Mostly accurate, minor inaccuracies. 5 (Excellent): Highly accurate, detailed, fully reliable. |
| Guideline Adherence | 1-5          | 1 (Poor): Ignores clinical guidelines. 2 (Fair): Struggles with guidelines, frequent errors. 3 (Average): Generally follows guidelines. 4 (Good): Consistently adheres to guidelines. 5 (Excellent): Perfect adherence, no exceptions. |
| Clarity              | 1-5          | 1 (Poor): Very confusing, unclear. 2 (Fair): Somewhat understandable, uses complex jargon. 3 (Average): Clear with occasional complex language. 4 (Good): Very clear, minimal jargon. 5 (Excellent): Exceptionally clear, straightforward. |
| Empathy              | 1-5          | 1 (Poor): Completely detached, inappropriate. 2 (Fair): Limited empathy, often seems indifferent. 3 (Average): Shows basic empathy, somewhat supportive. 4 (Good): Very empathetic and supportive. 5 (Excellent): Exceptionally empathetic, always supportive. |
| Response Relevance   | 1-5          | 1 (Poor): Responses mostly irrelevant or off-topic. 2 (Fair): Often irrelevant or slightly off-topic. 3 (Average): Mostly relevant, some off-topic responses. 4 (Good): Highly relevant, consistently on-topic. 5 (Excellent): Always relevant, perfectly on-topic. |

| Category             | Rating (1-5) | Evaluator Comments (Doctors' Feedback)                                                                                               |
|----------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Medical Accuracy     | 2            | "Frequently inaccurate or overly generic, lacking specific medical detail."                                                          |
| Guideline Adherence | 2            | "Often fails to follow clinical guidelines, especially in complex cases."                                                            |
| Clarity              | 3            | "Responses are understandable but sometimes use jargon that could confuse patients."                                                   |
| Empathy              | 2            | "Struggles to convey genuine empathy, often comes off as detached."                                                                   |
| Response Relevance   | 2            | "Irrelevant or off-topic responses are common, particularly in nuanced discussions."                                                   |



## Deployment
### Chat Interface Functionality

- Allows users to ask questions, send them, and receive responses from the chatbot.
- Messages are displayed in a visually distinct format, with user messages on the right and bot responses on the left.

<img src="figures/app4.png"> 



---

## Project Management

### Task Distribution
- This project was completed independently, and all responsibilities were handled by a single developer.

| SN | Task                  | Description                                 | Assignee     |
| -- | --------------------- | ------------------------------------------- | ------------ |
| 1  | Data Collection       | Dataset research and selection              | Sachin Kumar |
| 2  | Data Preprocessing    | Cleaning, tokenization, and data splitting  | Sachin Kumar |
| 3  | Model Research        | Study of NLP and deep learning techniques   | Sachin Kumar |
| 4  | Model Training        | Training and fine-tuning GPT-2 and Seq2Seq  | Sachin Kumar |
| 5  | Evaluation            | Performance analysis using standard metrics | Sachin Kumar |
| 6  | Frontend & Backend    | Development of user interface               | Sachin Kumar |
| 7  | Integration & Testing | System integration and testing              | Sachin Kumar |
| 8  | Deployment            | GitHub deployment and system setup          | Sachin Kumar |
| 9  | Documentation         | Preparation of README and project report    | Sachin Kumar |


---

## References  

1. Xia, F. et al. (2022). *MedConQA: Medical Conversational Question Answering System*. EMNLP.  
   https://aclanthology.org/2022.emnlp-demos.15  

2. He, Y. et al. (2020). *Infusing Disease Knowledge into BERT*. EMNLP.  
   https://aclanthology.org/2020.emnlp-main.372  

3. Adhikari, S. et al. *Evaluation of Clinical Question Answering*.  
   https://aclanthology.org/W09-1322.pdf  

4. Phuyal, A. et al. *Incorporating Medical Knowledge in BERT*.  
   https://aclanthology.org/2021.emnlp-main.435  

5. MedQuad Dataset – HuggingFace  
   https://huggingface.co/datasets/keivalya/MedQuad-MedicalQnADataset  