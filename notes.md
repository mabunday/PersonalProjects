### PyCharm Docstrings

When you define a function, PyCharm can autocomplete the docstring (documentation string) for you
How to: On the line right below a function definition: 

1.
def example_function(a,b,c):
----> *insert triple pairs of double quotation marks here*
2.
def example_function(a,b,c):
----> """*With your cursor in the middle of them (no spaces) hit enter to insert a new line*""""
3. 
The doc string should auto-generate. If you search "docstring" in preferences/settings and go to "Python Integrated Tools" you can change the format of the doc string. For your file I used "numpy", but you can use Google or whatever else, too. 