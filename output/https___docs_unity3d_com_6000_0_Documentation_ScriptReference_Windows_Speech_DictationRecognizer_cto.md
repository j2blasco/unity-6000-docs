* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer-ctor.html

# DictationRecognizer Constructor
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
public DictationRecognizer(); 
## Declaration
public DictationRecognizer([Windows.Speech.ConfidenceLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.ConfidenceLevel.html) confidenceLevel); 
## Declaration
public DictationRecognizer([Windows.Speech.DictationTopicConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationTopicConstraint.html) topic); 
## Declaration
public DictationRecognizer([Windows.Speech.ConfidenceLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.ConfidenceLevel.html) minimumConfidence, [Windows.Speech.DictationTopicConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationTopicConstraint.html) topic); 
### Parameters
Parameter | Description  
---|---  
minimumConfidence | The confidence level at which the recognizer will begin accepting phrases.  
topic | The dictation topic that this dictation recognizer should optimize its recognition for.  
### Description
Create a DictationRecognizer with the specified minimum confidence and dictation topic constraint. Phrases under the specified minimum level will be ignored.
Default confidence level is Medium. Default dictation topic constraint is Dictation.
* * *
