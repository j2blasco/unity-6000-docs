* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MakeEditable.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).MakeEditable
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
public static bool MakeEditable(string path); 
### Parameters
Parameter | Description  
---|---  
path | Specifies the path to a file relative to the project root.  
### Returns
**bool** `true` if Unity successfully made the file editable in the version control system. Otherwise, returns `false`. 
### Description
Makes a file open for editing in version control.
Your version control system may be configured to only allow a single person at a time to edit certain types of files in order to avoid merge conflicts that arise when multiple people edit the same file. In this case, you must 'open' that file for editing (also known as 'checking out') to ensure that you have permission to edit the file at this time. Use this function to make a file 'open for editing' in a version control system that supports it.  
  
File paths that are outside of Unity project folder, or not under version controlled folders (for example, "Library" or "Temp"), are always considered editable. `MakeEditable` returns `true` for them, and otherwise does nothing.  
  
File paths that refer to non-local Package folders are always considered to be non-editable. `MakeEditable` returns `false` for them.  
  
When no version control system is active, then file paths inside the project are all considered already editable. `MakeEditable` returns `true` and otherwise does nothing.  
  
When using a version control system, for example Perforce Helix, `MakeEditable` triggers a "Checkout" operation on the files, unless they are already editable. For files that were not added to version control yet, `MakeEditable/` will add them to version control.  
  
If you set up a pre-checkout callback, Unity calls it as part of `MakeEditable`. See [PreCheckoutCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.PreCheckoutCallback.html) for more details.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Checkout Selected Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)")]
    public static void MenuExample()
    {
        var path = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html));
        var ok = AssetDatabase.MakeEditable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MakeEditable.html)(path);
        if (!ok)
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"Could not make {path} editable");
    }
}

```

Additional resources: [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html).
* * *
## Declaration
public static bool MakeEditable(string[] paths, string prompt, List<string> outNotEditablePaths); 
### Parameters
Parameter | Description  
---|---  
paths | Specifies an array of file paths relative to the project root.  
prompt | Dialog prompt to show to the user, if a version control operation needs to be done. If `null` (default), no prompt is shown.  
outNotEditablePaths | Output list of file paths that could not be made editable.  
### Returns
**bool** `true` if Unity successfully made all files editable in the version control system. 
### Description
Makes a list of files open for editing in version control.
A multi-file variant of `MakeEditable`, that can also optionally show a prompt to the user if a Checkout/Add version control operation needs to be done. If the user cancels the dialog, Unity does not make the files editable. If the Unity Editor is operating in batch mode, Unity does not show a dialog and acts as if the user accepted the dialog prompt.  
  
If you pass an `outNotEditablePaths` List, this function fills it with file paths that Unity could make editable.
```
using System.Linq;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Checkout Selected Assets")]
    public static void MenuExample()
    {
        var guids = Selection.assetGUIDs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-assetGUIDs.html);
        var paths = guids.Select(AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)).ToArray();
        var ok = AssetDatabase.MakeEditable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MakeEditable.html)(paths, "These files need to be checked out");
        if (!ok)
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Could not make some files editable");
    }
}

```

Additional resources: [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html).
* * *
