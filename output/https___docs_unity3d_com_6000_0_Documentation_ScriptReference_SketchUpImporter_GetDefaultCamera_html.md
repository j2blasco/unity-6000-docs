* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.GetDefaultCamera.html

#  [SketchUpImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html).GetDefaultCamera
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
public [SketchUpImportCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera.html) GetDefaultCamera(); 
### Returns
**SketchUpImportCamera** The default camera. 
### Description
The default camera or the camera of the active Scene which the SketchUp file was saved with.
The following is an example of extracting the default camera and logging if the camera is a perspective camera stored in [SketchUpImportCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SketchUpUtility
{
    public static void IsDefaultCameraPerspective(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go)
    {
        string assetPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(go); // get asset path
        // get SketchUpImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html)
        SketchUpImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html) importer = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as SketchUpImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html);
        if (importer == null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This object is not imported by SketchUpImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html)");
            return;
        }  
  
        SketchUpImportCamera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera.html) camera = importer.GetDefaultCamera();  // get all the scenes  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The default camera is " + (camera.isPerspective ? "perspective" : "orthogonal"));
    }
}

```

* * *
