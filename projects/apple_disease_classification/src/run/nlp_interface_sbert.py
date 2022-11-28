from sentence_transformers import SentenceTransformer, util

# import aql.py
 
model = SentenceTransformer('all-MiniLM-L6-v2') 

# retrieve from AQL

sampleBatch = 80

appleScore = 75
blotchApple = 1
rotApple = 1
scabApple = 3
rejectedApple = 5

healthyPercentage = 93.5
blotchPercentage = 1.25
rotPercentage = 1.25
scabPercentage = 2.5
rejectedPercentage = 5

classOne = "Class 1"
classTwo = "Class 2" 
classThree = "Class 3"
classRej = "Rejected"

sentencesOptimized = [
                      f"This batch has been classified as {classOne}.",
                      f"This batch has been classified as {classTwo}.",
                      f"This batch has been classified as {classThree}.",
                      f"This batch has been classified as {classRej}.",
                      "The batch has been rejected.",
                      "The batch is completely unsuitable and will be composted.",
                      f"The batch contains {appleScore} healthy apples, this is {healthyPercentage}% of the total batch.",
                      f"The batch contains {rotApple} rotten apples, this is {rotPercentage}% of the batch.",
                      f"The batch contains {blotchApple} apples with blotch, this is {blotchPercentage}% of the batch.",
                      f"The batch contains {scabApple} apples with scabs, this is {scabPercentage}% of the batch.",
                      f"The batch has been rejected:\n"
                      f"                  With {rotApple} rotten, {blotchApple} blotched and {scabApple} scabbed apples,\n"
                      f"                  a total of {rejectedPercentage}% damage makes the batch completely unsuitable.",
                      f"The percentage of apples with diseases is {rejectedPercentage}.",
                      f"The complete batch consist of {sampleBatch} apples."
                     ]

print("A conversation with Apple Classifying chatbot: Botnita Applebum")  

def chatSbert(): 
    
    questions = 0
    
    while questions < 3:
        query_embedding = input("Botnita Applebum: What would you like to know regarding the tested batch of apples?")
        
        print("\nYou             :", query_embedding)
        
        embeddingsApples = model.encode(sentencesOptimized)
        
        passage_embedding = model.encode(query_embedding, convert_to_tensor=True)
        answer_array = util.dot_score(passage_embedding, embeddingsApples)

        answer_location = answer_array.argmax()

        print("Botnita Applebum:", sentencesOptimized[answer_location.item()])
        questions += 1
        
    print("\nBotnita Applebum: Those are all the questions I can answer today, see you tomorrow!\n"
          "\n                  And remember: An apple a day, keeps the doctor away!\n"
          "                  (unless it is rotten, blotched or scabbed)")  
    
chatSbert() 


