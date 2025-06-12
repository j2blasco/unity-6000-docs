* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest-forcePlayerLoopUpdate.html

#  [AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html).forcePlayerLoopUpdate
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
forcePlayerLoopUpdate; 
### Description
In the Editor, defines whether the Player loop is updated while the GPU request is in flight.
Defaults value: true. If true, forces the Player loop to be updated until the GPU request is fulfilled. This guarantees that the request is completed as fast as possible, but if a new [AsyncGPUReadback.Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.Request.html) is issued every frame, the Editor will never go into the idle state. If false, the Player loop is not forced to update, so the Editor is able to enter the idle state immediately after this request. The request might not finish until the Editor wakes up again, for example, when the Scene view camera is moved or an inspector property changes. 
* * *
