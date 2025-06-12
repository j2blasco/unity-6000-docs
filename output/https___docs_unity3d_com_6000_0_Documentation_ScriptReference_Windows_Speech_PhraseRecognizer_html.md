* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.html

# PhraseRecognizer
class in UnityEngine.Windows.Speech
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
A common base class for both keyword recognizer and grammar recognizer.
Phrase recognizer is the smallest speech recognition unit that can be individually started and stopped. Typically, you should create all your phrase recognizers at the start of the Scene, and the start and stop them on demand as needed.
### Properties
Property | Description  
---|---  
[IsRunning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.IsRunning.html) | Tells whether the phrase recognizer is listening for phrases.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.Dispose.html) | Disposes the resources used by phrase recognizer.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.Start.html) | Makes the phrase recognizer start listening to phrases.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.Stop.html) | Stops the phrase recognizer from listening to phrases.  
### Events
Event | Description  
---|---  
[OnPhraseRecognized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.OnPhraseRecognized.html) | Event that gets fired when the phrase recognizer recognizes a phrase.  
### Delegates
Delegate | Description  
---|---  
[PhraseRecognizedDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.PhraseRecognizedDelegate.html) | Delegate for OnPhraseRecognized event.  
* * *
