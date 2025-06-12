* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.Update.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).Update
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
public void Update(float deltaTime); 
### Parameters
Parameter | Description  
---|---  
deltaTime | The time delta.  
### Description
Evaluates the animator based on deltaTime.
Updating the animator with this function might not work well with the physics engine or any other system that is normally evaluated by the Game loop.
* * *
