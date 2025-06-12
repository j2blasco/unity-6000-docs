* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-textureCoord2.html

#  [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html).textureCoord2
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) textureCoord2; 
### Description
The secondary uv texture coordinate at the impact point.
This can be used for 3D texture painting or drawing bullet marks. If the collider is not a mesh collider, [Vector2.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html) will be returned. If the mesh contains no secondary uv set, the uv of the primary uv set will be returned. This property can be accessed off the main thread.  
  
**Note:** A [textureCoord2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-textureCoord2.html) requires the collider to be a [MeshCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Attach this script to a camera and it will paint black pixels in 3D
    // on whatever the user clicks. Make sure the mesh you want to paint
    // on has a mesh collider attached.  
  
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        cam = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Only when we press the mouse
        if (!Input.GetMouseButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButton.html)(0))
        {
            return;
        }  
  
        // Only if we hit something, do we continue
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
        if (!Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(cam.ScreenPointToRay(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html)), out hit))
        {
            return;
        }  
  
        // Just in case, also make sure the collider also has a renderer
        // material and texture. Also we should ignore primitive colliders.
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = hit.transform.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
        MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html) meshCollider = hit.collider as MeshCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshCollider.html);  
  
        if (rend == null || rend.sharedMaterial == null ||
            rend.sharedMaterial.mainTexture == null || meshCollider == null)
        {
            return;
        }  
  
        // Now draw a pixel where we hit the object
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = rend.material.mainTexture as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pixelUV = hit.textureCoord2;
        pixelUV.x *= tex.width;
        pixelUV.y *= tex.height;  
  
        tex.SetPixel(Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(pixelUV.x), Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(pixelUV.y), Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html));  
  
        tex.Apply();
    }
}

```

* * *
