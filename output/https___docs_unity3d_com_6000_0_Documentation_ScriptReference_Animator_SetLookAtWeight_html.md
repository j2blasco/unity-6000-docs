* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetLookAtWeight.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetLookAtWeight
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
public void SetLookAtWeight(float weight); 
## Declaration
public void SetLookAtWeight(float weight, float bodyWeight); 
## Declaration
public void SetLookAtWeight(float weight, float bodyWeight, float headWeight); 
## Declaration
public void SetLookAtWeight(float weight, float bodyWeight, float headWeight, float eyesWeight); 
## Declaration
public void SetLookAtWeight(float weight, float bodyWeight = 0.0f, float headWeight = 1.0f, float eyesWeight = 0.0f, float clampWeight = 0.5f); 
### Parameters
Parameter | Description  
---|---  
weight | (0-1) the global weight of the LookAt, multiplier for other parameters.  
bodyWeight | (0-1) determines how much the body is involved in the LookAt.  
headWeight | (0-1) determines how much the head is involved in the LookAt.  
eyesWeight | (0-1) determines how much the eyes are involved in the LookAt.  
clampWeight | (0-1) 0.0 means the character is unrestrained in motion. 1.0 means the character is clamped (look at becomes impossible). 0.5 means the character is able to move on half of the possible range (180 degrees).  
### Description
Set look at weights.
* * *
