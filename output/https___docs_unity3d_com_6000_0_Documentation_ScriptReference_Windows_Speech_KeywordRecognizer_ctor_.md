* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.KeywordRecognizer-ctor.html

# KeywordRecognizer Constructor
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
public KeywordRecognizer(string[] keywords); 
## Declaration
public KeywordRecognizer(string[] keywords, [Windows.Speech.ConfidenceLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.ConfidenceLevel.html) minimumConfidence); 
### Parameters
Parameter | Description  
---|---  
keywords | The keywords that the recognizer will listen to.  
minimumConfidence | The minimum confidence level of speech recognition that the recognizer will accept.  
### Description
Create a KeywordRecognizer which listens to specified keywords with the specified minimum confidence. Phrases under the specified minimum level will be ignored.
If no minimum confidence level is specified, then the confidence level is assumed to be Medium.
* * *
