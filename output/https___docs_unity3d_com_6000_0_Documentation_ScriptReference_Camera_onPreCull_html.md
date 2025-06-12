* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPreCull.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).OnPreCull()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
### Description
[Event function](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html) that Unity calls before a Camera culls the scene.
In the Built-in Render Pipeline, Unity calls `OnPreCull` on MonoBehaviours that are attached to the same GameObject as an enabled Camera component, just before performing the culling operation that determines what that Camera can see. For a full description and code example, see [MonoBehaviour.OnPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreCull.html).  
  
For similar functionality that does not require the script to be on the same GameObject as a Camera component, see [Camera.onPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreCull.html).  
  
If you're using a Scriptable Render Pipeline, for example the Universal Render Pipeline, use [RenderPipelineManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html) instead.
* * *
