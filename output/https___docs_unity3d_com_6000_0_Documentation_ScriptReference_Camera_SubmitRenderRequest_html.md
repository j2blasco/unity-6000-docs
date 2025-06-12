* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SubmitRenderRequest.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).SubmitRenderRequest
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
## Declaration
public void SubmitRenderRequest(RequestData renderRequest); 
### Parameters
Parameter | Description  
---|---  
renderRequest | RequestData.  
### Description
Submit a renderRequest.
Call this method via ScriptableRenderer.SubmitRenderRequest. Use ScriptableRenderer.SupportsRenderRequest to check if the active render pipeline supports the `RequestData` type you selected.  
  
The UniversalRenderPipeline supports:  
  
- ScriptableRenderer.StandardRequest, which renders a full URP camera stack and outputs the result to the given target. You can only call this request on Base Cameras. - UniversalRenderPipeline.SingleCameraRequest, which renders a single URP camera and outputs the result to the given target.  
  
The HDRenderPipeline supports ScriptableRenderer.StandardRequest, which renders a single HDRP camera without [Arbitrary Output Variables](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/AOVs.html) (AOVs) and outputs the result to the given target. It uses a separate camera history from the render loop, to ensure temporal effects are consistent.  
  
Refer to [Render requests](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest/index.html?subfolder=/manual/User-Render-Requests.html) for more information about render requests in scriptable render pipelines (SRPs).
* * *
