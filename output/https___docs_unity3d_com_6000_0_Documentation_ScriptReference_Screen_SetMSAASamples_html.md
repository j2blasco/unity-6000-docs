* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetMSAASamples.html

#  [Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html).SetMSAASamples
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
public static void SetMSAASamples(int numSamples); 
### Parameters
Parameter | Description  
---|---  
numSamples | Number of anti-aliased samples requested for the screen buffer.  
### Description
Sets the given number of MSAA samples for the screen buffer.
The value indicates the number of anti-aliasing samples per pixel that is requested for the screen buffer. Valid values are 0 (use the Quality settings value), 1, 2, 4, and 8. This function is a low level method that does not affect the rendering state or settings.   
  
If [SystemInfo.supportsMultisampledBackBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampledBackBuffer.html) returns false, the screen buffer doesn't support multisampling and Unity ignores the requested value.   
  
If the graphics API does not support the value you provide, it uses the next highest supported value.  
  
When Unity receives the request, it might not change the number of samples immediately. The exact time when the change happens is platform-dependent. Calling this method early in the frame rendering might have an effect during this frame on some platforms, but might defer to the next frame on other platforms where the switch is done at the end of the frame.  
  
This method is only available when using a Scriptable Render Pipeline (SRP) and will log an error when used with the Built-In Render Pipeline. The method enables the render pipeline to have a limited control of the system render target from a script. Calling this method from a script does not enable MSAA on the render pipeline. Please refer to the render pipeline documentation for information on how to enable MSAA rendering for the render pipeline in use.  
  
If you are writing your own render pipeline, you might want to implement your own anti-aliasing as part of your render pipeline's post processing chain. In that case, for best performance, set the number of samples to '1' to disable MSAA on the system render target. If the value is set to 0 (default), the behavior is identical to the Built-In Render Pipeline, which uses the MSAA sample count saved in the quality settings and Unity may allocate a MSAA render target that is not needed since your render pipeline already resolves as part of its post-processing.  
  
See also: [SystemInfo.supportsMultisampledBackBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampledBackBuffer.html), [msaaSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-msaaSamples.html)  
  
The example demonstrates how a render pipeline might use this function in combination with its own MSAA settings to ensure the system render target is properly configured for its use case:
```
using UnityEngine;
using UnityEngine.Rendering;  
  
[CreateAssetMenu(menuName = "MyRenderPipeline/Create New Pipeline Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)")]
public class MyRenderPipelineAsset : RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html)
{
    public int msaaSamples = 1;
    public bool directToScreen = false;  
  
    protected override RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html) CreatePipeline()
    {
        return new MyRenderPipeline(this);
    }
}  
  
public class MyRenderPipeline : RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html)
{
    MyRenderPipelineAsset asset;  
  
    public MyRenderPipeline(MyRenderPipelineAsset asset)
    {
        this.asset = asset;
        
        // Current setup doesn't support MSAA at system render target level
        if (!SystemInfo.supportsMultisampledBackBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampledBackBuffer.html)) return;  
  
        if (asset.directToScreen)
        {
            Screen.SetMSAASamples[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetMSAASamples.html)(asset.msaaSamples);
        }
        else
        {
            Screen.SetMSAASamples[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.SetMSAASamples.html)(1);
        }
    }  
  
    protected override void Render(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)[] cameras)
    {
        // Render frame, culling shadow maps ...  
  
        // Final output to screen
        if (asset.directToScreen && SystemInfo.supportsMultisampledBackBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampledBackBuffer.html))
        {
            // Render geometry directly to system buffer, no post processing is possible
            // the system provides the MSAA resolve as part of the final screen blit or desktop compositor
        }
        else
        {
            // Post processing resolves MSAA and eventually writes single sample data to the sceen
        }
    }
}

```

* * *
