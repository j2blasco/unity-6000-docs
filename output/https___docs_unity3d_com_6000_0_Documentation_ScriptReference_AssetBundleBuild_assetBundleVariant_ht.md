* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild-assetBundleVariant.html

#  [AssetBundleBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.html).assetBundleVariant
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
assetBundleVariant; 
### Description
AssetBundle variant.
When specified, this property is converted to lowercase and appended, like a file extension, to the assetBundleName property to build the complete AssetBundle filename.  
  
AssetBundle variants are used to achieve virtual assets in AssetBundles. Each AssetBundle with the same assetBundleName property will have the same internal IDs for equivalent Objects. For example one variant may contain high resolution images and the other could have matching images at a lower resolution. Other AssetBundles can reference the images, and depending on which variant is loaded, those will resolve to either high or low resolution equivalents.   
To function correctly, each variant of an AssetBundle should have a matching list of assets.   
Additional resources: [AssetImporter.assetBundleVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleVariant.html).
* * *
