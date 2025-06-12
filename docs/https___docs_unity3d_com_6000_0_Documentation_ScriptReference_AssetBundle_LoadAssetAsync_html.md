* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAssetAsync.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).LoadAssetAsync
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
public [AssetBundleRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleRequest.html) LoadAssetAsync(string name); 
## Declaration
public [AssetBundleRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleRequest.html) LoadAssetAsync(string name); 
## Declaration
public [AssetBundleRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleRequest.html) LoadAssetAsync(string name, Type type); 
### Parameters
Parameter | Description  
---|---  
name | Name of the Asset. For the most precise matching this should be the relative path of the Asset that was built into the AssetBundle, including the file extension. The relative path and file extension are optional, and Assets can be found and loaded based on the filename alone. However this opens the potential for unexpected results if the filename is not unique within the AssetBundle. At build time it is also possible to specify a name for the Asset using [AssetBundleBuild.addressableNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild-addressableNames.html). In that case that specified name will be expected to load the Asset instead of the Asset path.   
type | The provided type will be checked against the Asset's main object, and if that is not compatible it will be matched against visible objects within the Asset. Not all nested objects are visible, for example this will not work to directly retrieve a Transform, MonoBehaviour or other Component. In cases where there are multiple matches for the name argument, the requested type can determine which Asset to load.  
### Description
Asynchronously loads an Asset from the bundle.
The LoadAssetAsync<T> signature is recommended, so that the requested type is explicit and no type casting is necessary.   
  
Note: For Scenes inside AssetBundles call [SceneManager.LoadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html) instead of this method.   
  
Additional resources: [AssetBundleRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleRequest.html). 
* * *
