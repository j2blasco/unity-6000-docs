* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-textureCoord.html

#  [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html).textureCoord
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) textureCoord; 
### Description
The uv texture coordinate at the collision location.
A ray is fired into the Scene. The `textureCoord` is the location where the ray has hit a collider. `RaycastHit._textureCoord` is a texture coordinate when a hit occurs. A [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) zero is returned if no mesh collider is present in the `GameObject`. This property can be accessed off the main thread.  
  
**Note:** A [textureCoord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-textureCoord.html) requires the collider to be a [MeshCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html).
```
// Write black pixels onto the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that is located
// by the script. The script is attached to the camera.
// Determine where the collider hits and modify the texture at that point.
//
// Note that the MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html) on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) must have Convex turned off. This allows
// concave GameObjects to be included in collision in this example.
//
// Also to allow the texture to be updated by mouse button clicks it must have the Read/Write
// Enabled option set to true in its Advanced import settings.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        cam = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (!Input.GetMouseButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButton.html)(0))
            return;  
  
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
        if (!Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(cam.ScreenPointToRay(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html)), out hit))
            return;  
  
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = hit.transform.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html) meshCollider = hit.collider as MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html);  
  
        if (rend == null || rend.sharedMaterial == null || rend.sharedMaterial.mainTexture == null || meshCollider == null)
            return;  
  
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = rend.material.mainTexture as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pixelUV = hit.textureCoord;
        pixelUV.x *= tex.width;
        pixelUV.y *= tex.height;  
  
        tex.SetPixel((int)pixelUV.x, (int)pixelUV.y, Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html));
        tex.Apply();
    }
}

```

Additional resources: [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html), [Physics.Linecast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Linecast.html), [Physics.RaycastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html).
* * *
