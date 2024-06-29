import re
from xml_helper import get_all_text


def detect_bullet_point(string):
    """e.g. •"""
    if any(char in string.strip() for char in ['•','●','●','●','●']):
        return True
    return False

def detect_style_from_string(string):
    def detect_emphasis_capitalization(string):
        """Seen in amazon's 2024 10k e.g. We Have Foreign Exchange Risk"""
        words = string.split()
        if not words:
            return False
        for word in words:
            if word.lower() in ["of",'to','a','and','by','in','the','or','on','for']:
                continue
            if not word[0].isupper():
                return False
        return True
    
    def detect_item(string):
        """e.g. Item 1A. Risk Factors"""
        match = re.search(r"^Item\s+\d+[A-Z]{0,}",string, re.IGNORECASE)
        if match:
            return True
        return False
        
    def level_detection(string):
        """e.g. amazon Level 1"""
        match = re.search(r"^Level\s+\d+",string)
        if match:
            return True
        return False
        

    def note_detection(string):
        """e.g. Note 1"""
        match = re.search(r"^Note\s+\d+",string, re.IGNORECASE)
        if match:
            return True
        return False
    
    def all_caps(string):
        """e.g. FORM 10-K SUMMARY"""
        if string.isupper():
            return True
        return False
    
    
    if detect_emphasis_capitalization(string):
        return 'emphasis;'
    elif detect_item(string):
        return 'item;'
    elif level_detection(string):
        return 'level;'
    elif all_caps(string):
        return 'all caps;'
    elif note_detection(string):
        return 'note;'
    elif detect_bullet_point(string):
        return 'bullet point;'
    else:
        return ''
    
def detect_style_from_element(element):
    def detect_bold_from_css(element):
        """Detects bold from css"""
        if element.get('style'):
            if 'font-weight:bold' in element.get('style'):
                return 'font-weight:bold;'
            # change to be any font weight greater than 400
            elif 'font-weight:700' in element.get('style'):
                return 'font-weight:700;'
        return ''
    
    def detect_underline_from_css(element):
        """Detects underline from css"""
        if element.get('style'):
            if 'text-decoration:underline' in element.get('style'):
                return 'text-decoration:underline;'
        return ''
    
    def detect_italic_from_css(element):
        """Detects italic from css"""
        if element.get('style'):
            if 'font-style:italic' in element.get('style'):
                return 'font-style:italic;'
        return ''
    
    ["strong","b","em","i","u"]
    def detect_special_from_html(element):
        """Detects special from html"""
        if element.tag == 'b':
            return 'bold-tag;'
        elif element.tag == 'i':
            return 'italic-tag;'
        elif element.tag == 'u':
            return 'underline-tag;'
        elif element.tag == 'em':
            return 'emphasis-tag;'
        elif element.tag == 'strong':
            return 'strong-tag;'
        
        return ''
    
    # check it or descendants have text
    text = get_all_text(element).strip()
    if len(text) == 0:
        return ''

    
    style = ''
    style += detect_bold_from_css(element)
    style += detect_underline_from_css(element)
    style += detect_italic_from_css(element)
    style += detect_special_from_html(element)
    return style
    

# needs work 
def detect_table(table):
    """Detects if table or header disguised as a table"""
    if table.tag != 'table':
        return False
    text = get_all_text(table)

    if detect_bullet_point(text):
        return False
    number_count = len(re.findall(r'\d', text))
    if number_count > 5:
        return True
    
    char_count = len(text)
    if char_count > 400:
        return True
    
    return False


def detect_table_of_contents(element):
    toc_type = 'not-toc'
    """Detects if a table is likely to be a table of contents."""

    # toc - needs seperate parser if no links
    num_items = len(re.findall('Item(\s+|$|\n)', get_all_text(element), re.IGNORECASE))
    if num_items > 9:
        toc_type = 'toc'

    # linked toc
    # links = element.find_all('a')
    # if len(links) > 5:
    #     toc_type = 'toc-links'

    return toc_type

def detect_toc_link(node):
    """Detects if a node is a table of contents link."""
    if node.tag == 'a':
        text = get_all_text(node)
        if text.lower() in ['table of contents','toc']:
            return True
    return False

def detect_link(node):
    """Detects if a node is a link."""
    if node.tag == 'a':
        return True
    return False

def detect_image(node):
    """Detects if a node is an image."""
    if node.tag == 'img':
        return True
    return False