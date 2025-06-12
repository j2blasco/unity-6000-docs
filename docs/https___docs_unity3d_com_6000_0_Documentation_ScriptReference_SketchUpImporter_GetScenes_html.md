* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.GetScenes.html

#  [SketchUpImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html).GetScenes
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SketchUpImporter.html "Go to SketchUpImporter Component in the Manual")
## Declaration
public SketchUpImportScene[] GetScenes(); 
### Returns
**SketchUpImportScene[]** Array of scenes extracted from a SketchUp file. 
### Description
The method returns an array of SketchUpImportScene which represents SketchUp scenes.
[SketchUpImportScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportScene.html) is the structure to represent the Scene that was extracted from the SketchUp file.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SketchUpUtility
{
    public static void PrintSketchUpSceneName(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go)
    {
        string assetPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(go); // get asset path
        // get SketchUpImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html)
        SketchUpImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html) importer = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as SketchUpImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html);
        if (importer == null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This object is not imported by SketchUpImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html)");
            return;
        }  
  
        SketchUpImportScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportScene.html)[] scenes = importer.GetScenes();  // get all the scenes  
  
        foreach (SketchUpImportScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportScene.html) scene in scenes)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(scene.name);
        }
    }
}

```

The above example takes a GameObject that is imported from a SketchUp file and prints the name of the scenes in the SketchUp file.
* * *
