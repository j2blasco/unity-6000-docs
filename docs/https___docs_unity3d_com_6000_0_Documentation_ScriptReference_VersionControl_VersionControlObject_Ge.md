* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.GetExtension.html

#  [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html).GetExtension
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
public T GetExtension(); 
### Returns
**T** Extension object if it's supported by [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html). **null** otherwise. 
### Description
Gets optional extension object.
You can implement optional extensions in your [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html) to improve user experience. For example, the [IIconOverlayExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IIconOverlayExtension.html) enables you to draw VCS status overlays over asset icons. See the documentation for the full list of extensions. Future versions of Unity might add new extensions or stop calling existing ones.  
  
The default GetExtension implementation attempts to cast [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html) to extension type. This allows you to implement extensions directly in your [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html) derived class.
```
using UnityEditor.VersionControl;
using UnityEngine;  
  
[VersionControl("Custom")]
public class CustomVersionControlObject : VersionControlObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html), IIconOverlayExtension[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IIconOverlayExtension.html)
{
    static Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) s_Icon;  
  
    static Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetIcon()
    {
        if (s_Icon == null)
        {
            s_Icon = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(8, 8);
            for (var y = 0; y < s_Icon.height; ++y)
            {
                for (var x = 0; x < s_Icon.width; ++x)
                {
                    var border = y == 0 || y == s_Icon.height - 1 || x == 0 || x == s_Icon.width - 1;
                    var color = border ? Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html) : Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
                    s_Icon.SetPixel(x, y, color);
                }
            }
            s_Icon.Apply();
        }
        return s_Icon;
    }  
  
    public void DrawOverlay(string assetPath, IconOverlayType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IconOverlayType.html) type, Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect)
    {
        var topLeft = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(rect.x, rect.y, 8, 8);
        var icon = GetIcon();
        GUI.DrawTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTexture.html)(topLeft, icon);
    }
}

```

To support extensions implemented in separate classes you must overwrite this method and return an appropriate object.
```
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class CustomIconOverlayExtension : IIconOverlayExtension[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IIconOverlayExtension.html)
{
    public void DrawOverlay(string assetPath, IconOverlayType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IconOverlayType.html) type, Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rect)
    {
        var topLeft = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(rect.x, rect.y, 8, 8);
        GUI.DrawTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTexture.html)(topLeft, Texture2D.whiteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-whiteTexture.html));
    }
}  
  
[VersionControl("Custom")]
public class CustomVersionControlObject : VersionControlObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html)
{
    readonly IIconOverlayExtension[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IIconOverlayExtension.html) m_IconOverlayExtension = new CustomIconOverlayExtension();  
  
    public override T GetExtension<T>()
    {
        return m_IconOverlayExtension as T;
    }
}

```

Additional resources: [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html), [IIconOverlayExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IIconOverlayExtension.html), [IInspectorWindowExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IInspectorWindowExtension.html), [IPopupMenuExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IPopupMenuExtension.html), [ISettingsInspectorExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ISettingsInspectorExtension.html).
* * *
