* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-clipAnimations.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).clipAnimations
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
clipAnimations; 
### Description
Animation clips to split animation into. Additional resources: [ModelImporterClipAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterClipAnimation.html).
When you import a file for the first time clipAnimations will be always empty. If you need to populate clipAnimations before the first import you can use an [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html) and override [AssetPostprocessor.OnPreprocessAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessAnimation.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class CreateAnimationClip : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessAnimation()
    {
        var modelImporter = assetImporter as ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html);
        modelImporter.clipAnimations = modelImporter.defaultClipAnimations;
    }
}

```

* * *
