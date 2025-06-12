* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowEnvironmentSection.html

# LightingWindowEnvironmentSection
class in UnityEditor
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
Base class for the Inspector that overrides the Environment section of the Lighting window.
See also [SupportedOnRenderPipelineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedOnRenderPipelineAttribute.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.Rendering;  
  
[SupportedOnRenderPipeline(typeof(CustomSRPAsset))]
class CustomEnvironmentSection : LightingWindowEnvironmentSection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowEnvironmentSection.html)
{
    public override void OnInspectorGUI()
    {
        // The following will be displayed instead of the Environment section in the LightingWindow
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("My Custom Environment Section !!");
    }
}  
  

//Below is a custom empty render pipeline only here for explaining the filtering in ScriptableRenderPipelineExtension  
  
class CustomSRP : RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html)
{
    protected override void Render(ScriptableRenderContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) context, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)[] cameras)
    { /* My custom rendering algorithm */ }
}  
  
class CustomSRPAsset : RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html)
{
    protected override RenderPipeline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html) CreatePipeline()
    {
        return new CustomSRP();
    }
}
```

In this example, the Environment section of the Lighting window is overridden when the CustomSRP is in use.
### Public Methods
Method | Description  
---|---  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowEnvironmentSection.OnDisable.html) | OnDisable is called when this Inspector override is not used anymore.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowEnvironmentSection.OnEnable.html) | OnEnable is called when this Inspector override is used.  
[OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowEnvironmentSection.OnInspectorGUI.html) | A callback that is called when drawing the Environment section in the Lighting window.  
* * *
