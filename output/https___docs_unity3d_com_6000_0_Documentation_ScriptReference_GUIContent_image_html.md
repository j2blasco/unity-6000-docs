* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-image.html

#  [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html).image
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
[Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image; 
### Description
The icon image contained.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) icon;  
  
    void OnGUI()
    {
        if (!icon)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Add a texture on the inspector first");
            return;
        }
        GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 100, 20), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)(icon));
    }
}

```

* * *
