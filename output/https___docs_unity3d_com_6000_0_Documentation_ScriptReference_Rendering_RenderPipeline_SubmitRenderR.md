* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.SubmitRenderRequest.html

#  [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html).SubmitRenderRequest
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
public static void SubmitRenderRequest([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, RequestData data); 
### Description
Submit a renderRequest.
This triggers a pipeline render determined by the RequestData type. Use ScriptableRenderer.SupportsRenderRequest to check if the active RenderPipeline supports this RequestData type.  
  
The UniversalRenderPipeline supports: 
  * ScriptableRenderer.StandardRequest, which renders a full URP camera stack and outputs the result to the given target. Can only be called on Base Cameras.
  * UniversalRenderPipeline.SingleCameraRequest, which renders a single URP camera and outputs the result to the given target.


The HDRenderPipeline supports ScriptableRenderer.StandardRequest, which renders a single HDRP camera without [Arbitrary Output Variables](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/AOVs.html) (AOVs) and outputs the result to the given target. It uses a separate camera history from the render loop, to ensure temporal effects are consistent.  
  
Refer to [Render requests](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest/index.html?subfolder=/manual/User-Render-Requests.html) for more information about render requests in scriptable render pipelines (SRPs).  
  
Additional resources: [RenderPipeline.SupportsRenderRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.SupportsRenderRequest.html), RenderPipeline.StandardRequest.
* * *
