* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.SetSpatializerPluginName.html

#  [AudioSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSettings.html).SetSpatializerPluginName
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
public static void SetSpatializerPluginName(string pluginName); 
### Parameters
Parameter | Description  
---|---  
pluginName | The spatializer plugin name.  
### Description
Sets the spatializer plugin for all platform groups. If a null or empty string is passed in, the existing spatializer plugin will be cleared.
This is an Editor-only function. This function will throw an argument exception on an invalid plugin name.
* * *
