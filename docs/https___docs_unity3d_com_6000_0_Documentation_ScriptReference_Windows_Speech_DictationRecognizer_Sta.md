* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.Start.html

#  [DictationRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.html).Start
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public void Start(); 
### Description
Starts the dictation recognization session. Dictation recognizer can only be started if PhraseRecognitionSystem is not running.
DictationRecognizer requires that dictation is permitted in the user's Speech privacy policy (Settings->Privacy->Speech, inking & typing). If dictation is not enabled, DictationRecognizer will fail on [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.Start.html). Developers can handle this failure in an app-specific way by providing a [DictationError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationError.html) delegate and testing for SPERR_SPEECH_PRIVACY_POLICY_NOT_ACCEPTED (0x80045509).
* * *
