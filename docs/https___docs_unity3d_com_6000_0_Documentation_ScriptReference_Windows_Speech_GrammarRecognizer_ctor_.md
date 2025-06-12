* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.GrammarRecognizer-ctor.html

# GrammarRecognizer Constructor
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
public GrammarRecognizer(string grammarFilePath); 
## Declaration
public GrammarRecognizer(string grammarFilePath, [Windows.Speech.ConfidenceLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.ConfidenceLevel.html) minimumConfidence); 
### Parameters
Parameter | Description  
---|---  
grammarFilePath | Path of the grammar file.  
minimumConfidence | The confidence level at which the recognizer will begin accepting phrases.  
### Description
Creates a grammar recognizer using specified file path and minimum confidence.
Note: only one grammar recognizer can be created at a time with the same grammar file.
* * *
