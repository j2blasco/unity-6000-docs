* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetMaxImpulse.html

#  [ModifiableContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.html).SetMaxImpulse
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
public void SetMaxImpulse(int i, float value); 
### Parameters
Parameter | Description  
---|---  
i | Index of the contact point.  
value | The maximum impulse that can be applied.  
### Description
Set the maximum impulse that the solver can apply at a particular contact point in this contact pair.
Note that setting zero maximum impulse will be the same as disabling the contact point.
* * *
