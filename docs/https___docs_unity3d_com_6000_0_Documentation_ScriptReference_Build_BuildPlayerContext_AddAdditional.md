* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerContext.AddAdditionalPathToStreamingAssets.html

#  [BuildPlayerContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerContext.html).AddAdditionalPathToStreamingAssets
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
public void AddAdditionalPathToStreamingAssets(string directoryOrFile, string pathInStreamingAssets); 
### Parameters
Parameter | Description  
---|---  
directoryOrFile | Path representing an existing file or directory. If the path doesn't exist, this function throws a FileNotFoundException.  
pathInStreamingAssets | The path within the StreamingAssets folder at which to place the additional assets. If null, the file or directory is placed directly in the StreamingAssets folder.  
### Description
Add additional streaming assets to the built player data. For example, you can include AssetBundles or other streaming assets without first putting them in the project StreamingAssets folder.
You can add a single file or an entire directory.  
  
If a file or directory with the same destination path has already been added to the BuildPlayerContext, then this function throws an ArgumentException.  
  
If a file or directory with the same destination path already exists in the project, an exception is thrown later in the build process.
* * *
