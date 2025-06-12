* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle-active.html

#  [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).active
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GUIStyle.html "Go to GUIStyle Component in the Manual")
[GUIStyleState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyleState.html) active; 
### Description
Rendering settings for when the control is pressed down.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Assigns a texture to button for when the control
    // is pressed down  
  
    Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) aTexture;  
  
    void OnGUI()
    {
        if (!aTexture)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Assign a texture on the editor first");
            return;
        }  
  
        GUI.skin.button.active.background = aTexture;
    }
}

```

* * *
