* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.html

# DictationRecognizer
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
DictationRecognizer listens to speech input and attempts to determine what phrase was uttered.
Users can register and listen for hypothesis and phrase completed events. Start() and Stop() methods respectively enable and disable dictation recognition. Once done with the recognizer, it must be disposed using Dispose() method to release the resources it uses. It will release these resources automatically during garbage collection at an additional performance cost if they are not released prior to that.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Windows.Speech;  
  
public class DictationScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Text m_Hypotheses;  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Text m_Recognitions;  
  
    private DictationRecognizer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.html) m_DictationRecognizer;  
  
    void Start()
    {
        m_DictationRecognizer = new DictationRecognizer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.html)();  
  
        m_DictationRecognizer.DictationResult += (text, confidence) =>
        {
            Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("Dictation result: {0}", text);
            m_Recognitions.text += text + "\n";
        };  
  
        m_DictationRecognizer.DictationHypothesis += (text) =>
        {
            Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("Dictation hypothesis: {0}", text);
            m_Hypotheses.text += text;
        };  
  
        m_DictationRecognizer.DictationComplete += (completionCause) =>
        {
            if (completionCause != DictationCompletionCause.Complete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationCompletionCause.Complete.html))
                Debug.LogErrorFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogErrorFormat.html)("Dictation completed unsuccessfully: {0}.", completionCause);
        };  
  
        m_DictationRecognizer.DictationError += (error, hresult) =>
        {
            Debug.LogErrorFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogErrorFormat.html)("Dictation error: {0}; HResult = {1}.", error, hresult);
        };  
  
        m_DictationRecognizer.Start();
    }
}

```

Dictation recognizer is currently functional only on Windows 10, and requires that dictation is permitted in the user's Speech privacy policy (Settings->Privacy->Speech, inking & typing). If dictation is not enabled, DictationRecognizer will fail on [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.Start.html). Developers can handle this failure in an app-specific way by providing a [DictationError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationError.html) delegate and testing for SPERR_SPEECH_PRIVACY_POLICY_NOT_ACCEPTED (0x80045509).
### Properties
Property | Description  
---|---  
[AutoSilenceTimeoutSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.AutoSilenceTimeoutSeconds.html) | The time length in seconds before dictation recognizer session ends due to lack of audio input.  
[InitialSilenceTimeoutSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.InitialSilenceTimeoutSeconds.html) | The time length in seconds before dictation recognizer session ends due to lack of audio input in case there was no audio heard in the current session.  
[Status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.Status.html) | Indicates the status of dictation recognizer.  
### Constructors
Constructor | Description  
---|---  
[DictationRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer-ctor.html) | Create a DictationRecognizer with the specified minimum confidence and dictation topic constraint. Phrases under the specified minimum level will be ignored.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.Dispose.html) | Disposes the resources this dictation recognizer uses.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.Start.html) | Starts the dictation recognization session. Dictation recognizer can only be started if PhraseRecognitionSystem is not running.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.Stop.html) | Stops the dictation recognization session.  
### Events
Event | Description  
---|---  
[DictationComplete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationComplete.html) | Event that is triggered when the recognizer session completes.  
[DictationError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationError.html) | Event that is triggered when the recognizer session encouters an error.  
[DictationHypothesis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationHypothesis.html) | Event that is triggered when the recognizer changes its hypothesis for the current fragment.  
[DictationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationResult.html) | Event indicating a phrase has been recognized with the specified confidence level.  
### Delegates
Delegate | Description  
---|---  
[DictationCompletedDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationCompletedDelegate.html) | Delegate for DictationComplete event.  
[DictationErrorHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationErrorHandler.html) | Delegate for DictationError event.  
[DictationHypothesisDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationHypothesisDelegate.html) | Callback indicating a hypothesis change event. You should register with DictationHypothesis event.  
[DictationResultDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.DictationResultDelegate.html) | Callback indicating a phrase has been recognized with the specified confidence level. You should register with DictationResult event.  
* * *
