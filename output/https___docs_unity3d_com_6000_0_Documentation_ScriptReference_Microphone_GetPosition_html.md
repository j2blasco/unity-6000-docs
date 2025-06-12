* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.GetPosition.html

#  [Microphone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html).GetPosition
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
## Declaration
public static int GetPosition(string deviceName); 
### Parameters
Parameter | Description  
---|---  
deviceName | The name of the device.  
### Description
Get the position in samples of the recording.
If you pass a null or empty string for the device name then the default microphone will be used. You can get a list of available microphone devices from the [devices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone-devices.html) property.  
  
You can use this to control latency. If you want a 30ms latency, poll GetPosition() until 30ms (in samples) has gone and then start the audio.
* * *
