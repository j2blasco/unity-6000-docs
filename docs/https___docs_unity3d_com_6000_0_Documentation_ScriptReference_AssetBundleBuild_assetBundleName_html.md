* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild-assetBundleName.html

#  [AssetBundleBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.html).assetBundleName
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
assetBundleName; 
### Description
AssetBundle name.
When building an AssetBundle this property is converted to lowercase and used as the filename of the AssetBundle. On platforms with case sensitive file systems, such as Linux, the AssetBundle load would fail unless the lowercase form of the AssetBundle name is specified. To avoid surprises we recommend choosing a lowercase name for your AssetBundle.   
  
The name may start with folder names, for example "level1/materials/bundle_a", in which case the build creates those as subfolders of the output path.   
  
The provided name can end with a file extension, but typically AssetBundles are built with no extension because of the way AssetBundle variants work.   
  
In the case of AssetBundle variants, the name of the AssetBundle file is this string, concatenated with the [AssetBundleBuild.assetBundleVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild-assetBundleVariant.html) property as its extension, and all converted to lowercase. 
* * *
