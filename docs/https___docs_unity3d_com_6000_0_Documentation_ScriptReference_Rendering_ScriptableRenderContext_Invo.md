* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.InvokeOnRenderObjectCallback.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).InvokeOnRenderObjectCallback
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
public void InvokeOnRenderObjectCallback(); 
### Description
Schedules an invocation of the OnRenderObject callback for MonoBehaviour scripts.
This method triggers [MonoBehaviour.OnRenderObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnRenderObject.html). Call this function to issue the OnRenderObject callback from your render pipeline. You should typically call this function after the Camera renders the Scene but before adding post-processing.
* * *
