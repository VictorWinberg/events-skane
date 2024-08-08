from html_clean import clean_html
from llm_magic import llm_generate_prompt

MODEL = "qwen2:0.5b"

# Do some web Scaping
# ===> Logic <===
# Example HTML
input_html_str = """
<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Upcoming Events</h1>
    <div class="event">
        <h2>Book Fair</h2>
        <p class="location">Main Library</p>
        <p class="time">August 28, 2024, 9:00 AM</p>
        <p>Discover a wide selection of books and meet local authors at our annual book fair.</p>
    </div>
</body>
</html>
"""

# Pre-processing HTML
output_html = clean_html(input_html_str)

# Run output thru LLM / ML / AI-stuff

# Refining Interaction with LLM
# Prompt Engineering:
# Templates: Create structured prompts that guide the LLM to focus on specific pieces of information.
structured_prompt = f"""
Extract the following details from the HTML code:
Event Name: [Event Name]
Location: [Location]
Date: [Date]
Description: [Description]
Tags: [Tags]
Categories: [Categories]

Event HTML code:
{output_html}
"""

# Post-Processing:
# Use heuristics or additional models to refine the output from the LLM. This could involve correcting common errors, standardizing formats, or further structuring the data.

# Perhaps use sparrow or something make sure to get proper json objects

output_prompt = llm_generate_prompt(model=MODEL, query=structured_prompt)


print(output_prompt["response"])



