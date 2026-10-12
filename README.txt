Background service placeholder

No service code is included yet. A proper Android foreground service must:
- show a persistent notification while microphone is active;
- request and handle RECORD_AUDIO permission;
- use Android SpeechRecognizer or another supported speech API;
- obey Android background microphone restrictions and user consent;
- stop cleanly when the user taps Stop.

This file is intentionally a note rather than fake service code. The starter app
does not continuously listen with the screen off.
