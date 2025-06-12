* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetApplicationIdentifier.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetApplicationIdentifier
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
public static string GetApplicationIdentifier([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
### Returns
**string** Returns the application identifier associated with a [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html). 
### Description
Get the application identifier for the specified platform.
The location of the application identifier in the build output depends on the platform build target. On iOS, tvOS and Mac OS X platforms, the identifier is written to the 'CFBundleIdentifier' field in the info.plist file. This file is created and placed in the build output folder when the Unity project is built. Additionally, on Mac OS X, the bundle identifier can be found in the info.plist file in the final .app file, after finishing the Xcode build process. On Android the identifier is saved to the 'package' field in the AndroidManifest.xml file.
* * *
**Obsolete** Use GetApplicationIdentifier(NamedBuildTarget buildTarget) instead.
## Declaration
public static string GetApplicationIdentifier([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) targetGroup); 
### Description
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
