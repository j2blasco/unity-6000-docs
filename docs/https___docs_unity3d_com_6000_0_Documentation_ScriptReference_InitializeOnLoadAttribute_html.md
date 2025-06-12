* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadAttribute.html

# InitializeOnLoadAttribute
class in UnityEditor
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
### Description
Allows you to initialize an Editor class when Unity loads, and when your scripts are recompiled.
Static constructors with this attribute are called when scripts in the project are recompiled (also known as a [Domain Reload](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html)). This happens when Unity first loads your project, but also when Unity detects modifications to scripts (depending on your [Auto Refresh preferences](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html)), and when you enter Play Mode (depending on your [Play Mode configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode.html)).  
  
Asset operations such as asset loading should be avoided in InitializeOnLoad methods. InitializeOnLoad methods are called before asset importing is completed and therefore the asset loading can fail resulting in a null object. To do initialization after a domain reload which requires asset operations use the [AssetPostprocessor.OnPostprocessAllAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessAllAssets.html) callback. This callback supports all asset operations and has a parameter signaling if there was a domain reload.  
  
Additional resources: [running editor code on launch](https://docs.unity3d.com/6000.0/Documentation/Manual/running-editor-code-on-launch.html).
* * *
