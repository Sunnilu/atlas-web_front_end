
import sys
from css_parser import parse

def check_paragraph_after_span(html_file):
    """Checks if there is a paragraph (<p>) after the closing span tag 
    within the first form-field div of the first fieldset in the HTML file.
    """
    try:
        # Parse the HTML
        soup = parse(html_file)

        # (Assumed Logic) Find the first fieldset
        fieldset = soup.find('fieldset') 
        if not fieldset:
            raise ValueError("No fieldset found")

        # (Assumed Logic) Find the first form-field div
        form_field_div = fieldset.find('div', class_='form-field')
        if not form_field_div:
            raise ValueError("No form-field div found")

        # Find the span tag
        span_tag = form_field_div.find('span')
        if not span_tag:
            raise ValueError("No span tag found")

        # Check if the next sibling is a paragraph
        p_tag = span_tag.find_next_sibling('p')
        return p_tag is not None  # Returns True if a <p> is found

    except Exception as e:
        print(e) # This could be printing the "unexpected number of fieldsets" error
        return False

if __name__ == "__main__":
    html_file = sys.argv[1]
    result = check_paragraph_after_span(html_file)
    print(f"there is a p after the span: {result}") 