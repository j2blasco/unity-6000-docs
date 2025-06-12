* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager.ResizeBuffers.html

#  [ScalableBufferManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager.html).ResizeBuffers
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
public static void ResizeBuffers(float widthScale, float heightScale); 
### Parameters
Parameter | Description  
---|---  
widthScale | New scale factor for the width that the ScalableBufferManager uses to resize all render textures that are marked as `DynamicallyScalable`. The value should be greater than 0.0, and less than or equal to 1.0  
heightScale | New scale factor for the height that the ScalableBufferManager uses to resize all render textures that are marked as `DynamicallyScalable`. The value should be greater than 0.0, and less than or equal to 1.0.  
### Description
Function to resize all buffers marked as DynamicallyScalable.
Takes in new width and height scale and stores and applies it to all render textures marked as DynamicallyScalable. Note that the scale is applied to the render textures original dimensions so a scale factor of 1.0 will always be the full dimensions for the specified render target, etc.  
  
Vulkan and DirectX 12 only allow uniform scaling through the utilization of widthScale.
* * *
