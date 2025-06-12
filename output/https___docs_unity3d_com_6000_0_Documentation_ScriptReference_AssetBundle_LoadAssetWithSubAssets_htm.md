* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAssetWithSubAssets.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).LoadAssetWithSubAssets
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
public Object[] LoadAssetWithSubAssets(string name); 
## Declaration
public Object[] LoadAssetWithSubAssets(string name, Type type); 
## Declaration
public T[] LoadAssetWithSubAssets(string name); 
### Parameters
Parameter | Description  
---|---  
name | Name of the Asset.  
type | Type to load.  
### Description
Loads Asset and sub Assets from the AssetBundle synchronously.
Load objects from the Asset and its SubAssets. If the signatures that specify the type are called then the requested type is matched against the Main object and Visible objects in each Asset. Otherwise the main objects of each Asset is returned. An example usage is to load all sprites from an sprite that uses "Multiple" for its [Sprite Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html). 
* * *
