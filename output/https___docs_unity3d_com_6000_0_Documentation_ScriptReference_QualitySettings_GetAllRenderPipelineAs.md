* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetAllRenderPipelineAssetsForPlatform.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).GetAllRenderPipelineAssetsForPlatform
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
## Declaration
public static void GetAllRenderPipelineAssetsForPlatform(string buildTargetGroupName, ref List<RenderPipelineAsset> renderPipelineAssets); 
### Parameters
Parameter | Description  
---|---  
buildTargetGroupName | The platform to obtain the Render Pipeline Assets.  
renderPipelineAssets | The list that will be filled with the unfiltered Render Pipeline Assets. There might be null Render Pipeline Assets.  
### Description
[Editor Only] Fills the given list with all the Render Pipeline Assets on any Quality Level for the given platform. Without filtering by Render Pipeline Asset type or null.
```
public RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html)[] GetAllRenderPipelineAssets(BuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platform)
{
    var activeBuildTargetGroup = BuildPipeline.GetBuildTargetGroup(platform);
    var namedBuildTarget = NamedBuildTarget.FromBuildTargetGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.FromBuildTargetGroup.html)(activeBuildTargetGroup);
    List<RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html)> assets = new List<RenderPipelineAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html)>();
    QualitySettings.GetAllRenderPipelineAssetsForPlatform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetAllRenderPipelineAssetsForPlatform.html)(namedBuildTarget.TargetName, ref assets);
    return assets.ToArray();
}
```

Gets all the Render Pipeline Assets. That are included in all the Quality levels for the given platform.
* * *
