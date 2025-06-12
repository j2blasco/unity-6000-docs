* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Embed.html

#  [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html).Embed
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html "Go to PackageManager Component in the Manual")
## Declaration
public static [PackageManager.Requests.EmbedRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.EmbedRequest.html) Embed(string packageName); 
### Parameters
Parameter | Description  
---|---  
packageName | The name of the package to embed. This package must be a direct dependency of the project. `ArgumentException` is thrown if `packageName` is `null` or empty.  
### Returns
**EmbedRequest** An [EmbedRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.EmbedRequest.html) instance, which you can use to get the [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html) representing the embedded package from the `EmbedRequest.Result` property. 
### Description
[Embeds](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-embed.html) a package inside the project.
The Package Manager makes a copy of the original package inside the `Packages` folder of the project. All files inside that package become writable.  
  
`Embed()` is an asynchronous operation. Before the operation is complete, you can use the `EmbedRequest` instance to monitor the asynchronous operation.  
  
  
**Note:** Make sure any other Client operations have completed before calling this method. For more information, see the note on the [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) class reference page.
* * *
