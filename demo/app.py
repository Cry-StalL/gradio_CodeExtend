
import gradio as gr
from gradio_codeextend import CodeExtend


example = CodeExtend().example_value()

demo = gr.Interface(
    lambda x:x,
    CodeExtend(language="vue"),  # interactive version of your component
    CodeExtend(language="vue"),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
