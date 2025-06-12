* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognitionSystem.OnError.html

#  [PhraseRecognitionSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognitionSystem.html).OnError
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
### Parameters
Parameter | Description  
---|---  
value | Delegate that will be invoked when the event occurs.  
### Description
Event that gets invoked when phrase recognition system encounters an error.
If any errors occurred due to issues the user can fix (e.g. the microphone being unavailable), you should tell the user to correct the issue. In this example, you should show a message asking the user to reconnect the microphone and then attempt to restart the phrase recognition system.
* * *
