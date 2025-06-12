* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetAllBoneWeights
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public NativeArray<BoneWeight1> GetAllBoneWeights(); 
### Returns
**NativeArray <BoneWeight1>** Returns all non-zero bone weights for the Mesh, in vertex index order. 
### Description
Gets the bone weights for the Mesh.
Use [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html) to get the number of non-zero weights for each vertex, and then use that to iterate over this data.  
  
For each vertex, the [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) structs are sorted by [BoneWeight1.weight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1-weight.html), in descending order.  
  
Additional resources: [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html), [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html), [Mesh.boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html), [Mesh.GetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html) [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
```
using UnityEngine;  
  
public class TestSkinnedMesh : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {
    void Start()
    {
        // Get a reference to the mesh
        var skinnedMeshRenderer = GetComponent<SkinnedMeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html)>();
        var mesh = skinnedMeshRenderer.sharedMesh;  
  
        // Get the number of bone weights per vertex
        var bonesPerVertex = mesh.GetBonesPerVertex();
        if (bonesPerVertex.Length == 0)
        {
             return;
        }  
  
        // Get all the bone weights, in vertex index order
        var boneWeights = mesh.GetAllBoneWeights();  
  
        // Keep track of where we are in the array of BoneWeights, as we iterate over the vertices
        var boneWeightIndex = 0;  
  
        // Iterate over the vertices
        for (var vertIndex = 0; vertIndex < mesh.vertexCount; vertIndex++)
        {
            var totalWeight = 0f;
            var numberOfBonesForThisVertex = bonesPerVertex[vertIndex];
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This vertex has " + numberOfBonesForThisVertex + " bone influences");  
  
            // For each vertex, iterate over its BoneWeights
            for (var i = 0; i < numberOfBonesForThisVertex; i++)
            {
                var currentBoneWeight = boneWeights[boneWeightIndex];
                totalWeight += currentBoneWeight.weight;
                if (i > 0)
                {
                    Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(boneWeights[boneWeightIndex - 1].weight >= currentBoneWeight.weight);
                }
                boneWeightIndex++;
            }
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(Mathf.Approximately[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Approximately.html)(1f, totalWeight));
        }
    }
}

```

* * *
