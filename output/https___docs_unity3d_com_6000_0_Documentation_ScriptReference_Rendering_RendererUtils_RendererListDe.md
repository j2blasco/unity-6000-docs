* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererUtils.RendererListDesc.ConvertToParameters.html

#  [RendererListDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererUtils.RendererListDesc.html).ConvertToParameters
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
public static [Rendering.RendererListParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams.html) ConvertToParameters(ref [Rendering.RendererUtils.RendererListDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererUtils.RendererListDesc.html) desc); 
### Returns
**RendererListParams** If the RendererListDesc is valid, this returns a [RendererListParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams.html) struct. Otherwise, this returns [RendererListParams.Invalid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams.Invalid.html). 
### Description
Convert a given RendererListDesc to a [RendererListParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams.html) struct with equivalent parameters.
Additional resources: [RendererListParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams.html), [ScriptableRenderContext.CreateRendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.CreateRendererList.html)
* * *
