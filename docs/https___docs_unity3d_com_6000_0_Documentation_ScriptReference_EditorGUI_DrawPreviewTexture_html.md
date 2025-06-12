* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawPreviewTexture.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).DrawPreviewTexture
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
public static void DrawPreviewTexture([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat = null, [ScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.html) scaleMode = ScaleMode.StretchToFill, float imageAspect = 0, float mipLevel = -1, [Rendering.ColorWriteMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ColorWriteMask.html) colorWriteMask = ColorWriteMask.All, float exposure = 0); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to draw the texture within.  
image |  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to display.  
mat | Material to be used when drawing the texture.  
scaleMode | How to scale the image when the aspect ratio of it doesn't fit the aspect ratio to be drawn within.  
imageAspect | Aspect ratio to use for the source image. If 0 (the default), the aspect ratio from the image is used.  
mipLevel | The mip-level to sample. If negative, the texture is sampled normally. Sets material's _Mip property.  
colorWriteMask | Specifies which color components of image will get written. Sets material's _ColorMask property.  
exposure | Specifies the exposure for the texture. Sets material's _Exposure property.  
### Description
Draws the texture within a rectangle.
If mat is null (the default), an appropriate material will be chosen for a RGBM or doubleLDR lightmap or a normal map and the fallback blit material will be chosen otherwise.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIDrawPreviewTexture.png)  
_Preview Texture in an Editor Window._  
  

```
// Load a texture, display the texture, display its alpha channel and
// show a preview of the inverted texture
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
class EditorGUITextures : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture;
    Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) invertedTexture;
    bool showInverted = false;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Previewer")]
    static void Init()
    {
        var window = GetWindow<EditorGUITextures>("Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Previewer");
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 400, 200);
        window.Show();
    }  
  
    void OnGUI()
    {
        texture = (Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html))EditorGUI.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ObjectField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, 200, 20),
            "Add a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html):",
            texture,
            typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)));
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(208, 3, position.width - 210, 20), "Process Inverted"))
        {
            if (invertedTexture)
                DestroyImmediate(invertedTexture);
            //Copy the new texture
            invertedTexture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(texture.width,
                texture.height,
                texture.format,
                (texture.mipmapCount != 0));
            for (int m = 0; m < texture.mipmapCount; m++)
                invertedTexture.SetPixels(texture.GetPixels(m), m);
            InvertColors();
            showInverted = true;
        }
        if (texture)
        {
            EditorGUI.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PrefixLabel.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 45, 100, 15), 0, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Preview:"));
            EditorGUI.DrawPreviewTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawPreviewTexture.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 60, 100, 100), texture);
            EditorGUI.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PrefixLabel.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(150, 45, 100, 15), 0, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Alpha:"));
            EditorGUI.DrawTextureAlpha[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawTextureAlpha.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(150, 60, 100, 100), texture);
            EditorGUI.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PrefixLabel.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(275, 45, 100, 15), 0, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Inverted:"));
            if (showInverted)
                EditorGUI.DrawPreviewTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawPreviewTexture.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(275, 60, 100, 100), invertedTexture);
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, position.height - 25, position.width - 6, 20), "Clear texture"))
            {
                texture = EditorGUIUtility.whiteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-whiteTexture.html);
                showInverted = false;
            }
        }
        else
        {
            EditorGUI.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PrefixLabel.html)(
                new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, position.height - 25, position.width - 6, 20),
                0,
                new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("No texture found"));
        }
    }  
  
    void InvertColors()
    {
        for (int m = 0; m < invertedTexture.mipmapCount; m++)
        {
            Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] c = invertedTexture.GetPixels(m);
            for (int i = 0; i < c.Length; i++)
            {
                c[i].r = 1 - c[i].r;
                c[i].g = 1 - c[i].g;
                c[i].b = 1 - c[i].b;
            }
            invertedTexture.SetPixels(c, m);
        }
        invertedTexture.Apply();
    }
}

```

* * *
