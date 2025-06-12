* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetPlatformIcons.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetPlatformIcons
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
public static PlatformIcon[] GetPlatformIcons([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, [PlatformIconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html) kind); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
kind | Each platform supports a different set of [icon kinds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html). These can be found in the specific platform namespace (for example [iOSPlatformIconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.iOSPlatformIconKind.html).  
### Description
Gets the list of available icon slots for the specified build target and [kind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html).
If you use [PlayerSettings.SetPlatformIcons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetPlatformIcons.html) to set icons, Unity needs to retrieve each icon's build target and [icon kind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html)."
* * *
**Obsolete** Use GetPlatformIcons(NamedBuildTarget , PlatformIconKind) instead.
## Declaration
public static PlatformIcon[] GetPlatformIcons([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) platform, [PlatformIconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html) kind); 
### Parameters
Parameter | Description  
---|---  
platform | The full list of platforms that support this API and the supported icon kinds can be found in [icon kinds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html).  
kind | Each platform supports a different set of [icon kinds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html). These can be found in the specific platform namespace (for example [iOSPlatformIconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.iOSPlatformIconKind.html)).  
### Description
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
