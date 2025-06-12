* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-vulkanEnableSetSRGBWrite.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).vulkanEnableSetSRGBWrite
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
vulkanEnableSetSRGBWrite; 
### Description
Enables Graphics.SetSRGBWrite() on Vulkan renderer.
If enabled, allows toggling sRGB write mode on/off at runtime (this setting is always enabled in the editor). Enabling this setting causes an extra blit when presenting the back buffer, and may cause additional performance degradation, especially on tile-based GPUs. This setting should be kept disabled unless toggling sRGB write mode is required by the application.
* * *
