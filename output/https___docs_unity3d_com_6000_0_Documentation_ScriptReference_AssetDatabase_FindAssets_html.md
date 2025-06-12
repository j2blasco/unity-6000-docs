* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).FindAssets
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
public static string[] FindAssets(string filter); 
## Declaration
public static string[] FindAssets(string filter, string[] searchInFolders); 
### Parameters
Parameter | Description  
---|---  
filter | The filter string can contain search data. See below for details about this string.  
searchInFolders | The folders where the search will start.  
### Returns
**string[]** Array of matching asset. Note that GUIDs will be returned. If no matching assets were found, returns empty array. 
### Description
Search the asset database using the search filter string.
FindAssets allows you to search for Assets. The `string` argument can provide names, labels or types (classnames). The filter string can include:  
  
**Name** : Filter assets by their filename (without extension). Words separated by whitespace are treated as a separate name searches. So, for example `"test asset"`, is a name of an Asset which will be searched for. Note that name can be used to identify an asset. Further, the name used in the filter `string` can be specified as a subsection. For example the `test asset` example above can be matched using `test`.  
  
**Labels (l:)** : Assets can have labels attached to them. Assets with particular labels can be found using the keyword `'l:'` before each label. This indicates that the string is searching for labels.  
  
**Types (t:)** : Find assets based on explicitly identified types. The keyword `'t:'` is used as a way to specify that typed assets are being looked for. If more than one type is included in the filter `string` then assets that match one class will be returned. Types can either be builtin types such as `Texture2D` or user created script classes. User created classes are assets created from a ScriptableObject class in the project. If all assets are wanted use `Object` as all assets derive from Object. Specifying one or more folders using the `searchInFolders` argument will limit the searching to these folders and their child folders. This is faster than searching all assets in all folders.  
  
**AssetBundles (b:)** : Find assets which are part of an Asset bundle. The keyword `'b:'` is used to determine that Asset bundles names should be part of the query.  
  
**Area (a:)** : Find assets in a specific **area** of a project. Valid values are `"all"`, `"assets"` and `"packages"`. Use this to make your query more specific using the `'a:'` keyword followed by the area name to speed up searching.  
  
**Globbing (glob:)** : Use globbing to match specific rules. The keyword `glob:` is followed by the query. For example, `glob:Editor` will find all Editor folders in a project, `glob:(Editor|Resources)` will find all Editor and Resources folders in a project, `glob:Editor/*` will return all Assets inside Editor folders in a project, while `glob:Editor/**` will return all Assets within Editor folders recursively.  
  
**Note:**   
Searching is case insensitive.  
  
Use [AssetDatabase.GUIDToAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html) to get asset paths and [AssetDatabase.LoadAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html) to load an asset.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/FindAssets Example")]
    static void ExampleScript()
    {
        // Find all assets labelled with 'architecture' :
        string[] guids1 = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("l:architecture", null);  
  
        foreach (string guid1 in guids1)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid1));
        }  
  
        // Find all Texture2Ds that have 'co' in their filename, that are labelled with 'architecture' and are placed in 'MyAwesomeProps' folder
        string[] guids2 = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("co l:architecture t:texture2D", new[] {"Assets/MyAwesomeProps"});  
  
        foreach (string guid2 in guids2)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid2));
        }
    }
}
```

The following script example shows how the Names, Labels and Types details added to Assets can be located. The [FindAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html) function is demonstrated. The assets created in this example use the `ScriptObj` class.
```
// This script file has two CS classes.  The first is a simple Unity ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) script.
// The class it defines is used by the Example class below.
// (This is a single Unity script file. You could split this file into a ScriptObj.cs and an
// Example.cs file which is more structured.)  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.IO;  
  
public class ScriptObj : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public void Awake()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("ScriptObj created");
    }
}  
  
// Use ScriptObj to show how AssetDabase.FindAssets can be used  
  
public class Example
{
    static ScriptObj testI;
    static ScriptObj testJ;
    static ScriptObj testK;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/FindAssets Example two")]
    static void ExampleScript()
    {
        CreateAssets();
        NamesExample();
        LabelsExample();
        TypesExample();
    }  
  
    static void CreateAssets()
    {
        if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)("Assets/AssetFolder"))
        {
            AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", "AssetFolder");
        }  
  
        if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)("Assets/AssetFolder/SpecialFolder"))
        {
            AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets/AssetFolder", "SpecialFolder");
        }  
  
        testI = (ScriptObj)ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)(typeof(ScriptObj));
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(testI, "Assets/AssetFolder/testI.asset");  
  
        testJ = (ScriptObj)ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)(typeof(ScriptObj));
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(testJ, "Assets/AssetFolder/testJ.asset");  
  
        // create an asset in a sub-folder and with a name which contains a space
        testK = (ScriptObj)ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)(typeof(ScriptObj));
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(testK, "Assets/AssetFolder/SpecialFolder/testK example.asset");  
  
        // an asset with a material will be used later
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, "Assets/AssetFolder/SpecialFolder/MyMaterial.mat");
    }  
  
    static void NamesExample()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("*** FINDING ASSETS BY NAME ***");  
  
        string[] results;  
  
        results = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("testI");
        foreach (string guid in results)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("testI: " + AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid));
        }  
  
        results = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("testJ");
        foreach (string guid in results)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("testJ: " + AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid));
        }  
  
        results = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("testK example");
        foreach (string guid in results)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("testK example: " + AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid));
        }  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("*** More complex asset search ***");  
  
        // find all assets that contain test (which is all assets)
        results = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("test");
        foreach (string guid in results)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("name:test - " + AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid));
        }
    }  
  
    static void LabelsExample()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("*** FINDING ASSETS BY LABELS ***");  
  
        string[] setLabels;  
  
        setLabels = new string[] { "wrapper" };
        AssetDatabase.SetLabels[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetLabels.html)(testI, setLabels);  
  
        setLabels = new string[] { "bottle", "banana", "carrot" };
        AssetDatabase.SetLabels[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetLabels.html)(testJ, setLabels);  
  
        setLabels = new string[] { "swappable", "helmet" };
        AssetDatabase.SetLabels[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetLabels.html)(testK, setLabels);  
  
        // label searching:
        //   testI has wrapper, testK has swappable, so both have 'app'
        //   testJ has bottle, so have a label searched as 'bot'
        string[] getGuids = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("l:app l:bot");
        foreach (string guid in getGuids)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("label lookup: " + AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid));
        }
    }  
  
    static void TypesExample()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("*** FINDING ASSETS BY TYPE ***");  
  
        string[] guids;  
  
        guids = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:material");
        foreach (string guid in guids)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html): " + AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid));
        }  
  
        guids = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:Object l:helmet");
        foreach (string guid in guids)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("ScriptObj+helmet: " + AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid));
        }
    }
}
```

* * *
