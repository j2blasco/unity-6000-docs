* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.SetCursor.html

#  [Cursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html).SetCursor
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
public static void SetCursor([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) hotspot, [CursorMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorMode.html) cursorMode); 
### Parameters
Parameter | Description  
---|---  
texture | The texture to use for the cursor. To use a texture, import it with `Read/Write` enabled. Alternatively, you can use the default cursor import setting. If you created your cursor texture from code, it must be in RGBA32 format, have alphaIsTransparency enabled, and have no mip chain. To use the default cursor, set the texture to `Null`.  
hotspot | The offset from the top left of the texture to use as the target point. This must be in the bounds of the cursor.  
cursorMode | Whether to render this cursor as a hardware cursor on supported platforms, or force software cursor.  
### Description
Sets a custom cursor to use as your cursor.
Call Cursor.SetCursor with a [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) to change the appearance of the hardware pointer (mouse cursor).
```
using UnityEngine;  
  
// Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html), then mouse over the object to see your cursor change.
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) cursorTexture;
    public CursorMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorMode.html) cursorMode = CursorMode.Auto[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorMode.Auto.html);
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) hotSpot = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);  
  
    void OnMouseEnter()
    {
        Cursor.SetCursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.SetCursor.html)(cursorTexture, hotSpot, cursorMode);
    }  
  
    void OnMouseExit()
    {
        // Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html) 'null' to the texture parameter to use the default system cursor.
        Cursor.SetCursor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.SetCursor.html)(null, Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html), cursorMode);
    }
}

```

* * *
