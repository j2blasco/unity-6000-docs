* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ContactEventDelegate.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).ContactEventDelegate
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
public delegate void ContactEventDelegate([PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) scene, ReadOnly<ContactPairHeader> headerArray); 
### Parameters
Parameter | Description  
---|---  
scene | The physics scene that the contacts belong to.  
headerArray | A contact buffer where all the contact data of the previous simulation step is stored.  
### Description
* * *
