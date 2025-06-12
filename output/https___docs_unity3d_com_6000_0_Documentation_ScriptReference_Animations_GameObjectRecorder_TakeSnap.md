* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.TakeSnapshot.html

#  [GameObjectRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html).TakeSnapshot
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
public void TakeSnapshot(float dt); 
### Parameters
Parameter | Description  
---|---  
dt | Delta time.  
### Description
Forwards the animation by **dt** seconds, then record the values of the added bindings.
To add bindings, use the bindings methods: [BindComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.BindComponent.html), [BindComponentsOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.BindComponentsOfType.html), [BindAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.BindAll.html), or [Bind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.Bind.html).  
  
Note that **dt** is not added the first time this function is called so that the clip will start at 0.0f. This means the forwarding only starts on the subsequent calls.
* * *
