* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-whiteTexture.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).whiteTexture
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
[Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) whiteTexture; 
### Description
Get a white texture.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIUtilityWhiteTexture.png)   
_White texture in an Editor Window._
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class EditorGUITextures : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = null;
    static Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) invertedTexture;
    bool showInverted = false;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Previewer")]
    static void Init()
    {
        EditorGUITextures window =
            EditorWindow.GetWindowWithRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html)<EditorGUITextures>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 410, 250));
        window.Show();
    }  
  
    void OnGUI()
    {
        texture = (Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html))EditorGUI.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ObjectField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, 200, 50),
            "Add a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html):",
            texture,
            typeof(Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)));  
  

        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(250, 3, 100, 20), "Process Inverted"))
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
            EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 200, 100, 25), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Preview:"));
            EditorGUI.DrawPreviewTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawPreviewTexture.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 70, 100, 100), texture);
            EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(150, 200, 100, 25), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Alpha:"));
            EditorGUI.DrawTextureAlpha[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawTextureAlpha.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(150, 70, 100, 100), texture);
            EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(275, 200, 100, 25), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Inverted:"));  
  
            if (showInverted)
            {
                EditorGUI.DrawPreviewTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawPreviewTexture.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(275, 70, 100, 100), invertedTexture);
            }  
  
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
  
    static void InvertColors()
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
  
    void OnInspectorUpdate()
    {
        this.Repaint();
    }
}

```

* * *
