* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawGUITexture.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawGUITexture
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
public static void DrawGUITexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat = null); 
## Declaration
public static void DrawGUITexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) screenRect, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture, int leftBorder, int rightBorder, int topBorder, int bottomBorder, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat = null); 
### Parameters
Parameter | Description  
---|---  
screenRect | The size and position of the texture on the "screen" defined by the XY plane.  
texture | The texture to be displayed.  
mat | An optional material to apply the texture.  
leftBorder | Inset from the rectangle's left edge.  
rightBorder | Inset from the rectangle's right edge.  
topBorder | Inset from the rectangle's top edge.  
bottomBorder | Inset from the rectangle's bottom edge.  
### Description
Draw a texture in the Scene.
The chosen texture is drawn in 3D space on a "screen" defined by the XY plane (ie, the plane where the Z coordinate is zero). The values of the texture rectangle are given in Scene units. The optional border values specify an inset from each edge within the rectangle in Scene units; the texture is drawn inside the inset rectangle and the edge pixels are repeated outwards. This is a useful quick way to create a large background region around the main texture when its edges are of a single colour.  
  
This function can be useful for creating GUI backgrounds in conjunction with a camera pointing directly at the texture.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) myTexture;  
  
    void OnDrawGizmosSelected()
    {
        // Draw a texture rectangle on the XY plane of the scene
        Gizmos.DrawGUITexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawGUITexture.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 20, 20), myTexture);
    }
}

```

* * *
