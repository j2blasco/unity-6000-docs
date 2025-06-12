* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetBounciness.html

#  [ModifiableContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.html).GetBounciness
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
public float GetBounciness(int i); 
### Parameters
Parameter | Description  
---|---  
i | Index of the contact point.  
### Returns
**float** Bounciness value for the specified contact point. 
### Description
Get the restitution value for the specified contact point in this contact pair.
Restitution value specifies how bouncy the surfaces at the specified contact point are.  
  
Bounciness of 0 means absolutely not bouncy at all (all the kinetic energy is lost at contact). A value of 1 means all the kinetic energy (and then some due to computational errors) will be conserved. Because of that, normally, bounciness is somewhere in between 0 and 1.
* * *
