# CSS Selectors

## Fixing some quarto+plotly render problems:
See this [campuswire thread](https://campuswire.com/c/GE12A81FB/feed/54)

Some additional things:
1. Make sure you have `Jupyter Notebook Renderers` vscode extension installed.
2. Don't just return the figures, plot them!
    Change:

    ```
    f() #f is a function that returns figure object
    ```
    To:
    ````
    fig = f()
    fig.show(renderer="notebook")                    
    ```
3. Don't use jupyter notebook/lab's render function. Use `quarto render <notebook>.ipynb`
4. Google your errors! Debug using stackoverflow threads and github issues.


# CSS Selectors Activity:
CSS Diner: https://flukeout.github.io/

# CSS Selectors in Scrapy:
1. Run `scrapy shell 'https://quotes.toscrape.com/page/1/'`
2. "response" object contains the webpage
3. response.css('<selector>').get() or response.css('<selector>').getall()
3. Play with different `<selector>`s
4. Read the scrapy tutorial for more: https://docs.scrapy.org/en/latest/intro/tutorial.html

## Some pointers:
1. Selecting attributes like href: `attr(href)`
1. Selecting attributes like style: `attr(style)`

# CSS Selectors on the browser
1. Press Option + ⌘ + J (on macOS), or Shift + CTRL + J to open console
2. Type `$$(<css_query>)` to run  a css_query
3. Tip: Press control+l to clear the clutter! (usually works on any console -- OS terminal or browser or vscode)