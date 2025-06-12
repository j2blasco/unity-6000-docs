* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-hasModifiableContacts.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).hasModifiableContacts
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
hasModifiableContacts; 
### Description
Specify whether this Collider's contacts are modifiable or not.
All pairs with Colliders that have this flag set will be available to scripts via Physics.ContactModifyEvent.  
  
Note that pairs are only notified to scripts as long as the corresponding bodies are awake. Once they fall asleep, there will no longer be any notification for such pairs.
* * *
