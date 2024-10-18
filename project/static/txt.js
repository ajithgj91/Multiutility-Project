// Check if browser supports speech synthesis
if ('speechSynthesis' in window) {
  const speakButton = document.getElementById('speak-button');
  const textToSpeak = document.getElementById('text-to-speak');

  speakButton.addEventListener('click', () => {
      const text = textToSpeak.value.trim();
      if (text !== '') {
          // Create a new instance of SpeechSynthesisUtterance
          const utterance = new SpeechSynthesisUtterance(text);

          // Speak the text
          speechSynthesis.speak(utterance);
      } else {
          alert('Please enter some text to speak.');
      }
  });
} else {
  alert('Sorry, your browser does not support speech synthesis.');
}
// Check if the browser supports the Web Speech API
if ('webkitSpeechRecognition' in window) {
  const startStopBtn = document.getElementById('startStopBtn');
  const transcriptArea = document.getElementById('transcript');
  let recognition = new webkitSpeechRecognition();
  let isRecording = false;

  // Configure the recognition object
  recognition.continuous = true; // Keep listening until stopped
  recognition.interimResults = false; // Show only final results
  recognition.lang = 'en-US'; // Set language

  // Start recording
  startStopBtn.addEventListener('click', () => {
      if (isRecording) {
          recognition.stop();
          startStopBtn.textContent = 'Start Recording';
          isRecording = false;
      } else {
          recognition.start();
          startStopBtn.textContent = 'Stop Recording';
          isRecording = true;
      }
  });

  // Handle the results
  recognition.onresult = (event) => {
      let transcript = '';
      for (let i = event.resultIndex; i < event.results.length; ++i) {
          transcript += event.results[i][0].transcript;
      }
      transcriptArea.value = transcript;
  };

  // Handle errors
  recognition.onerror = (event) => {
      console.error(event.error);
      startStopBtn.textContent = 'Start Recording';
      isRecording = false;
  };
} else {
  alert('Web Speech API is not supported in this browser.');
}
