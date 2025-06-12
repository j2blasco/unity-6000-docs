* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetColor.html

#  [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).SetColor
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
public void SetColor(string name, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
## Declaration
public void SetColor(int nameID, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property.  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
value | The [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value to set.  
### Description
Set a color property.
Adds a property to the block. If a color property with the given name already exists, the old value is replaced.  
  
The color value is considered to be always set in sRGB space and is converted to linear if the active color space is linear. You need manual updating of the color value if you switch between color spaces.
```
using UnityEngine;  
  
// Draws 3 meshes with the same material but with different colors.
using UnityEngine;
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;
    private MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) block;  
  
    void Start()
    {
        block = new MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html)();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // setup render params
        RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rp = new RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html)(material) {matProps = block};  
  
        // red mesh
        block.SetColor("_Color", Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
        Graphics.RenderMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html)(rp, mesh, 0, Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0)));  
  
        // green mesh
        block.SetColor("_Color", Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
        Graphics.RenderMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html)(rp, mesh, 0, Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5, 0, 0)));  
  
        // blue mesh
        block.SetColor("_Color", Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html));
        Graphics.RenderMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html)(rp, mesh, 0, Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-5, 0, 0)));
    }
}

```

Function variant that takes `nameID` is faster. If you are changing properties with the same name repeatedly, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get unique identifier for the name, and pass the identifier to SetColor.
```
using UnityEngine;  
  
// Draws 3 meshes with the same material but with different colors.
using UnityEngine;
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh;
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material;
    private MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) block;  
  
    void Start()
    {
        block = new MaterialPropertyBlock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html)();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // setup render params
        RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) rp = new RenderParams[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html)(material) {matProps = block};  
  
        // red mesh
        block.SetColor("_Color", Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
        Graphics.RenderMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html)(rp, mesh, 0, Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0)));  
  
        // green mesh
        block.SetColor("_Color", Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
        Graphics.RenderMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html)(rp, mesh, 0, Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5, 0, 0)));  
  
        // blue mesh
        block.SetColor("_Color", Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html));
        Graphics.RenderMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html)(rp, mesh, 0, Matrix4x4.Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-5, 0, 0)));
    }
}

```

Additional resources: [SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetFloat.html), [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetVector.html), [SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetMatrix.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetTexture.html).
* * *
