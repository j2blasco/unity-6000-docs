* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.BindAll.html

#  [GameObjectRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html).BindAll
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
public void BindAll([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) target, bool recursive); 
### Parameters
Parameter | Description  
---|---  
target |  [root](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder-root.html) or any of its children.  
recursive | Binds also all the **target** 's children properties when set to `true`.  
### Description
Adds bindings for all of **target** 's properties, and also for all the **target** 's children if **recursive** is `true`.
* * *
