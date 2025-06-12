* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.FindTexture.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).FindTexture
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
public static [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) FindTexture(string name); 
### Description
Get a texture from its source filename.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIUtilityFindTexture.png)   
_Checks the path of a texture._
```
// Simple editor window that lets you quick check a path of
// a texture in the editor.
//
// If the path exists then it shows a message
// else displays an error message  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class FindTextureExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string s;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Find editor texture")]
    static void findTextureExample()
    {
        FindTextureExample window = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<FindTextureExample>(true);
        window.Show();
    }  
  
    void OnGUI()
    {
        s = EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)("Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) To Locate:", s);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Check"))
            if (EditorGUIUtility.FindTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.FindTexture.html)(s))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) found at: " + s);
            }
            else
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No texture found at: " + s + ". Check your filename.");
            }
    }
}

```

**Note:** This function is used for searching for editor icons only.
* * *
