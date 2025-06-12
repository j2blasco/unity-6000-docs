* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.CopyAnimationStreamMotion.html

#  [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html).CopyAnimationStreamMotion
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
public void CopyAnimationStreamMotion([Animations.AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) animationStream); 
### Parameters
Parameter | Description  
---|---  
animationStream | The source animation stream with the motion to deep copy.  
### Description
Deep copies motion from a source animation stream to the current animation stream.
The copied motion includes velocity, angular velocity, and other hidden velocity properties such as avatar foot velocity.
* * *
