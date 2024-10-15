#!/usr/bin/env python3

"""
    0-main.py
"""

import sys
from bs4 import BeautifulSoup

def check_input_tag(soup, tag_name, tag_attr, tag_attr_value, tag_text):
    """
    Checks if the given tag exists in the HTML document
    """
    tag = soup.find(tag_name, {tag_attr: tag_attr_value})
    if tag is None:
        print(f"There is no {tag_name} tag with attribute '{tag_attr}' = '{tag_attr_value}'")
        return False
    if tag_text is not None and tag.text.strip() != tag_text:
        print(f"The {tag_name} tag with attribute '{tag_attr}' = '{tag_attr_value}' has unexpected text: '{tag.text.strip()}'")
        return False
    return True

def check_attrs(soup, tag_name, attrs):
    """
    Checks if the given tag has the expected attributes
    """
    tag = soup.find(tag_name)
    if tag is None:
        print(f"There is no {tag_name} tag")
        return False
    for attr, value in attrs.items():
        if attr not in tag.attrs:
            print(f"The {tag_name} tag is missing attribute '{attr}'")
            return False
        if tag.attrs.get(attr) != value:
            print(f"The {tag_name} tag has unexpected value for attribute '{attr}': '{tag.attrs.get(attr)}' instead of '{value}'")
            return False
    return True

def check_children(soup, tag_name, children_list):
    """
    Checks if the given tag has the expected children
    """
    tag = soup.find(tag_name)
    if tag is None:
        print(f"There is no {tag_name} tag")
        return False
    for child in children_list:
        child_tag = tag.find(child[0])
        if child_tag is None:
            print(f"The {tag_name} tag is missing child '{child[0]}'")
            return False
        if len(child_tag.attrs.get('class')) != 1 or child[1] != child_tag.attrs.get('class')[0]:
            print(f"The {tag_name} tag is missing child '{child[0]}' with class '{child[1]}'")
            return False
    return True

def check_form_group(soup, fieldset_index, div_index, label_for, label_text):
    """
    Checks if the form-group has the expected elements and attributes
    """
    fieldset = soup.find_all('fieldset')[fieldset_index]
    form_group = fieldset.find_all('div', {'class': 'form-group'})[div_index]
    label = form_group.find('label', {'for': label_for})
    if label is None:
        print(f"There is no label for '{label_for}' in form-group")
        return False
    if label.text.strip() != label_text:
        print(f"The label for '{label_for}' has unexpected text: '{label.text.strip()}'")
        return False
    return True

def check_form_field(soup, fieldset_index, div_index, form_field_container_index, input_type, input_name, input_id, input_placeholder, input_pattern, input_max_length, input_autocomplete, input_accesskey, input_required):
    """
    Checks if the form-field has the expected elements and attributes
    """
    fieldset = soup.find_all('fieldset')[fieldset_index]
    form_group = fieldset.find_all('div', {'class': 'form-group'})[div_index]
    form_field = form_group.find_all('div', {'class': 'form-field'})[0]
    form_field_container = form_field.find_all('span', {'class': 'form-field-container'})[form_field_container_index]
    input_tag = form_field_container.find('input', {'type': input_type})
    if input_tag is None:
        print(f"There is no input with type '{input_type}'")
        return False
    if input_tag.attrs.get('name') != input_name:
        print(f"The input has unexpected name: '{input_tag.attrs.get('name')}' instead of '{input_name}'")
        return False
    if input_tag.attrs.get('id') != input_id:
        print(f"The input has unexpected id: '{input_tag.attrs.get('id')}' instead of '{input_id}'")
        return False
    if input_tag.attrs.get('placeholder') != input_placeholder:
        print(f"The input has unexpected placeholder: '{input_tag.attrs.get('placeholder')}' instead of '{input_placeholder}'")
        return False
    if input_tag.attrs.get('pattern') != input_pattern:
        print(f"The input has unexpected pattern: '{input_tag.attrs.get('pattern')}' instead of '{input_pattern}'")
        return False
    if input_tag.attrs.get('maxlength') != input_max_length:
        print(f"The input has unexpected maxlength: '{input_tag.attrs.get('maxlength')}' instead of '{input_max_length}'")
        return False
    if input_tag.attrs.get('autocomplete') != input_autocomplete:
        print(f"The input has unexpected autocomplete: '{input_tag.attrs.get('autocomplete')}' instead of '{input_autocomplete}'")
        return False
    if input_tag.attrs.get('accesskey') != input_accesskey:
        print(f"The input has unexpected accesskey: '{input_tag.attrs.get('accesskey')}' instead of '{input_accesskey}'")
        return False
    if input_tag.attrs.get('required') != input_required:
        print(f"The input has unexpected required: '{input_tag.attrs.get('required')}' instead of '{input_required}'")
        return False
    return True

def check_form_help(soup, fieldset_index, div_index, form_help_text):
    """
    Checks if the form-help has the expected text
    """
    fieldset = soup.find_all('fieldset')[fieldset_index]
    form_group = fieldset.find_all('div', {'class': 'form-group'})[div_index]
    form_help = form_group.find('p', {'class': 'form-help'})
    if form_help is None:
        print(f"There is no form-help in form-group")
        return False
    if form_help.text.strip() != form_help_text:
        print(f"The form-help has unexpected text: '{form_help.text.strip()}' instead of '{form_help_text}'")
        return False
    return True

