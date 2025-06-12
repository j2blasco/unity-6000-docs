* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-stripEngineCode.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).stripEngineCode
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
stripEngineCode; 
### Description
Remove unused Engine code from your build (IL2CPP-only).
If this is enabled, unused modules and classes of the Unity Engine codebase will be removed in IL2CPP builds. This will result in smaller binary size. It is recommended to use this setting, however, you may want to disable it if you suspect this causes issues with your project. Note that byte code stripping of managed assemblies is always enabled for the IL2CPP scripting backend.
* * *
