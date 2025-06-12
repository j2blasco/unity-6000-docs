* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageStarted.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).importPackageStarted
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
### Description
Callback raised whenever a package import starts.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[InitializeOnLoad]
public class AssetDatabaseExamples
{
    static AssetDatabaseExamples()
    {
        AssetDatabase.importPackageStarted[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageStarted.html) += OnImportPackageStarted;
        AssetDatabase.importPackageCompleted[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageCompleted.html) += OnImportPackageCompleted;
        AssetDatabase.importPackageFailed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageFailed.html) += OnImportPackageFailed;
        AssetDatabase.importPackageCancelled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageCancelled.html) += OnImportPackageCancelled;
    }  
  
    private static void OnImportPackageCancelled(string packageName)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Cancelled the import of package: {packageName}");
    }  
  
    private static void OnImportPackageCompleted(string packagename)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Imported package: {packagename}");
    }  
  
    private static void OnImportPackageFailed(string packagename, string errormessage)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Failed importing package: {packagename} with error: {errormessage}");
    }  
  
    private static void OnImportPackageStarted(string packagename)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Started importing package: {packagename}");
    }
}
```

* * *
