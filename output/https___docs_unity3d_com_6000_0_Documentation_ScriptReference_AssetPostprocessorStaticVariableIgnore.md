* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessorStaticVariableIgnoreAttribute.html

# AssetPostprocessorStaticVariableIgnoreAttribute
class in UnityEditor
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
Allows you to decorate static variables in AssetPostprocessor and ScriptedImporter classes that should be ignored by the static variable warning system in the Import Activity window.  
  
This attribute is introduced to decorate static variables in PostProcessors and ScripttedImporters to prevent warnings about the usage of static variables. Though static variables in these classes can lead to subtle bugs when running on different Asset Import Workers as each worker has its own Mono Domain separate from the Main Editor, this attribute has been added to reduce the noise which could be generated in some difficult to fix situations involving static variables in said clasess.
Note: The static variable warnings are accessible through the "Analyze Import Process" button in the Import Activity Window.  
  
Static variables in AssetPostprocessor or ScriptedImporter classes can lead to unexpected behavior because their values are not shared across the different domains in the Main Editor and Asset Import Workers. When you modify a static variable in the Main Editor and expect the value to be reflected in the worker on its own domain, the value will not be updated, which may result in unexpected behavior.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class PostProcessorWithStaticVariable : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
   [AssetPostprocessorStaticVariableIgnore]
   public static bool enabled = false;  
  
   static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths, bool didDomainReload)
   {
     if(enabled == false)
       return;  
  
      //do something else
    }
}
```

* * *
