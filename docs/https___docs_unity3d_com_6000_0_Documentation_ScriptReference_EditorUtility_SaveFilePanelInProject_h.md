* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanelInProject.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).SaveFilePanelInProject
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
public static string SaveFilePanelInProject(string title, string defaultName, string extension, string message); 
## Declaration
public static string SaveFilePanelInProject(string title, string defaultName, string extension, string message, string path); 
### Parameters
Parameter | Description  
---|---  
title | The title of the window to display.  
defaultName | The placeholder text to display in the "Save As" text field. This is the name of file to be saved.   
extension | The file extension to use in the saved file path. For example, enter "png" to save an image in the PNG format.  
message | The text summary to display in the dialog window.  
path | The working directory for this dialog to open in. The default value is "Assets.".  
### Returns
**string** A string path to the saved file. If the dialog was canceled or the save failed, it returns an empty string. 
### Description
Displays the "save file" dialog in the Assets folder of the project and returns the selected path name.
Additional resources: [SaveFilePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html) function.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorUtilitySaveFilePanelInProject.png)  
_Save File panel in project._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.IO;  
  
public class SaveFilePanelInProjectExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Save Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) In Project")]
    static void Apply()
    {
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
        if (texture == null)
        {
            EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)("Select Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)", "You must select a texture first!", "OK");
            return;
        }  
  
        string path = EditorUtility.SaveFilePanelInProject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanelInProject.html)("Save png", texture.name + "png", "png",
            "Please enter a file name to save the texture to");
        if (path.Length != 0)
        {
            byte[] pngData = texture.EncodeToPNG();
            if (pngData != null)
            {
                File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)(path, pngData);  
  
                // As we are saving to the asset folder, tell Unity to scan for modified or new assets
                AssetDatabase.Refresh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html)();
            }
        }
    }
}

```

* * *
