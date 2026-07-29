from blessed import Terminal
import platform
import sys
import time

term = Terminal()


def write(text):
    sys.stdout.write(text)


def flush():
    sys.stdout.flush()


class TerminalUI:
    def __init__(self, title='Maxetui the ui that maxetow loves', subtitle='Press 1-3 for actions, Q to quit'):
        self.title = title
        self.subtitle = subtitle
        self.panels = {}
        self.active_key = None
        self.last_message = 'Choose a menu item to begin.'
        self.last_size = (term.width, term.height)

    def register_panel(self, key, title, message, content_builder):
        self.panels[key] = {
            'title': title,
            'message': message,
            'content_builder': content_builder,
        }

    def draw_border(self):
        width = term.width
        height = term.height
        horizontal = '─' * (width - 2)

        write(term.home + term.bold_blue('┌' + horizontal + '┐'))
        for y in range(1, height - 1):
            write(term.move_xy(0, y) + term.bold_blue('│'))
            write(term.move_xy(width - 1, y) + term.bold_blue('│'))
        write(term.move_xy(0, height - 1) + term.bold_blue('└' + horizontal + '┘'))

    def fill_background(self):
        width = term.width
        height = term.height
        blank = ' ' * (width - 2)
        for y in range(1, height - 1):
            write(term.move_xy(1, y) + term.on_black(blank))

    def draw_header(self):
        inner_width = term.width - 2
        title_text = f' {self.title} '
        subtitle_text = self.subtitle

        write(term.move_xy(1, 1) + term.on_blue(' ' * inner_width))
        write(term.move_xy((term.width - len(title_text)) // 2, 1) + term.on_blue(term.white(term.bold(title_text))))
        write(term.move_xy(1, 2) + term.on_black(' ' * inner_width))
        write(term.move_xy((term.width - len(subtitle_text)) // 2, 2) + term.blue(term.bold(subtitle_text)))

    def draw_menu(self):
        menu_start = 5
        panel_x, _ = self.panel_metrics()
        sidebar_width = panel_x - 3

        for row in range(menu_start, term.height - 4):
            write(term.move_xy(2, row) + term.on_black(' ' * sidebar_width))

        write(term.move_xy(4, menu_start) + term.yellow(term.bold('Menu')) + term.on_black(' ' * (sidebar_width - 6)))
        for key, panel in self.panels.items():
            self.draw_menu_option(key, panel['title'], self.active_key == key, sidebar_width)

    def draw_menu_option(self, key, title, active, sidebar_width):
        menu_start = 5
        label = f'{key}. {title}'
        padded = label.ljust(sidebar_width - 4)
        style = term.green if active else term.white
        write(term.move_xy(6, menu_start + int(key) * 2) + term.on_black(style(padded)))

    def draw_footer(self):
        footer = 'Reusable terminal UI template for future projects'
        ts = time.strftime('%Y-%m-%d %H:%M:%S')
        write(term.move_xy(4, term.height - 3) + term.cyan(footer))
        write(term.move_xy(term.width - len(ts) - 4, term.height - 3) + term.magenta(ts))

    def panel_metrics(self):
        panel_x = min(36, max(24, term.width // 2))
        panel_width = max(20, term.width - panel_x - 5)
        return panel_x, panel_width

    def build_panel_lines(self, active_key, message):
        if active_key in self.panels:
            return self.panels[active_key]['content_builder'](message)

        return [
            'Welcome! Choose a menu item to see more information.',
            '',
            'Use the numbered keys for quick actions.',
            '',
            'Register your own panels to adapt this UI for a new project.',
        ]

    def draw_panel(self, active_key, message):
        panel_x, panel_width = self.panel_metrics()
        write(term.move_xy(panel_x, 5) + term.bold_underline('Details') + term.on_black(' ' * (panel_width - len('Details'))))

        lines = self.build_panel_lines(active_key, message)
        for offset, line in enumerate(lines):
            write(term.move_xy(panel_x, 7 + offset) + term.white_on_black(str(line).ljust(panel_width)[:panel_width]))

        for row in range(7 + len(lines), term.height - 4):
            write(term.move_xy(panel_x, row) + term.on_black(' ' * panel_width))

    def refresh_screen(self):
        write(term.clear())
        self.draw_border()
        self.fill_background()
        self.draw_header()
        self.draw_menu()
        self.draw_panel(self.active_key, self.last_message)
        self.draw_footer()
        flush()

    def update_footer(self):
        ts = time.strftime('%Y-%m-%d %H:%M:%S')
        footer = 'Maxetui'
        footer_line = footer.ljust(max(0, term.width - len(ts) - 8))
        write(term.move_xy(4, term.height - 3) + term.on_black(term.cyan(footer_line)) + term.normal)
        write(term.move_xy(term.width - len(ts) - 4, term.height - 3) + term.magenta(ts))
        flush()

    def build_demo_panels(self):
        self.register_panel(
            '1',
            'System Status',
            'A clean starting point for dashboards, tools, and admin UIs.',
            lambda message: [
                message,
                '',
                f'Python Version: {platform.python_version()}',
                f'Platform: {platform.system()} {platform.release()}',
                f'Interpreter: {platform.python_implementation()}',
            ],
        )
        self.register_panel(
            '2',
            'Environment Info',
            'This layout is ready to be customized for your own app.',
            lambda message: [
                message,
                '',
                f'System: {platform.platform()}',
                f'Executable: {sys.executable}',
                f'Current Directory: {sys.path[0]}',
            ],
        )
        self.register_panel(
            '3',
            'Quick Demo',
            'Resize the terminal and the layout will adapt automatically.',
            lambda message: [
                message,
                '',
                'Try resizing the terminal to see the layout adapt.',
                'This UI updates every second and responds to key presses.',
            ],
        )

    def run(self):
        self.build_demo_panels()

        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            self.refresh_screen()
            while True:
                key = term.inkey(timeout=1)
                current_size = (term.width, term.height)

                if current_size != self.last_size:
                    self.last_size = current_size
                    self.refresh_screen()
                    continue

                if not key:
                    self.update_footer()
                    continue

                if key.lower() == 'q':
                    write(term.clear())
                    write(term.move_xy((term.width - 12) // 2, term.height // 2) + term.bold_red('Exiting...'))
                    break

                if key in self.panels:
                    previous_key = self.active_key
                    self.active_key = key
                    self.last_message = self.panels[key]['message']
                    sidebar_width = self.panel_metrics()[0] - 3

                    if previous_key:
                        self.draw_menu_option(previous_key, self.panels[previous_key]['title'], False, sidebar_width)
                    self.draw_menu_option(self.active_key, self.panels[self.active_key]['title'], True, sidebar_width)
                    self.draw_panel(self.active_key, self.last_message)
                    self.update_footer()


def main():
    app = TerminalUI()
    app.run()


if __name__ == '__main__':
    main()