* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.GetReactionTorque.html

#  [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).GetReactionTorque
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
public float GetReactionTorque(float timeStep); 
### Parameters
Parameter | Description  
---|---  
timeStep | The time to calculate the reaction torque for.  
### Returns
**float** The reaction torque of the joint in the specified `timeStep`. 
### Description
Gets the reaction torque of the joint given the specified `timeStep`.
When a joint tries to constrain a Rigidbody2D it may need to apply torque to do so. This is known as the reaction torque.  
  
Additional resources: [reactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-reactionTorque.html), [breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html).
* * *
