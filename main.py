from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from urllib.parse import quote_plus
import webbrowser

Window.clearcolor = get_color_from_hex("#101522")

class ShahidAssistant(App):
    def build(self):
        self.title = "SHAHID AI ASSISTANT"
        root = BoxLayout(orientation="vertical", padding=dp(16), spacing=dp(10))
        root.add_widget(Label(
            text="[b]SHAHID AI ASSISTANT[/b]",
            markup=True, font_size="24sp", size_hint_y=None, height=dp(65)
        ))
        self.status = Label(
            text="Ready — تیار ہوں", font_size="18sp",
            size_hint_y=None, height=dp(50)
        )
        root.add_widget(self.status)
        self.result = Label(text="Type a command below.", font_size="16sp")
        root.add_widget(self.result)
        self.command = TextInput(
            hint_text="Type: youtube, google, whatsapp, or a search",
            multiline=False, size_hint_y=None, height=dp(52)
        )
        self.command.bind(on_text_validate=self.run_command)
        root.add_widget(self.command)
        self.add_button(root, "Start voice recognition", self.start_voice)
        self.add_button(root, "Run typed command", self.run_command)
        self.add_button(root, "YouTube", self.youtube)
        self.add_button(root, "Google", self.google)
        self.add_button(root, "Stop voice recognition", self.stop_voice)
        self.voice_running = False
        return root

    def add_button(self, root, text, callback):
        btn = Button(
            text=text, font_size="17sp", size_hint_y=None, height=dp(52),
            background_normal="", background_color=get_color_from_hex("#245B9E")
        )
        btn.bind(on_press=callback)
        root.add_widget(btn)

    def say(self, text):
        self.result.text = text

    def open_url(self, url):
        try:
            webbrowser.open(url)
            self.say("Opening request sent: " + url)
        except Exception as exc:
            self.say("Error: " + str(exc))

    def youtube(self, *args):
        self.open_url("https://www.youtube.com")

    def google(self, *args):
        self.open_url("https://www.google.com")

    def start_voice(self, *args):
        self.voice_running = True
        self.say(
            "Voice recognition is not connected in this starter project. "
            "The Android speech service must be added and tested in the APK."
        )

    def stop_voice(self, *args):
        self.voice_running = False
        self.say("Voice recognition stopped.")

    def run_command(self, *args):
        original = self.command.text.strip()
        text = original.lower()
        if not text:
            self.say("Please type a command first.")
            return
        if any(x in text for x in ["youtube", "یوٹیوب", "यूट्यूब"]):
            self.youtube()
        elif any(x in text for x in ["google", "گوگل", "गूगल"]):
            self.google()
        elif any(x in text for x in ["whatsapp", "واٹس ایپ", "व्हाट्सएप"]):
            self.open_url("https://www.whatsapp.com")
        elif any(x in text for x in ["facebook", "فیس بک", "फेसबुक"]):
            self.open_url("https://www.facebook.com")
        elif any(x in text for x in ["instagram", "انسٹاگرام", "इंस्टाग्राम"]):
            self.open_url("https://www.instagram.com")
        elif any(x in text for x in ["tiktok", "ٹک ٹاک", "टिकटॉक"]):
            self.open_url("https://www.tiktok.com")
        else:
            self.open_url("https://www.google.com/search?q=" + quote_plus(original))

if __name__ == "__main__":
    ShahidAssistant().run()
