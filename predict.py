# Your Python code goes here
import pickle
model=pickle.load(open('spam_model.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))
def predict_spam(text):
  text_vec=vectorizer.transform([text])
  prediction=model.predict(text_vec)

  return "Spam" if prediction[0]==1 else "Not Spam"

while True:
  msg=input("Enter your message: ")
  print("prediction:",predict_spam(msg))

  stop=input("Do you want to stop? (y/n)")
  if stop.lower()=='y':
    break
