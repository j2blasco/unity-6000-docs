* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTextureWithTexCoords.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).DrawTextureWithTexCoords
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
public static void DrawTextureWithTexCoords([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) texCoords); 
## Declaration
public static void DrawTextureWithTexCoords([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) texCoords, bool alphaBlend); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to draw the texture within.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display.  
texCoords | How to scale the image when the aspect ratio of it doesn't fit the aspect ratio to be drawn within.  
alphaBlend | Whether to alpha blend the image on to the display (the default). If false, the picture is drawn on to the display.  
### Description
Draw a texture within a rectangle with the given texture coordinates.
Use this function for clipping or tiling the image within the given rectangle. The second [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) `texCoords` describes how the texture is adjusted to fit the position [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html). The first rectangle has its size in pixels provided; the second rectangle is given in a 0.0 to 1.0 range.  
  
Additional resources: [GUI.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html), [GUI.contentColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-contentColor.html).
```
using UnityEngine;  
  
// Use DrawTextureWithTexCoords() to draw a texture.  The texture is draw on the window
// inside a given pixel rectangle.  The size of the drawn texture is based on the value
// of hor.  This ranges from 0.5 to 1.25 so the bottom left half of the texture to a
// greater than normal value.  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex;
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect;
    private float hor;
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) hs;
    private Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) label;  
  
    void Start()
    {
        float center = Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2.0f;
        rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(center - 200, 200, 400, 250);
        hs = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(center - 200, 125, 400, 30);
        label = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(center - 20, 155, 50, 30);
        hor = 0.5f;
    }  
  
    void OnGUI()
    {
        hor = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(hs, hor, 0.5f, 1.25f);
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(label, hor.ToString("F3"));
        GUI.DrawTextureWithTexCoords[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTextureWithTexCoords.html)(rect, tex, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0.0f, 0.0f, hor, hor));
    }
}

```

* * *
