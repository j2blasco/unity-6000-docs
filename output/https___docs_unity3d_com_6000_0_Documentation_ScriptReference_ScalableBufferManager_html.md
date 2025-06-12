* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager.html

# ScalableBufferManager
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Scales render textures to support dynamic resolution if the target platform/graphics API supports it.
The `ScalableBufferManager` class handles the scaling of any render textures that you have marked as `DynamicallyScalable` when `ResizeBuffers` is called. All render textures marked as `DynamicallyScalable` are scaled by a width and height scale factor. The scale is controlled through a scale factor and not with a specific width and height value because even though render textures are of different sizes, they need to be scaled by a common factor.   
  
The current implementation only supports discrete scale factors in the range of 0.05 and 1.0 in steps of 0.05 to be consistent across all platforms. Unity automatically selects the closest supported scale factors. You can access the selected scale factors using [ScalableBufferManager.widthScaleFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager-widthScaleFactor.html) and [ScalableBufferManager.heightScaleFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager-heightScaleFactor.html).  
  
The scaled dimensions are calculated as follows:  
  
width = ceil(renderTexture.width * ScalableBufferManager.widthScaleFactor) height = ceil(renderTexture.height * ScalableBufferManager.heightScaleFactor)  
  
The render textures that you have marked as `DynamicallyScalableExplicit` are not scaled by a call to `ResizeBuffers` but by a call to `RenderTexture.ApplyDynamicScale`. Scaling is subject to the exact same process as `ResizeBuffers`. 
### Static Properties
Property | Description  
---|---  
[heightScaleFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager-heightScaleFactor.html) | Height scale factor to control dynamic resolution.  
[widthScaleFactor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager-widthScaleFactor.html) | Width scale factor to control dynamic resolution.  
### Static Methods
Method | Description  
---|---  
[ResizeBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager.ResizeBuffers.html) | Function to resize all buffers marked as DynamicallyScalable.  
* * *
