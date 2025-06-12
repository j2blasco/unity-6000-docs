* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetIcons.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetIcons
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
## Declaration
public static Texture2D[] GetIcons([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, [IconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IconKind.html) kind); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
kind | The [IconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IconKind.html).  
### Description
Returns the list of assigned icons for the specified build target.
Unity enables you to specify multiple icon textures for each platform.  
  
Each texture in the returned array corresponds to an entry in the list of icon sizes returned by GetIconSizesForTargetGroup. By default, [[GetIcons(NamedBuildTarget,IconKind)]] returns all icons for a platform unless you specify an [IconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IconKind.html) value. Only iOS supports icons which have a different kind than [IconKind.Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IconKind.Application.html).
* * *
