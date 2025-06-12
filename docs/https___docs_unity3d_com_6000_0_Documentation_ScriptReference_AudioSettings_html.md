* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.html

# AudioSettings
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSettings.html "Go to AudioSettings Component in the Manual")
### Description
Controls the global audio settings from script.
Setup speaker output and format.
### Static Properties
Property | Description  
---|---  
[driverCapabilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-driverCapabilities.html) | Returns the speaker mode capability of the current audio driver. (Read Only)  
[dspTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-dspTime.html) | Returns the current time of the audio system.  
[outputSampleRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-outputSampleRate.html) | Get the mixer's current output rate.  
[speakerMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings-speakerMode.html) |  AudioSettings.speakerMode is deprecated. Use AudioSettings.GetConfiguration and AudioSettings.Reset to adjust audio settings instead.  
### Static Methods
Method | Description  
---|---  
[GetConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetConfiguration.html) | Returns the current configuration of the audio device and system. The values in the struct may then be modified and reapplied via AudioSettings.Reset.  
[GetDSPBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetDSPBufferSize.html) | Get the mixer's buffer size in samples.  
[GetSpatializerPluginName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetSpatializerPluginName.html) | Returns the name of the spatializer selected on the currently-running platform.  
[GetSpatializerPluginNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.GetSpatializerPluginNames.html) | Returns an array with the names of all the available spatializer plugins.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.Reset.html) | Changes the device configuration and invokes the AudioSettings.OnAudioConfigurationChanged delegate with the argument deviceWasChanged=false. There's no guarantee that the exact settings specified are used, but Unity automatically uses the closest match that it supports. Note: This can cause main thread stalls if AudioSettings.Reset is called when objects are loading asynchronously.   
[SetSpatializerPluginName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.SetSpatializerPluginName.html) | Sets the spatializer plugin for all platform groups. If a null or empty string is passed in, the existing spatializer plugin will be cleared.  
### Events
Event | Description  
---|---  
[OnAudioConfigurationChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.OnAudioConfigurationChanged.html) | Unity calls this event whenever the global audio settings change.  
### Delegates
Delegate | Description  
---|---  
[AudioConfigurationChangeHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.AudioConfigurationChangeHandler.html) | A delegate called whenever the global audio settings are changed, either by AudioSettings.Reset or by an external device change such as the OS control panel changing the sample rate or because the default output device was changed, for example when plugging in an HDMI monitor or a USB headset.  
* * *
