import unittest
from bs4 import BeautifulSoup
from web_scraping import (
    remove_attributes,
    promote_single_child_elements,
    remove_empty_elements,
)


class TestHtmlFunctions(unittest.TestCase):

    def setUp(self):
        # Sample HTML for testing
        self.html_input = """
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
            <a href="some" class="button" style="some custom css"><p stroke="small" stroke-width="1px"></p></a>
          </body>
        </html>
        """

    def test_clean_html(self):
        html_output = remove_attributes(self.html_input)
        soup = BeautifulSoup(html_output, "lxml")
        # Check if unwanted attributes are removed
        for attr in [
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
        ]:
            self.assertIsNone(soup.find(attrs={attr: True}))

    def test_promote_single_child_elements(self):
        html_output = promote_single_child_elements(self.html_input)
        soup = BeautifulSoup(html_output, "html.parser")

        # Check if single-child elements have been promoted
        self.assertIsNone(soup.find(id="child1"))
        self.assertIsNone(soup.find(id="child2"))
        self.assertEqual(len(soup.find_all(id="parent1")), 1)
        self.assertEqual(len(soup.find_all(id="grandchild1")), 1)

    def test_remove_empty_elements(self):
        html_output = remove_empty_elements(self.html_input)
        soup = BeautifulSoup(html_output, "html.parser")
        # Check if empty elements are removed
        self.assertEqual(len(soup.find("p")), 1)


if __name__ == "__main__":
    unittest.main()
