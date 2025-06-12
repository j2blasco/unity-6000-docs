* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-skinWeightBufferLayout.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).skinWeightBufferLayout
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
[SkinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.html) skinWeightBufferLayout; 
### Description
The dimension of data in the bone weight buffer.
This value describes the layout of data in the mesh's bone weight buffer. It depends on how many bones that affect each vertex in the mesh.
```
using UnityEngine;
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        if(mesh.skinWeightBufferLayout == SkinWeights.FourBones[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.FourBones.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) is using four bones per vertex");
        }
    }
}

```

Additional resources: [Mesh.GetBoneWeightBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeightBuffer.html).
* * *
