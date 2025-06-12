* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-isStatic.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).isStatic
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
isStatic; 
### Description
Whether there are any Static Editor Flags set for the GameObject.
Returns `true` if any [StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html) are set. Returns `false` if no Static Editor Flags are set.  
  
Set to `true` to enable all Static Editor Flags. Set to `false` to disable all Static Editor Flags.  
  
Static Editor Flags determine which Unity systems consider a GameObject as static, and include the GameObject in their precomputations in the Unity Editor. Setting StaticEditorFlags at runtime has no effect on these systems.  
  
For more information, refer to [ Unity Manual documentation on Static Editor Flags](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html).  
  
Additional resources: [StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html), [GameObjectUtility.SetStaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html).
* * *
