* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioRenderer.html

# AudioRenderer
class in UnityEngine
/
Implemented in:[UnityEngine.AudioModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AudioModule.html)
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
Allow recording the main output of the game or specific groups in the AudioMixer.
### Static Methods
Method | Description  
---|---  
[GetSampleCountForCaptureFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioRenderer.GetSampleCountForCaptureFrame.html) | Returns the number of samples available since the last time AudioRenderer.Render was called. This is dependent on the frame capture rate.  
[Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioRenderer.Render.html) | Performs the recording of the main output as well as any optional mixer groups that have been registered via AudioRenderer.AddMixerGroupSink.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioRenderer.Start.html) | Enters audio recording mode. After this Unity will output silence until AudioRenderer.Stop is called.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioRenderer.Stop.html) | Exits audio recording mode. After this audio output will be audible again.  
* * *
