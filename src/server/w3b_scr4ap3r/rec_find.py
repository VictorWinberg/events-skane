from bs4 import BeautifulSoup

# Example HTML content
html_content = '''
<body>
<main>
Hello and welcome to my page
<div class="container">
<p> Hej hej</p>
<p> Hello</p>
<span> Important</span>
<div class="stuff">
<section>Date 1, Malmö, fun event <p>Hi</p></section>
<section>Date 4, Lund, another event <p>Hi</p></section>
<section>Date 43, Malmö, hihi event <p>Hi</p></section>
<section>Date 123123, aksdkjakd, fun event <p>Hi</p></section>
<section>Date 433445, Jamaica, fun event <p>Hi</p></section>
</div>
</div>
</main>
</body>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

def extract_text_from_elements_with_siblings(element: BeautifulSoup, min_count=3):
    """
    Recursively finds and extracts text content from elements with 3 or more siblings of the same type.
    """
    siblings = list(element.find_next_siblings())
    same_type_siblings = [sib for sib in siblings if sib.name == element.name]

    if len(same_type_siblings) >= min_count - 1:  # Current element is not included in the count
        print(element.get_text(strip=True))

    for child in element.find_all(recursive=False):  # Traverse only direct children
        extract_text_from_elements_with_siblings(child, min_count)

# Start recursive extraction from the root
extract_text_from_elements_with_siblings(soup)