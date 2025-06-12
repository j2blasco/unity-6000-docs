* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Normalize.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).Normalize
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Quaternion.html "Go to Quaternion Component in the Manual")
## Declaration
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) Normalize([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) q); 
### Description
Converts this quaternion to a quaternion with the same orientation but with a magnitude of 1.0.
Note that this method changes the current quaternion. If you want to keep the current quaternion unchanged, use the [normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-normalized.html) property instead.  
  
If this quaternion is too small to be normalized it will be set to [Quaternion.identity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html).  
  
Additional resources: [normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-normalized.html) variable.
* * *
