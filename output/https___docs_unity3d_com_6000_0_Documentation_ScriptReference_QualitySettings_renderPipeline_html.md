* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).renderPipeline
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
[Rendering.RenderPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) renderPipeline; 
### Description
The [RenderPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) that defines the override render pipeline for the current quality level.
This is the override render pipeline for the current quality level. If this value is `null`, no override value exists for the current quality level.  
  
Unity uses this value and the default render pipeline defined in GraphicsSettings.renderPipeline to determine the active render pipeline for the current quality level. For more information, see [GraphicsSettings.currentRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-currentRenderPipeline.html).
```
using UnityEngine;
using UnityEngine.Rendering;  
  
public class ActiveRenderPipelineExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // In the Inspector, assign a Render Pipeline Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) to each of these fields
    public RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) defaultRenderPipelineAsset;
    public RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) overrideRenderPipelineAsset;  
  
    void Start()
    {
        GraphicsSettings.defaultRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) = defaultRenderPipelineAsset;
        QualitySettings.renderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html) = overrideRenderPipelineAsset;  
  
        DisplayCurrentRenderPipeline();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // When the user presses the left shift key, switch the default render pipeline
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.LeftShift[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftShift.html)))
        {
            SwitchDefaultRenderPipeline();
            DisplayCurrentRenderPipeline();
        }
        // When the user presses the right shift key, switch the override render pipeline
        else if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.RightShift[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightShift.html)))
        {
            SwitchOverrideRenderPipeline();
            DisplayCurrentRenderPipeline();
        }
    }  
  
    // Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) the default render pipeline between null,
    // and the render pipeline defined in defaultRenderPipelineAsset
    void SwitchDefaultRenderPipeline()
    {
        if (GraphicsSettings.defaultRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) == defaultRenderPipelineAsset)
        {
            GraphicsSettings.defaultRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) = null;
        }
        else
        {
            GraphicsSettings.defaultRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) = defaultRenderPipelineAsset;
        }
    }  
  
    // Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) the override render pipeline between null,
    // and the render pipeline defined in overrideRenderPipelineAsset
    void SwitchOverrideRenderPipeline()
    {
        if (QualitySettings.renderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html) == overrideRenderPipelineAsset)
        {
            QualitySettings.renderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html) = null;
        }
        else
        {
            QualitySettings.renderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html) = overrideRenderPipelineAsset;
        }
    }  
  
    // Print the current render pipeline information to the console
    void DisplayCurrentRenderPipeline()
    {
        // GraphicsSettings.defaultRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) determines the default render pipeline
        // If it is null, the default is the Built-in Render Pipeline
        if (GraphicsSettings.defaultRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html) != null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The default render pipeline is defined by " + GraphicsSettings.defaultRenderPipeline.name);
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The default render pipeline is the Built-in Render Pipeline");
        }  
  
        // QualitySettings.renderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html) determines the override render pipeline for the current quality level
        // If it is null, no override exists for the current quality level
        if (QualitySettings.renderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html) != null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The override render pipeline for the current quality level is defined by " + QualitySettings.renderPipeline.name);
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No override render pipeline exists for the current quality level");
        }  
  
        // If an override render pipeline is defined, Unity uses that
        // Otherwise, it falls back to the default value
        if (QualitySettings.renderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-renderPipeline.html) != null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The active render pipeline is the override render pipeline");
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The active render pipeline is the default render pipeline");
        }  
  
        // To get a reference to the Render Pipeline Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) that defines the active render pipeline,
        // without knowing if it is the default or an override, use GraphicsSettings.currentRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-currentRenderPipeline.html)
        if (GraphicsSettings.currentRenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-currentRenderPipeline.html) != null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The active render pipeline is defined by " + GraphicsSettings.currentRenderPipeline.name);
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The active render pipeline is the Built-in Render Pipeline");
        }
    }
}

```

Additional resources: [How to get, set, and configure the active render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/srp-setting-render-pipeline-asset.html), [GraphicsSettings.currentRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-currentRenderPipeline.html) [GraphicsSettings.defaultRenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-defaultRenderPipeline.html), [QualitySettings.GetRenderPipelineAssetAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetRenderPipelineAssetAt.html)], [GraphicsSettings.allConfiguredRenderPipelines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-allConfiguredRenderPipelines.html).
* * *
