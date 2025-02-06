---
tags: [gradio-custom-component, Code]
title: gradio_codeextend
short_description: A gradio custom component
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_CodeExtend`
这是一个[Gradio](https://github.com/gradio-app/gradio)的[自定义组件(Custom Component)](https://www.gradio.app/guides/custom-components-in-five-minutes)，基于Gradio中的[Code组件](https://www.gradio.app/docs/gradio/code)修改，增加了若干编程语言的支持。

新增的支持语言：

Go, Java, Rust, SCSS, Vue, XML, PHP, Liquid

---
(以下文档为Gradio自动生成)

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

## `CodeExtend`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
str | Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Default value to show in the code editor. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>language</code></td>
<td align="left" style="width: 25%;">

```python
Literal[
        "python",
        "c",
        "cpp",
        "markdown",
        "json",
        "html",
        "css",
        "javascript",
        "jinja2",
        "typescript",
        "yaml",
        "dockerfile",
        "shell",
        "r",
        "sql",
        "sql-msSQL",
        "sql-mySQL",
        "sql-mariaDB",
        "sql-sqlite",
        "sql-cassandra",
        "sql-plSQL",
        "sql-hive",
        "sql-pgSQL",
        "sql-gql",
        "sql-gpSQL",
        "sql-sparkSQL",
        "sql-esper",
        "go",
        "java",
        "liquid",
        "php",
        "rust",
        "scss",
        "vue",
        "xml",
    ]
    | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The language to display the code as. Supported languages listed in `gr.Code.languages`.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
Timer | float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.</td>
</tr>

<tr>
<td align="left"><code>inputs</code></td>
<td align="left" style="width: 25%;">

```python
Component | Sequence[Component] | set[Component] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.</td>
</tr>

<tr>
<td align="left"><code>lines</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>5</code></td>
<td align="left">Minimum number of visible lines to show in the code editor.</td>
</tr>

<tr>
<td align="left"><code>max_lines</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Maximum number of visible lines to show in the code editor. Defaults to None and will fill the height of the container.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">the label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Whether user should be able to enter code or only view it.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.</td>
</tr>

<tr>
<td align="left"><code>wrap_lines</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, will wrap lines to the width of the container when overflow occurs. Defaults to False.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the CodeExtend changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the CodeExtend. |
| `focus` | This listener is triggered when the CodeExtend is focused. |
| `blur` | This listener is triggered when the CodeExtend is unfocused/blurred. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, passes the code entered as a `str`.
- **As input:** Should return, expects a `str` of code.

 ```python
 def predict(
     value: str | None
 ) -> str | None:
     return value
 ```
 
