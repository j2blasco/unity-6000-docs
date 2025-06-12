* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarBuilder.BuildHumanAvatar.html

#  [AvatarBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarBuilder.html).BuildHumanAvatar
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
public static [Avatar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Avatar.html) BuildHumanAvatar([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, [HumanDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription.html) humanDescription); 
### Parameters
Parameter | Description  
---|---  
go | Root object of your transform hierachy. It must be the top most gameobject when you create the avatar.  
humanDescription | Humanoid description of the avatar.  
### Returns
**Avatar** Returns the Avatar, you must always always check the avatar is valid before using it with [Avatar.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Avatar-isValid.html). 
### Description
Create a humanoid avatar.
The avatar is created using the supplied HumanDescription object which specifies the muscle space range limits and retargeting parameters like arm/leg twist and arm/leg stretch. Additional resources: [HumanDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription.html).
* * *
