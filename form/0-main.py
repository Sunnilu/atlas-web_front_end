#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET

def main():
    """
    Check if the post-comments section is a sibling of the post div.
    """

    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
    body = root.find('.//body')

    post_div = body.find('.//div[@class="post"]')
    post_comments_section = body.find('.//section[@class="post-comments"]')

    if post_comments_section is not None and post_div is not None:
        # Check if they have the same parent (which is the container div)
        if post_comments_section.getparent() == post_div.getparent():
            print('post-comments section is sibling to post div: True')
        else:
            print('post-comments section is sibling to post div: False')
    else:
        print('post-comments section is sibling to post div: False')

if __name__ == '__main__':
    main()