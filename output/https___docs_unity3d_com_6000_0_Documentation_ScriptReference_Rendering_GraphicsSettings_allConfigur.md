* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-allConfiguredRenderPipelines.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).allConfiguredRenderPipelines
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
allConfiguredRenderPipelines; 
### Description
An array containing the [RenderPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) instances that describe the default render pipeline and any quality level overrides.
The default render pipeline is defined in [GraphicsSettings.defaultRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html). The override render pipeline for the current quality level is defined in [QualitySettings.renderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html), or you can request the override value for a given quality level with [QualitySettings.GetRenderPipelineAssetAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetRenderPipelineAssetAt.html).  
  
This property returns all instances of [RenderPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) that are assigned to these fields. The same [RenderPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) can appear in this array more than once, if it is assigned to more than one field.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class AllConfiguredRenderPipelinesExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("All Render Pipeline Assets that define the default render pipeline, or an override: ");
        foreach (var asset in GraphicsSettings.allConfiguredRenderPipelines[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-allConfiguredRenderPipelines.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(asset.name);
        }
    }
}

```

Additional resources: [How to get, set, and configure the active render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/srp-setting-render-pipeline-asset.html), [GraphicsSettings.currentRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-currentRenderPipeline.html), [GraphicsSettings.defaultRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html), [QualitySettings.renderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html).
* * *
