
import gradio as gr
from app import demo as app
import os

_docs = {'CodeExtend': {'description': 'Creates a code editor for viewing code (as an output component), or for entering and editing code (as an input component).', 'members': {'__init__': {'value': {'type': 'str | Callable | None', 'default': 'None', 'description': 'Default value to show in the code editor. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'language': {'type': 'Literal[\n        "python",\n        "c",\n        "cpp",\n        "markdown",\n        "json",\n        "html",\n        "css",\n        "javascript",\n        "jinja2",\n        "typescript",\n        "yaml",\n        "dockerfile",\n        "shell",\n        "r",\n        "sql",\n        "sql-msSQL",\n        "sql-mySQL",\n        "sql-mariaDB",\n        "sql-sqlite",\n        "sql-cassandra",\n        "sql-plSQL",\n        "sql-hive",\n        "sql-pgSQL",\n        "sql-gql",\n        "sql-gpSQL",\n        "sql-sparkSQL",\n        "sql-esper",\n        "go",\n        "java",\n        "liquid",\n        "php",\n        "rust",\n        "scss",\n        "vue",\n        "xml",\n    ]\n    | None', 'default': 'None', 'description': 'The language to display the code as. Supported languages listed in `gr.Code.languages`.'}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': 'Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.'}, 'inputs': {'type': 'Component | Sequence[Component] | set[Component] | None', 'default': 'None', 'description': 'Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.'}, 'lines': {'type': 'int', 'default': '5', 'description': 'Minimum number of visible lines to show in the code editor.'}, 'max_lines': {'type': 'int | None', 'default': 'None', 'description': 'Maximum number of visible lines to show in the code editor. Defaults to None and will fill the height of the container.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'the label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'Whether user should be able to enter code or only view it.'}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}, 'wrap_lines': {'type': 'bool', 'default': 'False', 'description': 'If True, will wrap lines to the width of the container when overflow occurs. Defaults to False.'}}, 'postprocess': {'value': {'type': 'str | None', 'description': 'Expects a `str` of code.'}}, 'preprocess': {'return': {'type': 'str | None', 'description': 'Passes the code entered as a `str`.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the CodeExtend changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'input': {'type': None, 'default': None, 'description': 'This listener is triggered when the user changes the value of the CodeExtend.'}, 'focus': {'type': None, 'default': None, 'description': 'This listener is triggered when the CodeExtend is focused.'}, 'blur': {'type': None, 'default': None, 'description': 'This listener is triggered when the CodeExtend is unfocused/blurred.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'CodeExtend': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_codeextend`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

Python library for easily interacting with trained machine learning models
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_codeextend
```

## Usage

```python

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

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `CodeExtend`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["CodeExtend"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["CodeExtend"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes the code entered as a `str`.
- **As output:** Should return, expects a `str` of code.

 ```python
def predict(
    value: str | None
) -> str | None:
    return value
```
""", elem_classes=["md-custom", "CodeExtend-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          CodeExtend: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
