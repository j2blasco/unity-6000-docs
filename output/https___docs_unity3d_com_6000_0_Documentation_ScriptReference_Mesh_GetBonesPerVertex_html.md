* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetBonesPerVertex
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
public NativeArray<byte> GetBonesPerVertex(); 
### Returns
**NativeArray <byte>** Returns the number of non-zero bone weights for each vertex. 
### Description
The number of non-zero bone weights for each vertex.
The size of the returned array is either [Mesh.vertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-vertexCount.html) or zero. The array is sorted in vertex index order.  
  
Use in combination with [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html) to get bone weights for the vertices in the Mesh.  
  
You don't need to dispose the returned native array. However the native array points to memory that might be deallocated or reallocated, so you should either call `GetBonesPerVertex` every frame to get the correct data, or check the native array is still valid each frame.  
  
Additional resources: [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html), [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
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
