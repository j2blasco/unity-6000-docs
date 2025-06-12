* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-allowHDRDisplaySupport.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).allowHDRDisplaySupport
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
allowHDRDisplaySupport; 
### Description
Prepare the application to encode images for an HDR display.
When you enable `allowHDRDisplaySupport`, the application build includes all the resources, such as shaders, that are required to correctly encode the final output for an HDR display.   
  
Disabling this setting also disables [PlayerSettings.useHDRDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-useHDRDisplay.html) because you cannot use a display in HDR mode without the required resources.   
  
Enable this setting without enabling [PlayerSettings.useHDRDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-useHDRDisplay.html) if you don't want to use the main display in HDR mode, but do want to use an XR Display in HDR mode.   
  
Additional resources: [PlayerSettings.useHDRDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-useHDRDisplay.html).
* * *
