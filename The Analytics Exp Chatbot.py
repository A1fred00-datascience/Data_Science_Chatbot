import openai
import gradio as gr

openai.api_key = 'your-openai-api-key'

def process_input(user_input, previous_conversation):
    if user_input.strip():
        conversation = previous_conversation + f"\nUser: {user_input}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a Data Scientist with 30+ years of expertise."},
                          {"role": "user", "content": conversation}]
            )
            reply = response.choices[0].message['content']
            conversation += f"\nBot: {reply}"
            return reply, conversation
        except Exception as e:
            return f"An error occurred: {e}", conversation
    return "", previous_conversation

demo = gr.Interface(
    fn=process_input,
    inputs=[gr.Textbox(label="Your Question"), gr.Textbox(label="Conversation History", default="")],
    outputs=[gr.Textbox(label="ChatGPT Response"), gr.Textbox(label="Updated Conversation History")],
    title="The Analytics Experience Chatbot",
    description="""
        <img src='https://drive.google.com/uc?export=view&id=1cjNqLD0rKkgSjO54D-LI1dvlIOA9Ioa8' alt='Logo' style='height: 100px; width: 100px; border-radius: 50%; border: 2px solid white; display: block; margin-left: auto; margin-right: auto;' />
        <p>Type your data science related question below and get a response. / Escribe una pregunta de Data Science y obten una respuesta.</p>
    """,
    theme="default"
)

demo.launch(share=True)
