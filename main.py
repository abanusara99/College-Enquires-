#Author -- ABAnusara199
import nltk
import tkinter as tk
import logo
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
     [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["My name is ABAS bot", "I'm Bot, nice to meet you!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good", "I'm fine"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"i am fine",
        ["Great to hear that", "Awesome!"]
    ],    
    [
        r"what is college admission process?",
        ["The college admission process usually involves submitting an application, transcripts, test scores, and other required materials. Then, you may need to attend an interview or complete other assessments. After that, the college will notify you of their admission decision."]
    ],
    [
        r"when does college enrollment start?",
        ["College enrollment typically starts in the spring for the fall semester and in the fall for the spring semester. It's best to check with your chosen college for specific dates."]
    ],

    [
        r"quit",
        ["Goodbye! Have a great day!"],
    ],
]

def chatbot_gui():
    root = tk.Tk()
    root.geometry("400x500")
    root.title("College Enquiries Chatbot")
    root.configure(bg="cyan")
    
    nltk_chatbot = Chat(pairs, reflections)
    
    frame = tk.Frame(root)
    frame.pack()
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    text_box = tk.Text(frame, height=15, width=50, yscrollcommand=scrollbar.set,background="light gray", font=("Arial", 10, "bold"))
    text_box.pack()
    
    scrollbar.config(command=text_box.yview)
    
    entry_field = tk.Entry(root, width=50)
    entry_field.pack()
    
    def send_message(*args):
        user_input = entry_field.get()
        text_box.insert(tk.END, "You: " + user_input + "\n", "right")
        response = nltk_chatbot.respond(user_input)
        text_box.insert(tk.END, "Chatbot: " + response + "\n", "left")
        entry_field.delete(0, tk.END)
    
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()
    
    root.bind("<Return>", send_message)
    
    root.mainloop()

if __name__ == "__main__":
    chatbot_gui()
