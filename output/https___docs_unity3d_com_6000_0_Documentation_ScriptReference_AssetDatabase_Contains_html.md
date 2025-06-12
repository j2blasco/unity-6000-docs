* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Contains.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).Contains
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
public static bool Contains([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
## Declaration
public static bool Contains(int instanceID); 
### Description
Is object an asset?
Returns true when an object is an asset (corresponds to a file in the Assets folder), and false if it is not (for example object in the Scene, or an object created at runtime).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Contains Example")]
    static void ContainsExample()
    {
        //Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) is created in memory and the Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Database does not know about it
        var material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.Contains[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Contains.html)(material)); //Output will be false
        //Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) is then saved to disk as an asset and therefore Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Database knows that it exists
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, "Assets/Materials/MyMaterial.mat");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.Contains[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Contains.html)(material)); //Output will be true
    }
}
```

* * *
