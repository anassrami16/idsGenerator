# idsGenerator
generate unique ids for certain html elements

### Requirements
  * python 3
  * bs4 library ``` pip istall bs4 ```
### Generate random ids
* The program take as input the abspath of your directory that contains html template file 
* gives as output the number of elements affected
* Example:
  ```
  python3 ./idgenerator.py [absolute_path_of_your_directory]
  ```
#### Add other html Tags
* you can add other html tags to generate ids for. all you have to do is add your tag to TAGS list inside idgenerator.py
  ```
  # tags that shold be have ids
    TAGS = ['p', 'form', 'a', 'input', 'p', 'h1', 'h2',
            'h3', 'h4', 'h5', 'h6', 'label', 'span', 'select',
            'div', 'button', 'li' , 'img', 'tr' , 'td', 'th', 
            'b' , 'i', 'u', 'strong', 'em', 'ol', 'ul', 'table',
            'thead', 'tbody', 'tfoot', 'caption', 'colgroup',
            'col', 'tr', 'td', 'th', 'img', 'video', 'audio',
            'source', 'track', 'canvas', 'map', 'area', 'svg',
            'math', 'iframe', 'object', 'embed', 'time', 'mark',
            'wbr', 'textarea', 'noscript', 'style', 'script', 'head',
            'title', 'meta', 'link', 'base', 'body', 'html']
  ```
