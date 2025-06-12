* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.CombineMeshes.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).CombineMeshes
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
public void CombineMeshes(CombineInstance[] combine, bool mergeSubMeshes = true, bool useMatrices = true, bool hasLightmapData = false); 
### Parameters
Parameter | Description  
---|---  
combine | Descriptions of the Meshes to combine.  
mergeSubMeshes | Defines whether Meshes should be combined into a single sub-mesh.  
useMatrices | Defines whether the transforms supplied in the CombineInstance array should be used or ignored.  
hasLightmapData | Defines whether to transform the input Mesh lightmap UV data using the lightmap scale offset data in [CombineInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CombineInstance.html) structs.  
### Description
Combines several Meshes into this Mesh.
Combining Meshes is useful for performance optimization.  
  
If `mergeSubMeshes` is true, all the Meshes are combined together into a single sub-mesh. Otherwise, each Mesh is placed in a different sub-mesh. If all Meshes share the same Material, this property should be set to true.  
  
If `useMatrices` is true, the transform matrices in [CombineInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CombineInstance.html) structs are used. Otherwise, they are ignored.  
  
Set `hasLightmapData` to true to transform the input Mesh lightmap UV data using the lightmap scale offset data in [CombineInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CombineInstance.html) structs. The Meshes must share the same lightmap texture.  
  
For the combined Meshes to be in the same position as the parent Mesh occupies before the use of the method, save the parent Mesh's position and rotation then set these values to zero before you combine the Meshes. Once the combination is complete, set the parent Mesh's position and rotation back to the original values.
```
using UnityEngine;
using System.Collections;  
  
// Copy meshes from children into the parent's Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).
// CombineInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CombineInstance.html) stores the list of meshes.  These are combined
// and assigned to the attached Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)))]
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)[] meshFilters = GetComponentsInChildren<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>();
        CombineInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CombineInstance.html)[] combine = new CombineInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CombineInstance.html)[meshFilters.Length];  
  
        int i = 0;
        while (i < meshFilters.Length)
        {
            combine[i].mesh = meshFilters[i].sharedMesh;
            combine[i].transform = meshFilters[i].transform.localToWorldMatrix;
            meshFilters[i].gameObject.SetActive(false);  
  
            i++;
        }  
  
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        mesh.CombineMeshes(combine);
        transform.GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().sharedMesh = mesh;
        transform.gameObject.SetActive(true);
    }
}

```

* * *
