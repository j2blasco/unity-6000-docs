* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).SaveFilePanel
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
public static string SaveFilePanel(string title, string directory, string defaultName, string extension); 
### Parameters
Parameter | Description  
---|---  
title | The title of the window to display.  
directory | The working directory that this dialog opens on.  
defaultName | The placeholder text to display in the "Save As" text field. This is the name of file to be saved.   
extension | The file extension to use in the saved file path. For example, enter "png" to save an image in the PNG format.  
### Returns
**string** A string path to the saved file if the dialog was canceled or the save failed, it returns an empty string. 
### Description
Displays the "save file" dialog and returns the selected path name.
This function displays a dialog that prompts the user for a path to save an asset to. It does not create the file or parent directories. You are responsible for creating and writing to the file at the returned path location. **Note:** The dialog has a Save button and a Cancel button. If you click the Cancel button, the window closes without saving.  
  
Additional resources: [OpenFilePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanel.html) function.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorUtilitySaveFilePanel.png)  
_Save File Panel._
```
// Opens a file selection dialog for a PNG file and saves a selected texture to the file.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.IO;  
  
public class EditorUtilitySaveFilePanel : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Save Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to file")]
    static void Apply()
    {
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
        if (texture == null)
        {
            EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)(
                "Select Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)",
                "You Must Select a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) first!",
                "OK");
            return;
        }  
  
        var path = EditorUtility.SaveFilePanel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html)(
            "Save texture as PNG",
            "",
            texture.name + ".png",
            "png");  
  
        if (path.Length != 0)
        {
            var pngData = texture.EncodeToPNG();
            if (pngData != null)
                File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)(path, pngData);
        }
    }
}

```

* * *
