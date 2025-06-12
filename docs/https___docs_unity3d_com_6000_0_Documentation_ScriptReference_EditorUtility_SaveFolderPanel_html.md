* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFolderPanel.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).SaveFolderPanel
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
public static string SaveFolderPanel(string title, string folder, string defaultName); 
### Description
Displays the "save folder" dialog and returns the selected path name.
Additional resources: [SaveFilePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html), [OpenFilePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanel.html) functions.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorUtilitySaveFolderPanel.png)  
_Save Folder Panel._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.IO;  
  
public class SaveFolderPanelExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Save Textures To Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html)")]
    static void Apply()
    {
        Object[] textures = Selection.GetFiltered[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.GetFiltered.html)(typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)), SelectionMode.Unfiltered[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Unfiltered.html));
        if (textures.Length == 0)
        {
            EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)("Select Textures", "You must select at least one texture first!", "OK");
            return;
        }  
  
        string path = EditorUtility.SaveFolderPanel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFolderPanel.html)("Save textures to folder", "", "");
        if (path.Length != 0)
        {
            foreach (Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture in textures)
            {
                Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) processedTex = texture;  
  
                byte[] pngData = processedTex.EncodeToPNG();
                if (pngData != null)
                    File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)(path + "/" + texture.name + ".png", pngData);
                else
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Could not convert " + texture.name + " to png. Skipping saving texture.");
            }  
  
            // Just in case we are saving to the asset folder, tell Unity to scan for modified or new assets
            AssetDatabase.Refresh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html)();
        }
    }
}

```

* * *
