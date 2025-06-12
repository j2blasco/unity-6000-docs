* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html

#  [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).CalculateInterpolatedLightAndOcclusionProbes
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
## Declaration
public static void CalculateInterpolatedLightAndOcclusionProbes(Vector3[] positions, SphericalHarmonicsL2[] lightProbes, Vector4[] occlusionProbes); 
## Declaration
public static void CalculateInterpolatedLightAndOcclusionProbes(List<Vector3> positions, List<SphericalHarmonicsL2> lightProbes, List<Vector4> occlusionProbes); 
### Parameters
Parameter | Description  
---|---  
positions | The array of world space positions used to evaluate the probes.  
lightProbes | The array where the resulting light probes are written to.  
occlusionProbes | The array where the resulting occlusion probes are written to.  
### Description
Calculate light probes and occlusion probes at the given world space positions.
If there are no probes baked in the Scene, the ambient probe will be written to the `lightProbes` array and `Vector4` (1,1,1,1) will be written to the `occlusionProbes` array.   
ArgumentNullException is thrown if `positions` is `null`.  
You can omit either `lightProbes` or `occlusionProbes` array by passing `null` to the function, but you cannot omit both at the same time. If both arrays are omitted, an ArgumentException is thrown. `lightProbes` and `occlusionProbes` should be calculated together for better performance.  
For the overload which takes arrays as arguments, the `lightProbes` and `occlusionProbes` must have at least the same number of elements as the `positions` array.  
For the overload which takes lists as arguments, the output lists will be resized to fit the size of the `positions` array if there is not enough space in the given lists.  
The returned probes may be further used for instanced rendering by copying them to a MaterialPropertyBlock object via [MaterialPropertyBlock.CopySHCoefficientArraysFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopySHCoefficientArraysFrom.html) and [MaterialPropertyBlock.CopyProbeOcclusionArrayFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html).
```
using UnityEngine;  
  
// This script uses OnPreCull for the rendering. It is mandatory to put the script to a Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) object.
// Make sure light probes are placed and baked in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
// Use Shadowmask mode and mixed lights to see occlusion probes approximating shadowness.
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)))]
public class Simple : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;  
  
    private Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)[] transforms;
    private MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) properties;
    private Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) cubeMesh;  
  
    void Start()
    {
        const int kCount = 100;  
  
        // Generate 100 random positions
        var positions = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[kCount];
        for (int i = 0; i < kCount; ++i)
            positions[i] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-20.0f, 20.0f), Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-20.0f, 20.0f), Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-20.0f, 20.0f));  
  
        // Calculate probes at these positions
        var lightprobes = new UnityEngine.Rendering.SphericalHarmonicsL2[kCount];
        var occlusionprobes = new Vector4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html)[kCount];
        LightProbes.CalculateInterpolatedLightAndOcclusionProbes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html)(positions, lightprobes, occlusionprobes);  
  
        // Put them into the MPB
        properties = new MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html)();
        properties.CopySHCoefficientArraysFrom(lightprobes);
        properties.CopyProbeOcclusionArrayFrom(occlusionprobes);  
  
        // Compute the transforms list
        transforms = new Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)[kCount];
        for (int i = 0; i < kCount; ++i)
            transforms[i] = Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(positions[i]);  
  
        // Create the cube mesh
        cubeMesh = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html)).GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().sharedMesh;  
  
        // Make sure the material property is assigned
        if (material == null || !material.enableInstancing)
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("material must be assigned with one with instancing enabled.");
    }  
  
    // OnPreCull happens before every culling, which is the perfect timing to inject DrawMesh* function calls.
    void OnPreCull()
    {
        if (material != null && material.enableInstancing)
        {
            RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rp = new RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html)(material)
            {
                matProps = properties,
                lightProbeUsage = UnityEngine.Rendering.LightProbeUsage.CustomProvided, // enable instancing for probes
                shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.On,
                receiveShadows = true
            };
            Graphics.RenderMeshInstanced[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html)(rp, cubeMesh, 0, transforms);
        }
    }
}

```

The example demonstrates how to leverage the baked light probes to enhance the visual quality of instanced rendering.
* * *
