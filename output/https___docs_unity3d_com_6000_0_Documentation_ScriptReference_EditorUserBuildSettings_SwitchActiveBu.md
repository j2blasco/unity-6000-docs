* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.SwitchActiveBuildTarget.html

#  [EditorUserBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.html).SwitchActiveBuildTarget
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
**Obsolete** Please use SwitchActiveBuildTarget(BuildTargetGroup targetGroup, BuildTarget target).
## Declaration
public static bool SwitchActiveBuildTarget([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target); 
## Declaration
public static bool SwitchActiveBuildTarget([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) targetGroup, [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target); 
## Declaration
public static bool SwitchActiveBuildTarget([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) namedBuildTarget, [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target); 
### Parameters
Parameter | Description  
---|---  
target | Target build platform.  
targetGroup | Build target group.  
namedBuildTarget | Target named build platform.  
### Returns
**bool** True if the build target was successfully switched, false otherwise (for example, if license checks fail, files are missing, or if the user has cancelled the operation via the UI). 
### Description
Select a new build target to be active.
When changing the active build target, this function reimports Assets that are affected by the current platform settings, and then returns true if the operation completed successfully. All script files are compiled on the next editor update. To have scripts compile before the Assets are reimported, refer to [SwitchActiveBuildTargetAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.SwitchActiveBuildTargetAsync.html).  
  
If the given target is a standalone target, calling SwitchActiveBuildTarget will also affect [EditorUserBuildSettings.selectedStandaloneTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-selectedStandaloneTarget.html).  
  
**Note** : This method isn't available when running the Editor in [batch mode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html). Changing the build target requires recompiling script code for the given target, which can't be done while script code is executing. This isn't a problem in the Editor, as the operation is deferred to the next Editor update. However, in batch mode the Editor will stop after executing the designated script code, so deferring the operation isn't possible. To set the build target to use in batch mode, use the [buildtarget](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html) command-line argument.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SwitchPlatformExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) Platform")]
    public static void PerformSwitch()
    {
        // Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) to Windows standalone build.
        EditorUserBuildSettings.SwitchActiveBuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.SwitchActiveBuildTarget.html)(BuildTargetGroup.Standalone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.Standalone.html), BuildTarget.StandaloneWindows[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneWindows.html));
    }
}

```

* * *
