* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.HasInvokeOnRenderObjectCallbacks.html

#  [ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html).HasInvokeOnRenderObjectCallbacks
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
public bool HasInvokeOnRenderObjectCallbacks(); 
### Returns
**bool** True if there are OnRenderObject callbacks false if none. 
### Description
Check if any objects in the scene have OnRenderObject callbacks registered.
You can use this function to check if InvokeOnRenderObjectCallback will actually call any callbacks. This can be usefull to avoid calling InvokeOnRenderObjectCallback. It als means no arbitrary code will run in the callbacks that could change graphics state. This can help your renderpipeline to avoid doing unececarry graphics state changes before/after the callbacks.
* * *
