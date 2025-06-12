* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).CreatePrimitive
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) CreatePrimitive([PrimitiveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.html) type); 
### Parameters
Parameter | Description  
---|---  
type | The type of primitive object to create, specified as a member of the [PrimitiveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.html) enum.  
### Description
Creates a GameObject of the specified PrimtiveType with a mesh renderer and appropriate collider.
For `CreatePrimitive` to succeed at runtime, your project must reference the following components: 
  * [MeshFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)
  * [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)
  * [BoxCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)
  * [SphereCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html)


To ensure you have the required references, declare private properties of these types to prevent them being stripped from the build. Your project must also reference the Default-Material. If it doesn't, the primitive object will be shown in pink to indicate the missing material.  
  
For more information, refer to [Primitive and placeholder objects](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html) in the Manual. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Create a plane, sphere and cube in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).  
  
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) plane  = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));  
  
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        cube.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0.5f, 0);  
  
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) sphere = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html));
        sphere.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1.5f, 0);  
  
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) capsule = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Capsule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Capsule.html));
        capsule.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(2, 1, 0);  
  
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cylinder = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cylinder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cylinder.html));
        cylinder.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-2, 1, 0);
    }
}

```

Additional resources: [PrimitiveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.html)
* * *
