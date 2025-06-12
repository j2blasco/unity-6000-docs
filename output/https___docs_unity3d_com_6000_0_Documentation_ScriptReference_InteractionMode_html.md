* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html

# InteractionMode
enumeration
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
### Description
The mode of interaction, user or automated, that an API method is called with.
Some of Unity’s API methods allow you to specify whether the “interaction mode” is user-driven or automated. This affects whether Unity shows dialog boxes, and whether actions are recorded in the undo history. Automated actions do not record undo or present dialogs. User actions are recorded in the undo history, and may present the user with dialogs. You can only use this setting with methods that accept an InteractionMode parameter.  
  
This is useful if you want to create editor tools or automated processes which perform editor actions.
### Properties
Property | Description  
---|---  
[AutomatedAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.AutomatedAction.html) | Use this setting to prevent a method from showing any dialog boxes to the user, and to prevent it recording to the undo history.  
[UserAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.UserAction.html) | Use this setting to allow a method to show dialog boxes to the user, and to allow it to record to the undo history.  
* * *
