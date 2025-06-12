* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-normalized.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).normalized
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
[Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) normalized; 
### Description
Returns this quaternion with a magnitude of 1 (Read Only).
When normalized, a quaternion keeps the same orientation but its magnitude is 1.0.  
  
Note that the current quaternion is unchanged and a new normalized quaternion is returned. If you want to normalize the original quaternion, use the [Normalize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Normalize.html) method instead.  
  
If the quaternion is too small to be normalized [Quaternion.identity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html) will be returned.  
  
Additional resources: [Normalize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Normalize.html) function.
* * *
