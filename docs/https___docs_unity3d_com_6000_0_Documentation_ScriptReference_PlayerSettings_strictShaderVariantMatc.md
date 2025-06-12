* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-strictShaderVariantMatching.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).strictShaderVariantMatching
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
strictShaderVariantMatching; 
### Description
Enable strict shader variant matching in the player.
If you enable strict shader variant matching, Unity tries to find an exact match for the combination of enabled local shader keywords and global keyword overrides. If such a variant doesn't exist, Unity uses the error shader and displays an error in the Console. The error states which shader and combination of keywords caused the issue. Otherwise, Unity silently picks the variant that is closest to the requested set of keywords.
* * *
