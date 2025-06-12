* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html

# Microphone
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Microphone.html "Go to Microphone Component in the Manual")
### Description
Use this class to record to an [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) using a connected microphone.
You can get a list of connected microphones from the [devices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone-devices.html) property and then use the [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.Start.html) and [End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.End.html) functions to start or end a recording session using one of the available devices.  
  
**Note:** Microphone is not supported in the Unity Web player.
### Static Properties
Property | Description  
---|---  
[devices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone-devices.html) | A list of available microphone devices, identified by name.  
### Static Methods
Method | Description  
---|---  
[End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.End.html) | Stops recording.  
[GetDeviceCaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.GetDeviceCaps.html) | Get the frequency capabilities of a device.  
[GetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.GetPosition.html) | Get the position in samples of the recording.  
[IsRecording](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.IsRecording.html) | Query if a device is currently recording.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.Start.html) | Start Recording with device.  
* * *
