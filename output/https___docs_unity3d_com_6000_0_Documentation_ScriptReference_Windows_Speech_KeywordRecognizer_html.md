* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.KeywordRecognizer.html

# KeywordRecognizer
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
KeywordRecognizer listens to speech input and attempts to match uttered phrases to a list of registered keywords.
There can be many keyword recognizers active at any given time, but no two keyword recognizers may be listening for the same keyword.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEngine;
using UnityEngine.Windows.Speech;  
  
public class KeywordScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private string[] m_Keywords;  
  
    private KeywordRecognizer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.KeywordRecognizer.html) m_Recognizer;  
  
    void Start()
    {
        m_Recognizer = new KeywordRecognizer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.KeywordRecognizer.html)(m_Keywords);
        m_Recognizer.OnPhraseRecognized += OnPhraseRecognized;
        m_Recognizer.Start();
    }  
  
    private void OnPhraseRecognized(PhraseRecognizedEventArgs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizedEventArgs.html) args)
    {
        StringBuilder builder = new StringBuilder();
        builder.AppendFormat("{0} ({1}){2}", args.text, args.confidence, Environment.NewLine);
        builder.AppendFormat("\tTimestamp: {0}{1}", args.phraseStartTime, Environment.NewLine);
        builder.AppendFormat("\tDuration: {0} seconds{1}", args.phraseDuration.TotalSeconds, Environment.NewLine);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(builder.ToString());
    }
}

```

Keyword recognizer is currently functional only on Windows 10.
### Properties
Property | Description  
---|---  
[Keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.KeywordRecognizer.Keywords.html) | Returns the list of keywords which was supplied when the keyword recognizer was created.  
### Constructors
Constructor | Description  
---|---  
[KeywordRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.KeywordRecognizer-ctor.html) | Create a KeywordRecognizer which listens to specified keywords with the specified minimum confidence. Phrases under the specified minimum level will be ignored.  
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
