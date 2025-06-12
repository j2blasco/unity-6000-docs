* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-applicationIdentifier.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).applicationIdentifier
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
applicationIdentifier; 
### Description
The application identifier for the currently selected build target.
Currently supported by Android, iOS, tvOS and macOS.  
**Changing this only sets the identifier for the currently active platform.** Use [PlayerSettings.SetApplicationIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetApplicationIdentifier.html) and [PlayerSettings.GetApplicationIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetApplicationIdentifier.html) to set and retrieve it for a specific platform. [EditorUserBuildSettings.SwitchActiveBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.SwitchActiveBuildTarget.html) can be used to set the active platform while running the editor, but does not work in batch mode. If running the editor from batch mode you can change the active platform by launching it with this [argument](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html): '-buildTarget platform'.
* * *
