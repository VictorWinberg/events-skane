from bs4 import BeautifulSoup


def remove_attributes(html):
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style tags
    attrs_to_remove = [
        "d",
        "version",
        "viewbox",
        "width",
        "height",
        "stroke",
        "stroke-width",
        "transform",
        "class",
        "id",
        "style",
        "fill",
        "fill-rule",
        "xmlns",
        "encoding",
        "aria-hidden",
    ]
    for attr in attrs_to_remove:
        for tag in soup.find_all(attrs={f"{attr}": True}):
            del tag[attr]

    return soup.prettify()


def promote_single_child_elements(html):
    # Parse the HTML content
    soup = BeautifulSoup(html, "html.parser")

    def promote(element):
        # Traverse in reverse order to handle nested elements
        for tag in reversed(list(element.find_all(recursive=False))):
            children = list(tag.find_all(recursive=False))
            if len(children) == 1:
                child = children[0]
                # Preserve the attributes of the parent element
                parent_attributes = tag.attrs
                # Insert the child before the parent element and maintain the parent's attributes
                tag.insert_before(child)
                # Transfer attributes of the parent to the new position if necessary
                if parent_attributes:
                    child.attrs.update(parent_attributes)
                tag.decompose()  # Remove the old tag

    # Start promoting from the body tag
    body = soup.find("body")
    if body:
        promote(body)

    return soup.prettify()  # Return the HTML as a string


def remove_empty_elements(html):
    # Parse the HTML content
    soup = BeautifulSoup(html, "html.parser")

    def is_empty(element):
        # Check if the element is empty or only contains other empty tags, we want to remove script & style tag. But let's keep for now.
        if element.name in ["script", "style"]:
            return False  # Don't consider script and style tags as empty
        # Check if the element is empty but has attributes
        if element.get_text(strip=True) == "" and not any(
            child.name for child in element.children
        ):
            # If it has attributes, it should be preserved
            return not element.attrs
        return False

    def remove_empty(element):
        # Iterate over elements in reverse to handle nested elements correctly
        for tag in reversed(list(element.find_all(recursive=False))):
            if is_empty(tag):
                tag.decompose()
            else:
                # Recursively process child elements
                remove_empty(tag)

    # Start removing empty elements from the body tag
    body = soup.find("body")
    if body:
        remove_empty(body)

    # Return the prettified HTML as a string
    return str(soup.prettify())  # .prettify() returns a formatted HTML string


def pipe(value, *functions):
    for func in functions:
        value = func(value)
    return value


def clean_html(html):

    # Input html into pipe and pass on each method before returning value
    output = pipe(
        input_html_str,
        remove_attributes,
        promote_single_child_elements,
        remove_empty_elements,
    )
    return output


# Example HTML
input_html_str = """
<html>
    <body d="test" viewbox="123">
        <div id="parent1" datetime="2024-04-23" version="2.0">
            <div id="child1" data-info="important value">
                <p>Some content</p>
            </div>
        </div>
        <div id="parent2" width="30px" width="1px">
            <div id="child2">
                <div id="grandchild1" fill="hard" fill-rule="softis">
                    <p>More content</p>
                </div>
            </div>
        </div>
        <p></p>
        <a href="some" class="button" style="some custom css">
            <p stroke="small" stroke-width="1px"></p>
            <p></p>
        </a>
    </body>
</html>

"""

output_html  = clean_html(input_html_str)