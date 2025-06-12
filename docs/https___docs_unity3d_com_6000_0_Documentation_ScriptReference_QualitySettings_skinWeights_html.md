* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).skinWeights
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
[SkinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.html) skinWeights; 
### Description
The maximum number of bones per vertex that are taken into account during skinning, for all meshes in the project.
The value can be either One Bone, Two Bones, Four Bones or Auto. Note that higher bone counts may have a performance cost, especially above 4 bones per vertex.  
  
This setting does not change the underlying mesh data; it only affects the number of bone weights that Unity uses when performing skinning. This means that a mesh can have bone weight data that is unused due to this setting. You can change this value at runtime.  
  
You can set this value for a single mesh using [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html). You can set the maximum number of bone weights that mesh data stores for a single vertex using [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Set skin weights to one bone for all Meshes
        QualitySettings.skinWeights[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html) = SkinWeights.OneBone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.OneBone.html);
    }
}

```

Additional resources: [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [ModelImporter.minBoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-minBoneWeight.html), [ModelImporter.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html), [BoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html), [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html).
* * *
