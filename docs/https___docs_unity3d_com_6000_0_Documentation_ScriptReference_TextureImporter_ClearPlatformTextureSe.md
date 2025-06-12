* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.ClearPlatformTextureSettings.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).ClearPlatformTextureSettings
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
## Declaration
public void ClearPlatformTextureSettings(string platform); 
### Parameters
Parameter | Description  
---|---  
platform | The platform whose settings are to be cleared (see below).  
### Description
Clears specific target platform settings.
Refer to [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) for a list of valid platforms. To get the name of a platform as a string, use the `TargetName` property. For example, `UnityEditor.Build.NamedBuildTarget.Standalone.TargetName`.
* * *
