* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTexture.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).DrawTexture
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
public static void DrawTexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public static void DrawTexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [ScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.html) scaleMode); 
## Declaration
public static void DrawTexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [ScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.html) scaleMode, bool alphaBlend); 
## Declaration
public static void DrawTexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [ScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.html) scaleMode, bool alphaBlend, float imageAspect); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to draw the texture within.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display.  
scaleMode | How to scale the image when the aspect ratio of it doesn't fit the aspect ratio to be drawn within.  
alphaBlend | Whether to apply alpha blending when drawing the image (enabled by default).  
imageAspect | Aspect ratio to use for the source image. If 0 (the default), the aspect ratio from the image is used. Pass in w/h for the desired aspect ratio. This allows the aspect ratio of the source image to be adjusted without changing the pixel width and height.  
### Description
Draw a texture within a rectangle.
Additional resources: [GUI.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html), [GUI.contentColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-contentColor.html).
```
// Draws a texture in the left corner of the screen.
// The texture is drawn in a window 60x60 pixels.
// The source texture is given an aspect ratio of 10x1
// and scaled to fit in the 60x60 rectangle.  Because
// the aspect ratio is preserved, the texture will fit
// inside a 60x10 pixel area of the screen rectangle.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) aTexture;  
  
    void OnGUI()
    {
        if (!aTexture)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Assign a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) in the inspector.");
            return;
        }  
  
        GUI.DrawTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTexture.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 60, 60), aTexture, ScaleMode.ScaleToFit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.ScaleToFit.html), true, 10.0F);
    }
}

```

* * *
## Declaration
public static void DrawTexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [ScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.html) scaleMode, bool alphaBlend, float imageAspect, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, float borderWidth, float borderRadius); 
## Declaration
public static void DrawTexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [ScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.html) scaleMode, bool alphaBlend, float imageAspect, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) borderWidths, float borderRadius); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to draw the texture within.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display.  
scaleMode | How to scale the image when the aspect ratio of it doesn't fit the aspect ratio to be drawn within.  
alphaBlend | Whether to apply alpha blending when drawing the image (enabled by default).  
imageAspect | Aspect ratio to use for the source image. If 0 (the default), the aspect ratio from the image is used. Pass in w/h for the desired aspect ratio. This allows the aspect ratio of the source image to be adjusted without changing the pixel width and height.  
color | A tint color to apply on the texture.  
borderWidth | The width of the border. If 0, the full texture is drawn.  
borderWidths | The width of the borders (left, top, right and bottom). If Vector4.zero, the full texture is drawn.  
borderRadius | The radius for rounded corners. If 0, corners will not be rounded.  
borderRadiuses | The radiuses for rounded corners (top-left, top-right, bottom-right and bottom-left). If Vector4.zero, corners will not be rounded.  
### Description
Draws a border with rounded corners within a rectangle. The texture is used to pattern the border. Note that this method only works on shader model 2.5 and above.
* * *
