import speech_recognition as sr
import pyttsx3
import time

class VoiceController:
    def __init__(self):
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speaking rate
        
        # Available commands
        self.commands = {
            "play": ["çal", "oynat", "başlat"],
            "stop": ["dur", "durdur", "kapat"],
            "next": ["sonraki", "geç", "ileri"],
            "previous": ["önceki", "geri"],
            "shuffle": ["karıştır", "shuffle"],
            "exit": ["çık", "çıkış", "kapat"]
        }
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for voice commands"""
        with sr.Microphone() as source:
            print("\nDinleniyor... (Sesli komut vermek için konuşun)")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio, language="tr-TR")
                print(f"Söylenen: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                self.speak("Üzgünüm, sizi anlayamadım")
                return None
            except sr.RequestError:
                self.speak("Üzgünüm, ses tanıma servisi şu anda kullanılamıyor")
                return None
    
    def get_command(self):
        """Get and process voice command"""
        text = self.listen()
        if not text:
            return None
            
        # Check for commands
        for command, keywords in self.commands.items():
            if any(keyword in text for keyword in keywords):
                return command
                
        return None
    
    def start_voice_control(self, callback):
        """Start voice control loop"""
        self.speak("Sesli komut sistemi aktif")
        
        while True:
            command = self.get_command()
            if command:
                if command == "exit":
                    self.speak("Sesli komut sistemi kapatılıyor")
                    break
                callback(command) 