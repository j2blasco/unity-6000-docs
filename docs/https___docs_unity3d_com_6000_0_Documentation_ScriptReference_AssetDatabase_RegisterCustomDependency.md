* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RegisterCustomDependency.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).RegisterCustomDependency
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
public static void RegisterCustomDependency(string dependency, [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hashOfValue); 
### Parameters
Parameter | Description  
---|---  
dependency | Name of dependency. You can use any name you like, but because these names are global across all your Assets, it can be useful to use a naming convention (eg a path-based naming system) to avoid clashes with other custom dependency names.  
hashOfValue | A Hash128 value of the dependency.  
### Description
Allows you to register a custom dependency that Assets can be dependent on. If you register a custom dependency, and specify that an Asset is dependent on it, then the Asset will get re-imported if the custom dependency changes.
If an asset has a dependency to a custom dependency and the hash value of the custom dependency is changed, then the asset will get reimported. You can change the hash by calling RegisterCustomDependency again, and passing the same name, and a new value for the hash.  
  
The reimport happens when either AssetDatabase.Refresh is called or it imported using AssetDatabase.ImportAsset().  
  
For an example for how to use custom dependencies goto [AssetImportContext.DependsOnCustomDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.DependsOnCustomDependency.html)  
  
**Exception**  
You should not call RegisterCustomDependency from any code that is executed during the Asset import process. If you do, this method will throw an exception.
* * *
