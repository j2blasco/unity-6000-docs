* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetDynamicFriction.html

#  [ModifiableContactPair](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.html).SetDynamicFriction
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
public void SetDynamicFriction(int i, float dynamicFriction); 
### Parameters
Parameter | Description  
---|---  
i | Index of the contact point.  
dynamicFriction | Dynamic friction coefficient.  
### Description
Set the value of the dynamic friction for a specified contact point in this contact pair.
Dynamic friction slows down bodies that are sliding over other bodies.  
  
Normally, it is between 0 and 1.
* * *
