* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetSeparation.html

#  [ModifiableContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.html).GetSeparation
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
public float GetSeparation(int i); 
### Parameters
Parameter | Description  
---|---  
i | Index of the contact point.  
### Returns
**float** The separation at a contact point. 
### Description
Get the separation value at a particular contact point in this contact pair.
Separation shows the distance between the colliders at this contact point. Negative means the colliders overlap each other. Positive means the colliders are still separated.  
  
Note that the physics engine starts generating contact pairs when the distance between is lower than the sum of their respective [Collider.contactOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-contactOffset.html).
* * *
