* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanel.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).OpenFilePanel
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
public static string OpenFilePanel(string title, string directory, string extension); 
### Parameters
Parameter | Description  
---|---  
title | The text to display in the toolbar of the dialog window.   
directory | The default file directory that this dialog opens. This parameter is relative to the project directory. For example, "Assets" displays the Assets directory when this dialog opens.  
extension | The file extensions to filter in this dialog. Do not precede file extension names with a period. Enter an empty string to include all file types. Separate multiple file extensions with a comma.  
### Description
Displays the "open file" dialog and returns the selected path name.
Additional resources: [SaveFilePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html) function.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorUtilityOpenFilePanel.png)  
_Open File Panel._
```
using System.IO;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class OpenFilePanelExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Overwrite Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)")]
    static void Apply()
    {
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
        if (texture == null)
        {
            EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)("Select Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)", "You must select a texture first!", "OK");
            return;
        }  
  
        string path = EditorUtility.OpenFilePanel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanel.html)("Overwrite with png", "", "png");
        if (path.Length != 0)
        {
            var fileContent = File.ReadAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.ReadAllBytes.html)(path);
            texture.LoadImage(fileContent);
        }
    }
}

```

* * *
