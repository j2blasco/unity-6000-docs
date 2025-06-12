* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFolderPanel.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).OpenFolderPanel
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
public static string OpenFolderPanel(string title, string folder, string defaultName); 
### Description
Displays the "open folder" dialog and returns the selected path name.
Additional resources: [OpenFilePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanel.html), [SaveFolderPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFolderPanel.html) functions.  
  

```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.IO;  
  
public class OpenFolderPanelExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Load Textures To Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html)")]
    static void Apply()
    {
        string path = EditorUtility.OpenFolderPanel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFolderPanel.html)("Load png Textures", "", "");
        string[] files = Directory.GetFiles(path);  
  
        foreach (string file in files)
            if (file.EndsWith(".png"))
                File.Copy(file, EditorApplication.currentScene);
    }
}

```

* * *
