from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import BufferControl
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import Lexer
import os

keywords = ["display", "loop", "fun", "call", "get", "import", "pause", "/loop", "/fun","export","del","var"]
symbols = {'>': '#ffffff','<': '#00ffff','=': '#ffcc00','+': '#ff0000','-': '#00ffcc','*': '#ff00ff','/': '#00ffff',".":"#ffff00",'-':'#ffff00'}
style = Style.from_dict({'keyword': '#ff0066','number': '#ffaa00','text': '#00ff00','background': 'bg:#000000',**{f"symbol_{ord(k)}": v for k, v in symbols.items()}})

class MyLexer(Lexer):
    def lex_document(self, document):
        def get_line(lineno):
            line = document.lines[lineno]
            tokens = []
            word = ""
            for ch in line:
                if ch == ' ':
                    if word:
                        tokens.extend(self.process_word(word))
                        word = ""
                    tokens.append(('class:text', ' '))
                elif ch in symbols:
                    if word:
                        tokens.extend(self.process_word(word))
                        word = ""
                    tokens.append((f'class:symbol_{ord(ch)}', ch))
                else:
                    word += ch
            if word:
                tokens.extend(self.process_word(word))
            return tokens
        return get_line
    def process_word(self, word):
        if word in keywords:
            return [('class:keyword', word)]
        elif word.isdigit():
            return [('class:number', word)]
        else:
            return [('class:text', word)]

def editor(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            text = f.read()
    else:
        text = ""
    buffer = Buffer()
    buffer.text = text
    bindings = KeyBindings()
    @bindings.add('c-s')
    def save_and_exit(event):
        with open(filename, "w") as f:
            f.write(buffer.text)
        event.app.exit()
    @bindings.add('c-c')
    def exit_without_save(event):
        event.app.exit()
    @bindings.add('backspace')
    def delete_char(event):
        b = event.app.current_buffer
        if b.cursor_position > 0:
            b.delete_before_cursor()
            b.insert_text(' ', fire_event=False)
            b.cursor_position -= 1
    root_container = HSplit([Window(content=BufferControl(buffer=buffer, lexer=MyLexer(), focus_on_click=True))])
    app = Application(layout=Layout(root_container),key_bindings=bindings,mouse_support=True,full_screen=True,style=style)
    app.run()