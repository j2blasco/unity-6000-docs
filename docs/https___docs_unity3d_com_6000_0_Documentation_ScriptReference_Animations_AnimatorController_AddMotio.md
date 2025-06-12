* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.AddMotion.html

#  [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).AddMotion
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
## Declaration
public [Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) AddMotion([Motion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Motion.html) motion); 
## Declaration
public [Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) AddMotion([Motion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Motion.html) motion, int layerIndex); 
### Parameters
Parameter | Description  
---|---  
motion | The Motion that will be in the AnimatorState.  
layerIndex | The layer where the Motion will be added.  
### Description
Utility function that creates a new state with the motion in it.
The state asset that is created is added as a sub asset of the state machine to which it is added. This function pushes an Undo operation.
* * *
