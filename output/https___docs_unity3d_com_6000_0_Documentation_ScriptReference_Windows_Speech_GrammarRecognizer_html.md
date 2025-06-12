* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.GrammarRecognizer.html

# GrammarRecognizer
class in UnityEngine.Windows.Speech
/
Inherits from:[Windows.Speech.PhraseRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.html)
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
The GrammarRecognizer is a complement to the KeywordRecognizer. In many cases developers will find the KeywordRecognizer fills all their development needs. However, in some cases, more complex grammars will be better expressed in the form of an xml file on disk. The GrammarRecognizer uses Extensible Markup Language (XML) elements and attributes, as specified in the World Wide Web Consortium (W3C) Speech Recognition Grammar Specification (SRGS) Version 1.0. These XML elements and attributes represent the rule structures that define the words or phrases (commands) recognized by speech recognition engines.
For more information on this format, refer to [www.w3.org/TR/speech-grammar](http://www.w3.org/TR/speech-grammar/) or on MSDN.  
  
There can be many grammar recognizers active at any given point in time, but no two grammar recognizers may use the same grammar file.  
  
Grammar recognizer is currently functional only on Windows 10.
### Properties
Property | Description  
---|---  
[GrammarFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.GrammarRecognizer.GrammarFilePath.html) | Returns the grammar file path which was supplied when the grammar recognizer was created.  
### Constructors
Constructor | Description  
---|---  
[GrammarRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.GrammarRecognizer-ctor.html) | Creates a grammar recognizer using specified file path and minimum confidence.  
### Inherited Members
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