def check_form_icon(soup, fieldset_index, div_index, form_field_container_index):
    """
    Checks if the form-icon is present after the input in form-field-container
    """
    fieldset = soup.find_all('fieldset')[fieldset_index]
    form_group = fieldset.find_all('div', {'class': 'form-group'})[div_index]
    form_field = form_group.find_all('div', {'class': 'form-field'})[0]
    form_field_container = form_field.find_all('span', {'class': 'form-field-container'})[form_field_container_index]
    icon_tag = form_field_container.find('i', {'class': 'form-field-icon'})
    if icon_tag is None:
        print(f"There is no form-field-icon in form-field-container")
        return False
    if icon_tag.text.strip() != "":
        print(f"The form-field-icon has unexpected text: '{icon_tag.text.strip()}'")
        return False
    return True


def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: ./0-main.py <HTML_FILE>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    # Check if there is a i tag after input tag
    print(f"there is a i tag after input tag: {check_input_tag(soup, 'i', 'class', 'form-field-icon', None)}")

    # Check if i tag is empty
    print(f"i tag is empty: {check_input_tag(soup, 'i', 'class', 'form-field-icon', '')}")

    # Form-group: First Name
    if not check_form_group(soup, 0, 0, 'your-first-name', 'First Name'):
        sys.exit(1)
    if not check_form_field(soup, 0, 0, 0, 'text', 'your-first-name', 'your-first-name', 'e.g. Mike', '[A-Za-zÀ-ž\s]{3,}', '35', 'on', 'f', 'required'):
        sys.exit(1)
    if not check_form_help(soup, 0, 0, 'First name should be at least 3 characters and only contains letters.'):
        sys.exit(1)
    if not check_form_icon(soup, 0, 0, 0):
        sys.exit(1)

    # Form-group: Last Name
    if not check_form_group(soup, 0, 1, 'your-last-name', 'Last Name'):
        sys.exit(1)
    if not check_form_field(soup, 0, 1, 0, 'text', 'your-last-name', 'your-last-name', 'e.g. Smith', '[A-Za-zÀ-ž\s]{3,}', '40', 'on', 'l', 'required'):
        sys.exit(1)
    if not check_form_help(soup, 0, 1, 'Last name should be at least 3 characters and only contains letters.'):
        sys.exit(1)
    if not check_form_icon(soup, 0, 1, 0):
        sys.exit(1)

    # Form-group: Email
    if not check_form_group(soup, 0, 2, 'your-email', 'Email'):
        sys.exit(1)
    if not check_form_field(soup, 0, 2, 0, 'email', 'your-email', 'your-email', 'e.g. youremail@gmail.com', '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', '55', 'on', 'e', 'required'):
        sys.exit(1)
    if not check_form_icon(soup, 0, 2, 0):
        sys.exit(1)

    # Form-group: Title
    if not check_form_group(soup, 1, 0, 'your-title', 'Title'):
        sys.exit(1)
    if not check_form_field(soup, 1, 0, 0, 'text', 'your-title', 'your-title', 'e.g. I loved that article', '[A-Za-zÀ-ž\s]{4,}', '75', 'on', 't', 'required'):
        sys.exit(1)
    if not check_form_help(soup, 1, 0, 'Title should be at least 4 characters and only contains letters.'):
        sys.exit(1)
    if not check_form_icon(soup, 1, 0, 0):
        sys.exit(1)

    # Form-group: Comment
    if not check_form_group(soup, 1, 1, 'your-comment', 'Comment'):
        sys.exit(1)
    if not check_form_field(soup, 1, 1, 0, 'textarea', 'your-comment', 'your-comment', 'Write your comment here', None, None, None, 'c', 'required'):
        sys.exit(1)
    if not check_form_help(soup, 1, 1, 'Comment should be at least 10 characters.'):
        sys.exit(1)
    if not check_form_icon(soup, 1, 1, 0):
        sys.exit(1)

    # Check for post-comments section
    postcomm_section = soup.find('section', {'class': 'post-comments'})
    if postcomm_section is None:
        print(f"There is no section with class 'post-comments'")
        sys.exit(1)

    # Check if post-comments section has expected structure
    if len(postcomm_section.attrs.get('class')) != 1 or 'post-comments' != postcomm_section.attrs.get('class')[0]:
        print(f"The section with class 'post-comments' has unexpected classes: '{postcomm_section.attrs.get('class')}'")
        sys.exit(1)

    # Check for form element
    form_element = postcomm_section.find('form')
    if form_element is None:
        print(f"There is no form in the post-comments section")
        sys.exit(1)

    # Check for button element
    button_element = form_element.find('button')
    if button_element is None:
        print(f"There is no button in the form")
        sys.exit(1)
    if button_element.text.strip() != 'Post my comment':
        print(f"The button has unexpected text: '{button_element.text.strip()}' instead of 'Post my comment'")
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()