* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController-enableOverlapRecovery.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).enableOverlapRecovery
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html "Go to CharacterController Component in the Manual")
enableOverlapRecovery; 
### Description
Enables or disables overlap recovery. Enables or disables overlap recovery. Used to depenetrate character controllers from static objects when an overlap is detected.
Overlap recovery can be used to depenetrate character controllers (CCTs) from static objects when an overlap is detected. This can happen in three main cases:  
  
- when the CCT is directly spawned or teleported in another object  
  
- when the CCT algorithm fails due to limited FPU accuracy  
  
- when the "up vector" is modified, making the rotated CCT shape overlap surrounding objects  
  
When activated, the CCT module will automatically try to resolve the penetration, and move the CCT to a safe place where it does  
  
not overlap other objects anymore. This only concerns static objects, dynamic objects are ignored by overlap recovery.  
  
When overlap recovery is not activated, it is possible for the CCTs to go through static objects. By default, overlap recovery is enabled.  
  
Overlap recovery currently works with all geometries except heightfields.
* * *
