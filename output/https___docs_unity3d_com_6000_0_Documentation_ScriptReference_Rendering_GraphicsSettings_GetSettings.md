* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetSettingsForRenderPipeline.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).GetSettingsForRenderPipeline
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
public static [Rendering.RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) GetSettingsForRenderPipeline(Type renderPipelineType); 
## Declaration
public static [Rendering.RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) GetSettingsForRenderPipeline(); 
### Parameters
Parameter | Description  
---|---  
renderPipelineType | The type of [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html).  
### Returns
**RenderPipelineGlobalSettings** [RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) asset that is registered for the given pipeline. 
### Description
Get the registered [RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) for the given [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html).
This method iterates over all [RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) registered in the GraphicsSettings. If there is an instance registered for the given [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html), the method returns it, otherwise the method returns null. The function performs string comparison and may allocate memory. To improve runtime performance, cache the result of the function call.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ExampleRenderPipelineAsset : RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html)
{
    protected override RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html) CreatePipeline()
    {
        return new ExampleRenderPipeline();
    }
}  
  
public class ExampleRenderPipeline : RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html)
{
    public ExampleRenderPipeline()
    {
        var mySettings = ExampleRPGlobalSettings.Create();
        ExampleRPGlobalSettings.RegisterToGraphicsSettings(mySettings);
    }  
  
    protected override void Render(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) renderContext, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)[] cameras)
    {
        // Do something
    }  
  
    public virtual RenderPipelineGlobalSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) globalSettings
    {
        get { return ExampleRPGlobalSettings.instance; }
    }  
  
    protected virtual void Dispose(bool disposing)
    {
        ExampleRPGlobalSettings.UnregisterToGraphicsSettings();
    }
}  
  
public class ExampleRPGlobalSettings : RenderPipelineGlobalSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html)
{
    private static ExampleRPGlobalSettings cachedInstance = null;
    public static ExampleRPGlobalSettings instance
    {
        get
        {
            if (cachedInstance == null)
                cachedInstance = GraphicsSettings.GetSettingsForRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.GetSettingsForRenderPipeline.html)<ExampleRenderPipeline>() as ExampleRPGlobalSettings;
            return cachedInstance;
        }
    }  
  
    public static void RegisterToGraphicsSettings(ExampleRPGlobalSettings newSettings)
    {
        GraphicsSettings.RegisterRenderPipelineSettings<ExampleRenderPipeline>(newSettings as RenderPipelineGlobalSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html));
        cachedInstance = null;
    }  
  
    public static void UnregisterToGraphicsSettings()
    {
        GraphicsSettings.UnregisterRenderPipelineSettings<ExampleRenderPipeline>();
        cachedInstance = null;
    }  
  
    static public ExampleRPGlobalSettings Create()
    {
        ExampleRPGlobalSettings assetCreated = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<ExampleRPGlobalSettings>();
        return assetCreated;
    }
}

```

* * *
