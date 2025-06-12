* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StartAssetEditing.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).StartAssetEditing
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
public static void StartAssetEditing(); 
### Description
Pauses automatic asset import, allowing you to group several asset imports together into one larger import.
This method allows you to pause the Asset Database's automatic import of new or modified assets. This is useful if you want to perform actions via script that make multiple changes to assets without the Asset Database importing each change in a separate import process.   
  
Instead, you can pause imports, make multiple changes, then resume imports, which means Unity only performs one input process for all the changes you made while the importing was paused. The following example demonstrates this:
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class StartStopAssetEditingExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("APIExamples/StartStopAssetEditing")]
    static void CallAssetDatabaseAPIsBetweenStartStopAssetEditing()
    {
        try
        {
            //Place the Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Database in a state where
            //importing is suspended for most APIs
            AssetDatabase.StartAssetEditing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StartAssetEditing.html)();  
  
            AssetDatabase.CopyAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CopyAsset.html)("Assets/CopyAsset.txt", "Assets/Text/CopyAsset.txt");
            AssetDatabase.MoveAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAsset.html)("Assets/MoveAsset.txt", "Assets/Text/MoveAsset.txt");
        }
        finally
        {
            //By adding a call to StopAssetEditing inside
            //a "finally" block, we ensure the AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)
            //state will be reset when leaving this function
            AssetDatabase.StopAssetEditing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StopAssetEditing.html)();
        }
    }
}

```

`AssetDatabase.StartAssetEditing` places the Asset Database in a state that prevents imports until [AssetDatabase.StopAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StopAssetEditing.html) is called. This means that if an exception occurs between the two function calls, the Asset Database will be unresponsive. For this reason, you should always place calls to `AssetDatabase.StartAssetEditing` and `AssetDatabase.StopAssetEditing` inside either a try-catch or try-finally block.  
  
When automatic asset importing is paused, some `AssetDatabase` APIs won't work as expected. This is because assets created during the paused state aren't fully created in the asset database before the call to `StopAssetEditing`. As a rule of thumb you should limit your batch operations to those that don't require the assets involved to be fully imported. Supported and recommended methods for batching are: 
  * `AssetDatabase.ImportAsset`
  * `AssetDatabase.MoveAsset`
  * `AssetDatabase.CopyAsset`
  * `AddObjectToAsset`


Unity supports nested calls to `StartAssetEditing` and `StopAssetEditing`. The total number of calls to each method must be equal for automatic import to resume. This is tracked with a counter, where calling `StartAssetEditing` increments the counter and calling `StopAssetEditing` decrements the counter. If your code has more calls to `StartAssetEditing` than `StopAssetEditing`, automatic import won't resume. If there are more calls to `StopAssetEditing` than to `StartAssetEditing`, this causes an error.  
  
An alternative way of pausing and resuming asset database imports is to use the [AssetEditingScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetEditingScope.html) class in a `using` statement.  
  
Additional resources: [AssetEditingScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetEditingScope.html)
* * *
