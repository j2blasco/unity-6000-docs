* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.GetContact.html

#  [Collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html).GetContact
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
public [ContactPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html) GetContact(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the contact to retrieve.  
### Returns
**ContactPoint** The contact at the specified `index`. 
### Description
Gets the contact point at the specified `index`.
You can retrieve individual contacts for this collision by `index`. You can use [contactCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision-contactCount.html) to determine how many contacts are available.  
  
Additional resources: [contactCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision-contactCount.html) and [GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.GetContacts.html).
* * *
