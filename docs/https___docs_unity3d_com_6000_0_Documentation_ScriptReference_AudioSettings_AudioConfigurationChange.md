* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.AudioConfigurationChangeHandler.html

#  [AudioSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.html).AudioConfigurationChangeHandler
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSettings.html "Go to AudioSettings Component in the Manual")
## Declaration
public delegate void AudioConfigurationChangeHandler(bool deviceWasChanged); 
### Parameters
Parameter | Description  
---|---  
deviceWasChanged | True if the change was caused by an device change.  
### Description
A delegate called whenever the global audio settings are changed, either by [AudioSettings.Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html) or by an external device change such as the OS control panel changing the sample rate or because the default output device was changed, for example when plugging in an HDMI monitor or a USB headset.
See [AudioSettings.Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html) for an example.
* * *
