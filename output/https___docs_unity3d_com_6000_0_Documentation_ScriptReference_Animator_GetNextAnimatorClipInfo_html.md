* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetNextAnimatorClipInfo.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetNextAnimatorClipInfo
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html "Go to Animator Component in the Manual")
## Declaration
public AnimatorClipInfo[] GetNextAnimatorClipInfo(int layerIndex); 
### Parameters
Parameter | Description  
---|---  
layerIndex | The layer index.  
### Returns
**AnimatorClipInfo[]** An array of all the [AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) in the next state. 
### Description
Returns an array of all the [AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) in the next state of the given layer.
* * *
## Declaration
public void GetNextAnimatorClipInfo(int layerIndex, List<AnimatorClipInfo> clips); 
### Parameters
Parameter | Description  
---|---  
layerIndex | The layer index.  
clips | The list of [AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) to fill.  
### Description
Fills `clips` with the list of all the [AnimatorClipInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorClipInfo.html) in the next state of the given layer.
Additional resources: [GetNextAnimatorClipInfoCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetNextAnimatorClipInfoCount.html).
* * *
